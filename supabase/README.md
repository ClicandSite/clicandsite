# Back-office MyCreativeSite

Projet Supabase dédié : `avcynjwcyygygkjuxsdt` (compte contact@mycreativesite.fr), séparé d'Abracadeal et d'EPS.

- Schéma `clicandsite` (RLS activée, aucune policy : accès uniquement via les fonctions `cs_*`).
- `cs_admin_*` : réservées à l'admin (`cs_is_admin()` = e-mail confirmé présent dans `clicandsite.admins`).
- `cs_robot_*` : réservées au rôle service (fonction `clicandsite-prospect-finder`).
- Robot (méthode Abracadeal) : `clicandsite-search` toutes les 2 min (France entière, département par département, table `search_pages`) et `clicandsite-crawl` toutes les 20 s (devine les sites, lit accueil + contact + mentions légales, relève e-mail et téléphone). Il n'envoie jamais de mail.
- Espace admin : https://mycreativesite.fr/admin/ (noindex, exclu dans robots.txt).

## CRM « Mes demandes » (07/11/2026)
- Tables `clicandsite.leads` (demandes envoyées par les sites clients) et `clicandsite.lead_notes` (historique : notes, appels, statuts, relances). Migration : `supabase/migrations/20261107_crm_premium_v1b.sql`.
- Sur un site client, `assets/cs-edit.js` chargé avec `data-site="<slug>"` intercepte chaque formulaire, demande les coordonnées du visiteur (nom + téléphone ou e-mail) et appelle `cs_lead_submit` (public, 5 envois / 10 min par visiteur, 300 / jour par site, piège à robots). Les exemples pré-remplis des modèles deviennent des indications. Sans `data-site` (vitrine, aperçu de l'espace), rien n'est envoyé.
- Espace client, onglet « Mes demandes » : toutes les formules voient la liste de leurs demandes ; statut, relance, historique, vue par client et export sont réservés à Premium (`cs_site_premium` : plan `premium…` ou admin). Démo : `/espace/?demo=garage&vue=demandes`.
- Formule d'un site : Stripe, ou choix manuel dans l'admin (`cs_admin_site_plan`).
- Demandes de plus de 3 ans supprimées chaque dimanche (cron `cs-leads-purge`).

## Formule Boutique (07/11/2026)
- Métier `boutique` (modèle `modeles/boutique.html`, 20 styles) : catalogue = liste `items` du contenu (titre, infos dont la 1re = rayon, prix). Un prix en chiffres (« 24,90 € ») rend le produit achetable ; « Sur devis » / « Dès … » non.
- Panier dans le navigateur (`window.CSShop`). Sur un site client, `cs-edit.js` envoie la commande à la fonction `cs-shop` (action `checkout`) qui **recalcule les prix depuis le contenu enregistré** (`cs_shop_order_create`) puis ouvre un paiement Stripe Checkout **sur le compte Stripe du commerçant** (Connect, compte standard, en-tête Stripe-Account). Sans paiement par carte activé : la commande est enregistrée « à régler sur place ».
- Retour de paiement : action `confirm` ; filet de sécurité : cron `cs-shop-sweep` toutes les 15 min (clé `shop_internal`).
- Réglages (frais de livraison, seuil de gratuité, retrait, livraison) : `sites.shop`, via `cs_shop_settings_save` (espace client). Compte Stripe du commerçant : `clicandsite.shop_private`.
- Activation du paiement par carte : bouton dans l'espace client → action `connect` (création du compte Stripe + lien d'inscription), puis `status`.
- Stripe Connect activé et profil de plateforme confirmé (07/11) ; clé restreinte « boutique » (Accounts, Account Links en écriture sur le compte, Checkout Sessions en écriture sur les comptes connectés) dans le secret `STRIPE_SECRET_KEY`. Test réussi : création de compte et lien d'inscription OK. Un compte d'essai vide (acct_1UZAl3RKZJGhEkWI) reste dans Connect : Stripe interdit de supprimer un compte Standard en mode réel, il est inactif.
- Lien d'abonnement Boutique (99 €/mois) : https://buy.stripe.com/5kQ14n3ynbqP2Qh5W8gfu07

