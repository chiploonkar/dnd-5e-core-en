# ✅ Publication Checklist - dnd-5e-core

## 📋 Before Publication

### 1. Code Verification ✅

- [x] All tests pass
- [x] Code formatted (black)
- [x] No lint errors (flake8)
- [x] Type hints verified (mypy)
- [x] Documentation up to date

### 2. Metadata Verification ✅

- [x] Version updated in `pyproject.toml` (0.1.1)
- [x] Version updated in `setup.py` (0.1.1)
- [x] `CHANGELOG.md` up to date with new features
- [x] `README.md` up to date with examples
- [x] Complete PyPI metadata in `pyproject.toml`
- [x] MIT License present

### 3. File Verification ✅

- [x] `.gitignore` includes `*.egg-info/`, `dist/`, `build/`
- [x] `MANIFEST.in` includes data files
- [x] `requirements.txt` up to date
- [x] No sensitive files (tokens, passwords)

### 4. Data Verification ✅

- [x] 332 monsters in `collections/monsters.json`
- [x] 319 spells in `collections/spells.json`
- [x] All JSON files in `data/` are valid
- [x] `collections/` well populated

---

## 🏗️ Building the Package

### Step 1: Cleaning

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# Delete old builds
rm -rf dist/ build/ *.egg-info/

# Verify there are no important untracked files
git status
```

### Step 2: Tool Installation

```bash
# Install/update build tools
pip install --upgrade build twine setuptools wheel
```

### Step 3: Build

```bash
# Build the package (source + wheel)
python -m build

# Check the created files
ls -lh dist/
```

**Expected Files:**
```
dist/
  ├── dnd-5e-core-0.1.1.tar.gz         (source distribution)
  └── dnd_5e_core-0.1.1-py3-none-any.whl  (wheel)
```

### Step 4: Build Verification

```bash
# Verify package contents
tar -tzf dist/dnd-5e-core-0.1.1.tar.gz | head -20

