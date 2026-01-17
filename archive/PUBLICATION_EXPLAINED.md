# Guide de Publication du Package dnd-5e-core

## 📚 Questions Fréquentes

### 1. Le dossier `dnd_5e_core.egg-info` est-il nécessaire?

**Réponse:** Non, ce dossier n'est **PAS nécessaire** pour la publication.

**Explication:**
- Le dossier `.egg-info` est généré automatiquement lors de l'installation en mode développement (`pip install -e .`)
- Il contient des métadonnées temporaires pour votre installation locale
- Il doit être **ignoré par Git** (déjà dans `.gitignore`)
- Lors de la publication sur PyPI, c'est le fichier `pyproject.toml` qui fournit les métadonnées

**Fichiers générés automatiquement (à ne PAS versionner):**
```
dnd_5e_core.egg-info/    ❌ Ne pas commiter
dist/                    ❌ Ne pas commiter
build/                   ❌ Ne pas commiter
__pycache__/            ❌ Ne pas commiter
*.pyc                   ❌ Ne pas commiter
```

---

### 2. Où publier le package?

Vous avez **plusieurs options** pour publier votre package Python:

#### Option 1: PyPI (Python Package Index) - **RECOMMANDÉ** ✅

**C'est la plateforme officielle pour les packages Python.**

**Avantages:**
- Installation facile: `pip install dnd-5e-core`
- Découverte par la communauté Python
- Intégration avec pip, Poetry, etc.
- Badges de version automatiques
- Statistiques de téléchargement

**Comment publier sur PyPI:**
```bash
# 1. Installer les outils de build
pip install --upgrade build twine

# 2. Créer le package
python -m build

# 3. Uploader sur PyPI (production)
twine upload dist/*

# Ou d'abord tester sur TestPyPI
twine upload --repository testpypi dist/*
```

**Site web:** https://pypi.org/

---

#### Option 2: GitHub Releases 🐙

**Publier le code source sur GitHub.**

**Avantages:**
- Versioning du code source
- Issues et Pull Requests
- Documentation avec GitHub Pages
- Actions CI/CD
- Collaboration facile

**Comment publier sur GitHub:**
```bash
# 1. Créer un nouveau tag
git tag -a v0.1.1 -m "Version 0.1.1 - Complete D&D 5e implementation"

# 2. Pousser le tag
git push origin v0.1.1

# 3. Créer une release sur GitHub
# - Aller sur https://github.com/votre-username/dnd-5e-core/releases
# - Cliquer sur "Draft a new release"
# - Sélectionner le tag v0.1.1
# - Ajouter des notes de version
# - Attacher les fichiers dist/*.tar.gz et dist/*.whl
```

**Installation depuis GitHub:**
```bash
pip install git+https://github.com/votre-username/dnd-5e-core.git
```

---

#### Option 3: Les DEUX - PyPI + GitHub (MEILLEURE APPROCHE) 🏆

**Utilisez GitHub pour le développement et PyPI pour la distribution.**

**Workflow recommandé:**
1. Développement sur GitHub (code, issues, PRs)
2. Publier sur PyPI pour l'installation facile
3. Créer des GitHub Releases pour chaque version
4. Automatiser avec GitHub Actions

---

### 3. Métadonnées manquantes pour PyPI

PyPI affiche mieux votre package si vous fournissez toutes les métadonnées dans `pyproject.toml`:

#### ✅ Métadonnées actuellement présentes:
- ✅ `name`: "dnd-5e-core"
- ✅ `version`: "0.1.1"
- ✅ `description`: Description courte
- ✅ `readme`: README.md (description longue)
- ✅ `authors`: Auteur et email
- ✅ `license`: MIT
- ✅ `keywords`: Mots-clés pour la recherche
- ✅ `classifiers`: Catégories PyPI
- ✅ `dependencies`: Dépendances requises
- ✅ `urls`: Homepage, Repository, Issues, etc.

#### ✨ Métadonnées complètes (déjà configurées):

