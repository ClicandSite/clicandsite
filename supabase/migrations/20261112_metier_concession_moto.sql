-- 12/11/2026 (Anthony : « séparer concession auto et moto ») : p_trade 'moto' → site garage {"concession":true,"moto":true} ; site_orders.trade garde 'moto'.
do $$
declare d text;
begin
  select pg_get_functiondef('public.cs_order_submit'::regproc) into d;
  if position('''moto''' in d) = 0 then
    d := replace(d, '  select coalesce(array_agg(distinct o)', '  if p_trade = ''moto'' then tr := ''garage''; ct := ''{"concession":true,"moto":true}''::jsonb; end if;' || chr(10) || '  select coalesce(array_agg(distinct o)');
    if position('''moto''' in d) = 0 then raise exception 'cs_order_submit non modifiée'; end if;
    execute d;
  end if;
end $$;
