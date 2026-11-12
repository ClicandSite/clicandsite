-- 12/11/2026 (Anthony : « vérifie que l'admin n'est accessible que par moi ») : durcissement.
-- pg_net (envoi de requêtes web depuis la base) n'est plus appelable par anon / authenticated.
-- Seules cs_admin_robot et cs_admin_mail_test s'en servent, en SECURITY DEFINER : non concernées.
revoke execute on all functions in schema net from anon, authenticated, public;
revoke usage on schema net from anon, authenticated;
