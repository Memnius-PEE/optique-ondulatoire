# 0004 — Ranger le journal des décisions dans le registre

- Date : 2026-10-10
- Origine : [humain] « j'aimerai que les carte de decisions ne soient plus isolé du reste des registre (tout dans le dossier registre) »
- Décidé par : @Pwouette
- Options écartées : garder le journal à la racine, dans `decisions/`
- Source : décision 0016 du socle (dépôt registre de l'organisation)
- Remplace : —

Le journal passe de `decisions/` à `registre/decisions/`, avec son historique : tout ce qui décrit le
projet est dans `registre/`. Les entrées 0001 à 0003 sont déplacées telles quelles ; les chemins
`decisions/` qu'elles citent désignent désormais `registre/decisions/`.
