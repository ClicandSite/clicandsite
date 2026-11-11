-- 09/11/2026 (Claude, demande d'Anthony) — Agenda des sites clients : créneaux libres en ligne, sinon bouton « Appeler ».
-- Métiers concernés : beaute, bienetre, restaurant, garage (atelier). Réservation confirmée d'office.
-- Réglages dans sites.agenda (jsonb) :
--   on (bool), step (minutes entre deux créneaux proposés), duree (minutes occupées par une réservation),
--   places (places par créneau : coiffeurs, praticiens, postes atelier, ou couverts au restaurant),
--   week {"0".."6" : [["09:00","12:00"],["14:00","19:00"]]} (0 = dimanche), closed ["AAAA-MM-JJ", …],
--   notice (heures de délai minimum), ahead (jours de réservation à l'avance), maxparty (restaurant : couverts max par réservation)

alter table clicandsite.sites add column if not exists agenda jsonb;

create table if not exists clicandsite.bookings (
  id uuid primary key default gen_random_uuid(),
  site_id uuid not null references clicandsite.sites(id) on delete cascade,
  starts_at timestamptz not null,
  minutes int not null check (minutes between 5 and 720),
  places int not null default 1 check (places between 1 and 500),
  status text not null default 'confirme' check (status in ('confirme','annule','bloque')),
  source text not null default 'site' check (source in ('site','pro')),
  lead_id uuid references clicandsite.leads(id) on delete set null,
  name text, phone text, email text, service text, note text,
  created_at timestamptz not null default now(),
  cancelled_at timestamptz
);
create index if not exists bookings_site_start on clicandsite.bookings (site_id, starts_at);
alter table clicandsite.bookings enable row level security;

create or replace function public.cs_agenda_trade(t text) returns boolean language sql immutable set search_path to '' as $$
  select t in ('beaute','bienetre','restaurant','garage');
$$;

-- Réglages nettoyés (valeurs par défaut comprises)
create or replace function public.cs_agenda_cfg(a jsonb) returns jsonb language plpgsql immutable set search_path to '' as $$
declare w jsonb := '{}'::jsonb; d int; r jsonb; rr jsonb; c jsonb := '[]'::jsonb; x text; st int; du int;
begin
  a := coalesce(a, '{}'::jsonb);
  st := least(240, greatest(10, coalesce((a->>'step')::int, 30)));
  du := least(720, greatest(10, coalesce((a->>'duree')::int, st)));
  for d in 0..6 loop
    rr := '[]'::jsonb;
    if jsonb_typeof(a->'week'->(d::text)) = 'array' then
      for r in select * from jsonb_array_elements(a->'week'->(d::text)) limit 4 loop
        if jsonb_typeof(r) = 'array' and (r->>0) ~ '^([01]\d|2[0-3]):[0-5]\d$' and (r->>1) ~ '^([01]\d|2[0-3]):[0-5]\d$|^24:00$' and (r->>0) < (r->>1) then
          rr := rr || jsonb_build_array(jsonb_build_array(r->>0, r->>1));
        end if;
      end loop;
    end if;
    w := w || jsonb_build_object(d::text, rr);
  end loop;
  if jsonb_typeof(a->'closed') = 'array' then
    for x in select jsonb_array_elements_text(a->'closed') limit 200 loop
      if x ~ '^\d{4}-\d{2}-\d{2}$' then c := c || to_jsonb(x); end if;
    end loop;
  end if;
  return jsonb_build_object('on', coalesce((a->>'on')::boolean, false), 'step', st, 'duree', du,
    'places', least(500, greatest(1, coalesce((a->>'places')::int, 1))), 'week', w, 'closed', c,
    'notice', least(168, greatest(0, coalesce((a->>'notice')::int, 2))),
    'ahead', least(120, greatest(1, coalesce((a->>'ahead')::int, 30))),
    'maxparty', least(100, greatest(1, coalesce((a->>'maxparty')::int, 8))));
end $$;

-- Créneaux d'un site entre deux dates : [{d:'AAAA-MM-JJ', t:'HH:MM', left:n}]
create or replace function public.cs_agenda_slots(p_site uuid, p_from date, p_days int) returns jsonb
language plpgsql stable security definer set search_path to '' as $$
declare s clicandsite.sites; a jsonb; out jsonb := '[]'::jsonb; d date; r jsonb; m0 int; m1 int; m int;
  st timestamptz; used int; lim timestamptz; last date;
begin
  select * into s from clicandsite.sites where id = p_site;
  if s.id is null then return out; end if;
  a := public.cs_agenda_cfg(s.agenda);
  lim := now() + make_interval(hours => (a->>'notice')::int);
  last := (now() at time zone 'Europe/Paris')::date + (a->>'ahead')::int;
  for d in select generate_series(greatest(p_from, (now() at time zone 'Europe/Paris')::date), least(p_from + greatest(1, least(p_days, 62)) - 1, last), interval '1 day')::date loop
    continue when a->'closed' ? to_char(d, 'YYYY-MM-DD');
    for r in select * from jsonb_array_elements(a->'week'->(extract(dow from d)::int::text)) loop
      m0 := split_part(r->>0,':',1)::int*60 + split_part(r->>0,':',2)::int;
      m1 := split_part(r->>1,':',1)::int*60 + split_part(r->>1,':',2)::int;
      m := m0;
      while m + (a->>'duree')::int <= m1 loop
        st := (d + make_interval(mins => m)) at time zone 'Europe/Paris';
        if st >= lim then
          select coalesce(sum(b.places), 0) into used from clicandsite.bookings b
            where b.site_id = s.id and b.status in ('confirme','bloque')
              and b.starts_at < st + make_interval(mins => (a->>'duree')::int)
              and b.starts_at + make_interval(mins => b.minutes) > st;
          out := out || jsonb_build_array(jsonb_build_object('d', to_char(d,'YYYY-MM-DD'), 't', lpad((m/60)::text,2,'0')||':'||lpad((m%60)::text,2,'0'), 'left', greatest(0, (a->>'places')::int - used)));
        end if;
        m := m + (a->>'step')::int;
      end loop;
    end loop;
  end loop;
  return out;
end $$;

-- Public : état de l'agenda pour le site (créneaux sur p_days jours à partir de p_from)
create or replace function public.cs_agenda_public(p_slug text, p_from date default null, p_days int default 14) returns json
language plpgsql stable security definer set search_path to '' as $$
declare s clicandsite.sites; a jsonb;
begin
  select * into s from clicandsite.sites where slug = lower(p_slug) and status <> 'suspendu';
  if s.id is null or not public.cs_agenda_trade(s.trade) then return json_build_object('on', false); end if;
  a := public.cs_agenda_cfg(s.agenda);
  if not (a->>'on')::boolean then return json_build_object('on', false); end if;
  return json_build_object('on', true, 'step', a->'step', 'duree', a->'duree', 'unit', case when s.trade = 'restaurant' then 'couverts' else 'places' end,
    'maxparty', case when s.trade = 'restaurant' then least((a->>'maxparty')::int, (a->>'places')::int) else 1 end,
    'ahead', a->'ahead', 'slots', public.cs_agenda_slots(s.id, coalesce(p_from, (now() at time zone 'Europe/Paris')::date), p_days));
end $$;

-- Public : réserver un créneau (confirmé d'office). p_lead = false quand la demande part par le paiement en ligne (cs-shop crée la demande).
create or replace function public.cs_booking_submit(p_slug text, p_day text, p_time text, p_party int, p_service text, p_name text, p_phone text, p_email text,
  p_message text, p_fields jsonb, p_page text, p_hp text default null, p_lead boolean default true) returns json
language plpgsql security definer set search_path to '' as $$
declare s clicandsite.sites; a jsonb; d date; t time; st timestamptz; party int; ok boolean := false; r jsonb;
  ph text; em text; ip text; h text; f jsonb := '[]'::jsonb; e jsonb; lid uuid; bid uuid; lbl text;
begin
  if coalesce(p_hp,'') <> '' then return json_build_object('ok', true); end if;
  select * into s from clicandsite.sites where slug = lower(p_slug) and status = 'en_ligne' for update;
  if s.id is null or not public.cs_agenda_trade(s.trade) then raise exception 'Site introuvable'; end if;
  a := public.cs_agenda_cfg(s.agenda);
  if not (a->>'on')::boolean then raise exception 'La réservation en ligne n''est pas ouverte : appelez directement'; end if;
  if p_day !~ '^\d{4}-\d{2}-\d{2}$' or p_time !~ '^\d{2}:\d{2}$' then raise exception 'Choisissez un créneau'; end if;
  d := p_day::date; t := p_time::time; st := (d + t) at time zone 'Europe/Paris';
  party := case when s.trade = 'restaurant' then least(greatest(coalesce(p_party,1),1), (a->>'maxparty')::int) else 1 end;
  if coalesce(trim(p_name),'') = '' then raise exception 'Indiquez votre nom'; end if;
  ph := nullif(left(regexp_replace(coalesce(p_phone,''), '[^0-9+ .()-]', '', 'g'), 30), '');
  em := nullif(lower(left(trim(coalesce(p_email,'')), 160)), '');
  if em is not null and em !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$' then raise exception 'E-mail invalide'; end if;
  if ph is null and em is null then raise exception 'Indiquez un téléphone ou un e-mail'; end if;
  if ph is not null and length(regexp_replace(ph,'[^0-9]','','g')) < 8 then raise exception 'Téléphone invalide'; end if;
  begin ip := split_part(coalesce(current_setting('request.headers', true)::json->>'x-forwarded-for',''), ',', 1); exception when others then ip := ''; end;
  h := encode(extensions.digest(coalesce(ip,'') || ':' || s.id::text, 'sha256'), 'hex');
  if (select count(*) from clicandsite.leads where ip_hash = h and created_at > now() - interval '10 minutes') >= 5
     or (select count(*) from clicandsite.bookings where site_id = s.id and source = 'site' and created_at > now() - interval '1 day') >= 300 then
    raise exception 'Trop de demandes, réessayez plus tard';
  end if;
  -- le créneau doit exister dans les horaires et rester libre
  for r in select * from jsonb_array_elements(public.cs_agenda_slots(s.id, d, 1)) loop
    if r->>'t' = to_char(t,'HH24:MI') then ok := (r->>'left')::int >= party; exit; end if;
  end loop;
  if not ok then raise exception 'Ce créneau vient d''être pris ou n''est plus disponible. Choisissez-en un autre.'; end if;
  lbl := to_char(d, 'DD/MM/YYYY') || ' à ' || replace(to_char(t,'HH24:MI'), ':', 'h') || case when s.trade = 'restaurant' then ' · ' || party || ' couvert' || case when party > 1 then 's' else '' end else '' end;
  f := jsonb_build_array(jsonb_build_object('l','Créneau réservé (confirmé)','v', lbl));
  if jsonb_typeof(p_fields) = 'array' then
    for e in select * from jsonb_array_elements(p_fields) limit 20 loop
      if jsonb_typeof(e) = 'object' and coalesce(e->>'v','') <> '' then f := f || jsonb_build_array(jsonb_build_object('l', left(coalesce(e->>'l',''), 80), 'v', left(e->>'v', 500))); end if;
    end loop;
  end if;
  if p_lead then
    insert into clicandsite.leads (site_id, kind, name, phone, email, message, fields, page, contact_key, ip_hash)
    values (s.id, case when s.trade = 'restaurant' then 'reservation' else 'rendez-vous' end, left(trim(p_name),120), ph, em,
      nullif(left(trim(coalesce(p_message,'')), 2000), ''), f, left(p_page, 300), coalesce(em, nullif(regexp_replace(coalesce(ph,''),'[^0-9]','','g'),'')), h)
    returning id into lid;
  end if;
  insert into clicandsite.bookings (site_id, starts_at, minutes, places, status, source, lead_id, name, phone, email, service, note)
  values (s.id, st, (a->>'duree')::int, party, 'confirme', 'site', lid, left(trim(p_name),120), ph, em, nullif(left(trim(coalesce(p_service,'')),200),''), nullif(left(trim(coalesce(p_message,'')),500),''))
  returning id into bid;
  return json_build_object('ok', true, 'booking', bid, 'label', lbl);
end $$;

-- Espace client : réglages + réservations
create or replace function public.cs_agenda_get(p_site uuid, p_from date, p_to date) returns json
language plpgsql stable security definer set search_path to '' as $$
declare s clicandsite.sites;
begin
  if not public.cs_can_edit_site(p_site) then raise exception 'Accès refusé'; end if;
  select * into s from clicandsite.sites where id = p_site;
  return json_build_object('trade', s.trade, 'eligible', public.cs_agenda_trade(s.trade), 'cfg', public.cs_agenda_cfg(s.agenda), 'configured', s.agenda is not null,
    'bookings', coalesce((select jsonb_agg(jsonb_build_object('id', b.id, 'd', to_char(b.starts_at at time zone 'Europe/Paris','YYYY-MM-DD'), 't', to_char(b.starts_at at time zone 'Europe/Paris','HH24:MI'),
        'minutes', b.minutes, 'places', b.places, 'status', b.status, 'source', b.source, 'name', b.name, 'phone', b.phone, 'email', b.email, 'service', b.service, 'note', b.note, 'lead', b.lead_id) order by b.starts_at)
      from clicandsite.bookings b where b.site_id = p_site and b.starts_at >= (p_from::timestamp at time zone 'Europe/Paris') and b.starts_at < ((p_to + 1)::timestamp at time zone 'Europe/Paris')), '[]'::jsonb),
    'slots', case when public.cs_agenda_trade(s.trade) then public.cs_agenda_slots(p_site, p_from, (p_to - p_from) + 1) else '[]'::jsonb end);
end $$;

create or replace function public.cs_agenda_save(p_site uuid, p_cfg jsonb) returns json
language plpgsql security definer set search_path to '' as $$
begin
  if not public.cs_can_edit_site(p_site) then raise exception 'Accès refusé'; end if;
  update clicandsite.sites set agenda = public.cs_agenda_cfg(p_cfg), updated_at = now() where id = p_site;
  return json_build_object('ok', true);
end $$;

-- Rendez-vous pris par téléphone (p_kind 'rdv') ou créneau bloqué (p_kind 'bloque')
create or replace function public.cs_agenda_add(p_site uuid, p_day text, p_time text, p_minutes int, p_places int, p_kind text, p_name text, p_phone text, p_service text, p_note text) returns json
language plpgsql security definer set search_path to '' as $$
declare st timestamptz; bid uuid;
begin
  if not public.cs_can_edit_site(p_site) then raise exception 'Accès refusé'; end if;
  if p_day !~ '^\d{4}-\d{2}-\d{2}$' or p_time !~ '^([01]\d|2[0-3]):[0-5]\d$' then raise exception 'Date ou heure invalide'; end if;
  st := (p_day::date + p_time::time) at time zone 'Europe/Paris';
  insert into clicandsite.bookings (site_id, starts_at, minutes, places, status, source, name, phone, service, note)
  values (p_site, st, least(720, greatest(5, coalesce(p_minutes, 30))), least(500, greatest(1, coalesce(p_places, 1))),
    case when p_kind = 'bloque' then 'bloque' else 'confirme' end, 'pro',
    nullif(left(trim(coalesce(p_name,'')),120),''), nullif(left(trim(coalesce(p_phone,'')),30),''), nullif(left(trim(coalesce(p_service,'')),200),''), nullif(left(trim(coalesce(p_note,'')),500),''))
  returning id into bid;
  return json_build_object('ok', true, 'id', bid);
end $$;

create or replace function public.cs_agenda_cancel(p_site uuid, p_id uuid) returns json
language plpgsql security definer set search_path to '' as $$
begin
  if not public.cs_can_edit_site(p_site) then raise exception 'Accès refusé'; end if;
  update clicandsite.bookings set status = 'annule', cancelled_at = now() where id = p_id and site_id = p_site and status <> 'annule';
  return json_build_object('ok', true);
end $$;

revoke all on function public.cs_agenda_slots(uuid, date, int) from public, anon, authenticated;
grant execute on function public.cs_agenda_public(text, date, int) to anon, authenticated;
grant execute on function public.cs_booking_submit(text, text, text, int, text, text, text, text, text, jsonb, text, text, boolean) to anon, authenticated;
revoke all on function public.cs_agenda_get(uuid, date, date) from public, anon; grant execute on function public.cs_agenda_get(uuid, date, date) to authenticated;
revoke all on function public.cs_agenda_save(uuid, jsonb) from public, anon; grant execute on function public.cs_agenda_save(uuid, jsonb) to authenticated;
revoke all on function public.cs_agenda_add(uuid, text, text, int, int, text, text, text, text, text) from public, anon; grant execute on function public.cs_agenda_add(uuid, text, text, int, int, text, text, text, text, text) to authenticated;
revoke all on function public.cs_agenda_cancel(uuid, uuid) from public, anon; grant execute on function public.cs_agenda_cancel(uuid, uuid) to authenticated;
