-- 09/11/2026 (Anthony) : le Pack Auto, Moto & Immo ne propose plus que Concession et Agence immobilière.
-- Une commande garage en Pack crée un site au format concession ; une commande garage hors Pack (version atelier) un site au format atelier.
CREATE OR REPLACE FUNCTION public.cs_order_submit(p_trade text, p_style text, p_plan text, p_company text, p_city text, p_phone text, p_email text, p_message text, p_hp text DEFAULT NULL::text, p_self boolean DEFAULT true, p_options text[] DEFAULT '{}'::text[])
 RETURNS json
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO ''
AS $function$
declare ip text; h text; em text; ph text; base text; sl text; n int := 1; tr text; st text; pl text; op text[]; ct jsonb := '{}'::jsonb;
begin
  if coalesce(p_hp,'') <> '' then return json_build_object('ok', true); end if;
  em := nullif(lower(left(trim(coalesce(p_email,'')),160)),'');
  ph := nullif(left(regexp_replace(coalesce(p_phone,''),'[^0-9+ .()-]','','g'),30),'');
  if coalesce(trim(p_company),'') = '' then raise exception 'Indiquez le nom de votre entreprise'; end if;
  if em is null or em !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$' then raise exception 'Indiquez un e-mail valide'; end if;
  begin ip := split_part(coalesce(current_setting('request.headers', true)::json->>'x-forwarded-for',''), ',', 1); exception when others then ip := ''; end;
  h := encode(extensions.digest(coalesce(ip,'') || ':orders', 'sha256'), 'hex');
  if (select count(*) from clicandsite.site_orders where ip_hash = h and created_at > now() - interval '1 hour') >= 5 then raise exception 'Trop de demandes, réessayez plus tard'; end if;
  tr := case when p_trade in ('vtc','restaurant','garage','immobilier','batiment','beaute','bienetre','veterinaire','autoecole','coach','photographe','toiletteur','fleuriste','traiteur','nautisme','kine','dentiste','bijouterie','liberal','services','evenementiel','hebergement','tourisme','location','infirmier','boulangerie','depannage','boutique') then p_trade end;
  st := case when coalesce(p_style,'') ~ '^[a-z]{3,20}$' then p_style else 'moderne' end;
  pl := case when lower(coalesce(p_plan,'')) in ('essentiel','pro','premium','boutique','autoimmo') then lower(p_plan) end;
  if tr = 'garage' then ct := case when pl = 'autoimmo' then '{"concession":true}'::jsonb else '{"atelier":true}'::jsonb end; end if;
  select coalesce(array_agg(distinct o), '{}') into op from unnest(coalesce(p_options,'{}')) o
   where o in ('logo','google','mail','bilingue') and not (o in ('logo','bilingue') and pl in ('premium','boutique'));
  if tr is not null then
    base := left(trim(both '-' from regexp_replace(translate(lower(trim(p_company)), 'àâäáãåçéèêëíìîïñóòôöõúùûüýÿœæ', 'aaaaaaceeeeiiiinooooouuuuyyoa'), '[^a-z0-9]+', '-', 'g')), 34);
    if length(base) < 3 then base := 'site-' || substr(md5(random()::text),1,6); end if;
    sl := base;
    while exists (select 1 from clicandsite.sites where slug = sl) loop n := n + 1; sl := base || '-' || n; end loop;
    insert into clicandsite.sites (slug, name, trade, style, owner_email, status, plan, options, content) values (sl, left(trim(p_company),120), tr, st, em, 'brouillon', pl, op, ct);
  end if;
  insert into clicandsite.site_orders (trade, style, plan, company, city, phone, email, message, ip_hash, self, site_slug, options)
  values (left(p_trade,40), st, left(p_plan,20), left(trim(p_company),120), left(trim(coalesce(p_city,'')),80), ph, em, nullif(left(trim(coalesce(p_message,'')),1500),''), h, coalesce(p_self,true), sl, op);
  return json_build_object('ok', true, 'slug', sl);
end $function$;
