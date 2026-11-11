-- 09/11/2026 : nouveau métier « veterinaire » (modèle modeles/veterinaire.html, agenda de rendez-vous, robot de prospection NAF 75.00Z)
alter table clicandsite.sites drop constraint sites_trade_check;
alter table clicandsite.sites add constraint sites_trade_check check (trade = any (array['vtc','restaurant','garage','immobilier','batiment','beaute','bienetre','veterinaire','boulangerie','depannage','boutique']));
alter table clicandsite.prospects drop constraint prospects_trade_check;
alter table clicandsite.prospects add constraint prospects_trade_check check (trade = any (array['vtc','restaurant','garage','immobilier','batiment','veterinaire']));
create or replace function public.cs_agenda_trade(t text) returns boolean language sql immutable set search_path to '' as $$
  select t in ('beaute','bienetre','veterinaire','restaurant','garage');
$$;
-- cs_order_submit : 'veterinaire' ajouté à la liste des métiers acceptés (remplacement dans la définition existante)
do $$
declare d text;
begin
  select pg_get_functiondef('public.cs_order_submit'::regproc) into d;
  d := replace(d, '''beaute'',''bienetre'',''boulangerie''', '''beaute'',''bienetre'',''veterinaire'',''boulangerie''');
  if position('veterinaire' in d) = 0 then raise exception 'cs_order_submit non modifiée'; end if;
  execute d;
end $$;
