# CLAUDE.md — Fiche de contexte du projet `sudoku_solver`

## ⚠️ Règle principale : ne pas écrire de code sans demande explicite

Ce projet est un **projet d'apprentissage**. L'objectif est que **je progresse moi-même**.

- **Par défaut, Claude n'écrit PAS de code** : ni création de fichiers source, ni modification, ni « petit correctif rapide », ni solution complète glissée dans une explication.
- Claude peut en revanche :
  - expliquer des concepts (structures de données, algorithmes, complexité, ML…) ;
  - poser des questions pour me guider (approche socratique) ;
  - donner des indices progressifs, du pseudo-code de haut niveau **seulement si je le demande** ;
  - relire mon code et pointer les bugs, maladresses ou pistes d'amélioration en expliquant **pourquoi**, sans réécrire le code à ma place ;
  - proposer des tests ou des cas limites à vérifier (en les décrivant, pas en les codant).
- **Si je demande explicitement du code** (« code-le », « écris la fonction », « implémente… », « corrige-le directement »), alors Claude code, en se limitant au périmètre demandé.
- En cas de doute sur le fait que je demande du code ou non : **demander avant d'écrire**.

## Objectif du projet

1. **Modéliser un sudoku** : représentation de la grille, lecture/affichage, vérification des contraintes (lignes, colonnes, blocs 3×3), détection d'une grille valide / résolue.
2. **Résolution par backtracking** : au moins un algorithme de backtracking, puis éventuellement des améliorations (choix de la case la plus contrainte / MRV, propagation de contraintes, ensembles de candidats, etc.).
3. **(Optionnel) Approche Machine Learning** : tenter une résolution ou une aide à la résolution par ML (ex. réseau de neurones prédisant les chiffres), et comparer avec le backtracking.

## État d'avancement

- [x] Récupération des données (dataset Kaggle)
- [ ] Modélisation de la grille — en cours (classe `Sudoku_grid` : conversion grille/solution, `select_case` ; pas encore de propagation ni de vérification des contraintes)
- [ ] Solveur par backtracking (version naïve)
- [ ] Optimisations du backtracking
- [ ] Exploration ML

## Choix techniques

- Langage : Python, avec numpy. Environnement virtuel dans `.venv/`, dépendances dans `requirements.txt`.
- Données : Kaggle `radcliffe/3-million-sudoku-puzzles-with-ratings`, téléchargé par `kagglehub_launcher/importing_dataset.py` dans `data/sudoku-3m.csv` (ignoré par Git via `data/*`). Colonnes `id,puzzle,solution,clues,difficulty` ; grilles en chaînes de 81 caractères lues ligne par ligne, `.` = case vide ; `difficulty` est un flottant.
  - ⚠️ `output_dir` de kagglehub vide le dossier cible avec `force_download=True` : ne rien mettre d'autre dans `data/`.
- Les scripts se lancent toujours **depuis la racine du projet** (chemins relatifs).
- Modélisation (`backtracking/classes/sudoku_grid.py`) :
  - `puzzle` = tableau de candidats **booléens 9×9×9** ; `puzzle[l, c, k]` vrai si le chiffre `k+1` est encore possible (attention au décalage chiffre/indice).
  - `solution` = tableau d'entiers 9×9.
  - Indice `i` de la chaîne → ligne `i // 9`, colonne `i % 9`.
- Pistes pour le ML : ne pas instancier 3M objets ; charger toutes les grilles d'un bloc en tableau `(N, 9, 9)` sans boucle Python.

## Maintenance de ce fichier

Claude met à jour ce `CLAUDE.md` lorsqu'il y a une **avancée importante** (nouvelle étape terminée, choix technique arrêté, changement de structure, décision de conception notable). Les mises à jour portent sur les sections « État d'avancement » et « Choix techniques » ; la règle principale ci-dessus ne doit pas être modifiée sans mon accord.
