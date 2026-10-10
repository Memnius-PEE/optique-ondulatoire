# Index du registre — Optique ondulatoire

_Généré par `memnius.py index` à partir des cartes de `registre/` et du journal `registre/decisions/`. Ne pas éditer : modifier ou ajouter une carte, puis relancer l'outil._

7 cartes : 4 décisions, 1 code, 0 données, 2 sources.

## Décisions

| Carte | Résumé | Décidé par | Date |
|---|---|---|---|
| [0001 — Adopter le socle commun Memnius v1](decisions/0001-adopter-le-socle.md) | Le sujet suit les règles C1–C10 et les gardes A1–A6 du socle v1, au niveau `recommande` : des agents y écrivent régulièrement, donc R1–R8 s'appliquent aussi. | @Pwouette | 2026-09-26 |
| [0002 — Calculs en Python sans dépendance](decisions/0002-calculs-sans-dependance.md) | Les scripts de `travaux/` n'utilisent que la bibliothèque standard tant qu'aucun tracé n'est nécessaire. | @Pwouette | 2026-09-26 |
| [0003 — Passer au socle v2 et tenir le registre du projet](decisions/0003-passer-au-socle-v2.md) | Le projet suit désormais le socle v2 (règles C1–C11, gardes A1–A7). Chaque script, jeu de données ou source notable a sa carte dans `registre/`, et l'index `registre/INDEX.md` est régénéré à chaque changement. | @Pwouette | 2026-10-10 |
| [0004 — Ranger le journal des décisions dans le registre](decisions/0004-decisions-dans-le-registre.md) | Le journal passe de `decisions/` à `registre/decisions/`, avec son historique : tout ce qui décrit le projet est dans `registre/`. Les entrées 0001 à 0003 sont déplacées telles quelles ; les chemins `decisions/` qu'elles citent désignent désormais `registre/decisions/`. | @Pwouette | 2026-10-10 |

## Code

| Carte | Résumé | Qui | Où | Date |
|---|---|---|---|---|
| [Calcul de l'interfrange des fentes d'Young](code/interfrange.md) (à relire) | Calcule l'interfrange i = λD/a des fentes d'Young et affiche l'ordre de grandeur pour un pointeur laser rouge. | @Pwouette | [`travaux/interfrange.py`](../travaux/interfrange.py) | 2026-09-26 |

## Données

_Aucune carte pour l'instant._

## Sources

| Carte | Résumé | Qui | Où | Date |
|---|---|---|---|---|
| [Hecht, Optics (5e édition)](sources/hecht-optics.md) (à relire) | Manuel de référence pour l'optique ondulatoire ; le chapitre 9 traite des interférences et des fentes d'Young. | @Pwouette | [`sources/references.bib`](../sources/references.bib) | 2026-09-26 |
| [Cours d'optique ondulatoire (Wikiversité)](sources/wikiversite-optique.md) (à relire) | Cours d'introduction en ligne, libre, utile pour les contributeur·ices qui découvrent le sujet. | @Pwouette | [`sources/liens.md`](../sources/liens.md), [fr.wikiversity.org](https://fr.wikiversity.org/wiki/Optique_ondulatoire) | 2026-09-26 |

## Qui a fait quoi

- **@Pwouette** : décisions [0001](decisions/0001-adopter-le-socle.md), [0002](decisions/0002-calculs-sans-dependance.md), [0003](decisions/0003-passer-au-socle-v2.md), [0004](decisions/0004-decisions-dans-le-registre.md) ; code [interfrange](code/interfrange.md) ; sources [hecht-optics](sources/hecht-optics.md), [wikiversite-optique](sources/wikiversite-optique.md)
