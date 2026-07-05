# Projet FTML 2026

Groupe : Ilias Kalalou, Kaelan Grall, Simon Arbiser.

Ce dépôt contient les sept exercices du projet FTML 2026. Chaque exercice est dans son propre dossier, avec un notebook qui rassemble les explications, les démonstrations, le code et les figures. Les sept notebooks sont fournis déjà exécutés : les scores, les sorties et les figures sont visibles sans rien relancer. Les données nécessaires sont incluses dans le dépôt, sous `data/`, y compris le sous-ensemble Animals-10 et le cache de caractéristiques partagé par les exercices 6 et 7.

## Structure

| Dossier | Exercice | Type | Livrable |
|---|---|---|---|
| `exercice_1_bayes_estimator/` | 1 - Bayes estimator and Bayes risk | maths + code | `exercice_1.ipynb` |
| `exercice_2_absolute_loss/` | 2 - Bayes risk with absolute loss | maths + code | `exercice_2.ipynb` |
| `exercice_3_ols_empirical_risk/` | 3 - Expected value of empirical risk for OLS | maths + code | `exercice_3.ipynb` |
| `exercice_4_regression/` | 4 - Regression on a given dataset | code | `exercice_4.ipynb` |
| `exercice_5_classification/` | 5 - Classification on a given dataset | code | `exercice_5.ipynb` |
| `exercice_6_supervised_animals/` | 6 - Application of supervised learning | code | `exercice_6.ipynb` |
| `exercice_7_unsupervised_animals/` | 7 - Application of unsupervised learning | code | `exercice_7.ipynb` |

## Résultats en un coup d'oeil

- Exercice 1 : démonstration que l'estimateur de Bayes pour la perte quadratique est l'espérance conditionnelle.
- Exercice 2 : démonstration que l'estimateur de Bayes pour la perte absolue est la médiane conditionnelle.
- Exercice 3 : démonstration que l'espérance du risque empirique de l'OLS vaut (n - d) / n fois sigma carré, vérifiée par simulation.
- Exercice 4 : meilleure régression obtenue avec le Lasso, R2 test de 0.9231, proche du risque de Bayes annoncé (environ 0.92).
- Exercice 5 : meilleure classification obtenue avec un SVC à noyau RBF, accuracy test de 0.80. L'objectif de 0.85 est discuté en détail et n'est pas atteint sur les données fournies.
- Exercice 6 : SVC à noyau RBF sur descripteurs image, accuracy test de 0.49 sur dix classes.
- Exercice 7 : k-means et mélange de gaussiennes sur les mêmes descripteurs, ARI de 0.04 et NMI de 0.09, soit un alignement quasi nul entre clusters et espèces.

## Installation

Depuis la racine du dépôt :

```
pip install -r requirements.txt
```

Les notebooks reposent sur la pile scientifique standard (numpy, scipy, scikit-learn, matplotlib, pandas). Le fichier `requirements.txt` ajoute les dépendances propres au projet : scikit-image et Pillow pour le traitement des images des exercices 6 et 7, ainsi que torchvision, umap-learn et kagglehub, qui sont optionnels.

## Données

Toutes les données sont incluses dans le dépôt, sous `data/` :

- Exercice 4 : `data/regression/`, également recopié dans `exercice_4_regression/data/` (fichiers identiques), le notebook lit la copie locale.
- Exercice 5 : `data/classification/`.
- Exercices 6 et 7 : sous-ensemble équilibré d'Animals-10 dans `data/animals10_1k/` (dix classes, mille images par classe) et cache de caractéristiques dans `data/animals10_features/`. Dataset d'origine sur Kaggle : https://www.kaggle.com/datasets/alessiocorrado99/animals10.

Les données étant déjà fournies, aucun téléchargement n'est nécessaire. Pour reconstruire le sous-ensemble Animals-10 à partir de l'archive Kaggle complète :

```
python scripts/download_data.py     # télécharge puis réduit
# ou, si l'archive est déjà dans ~/Downloads/archive/raw-img/ :
python scripts/reduce_animals10.py
```

## Exécution

Les notebooks sont déjà exécutés ; leur lecture ne nécessite aucun relancement.

Pour les rejouer, ouvrir chaque notebook dans Jupyter ou VS Code depuis son dossier et exécuter les cellules.

- Exercices 1 à 5 : de quelques secondes à quelques minutes.
- Exercices 6 et 7 : le cache de caractéristiques étant fourni, l'extraction sur les 10 000 images n'est pas rejouée. L'exercice 6 recharge le cache en quelques secondes, puis la sélection de modèles par validation croisée prend plusieurs minutes. L'exercice 7 recharge le même cache. Si le cache venait à manquer, l'exercice 6 le reconstruit au premier lancement, en quinze à vingt-cinq minutes.

## Notes méthodologiques

- Tous les scores sont annoncés explicitement comme train, validation croisée, ou test.
- Le test ne sert jamais au réglage des hyperparamètres ni à la sélection des modèles ; la validation croisée porte sur le train uniquement.
- Les axes des figures sont labellisés, avec les unités lorsque pertinent.
- Les concepts vus en cours (régression linéaire, Ridge, Lasso, PCA, k-means, SVM) ne sont pas réexpliqués.
- Les méthodes hors programme (t-SNE, UMAP, ARI, NMI, silhouette) sont brièvement présentées dans les exercices 6 et 7.