## Paiement avant le nom de domaine (07/11/2026)
- Règle d'Anthony : le client paie **avant** qu'on réserve son nom de domaine.
- Le site est d'abord montré sur une adresse provisoire : https://mycreativesite.fr/apercu/?s=<slug> (statut brouillon accepté, `cs_site_preview`, page noindex et exclue de robots.txt). Bouton « Valider et payer » = lien Stripe de la formule du site (régler la formule dans l'admin). Lien « Aperçu client » dans Sites clients.
- Commandes du formulaire de l'accueil : table `site_orders`, `cs_order_submit` (public), `cs_admin_orders` / `cs_admin_order_update`, onglet « Commandes » de l'admin.

## Site bilingue français / anglais (07/11/2026)
- Droit : formules Premium et Boutique, ou option bilingue (+10 €/mois) cochée dans l'admin (`sites.bilingual`, `cs_admin_site_bilingual`). Fonction `cs_site_bilingual`.
- Contenu : `content.en = { on, dict: { "texte français": "English text" } }`. `cs_site_content` / `cs_site_preview` n'envoient `en` que si le site y a droit et l'a activé (`cs_public_content`).
- Site client (`assets/cs-edit.js`) : bouton FR / EN dans le bandeau, `?lang=en` (choix mémorisé), liens hreflang ; chaque texte, placeholder, title, alt est remplacé par sa traduction (MutationObserver pour les textes ajoutés ensuite). Jamais traduits : nom (.logo), adresse, coordonnées, avis Google. Les demandes arrivent chez le pro avec les libellés en français.
- Traduction (espace client, rubrique « Version anglaise ») : dictionnaire des modèles `assets/cs-en.json` (traduit à la main), puis fonction `cs-translate` (cache `clicandsite.tr_cache` ; DeepL si le secret `DEEPL_KEY` est ajouté), puis Google Traduction depuis le navigateur du pro (Google refuse les serveurs Supabase). Les textes nouveaux ou modifiés sont retraduits à l'enregistrement ; chaque phrase est corrigeable.
- Ajouter une phrase à un modèle : penser à ajouter sa traduction dans `assets/cs-en.json`.

## Agenda des rendez-vous (09/11/2026)
- Métiers : coiffure et beauté, bien-être, restaurant, garage (atelier ; pas en format concession). Migration `supabase/migrations/20261109_agenda.sql`.
- Réglages dans `sites.agenda` (horaires par jour, 2 plages max, créneau toutes les X min, durée occupée, places par créneau — couverts au restaurant —, délai minimum, jours à l'avance, couverts max par réservation, jours de fermeture). `cs_agenda_cfg` nettoie et complète.
- Réservations : table `clicandsite.bookings` (confirme / annule / bloque, source site ou pro). Places libres = places − réservations qui chevauchent le créneau.
- Public : `cs_agenda_public(slug)` (créneaux sur 21 jours) et `cs_booking_submit` (verrou sur le site, re-vérifie le créneau, crée la demande « Mes clients » + la réservation confirmée ; `p_lead=false` quand l'acompte part par `cs-shop`).
- Espace client, onglet « Mon agenda » (`assets/cs-agenda.js`) : semaine, réservations du jour, ajouter un rendez-vous pris par téléphone, bloquer un créneau, annuler, réglages. `cs_agenda_get / save / add / cancel`. Démo : `/espace/?demo=restaurant&vue=agenda`.
- Site client (`assets/cs-edit.js`) : formulaire `#bookform` → sélecteur jour + heure (créneaux complets barrés). Agenda fermé, pas encore réglé ou plus aucun créneau sur 21 jours → bouton « Appeler le … » (numéro du bloc contact) à la place du formulaire.
