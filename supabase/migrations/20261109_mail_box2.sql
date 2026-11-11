-- 09/11/2026 (Anthony) : 2e boîte d'envoi pour la prospection MyCreativeSite.
-- Adresse et mot de passe saisis par Anthony dans l'admin ; montée en douceur propre à la boîte ; envois répartis entre les deux boîtes.
alter table clicandsite.mail_settings add column if not exists box2_email text, add column if not exists box2_enabled boolean not null default false,
  add column if not exists box2_limit int not null default 5;
alter table clicandsite.mail_recipients add column if not exists sender text;

create or replace function public.cs_admin_mail_box2(p_email text, p_password text)
 returns jsonb language plpgsql security definer set search_path to 'clicandsite','public' as $$
declare em text := lower(trim(coalesce(p_email,'')));
begin
  if not cs_is_admin() then raise exception 'forbidden'; end if;
  if em !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$' then raise exception 'Adresse invalide'; end if;
  if em = 'contact@mycreativesite.fr' then raise exception 'C''est déjà la première boîte'; end if;
  if coalesce(p_password,'') <> '' then
    if length(p_password) < 4 then raise exception 'Mot de passe trop court'; end if;
    insert into secrets(name, value) values ('smtp_password_2', p_password) on conflict (name) do update set value = excluded.value;
  end if;
  if not exists (select 1 from secrets where name = 'smtp_password_2') then raise exception 'Saisis le mot de passe de la boîte'; end if;
  update mail_settings set box2_email = em, box2_enabled = true,
    box2_limit = case when box2_email is distinct from em then warmup_start else box2_limit end, updated_at = now() where id = 1;
  return jsonb_build_object('ok', true);
end $$;
revoke all on function public.cs_admin_mail_box2(text,text) from public, anon;
grant execute on function public.cs_admin_mail_box2(text,text) to authenticated;

create or replace function public.cs_admin_mail_box2_off()
 returns jsonb language plpgsql security definer set search_path to 'clicandsite','public' as $$
begin
  if not cs_is_admin() then raise exception 'forbidden'; end if;
  update mail_settings set box2_enabled = false, updated_at = now() where id = 1;
  return jsonb_build_object('ok', true);
end $$;
revoke all on function public.cs_admin_mail_box2_off() from public, anon;
grant execute on function public.cs_admin_mail_box2_off() to authenticated;

-- montée en douceur : chaque boîte compte ses propres jours d'envoi
create or replace function clicandsite.mail_warmup_tick()
 returns void language plpgsql security definer set search_path to 'clicandsite','public' as $$
declare d int; d2 int; b2 text;
begin
  select count(*) into d from mail_runs where sent > 0 and run_date < (now() at time zone 'Europe/Paris')::date;
  update mail_settings set daily_limit = least(warmup_cap, warmup_start + warmup_step * d), updated_at = now() where id = 1 and warmup;
  select box2_email into b2 from mail_settings where id = 1 and box2_enabled;
  if b2 is not null then
    select count(distinct (sent_at at time zone 'Europe/Paris')::date) into d2 from mail_recipients
     where status = 'envoyé' and lower(sender) = b2 and (sent_at at time zone 'Europe/Paris')::date < (now() at time zone 'Europe/Paris')::date;
    update mail_settings set box2_limit = least(warmup_cap, warmup_start + warmup_step * d2), updated_at = now() where id = 1 and warmup;
  end if;
end $$;

create or replace function public.cs_admin_mail_status()
 returns jsonb language plpgsql security definer set search_path to 'clicandsite','public' as $$
declare r jsonb; tr text[];
begin
  if not cs_is_admin() then raise exception 'forbidden'; end if;
  select trades into tr from mail_settings where id = 1;
  select jsonb_build_object(
    'settings', (select to_jsonb(s) from mail_settings s where id = 1),
    'has_password', exists(select 1 from secrets where name = 'smtp_password'),
    'has_password2', exists(select 1 from secrets where name = 'smtp_password_2'),
    'today', (select to_jsonb(m) from mail_runs m where run_date = (now() at time zone 'Europe/Paris')::date),
    'today_box2', (select count(*) from mail_recipients m, mail_settings s where s.id = 1 and m.status = 'envoyé' and lower(m.sender) = s.box2_email
                    and (m.sent_at at time zone 'Europe/Paris')::date = (now() at time zone 'Europe/Paris')::date),
    'sent_total', (select count(*) from mail_recipients where status = 'envoyé'),
    'unsubscribed', (select count(*) from mail_recipients where status = 'désinscrit'),
    'ready', (select count(*) from prospects p where p.email is not null and p.status in ('nouveau','a_contacter')
               and coalesce(p.site_status,'aucun') <> 'moderne' and p.trade = any(tr)
               and not exists (select 1 from mail_recipients r where r.prospect_id = p.id)
               and not exists (select 1 from opposition o where lower(o.value) = lower(p.email)))
  ) into r;
  return r;
end $$;

drop function if exists public.cs_admin_mail_test();
create or replace function public.cs_admin_mail_test(p_box int default 1)
 returns bigint language plpgsql security definer set search_path to 'clicandsite','public','extensions' as $$
declare rid bigint; me text;
begin
  if not cs_is_admin() then raise exception 'forbidden'; end if;
  me := lower(coalesce(auth.jwt()->>'email',''));
  select net.http_post(
    url := 'https://avcynjwcyygygkjuxsdt.supabase.co/functions/v1/cs-prospecting',
    headers := jsonb_build_object('Content-Type','application/json','x-cs-key',(select value from secrets where name='mail_internal')),
    body := jsonb_build_object('mode','test','box',coalesce(p_box,1),'to', case when me in ('docheanthony@gmail.com','abracadeal@gmail.com') then me else 'docheanthony@gmail.com' end),
    timeout_milliseconds := 60000) into rid;
  return rid;
end $$;
revoke all on function public.cs_admin_mail_test(int) from public, anon;
grant execute on function public.cs_admin_mail_test(int) to authenticated;
