# Back-office MyCreativeSite

Projet Supabase dédié : `avcynjwcyygygkjuxsdt` (compte contact@mycreativesite.fr), séparé d'Abracadeal et d'EPS.

- Schéma `clicandsite` (RLS activée, aucune policy : accès uniquement via les fonctions `cs_*`).
- `cs_admin_*` : réservées à l'admin (`cs_is_admin()` = e-mail confirmé présent dans `clicandsite.admins`).
- `cs_robot_*` : réservées au rôle service (fonction `clicandsite-prospect-finder`).
- Robot (méthode Abracadeal) : `clicandsite-search` toutes les 2 min (France entière, département par département, table `search_pages`) et `clicandsite-crawl` toutes les 20 s (devine les sites, lit accueil + contact + mentions légales, relève e-mail et téléphone). Il n'envoie jamais de mail.
- Espace admin : https://mycreativesite.fr/admin/ (noindex, exclu dans robots.txt).

## CRM « Mes demandes » (07/11/2026)
- Tables `clicandsite.leads` (demandes envoyées par les sites clients) et `clicandsite.lead_notes` (historique : notes, appels, statuts, relances). Migration : `supabase/migrations/20261107_crm_premium_v1.sql`.
- Sur un site client, `assets/cs-edit.js` chargé avec `data-site="<slug>"` intercepte chaque formulaire, demande les coordonnées du visiteur (nom + téléphone ou e-mail) et appelle `cs_lead_submit` (public, 5 envois / 10 min par visiteur, 300 / jour par site, piège à robots). Les exemples pré-remplis des modèles deviennent des indications. Sans `data-site` (vitrine, aperçu de l'espace), rien n'est envoyé.
- Espace client, onglet « Mes demandes » : toutes les formules voient la liste de leurs demandes ; statut, relance, historique, vue par client et export sont réservés à Premium (`cs_site_premium` : plan `premium…` ou admin). Démo : `/espace/?demo=garage&vue=demandes`.
- Formule d'un site : Stripe, ou choix manuel dans l'admin (`cs_admin_site_plan`).
- Demandes de plus de 3 ans supprimées chaque dimanche (cron `cs-leads-purge`).
