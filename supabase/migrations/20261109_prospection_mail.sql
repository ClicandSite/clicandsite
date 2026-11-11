-- MyCreativeSite — envoi automatique des mails de prospection (09/11/2026), même principe que EPS :
-- API Gmail, jours ouvrés 9 h – 18 h (Paris), envois étalés, rapport quotidien, désinscription en 1 clic.
-- Le robot reste ÉTEINT (mail_settings.enabled = false) tant qu'Anthony n'a pas validé le mail et branché Gmail.

create table if not exists clicandsite.mail_settings (
  id int primary key default 1 check (id = 1),
  enabled boolean not null default false,
  daily_limit int not null default 20 check (daily_limit between 0 and 200),
  trades text[] not null default array['vtc','restaurant','garage','immobilier','batiment'],
  report_to text not null default 'docheanthony@gmail.com',
  updated_at timestamptz not null default now()
);
insert into clicandsite.mail_settings(id) values (1) on conflict do nothing;

create table if not exists clicandsite.mail_recipients (
  prospect_id uuid primary key references clicandsite.prospects(id) on delete cascade,
  email text not null,
  status text not null default 'en cours' check (status in ('en cours','envoyé','échec','désinscrit')),
  attempts int not null default 0,
  template text,
  gmail_id text,
  sent_at timestamptz,
  last_error text,
  created_at timestamptz not null default now()
);
create index if not exists mail_recipients_sent_idx on clicandsite.mail_recipients (sent_at);

create table if not exists clicandsite.mail_runs (
  run_date date primary key,
  status text not null default 'pending',
  sent int not null default 0,
  failed int not null default 0,
  token_failures int not null default 0,
  started_at timestamptz,
  finished_at timestamptz,
  report_sent_at timestamptz,
  alert_sent_at timestamptz,
  details jsonb
);

alter table clicandsite.mail_settings enable row level security;
alter table clicandsite.mail_recipients enable row level security;
alter table clicandsite.mail_runs enable row level security;

insert into clicandsite.secrets(name, value)
values ('mail_internal', encode(gen_random_bytes(24), 'hex'))
on conflict (name) do nothing;

-- Admin : état et réglages du robot d'envoi
create or replace function public.cs_admin_mail_status()
returns jsonb language plpgsql security definer set search_path = clicandsite, public as $$
declare r jsonb;
begin
  if not cs_is_admin() then raise exception 'forbidden'; end if;
  select jsonb_build_object(
    'settings', (select to_jsonb(s) from mail_settings s where id = 1),
    'today', (select to_jsonb(m) from mail_runs m where run_date = (now() at time zone 'Europe/Paris')::date),
    'sent_total', (select count(*) from mail_recipients where status = 'envoyé'),
    'unsubscribed', (select count(*) from mail_recipients where status = 'désinscrit'),
    'ready', (select count(*) from prospects p where p.email is not null and p.status in ('nouveau','a_contacter')
               and coalesce(p.site_status,'aucun') <> 'moderne'
               and not exists (select 1 from mail_recipients r where r.prospect_id = p.id)
               and not exists (select 1 from opposition o where lower(o.value) = lower(p.email)))
  ) into r;
  return r;
end $$;

create or replace function public.cs_admin_mail_settings(p_enabled boolean, p_daily_limit int, p_trades text[])
returns jsonb language plpgsql security definer set search_path = clicandsite, public as $$
begin
  if not cs_is_admin() then raise exception 'forbidden'; end if;
  update mail_settings set enabled = coalesce(p_enabled, enabled),
    daily_limit = least(200, greatest(0, coalesce(p_daily_limit, daily_limit))),
    trades = coalesce(p_trades, trades), updated_at = now() where id = 1;
  return public.cs_admin_mail_status();
end $$;

revoke all on function public.cs_admin_mail_status() from public, anon;
revoke all on function public.cs_admin_mail_settings(boolean, int, text[]) from public, anon;
grant execute on function public.cs_admin_mail_status() to authenticated;
grant execute on function public.cs_admin_mail_settings(boolean, int, text[]) to authenticated;
