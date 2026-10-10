# Passation — 2026-10-10 — rédigée par un agent (Claude), vérifiée par : —

## 0. En une phrase *
Projet passé au socle v2 : registre créé (une carte de code, deux de sources) ; la note sur les fentes d'Young est toujours à relire.

## 1. État mesuré *
```
$ python3 travaux/interfrange.py
lambda = 650 nm, a = 0.2 mm, D = 2.0 m -> interfrange i = 6.50 mm
```

## 2. Ce qui est entré, et qui l'a vérifié
- `travaux/interfrange.py` : formule i = λD/a, sortie ci-dessus ; pas encore relu par une personne.

## 3. Décisions prises (numéros du journal)
- 0001 : socle v1, niveau recommandé.
- 0002 : calculs sans dépendance.
- 0003 : passage au socle v2 et tenue du registre.

## 4. Manquements aux règles (R8)
- Aucun.

## 5. Ce qui reste dû ou en cours *
1. Relire `notes/fentes-young.md` (bon premier ticket).
2. Mesurer l'interfrange avec un pointeur laser rouge et comparer au calcul.
3. Ajouter une note sur les réseaux de diffraction.

## 6. Pièges rencontrés
- Garder les unités SI dans les scripts : a en mètres, pas en millimètres.

## 7. Ce qui n'a PAS été vérifié *
- Les cartes du registre ont été rédigées par un agent (`statut: a-relire`) : à relire par le mainteneur.
- La longueur d'onde de 650 nm est une valeur typique de pointeur rouge `[non vérifié]` pour un pointeur donné.
