# Contribuer

Ce dépôt fait partie du groupe d'étude Memnius. Les règles communes à tous les projets
sont décrites dans <https://github.com/Memnius-PEE/registre> ; voici l'essentiel.

## Selon votre implication

| Vous êtes… | Vous pouvez… | Comment |
|---|---|---|
| **De passage** | signaler, commenter, proposer | ouvrir un ticket, commenter une pull request |
| **Contributeur·ice occasionnel·le** | corriger, ajouter une note | bouton « crayon » de GitHub → pull request ; aucun outil à installer |
| **Contributeur·ice régulier·e** | travailler sur des branches | rôle *Write* ; branches `<pseudo>/<objet>` |
| **Mainteneur·ice** | fusionner, trier, tenir `PASSATION.md` | rôle *Maintain* ; un par projet, nommé par le comité du socle |

## Règles minimales

- `main` est protégée : tout passe par une pull request relue par une autre personne.
- Avant de commencer, lisez la section 5 de `PASSATION.md` (ce qui reste à faire).
- Une décision qui engage le projet s'écrit dans un nouveau fichier de `decisions/` ; on ne modifie jamais une décision publiée.
- Écrivez dans la langue du dépôt (champ `langue` de `memnius.yaml`) ; noms de fichiers en minuscules, sans accents ni espaces (`mon-fichier.md`).
- Travail fait avec un agent IA : ajoutez `Assisted-by: <outil>` au message de commit.
- Fichiers de plus de 10 Mo : refusés par la CI (garde A6) ; passez par Git LFS (configuré dans `.gitattributes`) ou le drive commun, décrit par une carte de `registre/donnees/`.
- Vous ajoutez un script, un jeu de données ou une source importante : ajoutez sa carte dans `registre/` (voir [`registre/README.md`](registre/README.md)). Si vous ne savez pas faire, dites-le dans la pull request : un·e mainteneur·ice s'en chargera.
- Pas de secrets, pas de données personnelles.
