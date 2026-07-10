# 📦 PyPI Publication Guide - dnd-5e-core

## 🎯 Overview

The script `build_package.sh` allows building and publishing the `dnd-5e-core` package on PyPI.

---

## 🚀 Quick Start

### 1. Local Build (Test)

```bash
# Clean and build
./build_package.sh --clean --build

# Verify generated files
ls -lh dist/
```

### 2. Publication on TestPyPI (Recommended for testing)

```bash
# Publish on TestPyPI
./build_package.sh --test

# Install from TestPyPI to test
pip install --index-url https://test.pypi.org/simple/ dnd-5e-core
```

### 3. Publication on PyPI (Production)

```bash
# Complete publication (clean + build + publish)
./build_package.sh --all

# OR step-by-step
./build_package.sh --clean
./build_package.sh --build
./build_package.sh --publish
```

---

## 📋 Script Options

| Option | Description |
|--------|-------------|
| `--clean` | Cleans previous build files (dist/, build/, *.egg-info) |
| `--build` | Builds the package (wheel and source distribution) |
| `--test` | Publishes on TestPyPI (test environment) |
| `--publish` | Publishes on PyPI production (⚠️ irreversible) |
| `--all` | Runs clean + build + publish |
| `--help` | Displays help |

---

## 🔧 Prerequisites

### 1. PyPI Configuration

#### Create a PyPI Account
- Production: https://pypi.org/account/register/
- Test: https://test.pypi.org/account/register/

#### Create an API Token
1. Log in to PyPI
2. Account settings → API tokens
3. Create a token with scope "Entire account" or "Project: dnd-5e-core"
4. Copy the token (starts with `pypi-`)

#### Configure `~/.pypirc`

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TEST_TOKEN_HERE
```

**Permissions**:
```bash
chmod 600 ~/.pypirc
```

### 2. Python Tools

The script automatically installs:
- `build` - Modern build tool
- `twine` - Secure publication on PyPI
- `wheel` - Wheel package support
- `setuptools` - Packaging tools

---

## 📝 Publication Workflow

### Step 1: Prepare the Release

```bash
# 1. Update version in setup.py
vim setup.py  # version='0.2.6'

# 2. Update CHANGELOG.md
vim CHANGELOG.md

# 3. Commit changes
git add setup.py CHANGELOG.md
git commit -m "Bump version to 0.2.6"
git push
```

### Step 2: Build and Test

```bash
# Clean and build
./build_package.sh --clean --build

# Verify content
tar -tzf dist/dnd-5e-core-0.2.6.tar.gz | head -20

# Test locally
pip install dist/dnd-5e-core-0.2.6-py3-none-any.whl --force-reinstall
```

### Step 3: Publish on TestPyPI

```bash
# Publish on test
./build_package.sh --test

# Install from test to verify
pip install --index-url https://test.pypi.org/simple/ dnd-5e-core==0.2.6

# Test the package
python -c "from dnd_5e_core import ClassAbilities; print('OK')"
```

### Step 4: Publish on PyPI

```bash
# Final publication
./build_package.sh --publish

# Verify on PyPI
# https://pypi.org/project/dnd-5e-core/
```

### Step 5: Create a Git Tag

```bash
# Create a version tag
git tag -a v0.2.6 -m "Version 0.2.6 - Class abilities and racial traits"
git push origin v0.2.6

# Create a release on GitHub
# https://github.com/votre-user/dnd-5e-core/releases/new
```

---

## ⚠️ Error Handling

### Error: "File already exists"

```
ERROR: File already exists. See https://pypi.org/help/#file-name-reuse
```

**Solution**: Increment the version in `setup.py`

PyPI does **not** allow re-uploading an existing version (even after deletion).

### Error: "Invalid credentials"

```
ERROR: Invalid or non-existent authentication information.
```

**Solutions**:
1. Verify `~/.pypirc`
2. Verify that the token is valid
3. Use `twine upload` manually to see the exact error

### Error: "Package name already taken"

If the name `dnd-5e-core` is already taken:
1. Choose another name in `setup.py`
2. OR contact the PyPI maintainers

---

## 🔍 Package Verification

### After Build

```bash
# Verify metadata
python setup.py check

# Verify with twine
twine check dist/*

# Inspect content
tar -tzf dist/dnd-5e-core-*.tar.gz
unzip -l dist/dnd-5e-core-*.whl
```

### After Publication

```bash
# Install in a clean environment
python -m venv test_env
source test_env/bin/activate
pip install dnd-5e-core

# Test
python -c "
from dnd_5e_core import ClassAbilities, RacialTraits
from dnd_5e_core.data.loaders import simple_character_generator
wizard = simple_character_generator(5, 'elf', 'wizard', 'Gandalf')
print(f'✅ {wizard.name} created successfully!')
"

# Clean up
deactivate
rm -rf test_env
```

---

## 📊 Publication Checklist

### Before Publication

- [ ] Version updated in `setup.py`
- [ ] CHANGELOG.md updated
- [ ] README.md updated
- [ ] Tests pass (`pytest`)
- [ ] Package builds without errors
- [ ] PyPI token configured
- [ ] Git commit and push

### Test PyPI

- [ ] Publication on TestPyPI successful
- [ ] Installation from TestPyPI works
- [ ] Import tests work
- [ ] Documentation accessible

### Production PyPI

- [ ] Published on PyPI
- [ ] Git tag created
- [ ] GitHub release created
- [ ] Announcement made (if applicable)

---

## 📚 Resources

### Official Documentation
- **PyPI**: https://pypi.org/project/dnd-5e-core/
- **TestPyPI**: https://test.pypi.org/project/dnd-5e-core/
- **Python Packaging Guide**: https://packaging.python.org/

### Tools
- **twine**: https://twine.readthedocs.io/
- **build**: https://pypa-build.readthedocs.io/
- **setuptools**: https://setuptools.pypa.io/

### D&D 5e API
- **Data source**: https://www.dnd5eapi.co
- **API Documentation**: https://5e-bits.github.io/docs/api

---

## 🎯 Command Examples

### Standard Complete Workflow

```bash
# 1. Prepare
vim setup.py  # version='0.2.6'
vim CHANGELOG.md
git add . && git commit -m "Version 0.2.6"

# 2. Build and local test
./build_package.sh --clean --build
pip install dist/*.whl --force-reinstall
python -c "import dnd_5e_core; print('OK')"

# 3. Test PyPI
./build_package.sh --test
# Verify on https://test.pypi.org/project/dnd-5e-core/

# 4. Production
./build_package.sh --publish
# Verify on https://pypi.org/project/dnd-5e-core/

# 5. Tag
git tag v0.2.6 && git push --tags
```

### Fast Workflow (Dangerous)

```bash
# All in a single command (not recommended for prod)
./build_package.sh --all
```

---

**Guide Version**: 1.0  
**Date**: January 18, 2026  
**Package**: dnd-5e-core  
**Status**: ✅ Production Ready

🎉 Complete guide to publish on PyPI! 📦✨
