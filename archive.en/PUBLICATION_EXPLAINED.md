# dnd-5e-core Package Publication Guide

## 📚 Frequently Asked Questions

### 1. Is the `dnd_5e_core.egg-info` folder necessary?

**Answer:** No, this folder is **NOT necessary** for publication.

**Explanation:**
- The `.egg-info` folder is automatically generated during installation in development mode (`pip install -e .`)
- It contains temporary metadata for your local installation
- It must be **ignored by Git** (already in `.gitignore`)
- When publishing on PyPI, it is the `pyproject.toml` file that provides the metadata

**Automatically generated files (NOT to be versioned):**
```
dnd_5e_core.egg-info/    ❌ Do not commit
dist/                    ❌ Do not commit
build/                   ❌ Do not commit
__pycache__/            ❌ Do not commit
*.pyc                   ❌ Do not commit
```

---

### 2. Where to publish the package?

You have **several options** for publishing your Python package:

#### Option 1: PyPI (Python Package Index) - **RECOMMENDED** ✅

**This is the official platform for Python packages.**

**Advantages:**
- Easy installation: `pip install dnd-5e-core`
- Discovery by the Python community
- Integration with pip, Poetry, etc.
- Automatic version badges
- Download statistics

**How to publish on PyPI:**
```bash
# 1. Install build tools
pip install --upgrade build twine

# 2. Build the package
python -m build

# 3. Upload to PyPI (production)
twine upload dist/*

# Or first test on TestPyPI
twine upload --repository testpypi dist/*
```

**Website:** https://pypi.org/

---

#### Option 2: GitHub Releases 🐙

**Publish source code on GitHub.**

**Advantages:**
- Source code versioning
- Issues and Pull Requests
- Documentation with GitHub Pages
- CI/CD Actions
- Easy collaboration

**How to publish on GitHub:**
```bash
# 1. Create a new tag
git tag -a v0.1.1 -m "Version 0.1.1 - Complete D&D 5e implementation"

# 2. Push the tag
git push origin v0.1.1

# 3. Create a release on GitHub
# - Go to https://github.com/your-username/dnd-5e-core/releases
# - Click on "Draft a new release"
# - Select the tag v0.1.1
# - Add release notes
# - Attach files dist/*.tar.gz and dist/*.whl
```

**Installation from GitHub:**
```bash
pip install git+https://github.com/your-username/dnd-5e-core.git
```

---

#### Option 3: BOTH - PyPI + GitHub (BEST APPROACH) 🏆

**Use GitHub for development and PyPI for distribution.**

**Recommended workflow:**
1. Development on GitHub (code, issues, PRs)
2. Publish on PyPI for easy installation
3. Create GitHub Releases for each version
4. Automate with GitHub Actions

---

### 3. Missing metadata for PyPI

PyPI displays your package better if you provide all metadata in `pyproject.toml`:

#### ✅ Metadata currently present:
- ✅ `name`: "dnd-5e-core"
- ✅ `version`: "0.1.1"
- ✅ `description`: Short description
- ✅ `readme`: README.md (long description)
- ✅ `authors`: Author and email
- ✅ `license`: MIT
- ✅ `keywords`: Keywords for search
- ✅ `classifiers`: PyPI Classifiers
- ✅ `dependencies`: Required dependencies
- ✅ `urls`: Homepage, Repository, Issues, etc.

#### ✨ Complete metadata (already configured):

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

## 🚀 Complete Publication Process

### Step 1: Prepare the package

```bash
# 1. Update version in pyproject.toml
# 2. Update CHANGELOG.md
# 3. Commit changes
git add .
git commit -m "Prepare version 0.1.1"
```

### Step 2: Build the package

```bash
# Install tools
pip install --upgrade build twine

# Clean up old builds
rm -rf dist/ build/ *.egg-info

# Build
python -m build
```

This will create:
- `dist/dnd-5e-core-0.1.1.tar.gz` (source distribution)
- `dist/dnd_5e_core-0.1.1-py3-none-any.whl` (wheel)

### Step 3: Test locally

```bash
# Create a new virtual environment
python -m venv test-env
source test-env/bin/activate

# Install from the wheel file
pip install dist/dnd_5e_core-0.1.1-py3-none-any.whl

# Test
python -c "from dnd_5e_core.data import load_monster; print(load_monster('goblin'))"
```

### Step 4: Publish on TestPyPI (optional but recommended)

```bash
# Create an account on https://test.pypi.org/
# Upload
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ dnd-5e-core
```

### Step 5: Publish on PyPI (production)

```bash
# Create an account on https://pypi.org/
# Upload
twine upload dist/*

# Verify
pip install dnd-5e-core
```

### Step 6: Create a GitHub Release

```bash
# Tag
git tag -a v0.1.1 -m "Version 0.1.1"
git push origin v0.1.1

# Create release on GitHub with dist/ files
```

---

## 🔐 Credentials Configuration

### PyPI Token (Recommended)

1. Go to https://pypi.org/manage/account/token/
2. Create a new API token
3. Create `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcC... (your token)

[testpypi]
username = __token__
password = pypi-AgENdGVzdC5weXBpLm9yZw... (your token)
```

---

## 📊 After Publication

### On PyPI

Your package will appear at:
- https://pypi.org/project/dnd-5e-core/

**Checks:**
- ✅ Long description (README.md)
- ✅ Sidebar links (Homepage, Repository, etc.)
- ✅ Classifiers
- ✅ Download statistics

### On GitHub

Add badges to README.md:

```markdown
[![PyPI version](https://badge.fury.io/py/dnd-5e-core.svg)](https://pypi.org/project/dnd-5e-core/)
[![Downloads](https://pepy.tech/badge/dnd-5e-core)](https://pepy.tech/project/dnd-5e-core)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```

---

## 🤖 Automation with GitHub Actions

Create `.github/workflows/publish.yml`:

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

## 📝 Summary

1. **dnd_5e_core.egg-info** ➜ **Is NOT necessary** (automatically generated)
2. **Where to publish** ➜ **PyPI + GitHub** (best approach)
3. **Metadata** ➜ **Already well configured in pyproject.toml**
4. **Publication** ➜ Follow the 6-step process above

**Essential commands:**
```bash
python -m build              # Build
twine upload dist/*          # Publish to PyPI
git tag -a v0.1.1 -m "..."  # Git version
```

Your package is now ready for publication! 🎉
