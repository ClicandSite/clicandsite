-- 12/11/2026 : métier Taxi = modèle VTC en version taxi (sites.trade = 'vtc', content.taxi = true).
-- site_orders.trade garde « taxi » pour que l'admin voie que c'est une commande taxi.
do $$
declare d text;
begin
  select pg_get_functiondef('public.cs_order_submit'::regproc) into d;
  if position('''taxi''' in d) = 0 then
    d := replace(d, '  select coalesce(array_agg(distinct o)', '  if p_trade = ''taxi'' then tr := ''vtc''; ct := ''{"taxi":true}''::jsonb; end if;' || chr(10) || '  select coalesce(array_agg(distinct o)');
    if position('''taxi''' in d) = 0 then raise exception 'cs_order_submit non modifiée'; end if;
    execute d;
  end if;
end $$;
