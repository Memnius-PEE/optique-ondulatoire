# 0006 — L'index est poussé par la clé de déploiement du projet

- Date : 2026-10-11
- Origine : [humain] correction des frictions relevées par l'essai d'un projet neuf, demandée par le comité du socle
- Décidé par : @Pwouette
- Options écartées : —
- Source : décision 0019 du socle (dépôt registre de l'organisation)
- Remplace : —

La CI commite l'index du registre avec la clé de déploiement du projet (secret `MEMNIUS_INDEX_CLE`), ce qui
relance normalement les gardes sur la pull request. Le workflow `memnius.yml` n'a plus besoin que du droit
`contents: read` et transmet ses secrets au workflow commun (`secrets: inherit`) ; les droits
`contents: write` et `actions: write` de la décision 0005 sont retirés.
