-- 08/11/2026 (Anthony) : flux API direct MyCreativeSite → Abracadeal pour le Pack Auto & Immo.
create table if not exists clicandsite.abracadeal_sync (
  site_id uuid primary key references clicandsite.sites(id) on delete cascade,
  agency_status text, last_hash text, last_result jsonb, last_error text,
  synced_at timestamptz, stopped_at timestamptz, updated_at timestamptz not null default now()
);
alter table clicandsite.abracadeal_sync enable row level security;
insert into clicandsite.secrets(name,value) values('abracadeal_partner_key','<clé éditeur Abracadeal, stockée en base>')
  on conflict do nothing;

-- Sites à traiter : packs Auto & Immo payés (garage / immobilier) + anciens packs encore diffusés à arrêter.
create or replace function public.cs_abra_targets()
 returns jsonb language sql stable security definer set search_path to '' as $$
 select coalesce(jsonb_agg(x),'[]'::jsonb) from (
  select s.id, s.slug, s.name, s.trade, s.owner_email,
         (lower(coalesce(s.plan,''))='autoimmo' and s.paid_at is not null and s.trade in ('garage','immobilier')
           and coalesce(s.billing_status,'active') not in ('canceled','unpaid','incomplete_expired')) as eligible,
         coalesce(s.content->'items','[]'::jsonb) as items,
         coalesce(p.data,'{}'::jsonb) as profile,
         a.agency_status, a.last_hash
    from clicandsite.sites s
    left join clicandsite.pro_profiles p on p.site_id=s.id
    left join clicandsite.abracadeal_sync a on a.site_id=s.id
   where (lower(coalesce(s.plan,''))='autoimmo' and s.paid_at is not null and s.trade in ('garage','immobilier'))
      or (a.site_id is not null and coalesce(a.agency_status,'')<>'stopped')
 ) x $$;
create or replace function public.cs_abra_mark(p_site uuid, p_status text, p_hash text, p_result jsonb, p_error text)
 returns void language sql security definer set search_path to '' as $$
 insert into clicandsite.abracadeal_sync(site_id,agency_status,last_hash,last_result,last_error,synced_at,stopped_at,updated_at)
 values(p_site,p_status,p_hash,p_result,p_error,now(),case when p_status='stopped' then now() end,now())
 on conflict (site_id) do update set agency_status=excluded.agency_status,
   last_hash=coalesce(excluded.last_hash,clicandsite.abracadeal_sync.last_hash), last_result=excluded.last_result,
   last_error=excluded.last_error, synced_at=now(), stopped_at=excluded.stopped_at, updated_at=now() $$;
create or replace function public.cs_abra_key() returns text language sql stable security definer set search_path to '' as $$
 select value from clicandsite.secrets where name='abracadeal_partner_key' $$;
revoke all on function public.cs_abra_targets() from public, anon, authenticated;
revoke all on function public.cs_abra_mark(uuid,text,text,jsonb,text) from public, anon, authenticated;
revoke all on function public.cs_abra_key() from public, anon, authenticated;
grant execute on function public.cs_abra_targets() to service_role;
grant execute on function public.cs_abra_mark(uuid,text,text,jsonb,text) to service_role;
grant execute on function public.cs_abra_key() to service_role;

-- Clé interne du cron + fonction (valeur stockée en base, pas ici)
-- insert into clicandsite.secrets(name,value) values('abracadeal_sync_internal','<secret>');
create or replace function public.cs_abra_internal_key() returns text language sql stable security definer set search_path to '' as $$
 select value from clicandsite.secrets where name='abracadeal_sync_internal' $$;
revoke all on function public.cs_abra_internal_key() from public, anon, authenticated;
grant execute on function public.cs_abra_internal_key() to service_role;
-- Cron toutes les 10 min : cs-abracadeal-sync (en-tête x-cs-key)

-- 08/11/2026 : infos saisies au paiement du pack (SIRET, adresse…) → profil du site (cs_abra_profile, appelée par le webhook Stripe)
create or replace function public.cs_abra_profile(p_slug text, p_data jsonb)
 returns uuid language plpgsql security definer set search_path to '' as $$
declare v_site uuid; v_cur jsonb; v_new jsonb; k text;
begin
  select id into v_site from clicandsite.sites where slug=lower(p_slug);
  if v_site is null then return null; end if;
  select data into v_cur from clicandsite.pro_profiles where site_id=v_site;
  v_new := coalesce(v_cur,'{}'::jsonb);
  for k in select jsonb_object_keys(coalesce(p_data,'{}'::jsonb)) loop
    if coalesce(p_data->>k,'')='' then continue; end if;
    if k='siret' or coalesce(v_new->>k,'')='' then v_new := v_new || jsonb_build_object(k, p_data->>k); end if;
  end loop;
  insert into clicandsite.pro_profiles(site_id,data,updated_at) values(v_site,v_new,now())
  on conflict (site_id) do update set data=excluded.data, updated_at=now();
  return v_site;
end $$;
revoke all on function public.cs_abra_profile(text,jsonb) from public, anon, authenticated;
grant execute on function public.cs_abra_profile(text,jsonb) to service_role;

-- 08/11/2026 : CRM inclus dans le Pack Auto & Immo (cs_site_premium, cs_my_sites) et état de la diffusion pour l'espace client
-- (cs_abra_status(p_site) : propriétaire du site ou admin). Appliqué via les migrations crm_autoimmo_20261108,
-- crm_autoimmo_my_sites_20261108 et cs_abra_status_20261108.
-- 08/11/2026 : diffusion des artisans, dépannage, beauté, bien-être et boutiques à partir de la formule Pro (migration abracadeal_from_pro_20261108).
-- 09/11/2026 : diffusion Abracadeal seulement à 99 € (Pack Auto & Immo, Boutique) — migration abracadeal_only_99_20261109.
