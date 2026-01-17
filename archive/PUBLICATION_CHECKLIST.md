# ✅ Checklist de Publication - dnd-5e-core

## 📋 Avant la Publication

### 1. Vérification du Code ✅

- [x] Tous les tests passent
- [x] Code formaté (black)
- [x] Pas d'erreurs de lint (flake8)
- [x] Type hints vérifiés (mypy)
- [x] Documentation à jour

### 2. Vérification des Métadonnées ✅

- [x] Version mise à jour dans `pyproject.toml` (0.1.1)
- [x] Version mise à jour dans `setup.py` (0.1.1)
- [x] `CHANGELOG.md` à jour avec les nouvelles fonctionnalités
- [x] `README.md` à jour avec les exemples
- [x] Métadonnées PyPI complètes dans `pyproject.toml`
- [x] License MIT présente

### 3. Vérification des Fichiers ✅

- [x] `.gitignore` inclut `*.egg-info/`, `dist/`, `build/`
- [x] `MANIFEST.in` inclut les fichiers de données
- [x] `requirements.txt` à jour
- [x] Pas de fichiers sensibles (tokens, mots de passe)

### 4. Vérification des Données ✅

- [x] 332 monstres dans `collections/monsters.json`
- [x] 319 sorts dans `collections/spells.json`
- [x] Tous les fichiers JSON dans `data/` sont valides
- [x] `collections/` bien peuplé

---

## 🏗️ Construction du Package

### Étape 1: Nettoyage

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# Supprimer les anciennes builds
rm -rf dist/ build/ *.egg-info/

# Vérifier qu'il n'y a pas de fichiers non suivis importants
git status
```

### Étape 2: Installation des Outils

```bash
# Installer/mettre à jour les outils de build
pip install --upgrade build twine setuptools wheel
```

### Étape 3: Build

```bash
# Construire le package (source + wheel)
python -m build

# Vérifier les fichiers créés
ls -lh dist/
```

**Fichiers attendus:**
```
dist/
  ├── dnd-5e-core-0.1.1.tar.gz         (source distribution)
  └── dnd_5e_core-0.1.1-py3-none-any.whl  (wheel)
```

### Étape 4: Vérification du Build

```bash
# Vérifier le contenu du package
tar -tzf dist/dnd-5e-core-0.1.1.tar.gz | head -20

