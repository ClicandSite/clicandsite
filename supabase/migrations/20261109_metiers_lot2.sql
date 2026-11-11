-- 09/11/2026 : 9 nouveaux métiers (auto-école, coach sportif, photographe, toiletteur, fleuriste, traiteur, location de bateaux, kinésithérapeute, dentiste)
alter table clicandsite.sites drop constraint sites_trade_check;
alter table clicandsite.sites add constraint sites_trade_check check (trade = any (array['vtc','restaurant','garage','immobilier','batiment','beaute','bienetre','veterinaire','autoecole','coach','photographe','toiletteur','fleuriste','traiteur','nautisme','kine','dentiste','boulangerie','depannage','boutique']));
alter table clicandsite.prospects drop constraint prospects_trade_check;
alter table clicandsite.prospects add constraint prospects_trade_check check (trade = any (array['vtc','restaurant','garage','immobilier','batiment','veterinaire','autoecole','coach','photographe','toiletteur','fleuriste','traiteur','nautisme','kine','dentiste']));
create or replace function public.cs_agenda_trade(t text) returns boolean language sql immutable set search_path to '' as $$
  select t in ('beaute','bienetre','veterinaire','autoecole','coach','photographe','toiletteur','nautisme','kine','dentiste','restaurant','garage');
$$;
do $$
declare d text;
begin
  select pg_get_functiondef('public.cs_order_submit'::regproc) into d;
  d := replace(d, '''bienetre'',''veterinaire'',''boulangerie''', '''bienetre'',''veterinaire'',''autoecole'',''coach'',''photographe'',''toiletteur'',''fleuriste'',''traiteur'',''nautisme'',''kine'',''dentiste'',''boulangerie''');
  if position('dentiste' in d) = 0 then raise exception 'cs_order_submit non modifiée'; end if;
  execute d;
end $$;
insert into clicandsite.search_pages(area,trade,rank)
  select s.area, t.trade, s.rank from clicandsite.search_pages s cross join unnest(array['autoecole','coach','photographe','toiletteur','fleuriste','traiteur','nautisme','kine','dentiste']) as t(trade)
  where s.trade='vtc' on conflict do nothing;
update clicandsite.robot_settings set trades = array(select distinct unnest(trades || array['autoecole','coach','photographe','toiletteur','fleuriste','traiteur','nautisme','kine','dentiste']));
update clicandsite.mail_settings set trades = array(select distinct unnest(trades || array['autoecole','coach','photographe','toiletteur','fleuriste','traiteur','nautisme','kine','dentiste']));