```toml
[project.urls]
Homepage = "https://github.com/codingame-team/dnd-5e-core"
Documentation = "https://github.com/codingame-team/dnd-5e-core/blob/main/README.md"
Repository = "https://github.com/codingame-team/dnd-5e-core"
"Source Code" = "https://github.com/codingame-team/dnd-5e-core"
Issues = "https://github.com/codingame-team/dnd-5e-core/issues"
"Bug Tracker" = "https://github.com/codingame-team/dnd-5e-core/issues"
Changelog = "https://github.com/codingame-team/dnd-5e-core/blob/main/CHANGELOG.md"
"Quick Start" = "https://github.com/codingame-team/dnd-5e-core/blob/main/QUICK_START_DATA.md"
```

---

## 🚀 Processus de Publication Complet

### Étape 1: Préparer le package

```bash
# 1. Mettre à jour la version dans pyproject.toml
# 2. Mettre à jour CHANGELOG.md
# 3. Commiter les changements
git add .
git commit -m "Prepare version 0.1.1"
```

### Étape 2: Construire le package

```bash
# Installer les outils
pip install --upgrade build twine

# Nettoyer les anciennes builds
rm -rf dist/ build/ *.egg-info

# Construire
python -m build
```

Cela créera:
- `dist/dnd-5e-core-0.1.1.tar.gz` (source distribution)
- `dist/dnd_5e_core-0.1.1-py3-none-any.whl` (wheel)

### Étape 3: Tester localement

```bash
# Créer un nouvel environnement virtuel
python -m venv test-env
source test-env/bin/activate

# Installer depuis le fichier wheel
pip install dist/dnd_5e_core-0.1.1-py3-none-any.whl

# Tester
python -c "from dnd_5e_core.data import load_monster; print(load_monster('goblin'))"
```

### Étape 4: Publier sur TestPyPI (optionnel mais recommandé)

```bash
# Créer un compte sur https://test.pypi.org/
# Uploader
twine upload --repository testpypi dist/*

# Tester l'installation
pip install --index-url https://test.pypi.org/simple/ dnd-5e-core
```

### Étape 5: Publier sur PyPI (production)

```bash
# Créer un compte sur https://pypi.org/
# Uploader
twine upload dist/*

# Vérifier
pip install dnd-5e-core
```

### Étape 6: Créer une GitHub Release

```bash
# Tag
git tag -a v0.1.1 -m "Version 0.1.1"
git push origin v0.1.1

# Créer la release sur GitHub avec les fichiers dist/
```

---

## 🔐 Configuration des Credentials

### PyPI Token (Recommandé)

1. Aller sur https://pypi.org/manage/account/token/
2. Créer un nouveau token API
3. Créer `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcC... (votre token)

[testpypi]
username = __token__
password = pypi-AgENdGVzdC5weXBpLm9yZw... (votre token)
```

---

## 📊 Après Publication

### Sur PyPI

Votre package apparaîtra sur:
- https://pypi.org/project/dnd-5e-core/

**Vérifications:**
- ✅ Description longue (README.md)
- ✅ Liens sidebar (Homepage, Repository, etc.)
- ✅ Classifiers
- ✅ Statistiques de téléchargement

### Sur GitHub

Ajoutez des badges dans README.md:

```markdown
[![PyPI version](https://badge.fury.io/py/dnd-5e-core.svg)](https://pypi.org/project/dnd-5e-core/)
[![Downloads](https://pepy.tech/badge/dnd-5e-core)](https://pepy.tech/project/dnd-5e-core)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```

---

## 🤖 Automatisation avec GitHub Actions

Créez `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        pip install build twine
    - name: Build package
      run: python -m build
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

---

## 📝 Résumé

1. **dnd_5e_core.egg-info** ➜ **N'est PAS nécessaire** (généré automatiquement)
2. **Où publier** ➜ **PyPI + GitHub** (meilleure approche)
3. **Métadonnées** ➜ **Déjà bien configurées dans pyproject.toml**
4. **Publication** ➜ Suivre le processus en 6 étapes ci-dessus

**Commandes essentielles:**
```bash
python -m build              # Construire
twine upload dist/*          # Publier sur PyPI
git tag -a v0.1.1 -m "..."  # Version Git
```

Votre package est maintenant prêt pour la publication! 🎉