# Verify metadata
twine check dist/*
```

**Expected Result:**
```
Checking dist/dnd-5e-core-0.1.1.tar.gz: PASSED
Checking dist/dnd_5e_core-0.1.1-py3-none-any.whl: PASSED
```

---

## 🧪 Testing the Package

### Test 1: Local Installation

```bash
# Create a test virtual environment
python -m venv test-env
source test-env/bin/activate  # or test-env\Scripts\activate on Windows

# Install from wheel
pip install dist/dnd_5e_core-0.1.1-py3-none-any.whl

# Test import
python -c "from dnd_5e_core.data import load_monster; print(load_monster('goblin')['name'])"
```

**Expected Result:** `Goblin`

### Test 2: Verify Dependencies

```bash
# List installed dependencies
pip show dnd-5e-core

# Verify that numpy and requests are installed
pip list | grep -E "numpy|requests"
```

### Test 3: Test Main Imports

```bash
python << EOF
from dnd_5e_core.entities import Sprite, Monster
from dnd_5e_core.equipment import HealingPotion, PotionRarity
from dnd_5e_core.mechanics import DamageDice
from dnd_5e_core.abilities import Abilities, AbilityType
from dnd_5e_core.data import load_monster, load_spell, list_monsters

print("✅ All imports work!")
print(f"✅ {len(list_monsters())} monsters available")
EOF
```

### Cleaning

```bash
deactivate
rm -rf test-env/
```

---

## 📤 Publishing on TestPyPI (Optional but Recommended)

### Configuration

1. Create an account on https://test.pypi.org/account/register/
2. Create an API token: https://test.pypi.org/manage/account/token/
3. Configure `~/.pypirc`:

```ini
[testpypi]
username = __token__
password = pypi-AgENdGVzdC5weXBpLm9yZw...
```

### Upload

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*
```

**Package URL:** https://test.pypi.org/project/dnd-5e-core/

### Installation Test

```bash
# Create a new environment
python -m venv test-testpypi
source test-testpypi/bin/activate

# Install from TestPyPI (with dependencies from PyPI)
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ dnd-5e-core

# Test
python -c "from dnd_5e_core.data import load_monster; print(load_monster('goblin')['name'])"

# Cleaning
deactivate
rm -rf test-testpypi/
```

---

## 🚀 Publishing on PyPI (Production)

### Configuration

1. Create an account on https://pypi.org/account/register/
2. Create an API token: https://pypi.org/manage/account/token/
3. Configure `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcC...
```

### Final Upload

```bash
# ⚠️ WARNING: This is the final publication!
# Once published, you cannot delete or modify the version

# Upload to PyPI
twine upload dist/*
```

**Result:**
```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading dnd-5e-core-0.1.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.7/8.7 MB
Uploading dnd_5e_core-0.1.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.7/8.7 MB

View at:
https://pypi.org/project/dnd-5e-core/0.1.1/
```

### Verification

```bash
# Install from PyPI
pip install dnd-5e-core

# Test
python -c "from dnd_5e_core.data import load_monster; print('✅ Package installed from PyPI!')"
```

**Public URL:** https://pypi.org/project/dnd-5e-core/

---

## 🐙 Publishing on GitHub

### 1. Commit and Push

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# Add all files
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

### 2. Create a Tag

```bash
# Create an annotated tag
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

# Push the tag
git push origin v0.1.1
```

### 3. Create a GitHub Release

**Option A: Via the Web Interface**

1. Go to https://github.com/codingame-team/dnd-5e-core/releases
2. Click **"Draft a new release"**
3. Select the tag: `v0.1.1`
4. Title: `v0.1.1 - Complete D&D 5e Rules Engine`
5. Description: Copy from `CHANGELOG.md`
6. Attach files:
   - `dist/dnd-5e-core-0.1.1.tar.gz`
   - `dist/dnd_5e_core-0.1.1-py3-none-any.whl`
7. Click **"Publish release"**

**Option B: Via GitHub CLI**

```bash
# Install GitHub CLI if necessary: brew install gh

# Create the release
gh release create v0.1.1 \
  --title "v0.1.1 - Complete D&D 5e Rules Engine" \
  --notes-file CHANGELOG.md \
  dist/dnd-5e-core-0.1.1.tar.gz \
  dist/dnd_5e_core-0.1.1-py3-none-any.whl
```

---

## 🎨 GitHub Configuration

### "About" Section

1. Go to the repository: https://github.com/codingame-team/dnd-5e-core
2. Click on ⚙️ to the right of "About"
3. Configure:

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

Add to the top of README.md:

```markdown
[![PyPI version](https://badge.fury.io/py/dnd-5e-core.svg)](https://pypi.org/project/dnd-5e-core/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/dnd-5e-core)](https://pepy.tech/project/dnd-5e-core)
[![GitHub stars](https://img.shields.io/github/stars/codingame-team/dnd-5e-core?style=social)](https://github.com/codingame-team/dnd-5e-core)
```

---

## 📣 Announcing the Publication

### On PyPI

✅ Automatic - your package will appear on:
- https://pypi.org/project/dnd-5e-core/
- PyPI searches for "dnd", "d&d", "5e", etc.

### On GitHub

✅ Automatic - visible on:
- Repository page with tag v0.1.1
- Releases section
- Topics/tags

### Social Media (Optional)

- Reddit: r/Python, r/DnD, r/gamedev
- Twitter/X: #Python #DnD #GameDev
- Discord: Python and D&D communities

**Suggested message:**
```
🎉 New Python package: dnd-5e-core v0.1.1

Complete D&D 5e Rules Engine with:
✨ 332 monsters, 319 spells
✨ 8.7 MB built-in JSON data
✨ Works offline
✨ UI-agnostic

pip install dnd-5e-core

https://pypi.org/project/dnd-5e-core/
https://github.com/codingame-team/dnd-5e-core
```

---

## 🔄 After Publication

### Monitoring

- [ ] Check download statistics on PyPI
- [ ] Monitor GitHub issues
- [ ] Answer user questions
- [ ] Update documentation if necessary

### Next Versions

To publish a new version:

1. Update `version` in `pyproject.toml` and `setup.py`
2. Update `CHANGELOG.md`
3. Commit and push
4. Rebuild: `python -m build`
5. Upload: `twine upload dist/*`
6. Create a new GitHub tag and release

---

## ✅ Final Checklist

### Before Publication
- [x] Code tested and functional
- [x] Complete metadata
- [x] CHANGELOG.md up to date
- [x] README.md up to date
- [x] Correct .gitignore
- [x] License present

### Build
- [ ] Old builds deleted (`rm -rf dist/ build/ *.egg-info/`)
- [ ] Build tools installed (`pip install --upgrade build twine`)
- [ ] Package built (`python -m build`)
- [ ] Build verified (`twine check dist/*`)

### Tests
- [ ] Local installation tested
- [ ] Main imports tested
- [ ] Data loading tested
- [ ] TestPyPI tested (optional)

### PyPI Publication
- [ ] PyPI account created
- [ ] API Token configured in `~/.pypirc`
- [ ] Package uploaded (`twine upload dist/*`)
- [ ] Installation from PyPI tested

### GitHub Publication
- [ ] Code committed and pushed
- [ ] Tag created and pushed (`git tag v0.1.1`)
- [ ] GitHub Release created with dist/ files
- [ ] "About" section configured
- [ ] Badges added to README

### Post-Publication
- [ ] Package visible on PyPI
- [ ] Release visible on GitHub
- [ ] Installation tested: `pip install dnd-5e-core`
- [ ] Documentation accessible

---

## 🎉 Congratulations!

Your package **dnd-5e-core** is now published and available to the community! 🚀

**Links:**
- PyPI: https://pypi.org/project/dnd-5e-core/
- GitHub: https://github.com/codingame-team/dnd-5e-core
- Installation: `pip install dnd-5e-core`

---

**Publication date:** [To be completed after publication]
**Version:** 0.1.1
**Status:** ✅ Ready for publication
