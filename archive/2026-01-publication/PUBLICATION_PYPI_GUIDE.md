# 📦 Guide de Publication PyPI - dnd-5e-core

## 🎯 Vue d'Ensemble

Le script `build_package.sh` permet de construire et publier le package `dnd-5e-core` sur PyPI.

---

## 🚀 Utilisation Rapide

### 1. Build Local (Test)

```bash
# Nettoyer et construire
./build_package.sh --clean --build

# Vérifier les fichiers générés
ls -lh dist/
```

### 2. Publication sur TestPyPI (Recommandé pour tester)

```bash
# Publier sur TestPyPI
./build_package.sh --test

# Installer depuis TestPyPI pour tester
pip install --index-url https://test.pypi.org/simple/ dnd-5e-core
```

### 3. Publication sur PyPI (Production)

```bash
# Publication complète (clean + build + publish)
./build_package.sh --all

# OU étape par étape
./build_package.sh --clean
./build_package.sh --build
./build_package.sh --publish
```

---

## 📋 Options du Script

| Option | Description |
|--------|-------------|
| `--clean` | Nettoie les fichiers de build précédents (dist/, build/, *.egg-info) |
| `--build` | Construit le package (wheel et source distribution) |
| `--test` | Publie sur TestPyPI (environnement de test) |
| `--publish` | Publie sur PyPI production (⚠️ irréversible) |
| `--all` | Exécute clean + build + publish |
| `--help` | Affiche l'aide |

---

## 🔧 Prérequis

### 1. Configuration PyPI

#### Créer un compte PyPI
- Production : https://pypi.org/account/register/
- Test : https://test.pypi.org/account/register/

#### Créer un token API
1. Se connecter sur PyPI
2. Account settings → API tokens
3. Créer un token avec scope "Entire account" ou "Project: dnd-5e-core"
4. Copier le token (commence par `pypi-`)

#### Configurer `~/.pypirc`

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-VOTRE_TOKEN_ICI

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-VOTRE_TOKEN_TEST_ICI
```

**Permissions** :
```bash
chmod 600 ~/.pypirc
```

### 2. Outils Python

Le script installe automatiquement :
- `build` - Outil de build moderne
- `twine` - Publication sécurisée sur PyPI
- `wheel` - Support des packages wheel
- `setuptools` - Outils de packaging

---

## 📝 Workflow de Publication

### Étape 1 : Préparer la Release

```bash
# 1. Mettre à jour la version dans setup.py
vim setup.py  # version='0.2.6'

# 2. Mettre à jour CHANGELOG.md
vim CHANGELOG.md

# 3. Commiter les changements
git add setup.py CHANGELOG.md
git commit -m "Bump version to 0.2.6"
git push
```

### Étape 2 : Build et Test

```bash
# Nettoyer et construire
./build_package.sh --clean --build

# Vérifier le contenu
tar -tzf dist/dnd-5e-core-0.2.6.tar.gz | head -20

# Tester localement
pip install dist/dnd-5e-core-0.2.6-py3-none-any.whl --force-reinstall
```

### Étape 3 : Publier sur TestPyPI

```bash
# Publier sur test
./build_package.sh --test

# Installer depuis test pour vérifier
pip install --index-url https://test.pypi.org/simple/ dnd-5e-core==0.2.6

# Tester le package
python -c "from dnd_5e_core import ClassAbilities; print('OK')"
```

### Étape 4 : Publier sur PyPI

```bash
# Publication finale
./build_package.sh --publish

# Vérifier sur PyPI
# https://pypi.org/project/dnd-5e-core/
```

### Étape 5 : Créer un Tag Git

```bash
# Créer un tag de version
git tag -a v0.2.6 -m "Version 0.2.6 - Class abilities and racial traits"
git push origin v0.2.6

