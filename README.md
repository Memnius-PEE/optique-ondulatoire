# Optique ondulatoire

> Étudier interférences et diffraction de la lumière, des fentes d'Young aux réseaux.

| | |
|---|---|
| **Statut** | actif |
| **Mainteneur·ices** | @Pwouette |
| **Niveau d'entrée** | facile |
| **Où en est-on ?** | voir « Ce qui reste à faire » ci-dessous et [`registre/INDEX.md`](registre/INDEX.md) |

_Projet d'exemple du kit Memnius : il montre un dépôt conforme au socle v2, registre compris._

## De quoi s'agit-il ?

La lumière se comporte comme une onde : deux faisceaux issus d'une même source peuvent s'ajouter ou
s'annuler. Ce projet part de l'expérience des fentes d'Young et va jusqu'aux réseaux de diffraction,
en reliant chaque formule à une manipulation faisable avec un pointeur laser.

## Contribuer en 5 minutes

1. Lire « Ce qui reste à faire » ci-dessous.
2. Choisir un ticket étiqueté « bon premier ticket » ou ouvrir un ticket pour proposer une idée.
3. Modifier directement sur GitHub (bouton « crayon », ou touche `.` pour l'éditeur web) ou en local,
   puis ouvrir une pull request. Aucune installation n'est nécessaire pour les notes.

Les règles communes à tous les projets sont dans [CONTRIBUTING.md](CONTRIBUTING.md).

## Organisation du dépôt

| Dossier | Contenu |
|---|---|
| `registre/` | le journal des décisions (`registre/decisions/`) et une carte par code, jeu de données ou source : qui l'a fait, où le trouver ; index dans [`registre/INDEX.md`](registre/INDEX.md) |
| `notes/` | notes de travail (`fentes-young.md`) |
| `sources/` | références (`references.bib`, `liens.md`) |
| `travaux/` | calculs (`interfrange.py`) |
| `donnees/`, `docs/`, `livrables/` | vides pour l'instant |

## Ce qui reste à faire

1. Relire `notes/fentes-young.md` (bon premier ticket).
2. Mesurer l'interfrange avec un pointeur laser rouge et comparer au calcul.
3. Ajouter une note sur les réseaux de diffraction.

## Licence

CC-BY-4.0 (voir `memnius.yaml`).
