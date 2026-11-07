-- 07/11/2026 (Claude, demande d'Anthony) : CRM de la formule Premium. Les demandes envoyées par les sites clients arrivent ici.
create table clicandsite.leads (
  id uuid primary key default gen_random_uuid(),
  site_id uuid not null references clicandsite.sites(id) on delete cascade,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  kind text not null default 'contact' check (kind in ('contact','reservation','rendez-vous','devis','commande','rappel','estimation','reprise')),
  name text, phone text, email text, message text,
  fields jsonb not null default '[]'::jsonb,
  page text,
  contact_key text,
  status text not null default 'nouveau' check (status in ('nouveau','en_cours','gagne','perdu','archive')),
  follow_up_at timestamptz,
  seen_at timestamptz,
  ip_hash text
);
create index leads_site_idx on clicandsite.leads(site_id, created_at desc);
create index leads_rate_idx on clicandsite.leads(ip_hash, created_at);
alter table clicandsite.leads enable row level security;

create table clicandsite.lead_notes (
  id bigint generated always as identity primary key,
  lead_id uuid not null references clicandsite.leads(id) on delete cascade,
  at timestamptz not null default now(),
  by_email text,
  kind text not null default 'note' check (kind in ('note','appel','email','rdv','statut','relance')),
  content text not null
);
create index lead_notes_lead_idx on clicandsite.lead_notes(lead_id, at desc);
alter table clicandsite.lead_notes enable row level security;
revoke all on clicandsite.leads, clicandsite.lead_notes from anon, authenticated;

create or replace function public.cs_site_premium(p_site uuid) returns boolean
language sql stable security definer set search_path to '' as $$
  select public.cs_is_admin() or exists (select 1 from clicandsite.sites s where s.id = p_site and lower(coalesce(s.plan,'')) like 'premium%');
$$;

create or replace function public.cs_lead_site(p_lead uuid) returns uuid
language sql stable security definer set search_path to '' as $$
  select l.site_id from clicandsite.leads l where l.id = p_lead and public.cs_can_edit_site(l.site_id);
$$;

-- Envoi depuis un site client (public)
create or replace function public.cs_lead_submit(p_slug text, p_kind text, p_name text, p_phone text, p_email text, p_message text, p_fields jsonb, p_page text, p_hp text default null)
returns json language plpgsql volatile security definer set search_path to '' as $$
declare s clicandsite.sites; ip text; h text; f jsonb := '[]'::jsonb; e jsonb; ph text; em text;
begin
  if coalesce(p_hp,'') <> '' then return json_build_object('ok', true); end if; -- robot : on fait comme si
  select * into s from clicandsite.sites where slug = lower(p_slug) and status = 'en_ligne';
  if s.id is null then raise exception 'Site introuvable'; end if;
  ph := nullif(left(regexp_replace(coalesce(p_phone,''), '[^0-9+ .()-]', '', 'g'), 30), '');
  em := nullif(lower(left(trim(coalesce(p_email,'')), 160)), '');
  if em is not null and em !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$' then raise exception 'E-mail invalide'; end if;
  if ph is null and em is null then raise exception 'Indiquez un téléphone ou un e-mail'; end if;
  if ph is not null and length(regexp_replace(ph,'[^0-9]','','g')) < 8 then raise exception 'Téléphone invalide'; end if;
  begin ip := split_part(coalesce(current_setting('request.headers', true)::json->>'x-forwarded-for',''), ',', 1); exception when others then ip := ''; end;
  h := encode(extensions.digest(coalesce(ip,'') || ':' || s.id::text, 'sha256'), 'hex');
  if (select count(*) from clicandsite.leads where ip_hash = h and created_at > now() - interval '10 minutes') >= 5
     or (select count(*) from clicandsite.leads where site_id = s.id and created_at > now() - interval '1 day') >= 300 then
    raise exception 'Trop de demandes, réessayez plus tard';
  end if;
  if jsonb_typeof(p_fields) = 'array' then
    for e in select * from jsonb_array_elements(p_fields) limit 20 loop
      if jsonb_typeof(e) = 'object' and coalesce(e->>'v','') <> '' then
        f := f || jsonb_build_array(jsonb_build_object('l', left(coalesce(e->>'l',''), 80), 'v', left(e->>'v', 500)));
      end if;
    end loop;
  end if;
  insert into clicandsite.leads (site_id, kind, name, phone, email, message, fields, page, contact_key, ip_hash)
  values (s.id, case when p_kind in ('contact','reservation','rendez-vous','devis','commande','rappel','estimation','reprise') then p_kind else 'contact' end,
          nullif(left(trim(coalesce(p_name,'')), 120), ''), ph, em, nullif(left(trim(coalesce(p_message,'')), 2000), ''), f, left(p_page, 300),
          coalesce(em, nullif(regexp_replace(coalesce(ph,''),'[^0-9]','','g'),'')), h);
  return json_build_object('ok', true);
end $$;

-- Liste pour l'espace client (tous les plans voient leurs demandes ; le suivi est Premium)
create or replace function public.cs_leads(p_site uuid) returns json
language plpgsql volatile security definer set search_path to '' as $$
declare r json; prem boolean;
begin
  if not public.cs_can_edit_site(p_site) then raise exception 'Accès refusé'; end if;
  prem := public.cs_site_premium(p_site);
  select coalesce(json_agg(x order by x.created_at desc), '[]') into r from (
    select l.id, l.created_at, l.kind, l.name, l.phone, l.email, l.message, l.fields, l.contact_key, l.status, l.follow_up_at, (l.seen_at is null) as unseen,
      (select count(*) from clicandsite.lead_notes n where n.lead_id = l.id and n.kind <> 'statut') as notes
    from clicandsite.leads l where l.site_id = p_site order by l.created_at desc limit 1000) x;
  if not public.cs_is_admin() then update clicandsite.leads set seen_at = now() where site_id = p_site and seen_at is null; end if;
  return json_build_object('premium', prem, 'leads', r);
end $$;

create or replace function public.cs_lead_update(p_id uuid, p_status text default null, p_follow_up timestamptz default null, p_set_follow boolean default false)
returns json language plpgsql volatile security definer set search_path to '' as $$
declare sid uuid := public.cs_lead_site(p_id); old clicandsite.leads; lab json := '{"nouveau":"Nouvelle","en_cours":"En cours","gagne":"Gagnée","perdu":"Perdue","archive":"Archivée"}';
begin
  if sid is null then raise exception 'Accès refusé'; end if;
  if not public.cs_site_premium(sid) then raise exception 'Le suivi des demandes est inclus dans la formule Premium'; end if;
  select * into old from clicandsite.leads where id = p_id;
  if p_status is not null and p_status <> old.status then
    if p_status not in ('nouveau','en_cours','gagne','perdu','archive') then raise exception 'Statut inconnu'; end if;
    update clicandsite.leads set status = p_status, updated_at = now() where id = p_id;
    insert into clicandsite.lead_notes (lead_id, by_email, kind, content) values (p_id, public.cs_my_email(), 'statut', 'Statut : ' || coalesce(lab->>p_status, p_status));
  end if;
  if p_set_follow then
    update clicandsite.leads set follow_up_at = p_follow_up, updated_at = now() where id = p_id;
    insert into clicandsite.lead_notes (lead_id, by_email, kind, content) values (p_id, public.cs_my_email(), 'relance',
      case when p_follow_up is null then 'Relance retirée' else 'Relance prévue le ' || to_char(p_follow_up at time zone 'Europe/Paris', 'DD/MM/YYYY') end);
  end if;
  return (select json_build_object('id', id, 'status', status, 'follow_up_at', follow_up_at) from clicandsite.leads where id = p_id);
end $$;

create or replace function public.cs_lead_add_note(p_id uuid, p_kind text, p_text text) returns json
language plpgsql volatile security definer set search_path to '' as $$
declare sid uuid := public.cs_lead_site(p_id); n clicandsite.lead_notes;
begin
  if sid is null then raise exception 'Accès refusé'; end if;
  if not public.cs_site_premium(sid) then raise exception 'Le suivi des demandes est inclus dans la formule Premium'; end if;
  if coalesce(trim(p_text),'') = '' then raise exception 'Note vide'; end if;
  insert into clicandsite.lead_notes (lead_id, by_email, kind, content)
  values (p_id, public.cs_my_email(), case when p_kind in ('note','appel','email','rdv') then p_kind else 'note' end, left(trim(p_text), 2000)) returning * into n;
  update clicandsite.leads set updated_at = now(), status = case when status = 'nouveau' then 'en_cours' else status end where id = p_id;
  return json_build_object('id', n.id, 'at', n.at, 'kind', n.kind, 'content', n.content);
end $$;

create or replace function public.cs_lead_history(p_id uuid) returns json
language plpgsql stable security definer set search_path to '' as $$
declare sid uuid := public.cs_lead_site(p_id);
begin
  if sid is null then raise exception 'Accès refusé'; end if;
  if not public.cs_site_premium(sid) then return '[]'::json; end if;
  return (select coalesce(json_agg(json_build_object('id', id, 'at', at, 'kind', kind, 'content', content) order by at desc), '[]') from clicandsite.lead_notes where lead_id = p_id);
end $$;

-- Suppression (demande d'un client final, RGPD) : tous les plans
create or replace function public.cs_lead_delete(p_id uuid) returns boolean
language plpgsql volatile security definer set search_path to '' as $$
begin
  if public.cs_lead_site(p_id) is null then raise exception 'Accès refusé'; end if;
  delete from clicandsite.leads where id = p_id;
  return true;
end $$;

create or replace function public.cs_admin_site_plan(p_slug text, p_plan text) returns boolean
language plpgsql volatile security definer set search_path to '' as $$
begin
  if not public.cs_is_admin() then raise exception 'Accès réservé à l''administrateur'; end if;
  if p_plan is not null and lower(p_plan) not in ('essentiel','pro','premium') then raise exception 'Formule inconnue'; end if;
  update clicandsite.sites set plan = lower(p_plan), updated_at = now() where slug = lower(p_slug);
  return found;
end $$;

create or replace function public.cs_my_sites() returns json
language plpgsql stable security definer set search_path to '' as $$
declare em text := public.cs_my_email(); adm boolean := public.cs_is_admin();
begin
  if em is null then return '[]'::json; end if;
  return (select coalesce(json_agg(x order by x.name),'[]') from (
    select s.id, s.slug, s.name, s.trade, s.style, s.domain, s.status, s.content, s.updated_at, s.plan,
      (adm or lower(coalesce(s.plan,'')) like 'premium%') as premium,
      (select count(*) from clicandsite.leads l where l.site_id = s.id and l.seen_at is null) as leads_new,
      (select count(*) from clicandsite.leads l where l.site_id = s.id and l.follow_up_at <= now() and l.status in ('nouveau','en_cours')) as leads_due
    from clicandsite.sites s where adm or (lower(s.owner_email) = em and s.status <> 'suspendu')) x);
end $$;

-- Purge : demandes de plus de 3 ans (RGPD)
select cron.schedule('cs-leads-purge', '17 3 * * 0', $$delete from clicandsite.leads where created_at < now() - interval '3 years'$$);

revoke all on function public.cs_site_premium(uuid), public.cs_lead_site(uuid) from public, anon, authenticated;
revoke all on function public.cs_lead_submit(text,text,text,text,text,text,jsonb,text,text), public.cs_leads(uuid), public.cs_lead_update(uuid,text,timestamptz,boolean), public.cs_lead_add_note(uuid,text,text), public.cs_lead_history(uuid), public.cs_lead_delete(uuid), public.cs_admin_site_plan(text,text) from public;
grant execute on function public.cs_lead_submit(text,text,text,text,text,text,jsonb,text,text) to anon, authenticated;
grant execute on function public.cs_leads(uuid), public.cs_lead_update(uuid,text,timestamptz,boolean), public.cs_lead_add_note(uuid,text,text), public.cs_lead_history(uuid), public.cs_lead_delete(uuid), public.cs_admin_site_plan(text,text) to authenticated;