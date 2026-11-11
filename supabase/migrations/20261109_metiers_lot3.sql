-- 09/11/2026 : lot 3 — professions libérales, services à domicile, événementiel, chambres d'hôtes et gîtes, tourisme et loisirs, location et déménagement
alter table clicandsite.sites drop constraint sites_trade_check;
alter table clicandsite.sites add constraint sites_trade_check check (trade = any (array['vtc','restaurant','garage','immobilier','batiment','beaute','bienetre','veterinaire','autoecole','coach','photographe','toiletteur','fleuriste','traiteur','nautisme','kine','dentiste','bijouterie','liberal','services','evenementiel','hebergement','tourisme','location','boulangerie','depannage','boutique']));
alter table clicandsite.prospects drop constraint prospects_trade_check;
alter table clicandsite.prospects add constraint prospects_trade_check check (trade = any (array['vtc','restaurant','garage','immobilier','batiment','veterinaire','autoecole','coach','photographe','toiletteur','fleuriste','traiteur','nautisme','kine','dentiste','bijouterie','depannage','beaute','bienetre','boulangerie','liberal','services','evenementiel','hebergement','tourisme','location']));
create or replace function public.cs_agenda_trade(t text) returns boolean language sql immutable set search_path to '' as $$
  select t in ('beaute','bienetre','veterinaire','autoecole','coach','photographe','toiletteur','nautisme','kine','dentiste','bijouterie','liberal','services','evenementiel','tourisme','location','restaurant','garage');
$$;
do $$
declare d text;
begin
  select pg_get_functiondef('public.cs_order_submit'::regproc) into d;
  d := replace(d, '''dentiste'',''bijouterie'',''boulangerie''', '''dentiste'',''bijouterie'',''liberal'',''services'',''evenementiel'',''hebergement'',''tourisme'',''location'',''boulangerie''');
  if position('hebergement' in d) = 0 then raise exception 'cs_order_submit non modifiée'; end if;
  execute d;
end $$;
insert into clicandsite.search_pages(area,trade,rank)
  select s.area, t.k, s.rank from clicandsite.search_pages s
  cross join unnest(array['liberal','services','couture','cours','evenementiel','animation','hebergement','conciergerie','tourisme','velo','location']) as t(k)
  where s.trade='vtc' on conflict do nothing;
update clicandsite.robot_settings set trades = array(select distinct unnest(trades || array['liberal','services','evenementiel','hebergement','tourisme','location']));
update clicandsite.mail_settings set trades = array(select distinct unnest(trades || array['liberal','services','evenementiel','hebergement','tourisme','location']));