# Créer une release sur GitHub
# https://github.com/votre-user/dnd-5e-core/releases/new
```

---

## ⚠️ Gestion des Erreurs

### Erreur : "File already exists"

```
ERROR: File already exists. See https://pypi.org/help/#file-name-reuse
```

**Solution** : Incrémenter la version dans `setup.py`

PyPI ne permet **pas** de réuploader une version existante (même après suppression).

### Erreur : "Invalid credentials"

```
ERROR: Invalid or non-existent authentication information.
```

**Solutions** :
1. Vérifier `~/.pypirc`
2. Vérifier que le token est valide
3. Utiliser `twine upload` manuellement pour voir l'erreur exacte

### Erreur : "Package name already taken"

Si le nom `dnd-5e-core` est déjà pris :
1. Choisir un autre nom dans `setup.py`
2. OU contacter les mainteneurs de PyPI

---

## 🔍 Vérification du Package

### Après Build

```bash
# Vérifier les métadonnées
python setup.py check

# Vérifier avec twine
twine check dist/*

# Inspecter le contenu
tar -tzf dist/dnd-5e-core-*.tar.gz
unzip -l dist/dnd-5e-core-*.whl
```

### Après Publication

```bash
# Installer dans un environnement propre
python -m venv test_env
source test_env/bin/activate
pip install dnd-5e-core

# Tester
python -c "
from dnd_5e_core import ClassAbilities, RacialTraits
from dnd_5e_core.data.loaders import simple_character_generator
wizard = simple_character_generator(5, 'elf', 'wizard', 'Gandalf')
print(f'✅ {wizard.name} créé avec succès!')
"

# Nettoyer
deactivate
rm -rf test_env
```

---

## 📊 Checklist de Publication

### Avant Publication

- [ ] Version mise à jour dans `setup.py`
- [ ] CHANGELOG.md mis à jour
- [ ] README.md à jour
- [ ] Tests passent (`pytest`)
- [ ] Package build sans erreurs
- [ ] Token PyPI configuré
- [ ] Git commit et push

### Test PyPI

- [ ] Publication sur TestPyPI réussie
- [ ] Installation depuis TestPyPI fonctionne
- [ ] Tests d'import fonctionnent
- [ ] Documentation accessible

### Production PyPI

- [ ] Publié sur PyPI
- [ ] Tag Git créé
- [ ] Release GitHub créée
- [ ] Annonce faite (si applicable)

---

## 📚 Ressources

### Documentation Officielle
- **PyPI** : https://pypi.org/project/dnd-5e-core/
- **TestPyPI** : https://test.pypi.org/project/dnd-5e-core/
- **Python Packaging Guide** : https://packaging.python.org/

### Outils
- **twine** : https://twine.readthedocs.io/
- **build** : https://pypa-build.readthedocs.io/
- **setuptools** : https://setuptools.pypa.io/

### API D&D 5e
- **Source des données** : https://www.dnd5eapi.co
- **Documentation API** : https://5e-bits.github.io/docs/api

---

## 🎯 Exemples de Commandes

### Workflow Complet Standard

```bash
# 1. Préparer
vim setup.py  # version='0.2.6'
vim CHANGELOG.md
git add . && git commit -m "Version 0.2.6"

# 2. Build et test local
./build_package.sh --clean --build
pip install dist/*.whl --force-reinstall
python -c "import dnd_5e_core; print('OK')"

# 3. Test PyPI
./build_package.sh --test
# Vérifier sur https://test.pypi.org/project/dnd-5e-core/

# 4. Production
./build_package.sh --publish
# Vérifier sur https://pypi.org/project/dnd-5e-core/

# 5. Tag
git tag v0.2.6 && git push --tags
```

### Workflow Rapide (Dangereux)

```bash
# Tout en une seule commande (non recommandé pour prod)
./build_package.sh --all
```

---

**Version du Guide** : 1.0  
**Date** : 18 Janvier 2026  
**Package** : dnd-5e-core  
**Status** : ✅ Production Ready

🎉 Guide complet pour publier sur PyPI ! 📦✨
