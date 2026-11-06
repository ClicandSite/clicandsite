# Back-office ClicandSite

Projet Supabase dédié : `avcynjwcyygygkjuxsdt` (compte contact@clicandsite.fr), séparé d'Abracadeal et d'EPS.

- Schéma `clicandsite` (RLS activée, aucune policy : accès uniquement via les fonctions `cs_*`).
- `cs_admin_*` : réservées à l'admin (`cs_is_admin()` = e-mail confirmé présent dans `clicandsite.admins`).
- `cs_robot_*` : réservées au rôle service (fonction `clicandsite-prospect-finder`).
- Robot : pg_cron `clicandsite-prospect-finder`, toutes les 10 min (minute 3). Il n'envoie jamais de mail.
- Espace admin : https://clicandsite.fr/admin/ (noindex, exclu dans robots.txt).
