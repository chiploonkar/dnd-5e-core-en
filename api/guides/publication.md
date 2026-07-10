# Publication Guide - dnd-5e-core

## 📦 Publication Options

### Option 1: GitHub only (Simple)

Your package is already usable directly from GitHub:

```bash
pip install git+https://github.com/codingame-team/dnd-5e-core.git
```

**Advantages:**
- No additional configuration required
- Free and immediate
- Perfect for internal or in-development projects

**Disadvantages:**
- Less visibility
- No easy versioning
- Requires Git installed

---

### Option 2: PyPI (Python Package Index) - RECOMMENDED

PyPI is the official Python package registry. This is where all packages installable via `pip install` are found.

#### Steps to publish on PyPI:

#### 1. Create a PyPI account
- Production: https://pypi.org/account/register/
- Test (recommended to start): https://test.pypi.org/account/register/

#### 2. Install build tools
```bash
pip install --upgrade build twine
```

#### 3. Create the package
```bash
# Clean up old builds
rm -rf dist/ build/ *.egg-info/

# Create distributions
python -m build
```

This will create two files in `dist/`:
- `dnd-5e-core-0.1.0.tar.gz` (source distribution)
- `dnd_5e_core-0.1.0-py3-none-any.whl` (wheel distribution)

#### 4. Test on TestPyPI (RECOMMENDED first)
```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test the installation
pip install --index-url https://test.pypi.org/simple/ dnd-5e-core
```

#### 5. Publish on PyPI (production)
```bash
twine upload dist/*
```

#### 6. User installation
```bash
pip install dnd-5e-core
```

---

## 🔧 Migration to pyproject.toml

I created a modern `pyproject.toml` file that replaces `setup.py`. It is the new Python standard (PEP 517/518).

### Advantages:
- Compatible with Python 3.13
- Simpler and declarative
- Modern standard
- Avoids obsolete setuptools errors

### What to do with setup.py?

You have **two options**:

**Option A: Keep both (maximum compatibility)**
- Keep `setup.py` AND `pyproject.toml`
- `pyproject.toml` will be used as priority
- Old `setup.py` remains for backward compatibility

**Option B: Use only pyproject.toml (modern)**
- Delete `setup.py`
- Cleaner, but requires `setuptools>=61.0`

I recommend **Option B** for a new project.

---

## Files to Exclude from Git

Your `.gitignore` is already well configured. These files MUST NOT be versioned:

- `*.egg-info/` - Local build artifacts
- `build/` - Temporary build folder
- `dist/` - Created distributions (tar.gz, whl)
- `__pycache__/` - Python cache

These files are already excluded in your `.gitignore`

---

## Recommended Publication Workflow

### 1. Development
```bash
# Installation in development mode
pip install -e .

# Or with dev dependencies
pip install -e ".[dev]"
```

### 2. Tests
```bash
pytest
```

### 3. Version update
Edit `pyproject.toml`:
```toml
version = "0.1.1"  # Increment the version
```

### 4. Build and publication
```bash
# Clean
rm -rf dist/ build/ *.egg-info/

# Build
python -m build

# Publish (TestPyPI first to test)
twine upload --repository testpypi dist/*

# Then PyPI if everything is OK
twine upload dist/*
```

### 5. Git Tag
```bash
git tag v0.1.1
git push origin v0.1.1
```

---

## 🔐 Security - PyPI Tokens

**Never use your password directly with twine!**

### Create an API Token:
1. Log in to PyPI
2. Account Settings > API Tokens
3. Create a token for your project
4. Use it during upload:

```bash
# Twine will ask you:
# Username: __token__
# Password: pypi-AgEIcHlwaS5vcmc... (your token)
```

Or configure `~/.pypirc`:
```ini
[testpypi]
username = __token__
password = pypi-AgEI...

[pypi]
username = __token__
password = pypi-AgEI...
```

---

## Summary

| Aspect | GitHub | PyPI |
|--------|--------|------|
| **Installation** | `pip install git+https://...` | `pip install dnd-5e-core` |
| **Visibility** | Medium | Maximum |
| **Setup** | None | Account + upload |
| **Cost** | Free | Free |
| **Recommended for** | Internal projects | Public projects |

---

## ❓ Frequently Asked Questions

### Should I delete setup.py?
Optional. `pyproject.toml` is sufficient for new installations.

### Is the .egg-info folder necessary?
**NO**. It is automatically generated and MUST NOT be versioned.

### What is the minimum Python version?
Your project specifies `>=3.10`. This is good for a modern project in 2026.

### Can I publish on both GitHub and PyPI?
**YES!** It is even recommended. GitHub for the source code, PyPI for distribution.

---

## Resources

- PyPI Documentation: https://packaging.python.org/
- Packaging guide: https://packaging.python.org/tutorials/packaging-projects/
- Twine: https://twine.readthedocs.io/
