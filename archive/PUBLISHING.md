# Publication du Package

## 📋 Métadonnées du Projet

### ⚠️ À propos du dossier `.egg-info`

Le dossier `dnd_5e_core.egg-info/` est un **artefact de build** automatiquement généré :
- ❌ **Ne PAS le versionner** sur Git (déjà dans `.gitignore`)
- ✅ **Automatiquement créé** lors du build
- 📦 **Utilisé par pip/setuptools** pour l'installation locale
- 🗑️ **Supprimé automatiquement** par `./build.sh`

### 📝 Métadonnées PyPI (dans `pyproject.toml`)

Toutes les métadonnées pour PyPI sont définies dans `pyproject.toml` :
- ✅ **Description & About**: Description courte et README complet
- ✅ **Authors & Maintainers**: Informations de contact
- ✅ **Keywords**: Mots-clés pour la recherche PyPI
- ✅ **Classifiers**: Catégorisation du package
- ✅ **Links**: Homepage, Documentation, Issues, Changelog, etc.
- ✅ **License**: MIT License

Ces informations apparaîtront automatiquement dans la **barre latérale PyPI** lors de la publication.

### 🌐 Plateformes de Publication

#### 1. **GitHub** (Actuel)
```bash
pip install git+https://github.com/codingame-team/dnd-5e-core.git
```
- ✅ Gratuit et simple
- ✅ Parfait pour les projets open source
- ✅ Pas besoin de compte PyPI
- ❌ Nécessite Git pour installer

#### 2. **PyPI** (Python Package Index)
```bash
pip install dnd-5e-core
```
- ✅ Installation standard avec pip
- ✅ Découverte facile par la communauté
- ✅ Gestion des versions et dépendances
- ✅ Statistiques de téléchargement
- ⚠️ Nécessite un compte PyPI
- ⚠️ Nom du package doit être unique

#### 3. **TestPyPI** (Test avant production)
```bash
pip install --index-url https://test.pypi.org/simple/ dnd-5e-core
```
- ✅ Test avant publication officielle
- ✅ Environnement de test identique à PyPI

## ⚡ Installation Rapide

### Pour les utilisateurs (GitHub uniquement)
```bash
pip install git+https://github.com/codingame-team/dnd-5e-core.git
```

### Pour les développeurs
```bash
git clone https://github.com/codingame-team/dnd-5e-core.git
cd dnd-5e-core
pip install -e ".[dev]"
```

## 📦 Build et Publication

### Build local
```bash
./build.sh
```

Ou manuellement :
```bash
rm -rf build/ dist/ *.egg-info/
python -m build
```

### Publication sur PyPI

1. **Créer un compte PyPI** sur https://pypi.org/account/register/

2. **Configurer les tokens d'API** (recommandé) :
```bash
# Créer un token sur https://pypi.org/manage/account/token/
# Puis dans ~/.pypirc :
[pypi]
username = __token__
password = pypi-<your-token-here>
```

3. **Test sur TestPyPI** (recommandé en premier)
```bash
twine upload --repository testpypi dist/*
```

4. **Production sur PyPI**
```bash
twine upload dist/*
```

## 📂 Fichiers à NE PAS versionner

Ces dossiers sont des artefacts de build et sont automatiquement exclus par `.gitignore` :
- `*.egg-info/` ❌ (artefact de build local)
- `build/` ❌ (fichiers de compilation)
- `dist/` ❌ (packages distribués)
- `__pycache__/` ❌ (bytecode Python)

## 🎯 Barre latérale GitHub

Pour configurer la barre latérale GitHub, voir le guide détaillé : `.github/GITHUB_ABOUT_SETUP.md`

**Résumé rapide** :
1. Aller sur le repository GitHub
2. Cliquer sur **⚙️** à côté de "About"
3. Remplir :
   - **Description** : Copier depuis `.github/DESCRIPTION.txt`
   - **Website** : `https://github.com/codingame-team/dnd-5e-core`
   - **Topics** : Voir `.github/TOPICS.md`

## 📊 Barre latérale PyPI

Les métadonnées PyPI sont dans `pyproject.toml` :
- ✅ **Authors & Maintainers** avec emails
- ✅ **Keywords** pour la recherche
- ✅ **Classifiers** complets
- ✅ **URLs** (Homepage, Documentation, Issues, Changelog, etc.)
- ✅ **License** (MIT)

Ces informations apparaîtront automatiquement sur PyPI après publication.

## 📖 Documentation complète

Voir les fichiers suivants pour plus de détails :
- **Publication** : [docs/GUIDE_PUBLICATION.md](docs/GUIDE_PUBLICATION.md)
- **Métadonnées** : [METADATA_SUMMARY.md](METADATA_SUMMARY.md)
- **GitHub About** : [.github/GITHUB_ABOUT_SETUP.md](.github/GITHUB_ABOUT_SETUP.md)



