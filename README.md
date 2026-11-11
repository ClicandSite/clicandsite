# Clic&Site — guide touristique (clicandsite.fr)

Sources du guide d'affiliation Clic&Site (iDream Lab). **Branche de sauvegarde, jamais publiée** : le site sera hébergé dans son propre dépôt `ClicandSite/clicandsite-guide` (GitHub Pages, domaine clicandsite.fr).

- `content.py` + `content_more.py` : textes (19 lieux de la Côte d’Azur, groupes, itinéraire 3 jours) — pas de prix ni d’horaires précis.
- `build.py` : génère le site dans `site/` (`python3 build.py`). Identifiants d'affiliation GetYourGuide / Viator dans `AFFILIATION`.
- Pied de page : « Site réalisé par MyCreativeSite ».

À faire (11/11/2026) : créer le dépôt `clicandsite-guide`, retirer la redirection OVH de clicandsite.fr vers mycreativesite.fr, créer contact@clicandsite.fr, puis inscription GetYourGuide / Viator une fois une dizaine de pages en ligne.

## Référencement (11/11/2026)
- `seo.py` : titres courts (< 62 caractères), titres H2 avec mots-clés (« Que voir à… », « Comment aller à… »), coordonnées GPS, mots déclenchant les liens internes, texte de la page À propos.
- `og.py` : images de partage 1200×630 générées pour chaque page (`site/assets/og/`). Nécessite `npm i @fontsource/young-serif @fontsource/public-sans` pour les polices.
- Après la mise en ligne : ajouter clicandsite.fr dans Google Search Console (compte abracadeal@gmail.com), envoyer `sitemap.xml`, demander l'indexation de l'accueil et de la page Côte d'Azur.

## Version anglaise (11/11/2026)
- `python3 build.py en` génère `site_en/` pour clicandsite.com (dépôt ClicandSite/clicandsite-guide-en). Textes dans `content_en.py`.
- Chaque page renvoie vers sa version dans l'autre langue (hreflang + bouton English/Français).
- Après chaque modification : `python3 build.py && python3 build.py en`, puis copier `site/` dans clicandsite-guide et `site_en/` dans clicandsite-guide-en.
