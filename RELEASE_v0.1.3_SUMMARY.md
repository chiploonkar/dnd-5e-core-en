# Résumé de la mise à jour v0.1.3

## Problème résolu

Le package `dnd-5e-core` version 0.1.2 installé depuis PyPI ne contenait pas le fichier `bestiary-sublist-data.json`, causant une erreur `FileNotFoundError` lors de l'utilisation de la fonction `search_monsters()`.

## Solution appliquée

### 1. Correction de l'empaquetage des données
- **Problème** : Le MANIFEST.in ne référençait que `data/` à la racine, mais les fichiers sont dans `dnd_5e_core/data/`
- **Solution** : Ajout de `recursive-include dnd_5e_core/data *.json` dans MANIFEST.in
- **Résultat** : Le fichier `bestiary-sublist-data.json` (422 KB) est maintenant inclus dans le package distribué

### 2. Optimisation de la taille du package
- **Problème** : Le package faisait 107 MB (limite PyPI : 100 MB) à cause des tokens d'images (102 MB)
- **Solution** : Exclusion du dossier `dnd_5e_core/data/monsters/tokens/` du package PyPI
- **Résultat** : Package réduit à 1.3 MB ✓

### 3. Documentation ajoutée
- Création de `dnd_5e_core/data/monsters/tokens/README.md` expliquant comment télécharger les tokens
- Mise à jour du CHANGELOG.md avec les changements de la v0.1.3

## Publication réussie

✅ **Package publié sur PyPI** : https://pypi.org/project/dnd-5e-core/0.1.3/
✅ **Taille finale** : 1.3 MB (wheel) / 1.8 MB (source)
✅ **Tests passés** : Le script `create_monster.py` fonctionne correctement

## Réponses aux questions initiales

### 1. Le dossier `dnd_5e_core.egg-info` est-il nécessaire ?
**Non**, ce dossier est généré automatiquement lors du build. Il ne doit **pas** être commité dans Git (déjà dans .gitignore) et n'est **pas nécessaire** pour la publication. Il est recréé à chaque build.

### 2. Où publier le package ?
- **PyPI** (https://pypi.org/) : Pour la distribution du package Python ✓ (fait)
- **GitHub** : Pour le code source, les issues, la documentation
- Le fichier `.egg-info` n'a rien à voir avec GitHub

### 3. Métadonnées PyPI
Vos métadonnées dans `pyproject.toml` sont **complètes et bien configurées** :
- ✓ Description détaillée
- ✓ Auteur et email
- ✓ Liens (Homepage, Documentation, Repository, Issues, Changelog)
- ✓ Classifiers appropriés
- ✓ Keywords pertinents

Tout est prêt pour une belle page PyPI !

## Fichiers modifiés

1. `MANIFEST.in` - Ajout de l'inclusion de `dnd_5e_core/data/` et exclusion des tokens
2. `setup.py` - Version 0.1.2 → 0.1.3
3. `pyproject.toml` - Version 0.1.2 → 0.1.3
4. `CHANGELOG.md` - Ajout de l'entrée v0.1.3
5. `dnd_5e_core/data/monsters/tokens/README.md` - Nouveau fichier créé

## Prochaines étapes recommandées

1. **Commit et push vers GitHub** :
   ```bash
   git add .
   git commit -m "Release v0.1.3: Fix package data inclusion and optimize size"
   git push
   ```

2. **Créer un tag de release** :
   ```bash
   git tag -a v0.1.3 -m "Version 0.1.3"
   git push origin v0.1.3
   ```

3. **Créer une GitHub Release** avec le CHANGELOG

4. **Télécharger les tokens** (optionnel pour les utilisateurs) :
   ```python
   from dnd_5e_core.utils.token_downloader import download_all_tokens
   download_all_tokens()
   ```

