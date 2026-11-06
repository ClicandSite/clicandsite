# Back-office MyCreativeSite

Projet Supabase dédié : `avcynjwcyygygkjuxsdt` (compte contact@mycreativesite.fr), séparé d'Abracadeal et d'EPS.

- Schéma `clicandsite` (RLS activée, aucune policy : accès uniquement via les fonctions `cs_*`).
- `cs_admin_*` : réservées à l'admin (`cs_is_admin()` = e-mail confirmé présent dans `clicandsite.admins`).
- `cs_robot_*` : réservées au rôle service (fonction `clicandsite-prospect-finder`).
- Robot (méthode Abracadeal) : `clicandsite-search` toutes les 2 min (France entière, département par département, table `search_pages`) et `clicandsite-crawl` toutes les 20 s (devine les sites, lit accueil + contact + mentions légales, relève e-mail et téléphone). Il n'envoie jamais de mail.
- Espace admin : https://mycreativesite.fr/admin/ (noindex, exclu dans robots.txt).