# Vérifier les métadonnées
twine check dist/*
```

**Résultat attendu:**
```
Checking dist/dnd-5e-core-0.1.1.tar.gz: PASSED
Checking dist/dnd_5e_core-0.1.1-py3-none-any.whl: PASSED
```

---

## 🧪 Tests du Package

### Test 1: Installation Locale

```bash
# Créer un environnement virtuel de test
python -m venv test-env
source test-env/bin/activate  # ou test-env\Scripts\activate sur Windows

# Installer depuis le wheel
pip install dist/dnd_5e_core-0.1.1-py3-none-any.whl

# Tester l'import
python -c "from dnd_5e_core.data import load_monster; print(load_monster('goblin')['name'])"
```

**Résultat attendu:** `Goblin`

### Test 2: Vérifier les Dépendances

```bash
# Lister les dépendances installées
pip show dnd-5e-core

# Vérifier que numpy et requests sont installés
pip list | grep -E "numpy|requests"
```

### Test 3: Tester les Imports Principaux

```bash
python << EOF
from dnd_5e_core.entities import Sprite, Monster
from dnd_5e_core.equipment import HealingPotion, PotionRarity
from dnd_5e_core.mechanics import DamageDice
from dnd_5e_core.abilities import Abilities, AbilityType
from dnd_5e_core.data import load_monster, load_spell, list_monsters

print("✅ Tous les imports fonctionnent!")
print(f"✅ {len(list_monsters())} monstres disponibles")
EOF
```

### Nettoyage

```bash
deactivate
rm -rf test-env/
```

---

## 📤 Publication sur TestPyPI (Optionnel mais Recommandé)

### Configuration

1. Créer un compte sur https://test.pypi.org/account/register/
2. Créer un token API: https://test.pypi.org/manage/account/token/
3. Configurer `~/.pypirc`:

```ini
[testpypi]
username = __token__
password = pypi-AgENdGVzdC5weXBpLm9yZw...
```

### Upload

```bash
# Uploader sur TestPyPI
twine upload --repository testpypi dist/*
```

**URL du package:** https://test.pypi.org/project/dnd-5e-core/

### Test d'Installation

```bash
# Créer un nouvel environnement
python -m venv test-testpypi
source test-testpypi/bin/activate

# Installer depuis TestPyPI (avec les dépendances depuis PyPI)
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ dnd-5e-core

# Tester
python -c "from dnd_5e_core.data import load_monster; print(load_monster('goblin')['name'])"

# Nettoyage
deactivate
rm -rf test-testpypi/
```

---

## 🚀 Publication sur PyPI (Production)

### Configuration

1. Créer un compte sur https://pypi.org/account/register/
2. Créer un token API: https://pypi.org/manage/account/token/
3. Configurer `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcC...
```

### Upload Final

```bash
# ⚠️ ATTENTION: Ceci est la publication finale!
# Une fois publié, vous ne pouvez pas supprimer ou modifier la version

# Upload sur PyPI
twine upload dist/*
```

**Résultat:**
```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading dnd-5e-core-0.1.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.7/8.7 MB
Uploading dnd_5e_core-0.1.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.7/8.7 MB

View at:
https://pypi.org/project/dnd-5e-core/0.1.1/
```

### Vérification

```bash
# Installer depuis PyPI
pip install dnd-5e-core

# Tester
python -c "from dnd_5e_core.data import load_monster; print('✅ Package installé depuis PyPI!')"
```

**URL publique:** https://pypi.org/project/dnd-5e-core/

---

## 🐙 Publication sur GitHub

### 1. Commit et Push

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# Ajouter tous les fichiers
git add .

# Commit
git commit -m "Release version 0.1.1

- Complete D&D 5e implementation
- 332 monsters, 319 spells
- Integrated JSON data (8.7 MB)
- UI-agnostic design
- Full offline support"

# Push
git push origin main
```

### 2. Créer un Tag

```bash
# Créer un tag annoté
git tag -a v0.1.1 -m "Version 0.1.1 - Complete D&D 5e Rules Engine

Features:
- Complete D&D 5e implementation with all core mechanics
- 332 monsters with full stat blocks
- 319 spells with complete details
- 65 weapons, 30 armors, 237 equipment items
- All data bundled (8.7 MB JSON)
- No external API required - works offline
- UI-agnostic design for any interface

See CHANGELOG.md for detailed changes."

# Push le tag
git push origin v0.1.1
```

### 3. Créer une GitHub Release

**Option A: Via l'interface Web**

1. Aller sur https://github.com/codingame-team/dnd-5e-core/releases
2. Cliquer sur **"Draft a new release"**
3. Sélectionner le tag: `v0.1.1`
4. Titre: `v0.1.1 - Complete D&D 5e Rules Engine`
5. Description: Copier depuis `CHANGELOG.md`
6. Attacher les fichiers:
   - `dist/dnd-5e-core-0.1.1.tar.gz`
   - `dist/dnd_5e_core-0.1.1-py3-none-any.whl`
7. Cliquer **"Publish release"**

**Option B: Via GitHub CLI**

```bash
# Installer GitHub CLI si nécessaire: brew install gh

# Créer la release
gh release create v0.1.1 \
  --title "v0.1.1 - Complete D&D 5e Rules Engine" \
  --notes-file CHANGELOG.md \
  dist/dnd-5e-core-0.1.1.tar.gz \
  dist/dnd_5e_core-0.1.1-py3-none-any.whl
```

---

## 🎨 Configuration GitHub

### Section "About"

1. Aller sur le dépôt: https://github.com/codingame-team/dnd-5e-core
2. Cliquer sur ⚙️ à droite de "About"
3. Configurer:

**Description:**
```
Complete D&D 5th Edition Rules Engine - Core game logic with 332 monsters, 319 spells, and full offline data. UI-agnostic Python package for building D&D applications.
```

**Website:**
```
https://pypi.org/project/dnd-5e-core/
```

**Topics:**
```
python, dnd, dungeons-dragons, dnd-5e, 5e, rpg, game-engine, 
tabletop, character-sheet, combat-engine, spells, monsters, 
dice-roller, game-development, python3, mit-license
```

### README Badges

Ajouter au début du README.md:

```markdown
[![PyPI version](https://badge.fury.io/py/dnd-5e-core.svg)](https://pypi.org/project/dnd-5e-core/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/dnd-5e-core)](https://pepy.tech/project/dnd-5e-core)
[![GitHub stars](https://img.shields.io/github/stars/codingame-team/dnd-5e-core?style=social)](https://github.com/codingame-team/dnd-5e-core)
```

---

## 📣 Annonce de la Publication

### Sur PyPI

✅ Automatique - votre package apparaîtra sur:
- https://pypi.org/project/dnd-5e-core/
- Recherches PyPI pour "dnd", "d&d", "5e", etc.

### Sur GitHub

✅ Automatique - visible sur:
- Page du dépôt avec le tag v0.1.1
- Section Releases
- Topics/tags

### Réseaux Sociaux (Optionnel)

- Reddit: r/Python, r/DnD, r/gamedev
- Twitter/X: #Python #DnD #GameDev
- Discord: Communautés Python et D&D

**Message suggéré:**
```
🎉 Nouveau package Python: dnd-5e-core v0.1.1

Complete D&D 5e Rules Engine avec:
✨ 332 monstres, 319 sorts
✨ 8.7 MB de données JSON intégrées
✨ Fonctionne hors ligne
✨ UI-agnostic

pip install dnd-5e-core

https://pypi.org/project/dnd-5e-core/
https://github.com/codingame-team/dnd-5e-core
```

---

## 🔄 Après la Publication

### Monitoring

- [ ] Vérifier les statistiques de téléchargement sur PyPI
- [ ] Surveiller les issues GitHub
- [ ] Répondre aux questions des utilisateurs
- [ ] Mettre à jour la documentation si nécessaire

### Prochaines Versions

Pour publier une nouvelle version:

1. Mettre à jour `version` dans `pyproject.toml` et `setup.py`
2. Mettre à jour `CHANGELOG.md`
3. Commit et push
4. Reconstruire: `python -m build`
5. Uploader: `twine upload dist/*`
6. Créer un nouveau tag et release GitHub

---

## ✅ Checklist Finale

### Avant Publication
- [x] Code testé et fonctionnel
- [x] Métadonnées complètes
- [x] CHANGELOG.md à jour
- [x] README.md à jour
- [x] .gitignore correct
- [x] License présente

### Build
- [ ] Anciennes builds supprimées (`rm -rf dist/ build/ *.egg-info/`)
- [ ] Outils de build installés (`pip install --upgrade build twine`)
- [ ] Package construit (`python -m build`)
- [ ] Build vérifié (`twine check dist/*`)

### Tests
- [ ] Installation locale testée
- [ ] Imports principaux testés
- [ ] Chargement de données testé
- [ ] TestPyPI testé (optionnel)

### Publication PyPI
- [ ] Compte PyPI créé
- [ ] Token API configuré dans `~/.pypirc`
- [ ] Package uploadé (`twine upload dist/*`)
- [ ] Installation depuis PyPI testée

### Publication GitHub
- [ ] Code commité et pushé
- [ ] Tag créé et pushé (`git tag v0.1.1`)
- [ ] GitHub Release créée avec fichiers dist/
- [ ] Section "About" configurée
- [ ] Badges ajoutés au README

### Post-Publication
- [ ] Package visible sur PyPI
- [ ] Release visible sur GitHub
- [ ] Installation testée: `pip install dnd-5e-core`
- [ ] Documentation accessible

---

## 🎉 Félicitations!

Votre package **dnd-5e-core** est maintenant publié et disponible pour la communauté! 🚀

**Liens:**
- PyPI: https://pypi.org/project/dnd-5e-core/
- GitHub: https://github.com/codingame-team/dnd-5e-core
- Installation: `pip install dnd-5e-core`

---

**Date de publication:** [À remplir après publication]
**Version:** 0.1.1
**Statut:** ✅ Prêt pour la publication

