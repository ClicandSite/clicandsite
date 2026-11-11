-- 07/11/2026 (Claude, demande d'Anthony) : site bilingue français / anglais.
-- content.en = { on: bool, dict: { "texte français": "English text" } } (traduction de tous les textes de la page)
-- Droit : formules Premium et Boutique, ou option bilingue (+10 €/mois) cochée par l'admin (sites.bilingual).
alter table clicandsite.sites add column if not exists bilingual boolean not null default false;

create table if not exists clicandsite.tr_cache (src text primary key, en text not null, at timestamptz not null default now());
alter table clicandsite.tr_cache enable row level security;

create or replace function public.cs_site_bilingual(p_site uuid) returns boolean
language sql stable security definer set search_path to '' as $$
  select exists (select 1 from clicandsite.sites s where s.id = p_site
    and (s.bilingual or lower(coalesce(s.plan,'')) ~ '^(premium|boutique)'));
$$;

-- contenu public : la version anglaise n'est envoyée que si le site y a droit et l'a activée
create or replace function public.cs_public_content(s clicandsite.sites) returns jsonb
language sql stable security definer set search_path to '' as $$
  select case when coalesce((s.content->'en'->>'on')::boolean, false) and public.cs_site_bilingual(s.id)
    then s.content else s.content - 'en' end;
$$;

create or replace function public.cs_site_content(p_slug text) returns json
language sql stable security definer set search_path to '' as $$
  select (public.cs_public_content(s) || jsonb_build_object('style', s.style)
    || case when s.trade = 'boutique' then jsonb_build_object('shop', public.cs_shop_public(s.id)) else '{}'::jsonb end
    || coalesce(case when s.trade <> 'boutique' then jsonb_strip_nulls(jsonb_build_object('pay', public.cs_pay_public(s.id))) end, '{}'::jsonb))::json
  from clicandsite.sites s where s.slug = p_slug and s.status = 'en_ligne';
$$;

create or replace function public.cs_site_preview(p_slug text) returns json
language sql stable security definer set search_path to '' as $$
  select json_build_object('name', s.name, 'trade', s.trade, 'style', s.style, 'plan', s.plan, 'status', s.status,
    'paid', coalesce(s.billing_status in ('active','trialing'), false),
    'content', (public.cs_public_content(s) || jsonb_build_object('style', s.style) || case when s.trade = 'boutique' then jsonb_build_object('shop', public.cs_shop_public(s.id)) else '{}'::jsonb end))
  from clicandsite.sites s where s.slug = lower(p_slug) and s.status in ('brouillon','en_ligne');
$$;

create or replace function public.cs_my_sites() returns json
language plpgsql stable security definer set search_path to '' as $$
declare em text := public.cs_my_email(); adm boolean := public.cs_is_admin();
begin
  if em is null then return '[]'::json; end if;
  return (select coalesce(json_agg(x order by x.name),'[]') from (
    select s.id, s.slug, s.name, s.trade, s.style, s.domain, s.status, s.content, s.updated_at, s.plan, s.billing_status, s.paid_at,
      (adm or lower(coalesce(s.plan,'')) like 'premium%' or lower(coalesce(s.plan,'')) like 'boutique%') as premium,
      (adm or public.cs_site_bilingual(s.id)) as bilingual,
      (select count(*) from clicandsite.leads l where l.site_id = s.id and l.seen_at is null) as leads_new,
      (select count(*) from clicandsite.leads l where l.site_id = s.id and l.follow_up_at <= now() and l.status in ('nouveau','en_cours')) as leads_due
    from clicandsite.sites s where adm or (lower(s.owner_email) = em and s.status <> 'suspendu')) x);
end $$;

create or replace function public.cs_admin_sites() returns json
language plpgsql security definer set search_path to '' as $$
begin
  if not public.cs_is_admin() then raise exception 'Accès réservé à l''administrateur'; end if;
  return (select coalesce(json_agg(x order by x.created_at desc),'[]') from (
    select s.id, s.slug, s.name, s.trade, s.style, s.owner_email, s.domain, s.status, s.plan, s.billing_status, s.created_at, s.updated_at, s.bilingual,
      coalesce((s.content->'en'->>'on')::boolean, false) as en_on,
      case when coalesce(s.content->'google'->>'done','') = 'true' then 'fait'
           when lower(coalesce(s.plan,'')) in ('pro','premium','boutique') and coalesce(nullif(s.content->'google'->>'url',''), nullif(b.data->>'google','')) is not null then 'a_faire' end as avis_google,
      coalesce(nullif(s.content->'google'->>'url',''), nullif(b.data->>'google','')) as google_url
    from clicandsite.sites s left join clicandsite.site_briefs b on b.site_id = s.id) x);
end $$;

create or replace function public.cs_admin_site_bilingual(p_slug text, p_on boolean) returns boolean
language plpgsql security definer set search_path to '' as $$
begin
  if not public.cs_is_admin() then raise exception 'Accès réservé à l''administrateur'; end if;
  update clicandsite.sites set bilingual = coalesce(p_on,false), updated_at = now() where slug = lower(p_slug);
  return found;
end $$;

-- cache des traductions (partagé entre les sites : les textes des modèles ne sont traduits qu'une fois)
create or replace function public.cs_tr_cache_get(p_src text[]) returns json
language sql stable security definer set search_path to '' as $$
  select coalesce(json_object_agg(src, en), '{}'::json) from clicandsite.tr_cache where src = any(p_src);
$$;
create or replace function public.cs_tr_cache_put(p_rows jsonb) returns void
language sql security definer set search_path to '' as $$
  insert into clicandsite.tr_cache (src, en) select key, value #>> '{}' from jsonb_each(p_rows)
  where length(key) <= 4000 and length(value #>> '{}') between 1 and 6000
  on conflict (src) do update set en = excluded.en, at = now();
$$;
revoke all on function public.cs_tr_cache_get(text[]), public.cs_tr_cache_put(jsonb), public.cs_public_content(clicandsite.sites) from public, anon, authenticated;
grant execute on function public.cs_tr_cache_get(text[]), public.cs_tr_cache_put(jsonb) to service_role;
grant execute on function public.cs_site_bilingual(uuid) to anon, authenticated;
grant execute on function public.cs_admin_site_bilingual(text, boolean) to authenticated;
