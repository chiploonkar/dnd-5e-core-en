# 📤 Publication Guide - Version 0.1.1

## ✅ Current Step: READY TO PUBLISH

Version 0.1.1 is built and ready to be published on PyPI.

---

## 🔑 Publishing on PyPI

### Method 1: With API token (recommended)

```bash
cd /Users/display/PycharmProjects/dnd-5e-core
twine upload dist/*
```

When prompted:
```
Enter your API token: [Paste your PyPI token here]
```

### Method 2: With ~/.pypirc configuration

Create/edit `~/.pypirc`:
```ini
[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE
```

Then:
```bash
twine upload dist/*
```

---

## 🎯 After Publication

### 1. Verify on PyPI
- URL: https://pypi.org/project/dnd-5e-core/
- Version 0.1.1 should appear
- Verify metadata in the sidebar

### 2. Test installation
```bash
# In a new environment
pip install dnd-5e-core==0.1.1

# Verify
python -c "import dnd_5e_core; print(dnd_5e_core.__version__ if hasattr(dnd_5e_core, '__version__') else 'Package imported successfully')"
```

### 3. Create a Git Tag
```bash
git add pyproject.toml setup.py CHANGELOG.md
git commit -m "Release version 0.1.1 - Enhanced PyPI metadata"
git tag v0.1.1
git push origin main
git push origin v0.1.1
```

### 4. Create a GitHub Release
1. Go to: https://github.com/codingame-team/dnd-5e-core/releases/new
2. Tag: `v0.1.1`
3. Title: `v0.1.1 - Enhanced PyPI Metadata`
4. Description:
```markdown
## What's Changed

### Added
- **PyPI Metadata**: Complete metadata for better discoverability
  - Authors and maintainers with contact emails
  - 11 keywords for search optimization
  - 17 detailed classifiers
  - 8 project URLs (Homepage, Docs, Issues, etc.)
  
- **GitHub Configuration**: Files for "About" section setup
  - Complete project description
  - Recommended topics/tags
  - Setup instructions

### Improved
- Enhanced `pyproject.toml` with full PyPI metadata
- Updated documentation for publication

**Full Changelog**: https://github.com/codingame-team/dnd-5e-core/compare/v0.1.0...v0.1.1

### Installation
```bash
pip install dnd-5e-core==0.1.1
```
```

---

## 📊 Final Checks

Before publishing, verify:

✅ Version updated: 0.1.1
```bash
grep "version = " pyproject.toml
# Should display: version = "0.1.1"
```

✅ Successful Build:
```bash
ls -lh dist/
# Should show:
# dnd_5e_core-0.1.1-py3-none-any.whl
# dnd_5e_core-0.1.1.tar.gz
```

✅ Metadata present:
```bash
python -m zipfile -l dist/dnd_5e_core-0.1.1-py3-none-any.whl | grep METADATA
# Should display the METADATA file
```

✅ Updated CHANGELOG:
```bash
head -20 CHANGELOG.md
# Should show [0.1.1] - 2026-01-03
```

---

## 🎉 Expected Result

### On PyPI (https://pypi.org/project/dnd-5e-core/)

The page will display:

**Sidebar**:
```
┌─────────────────────────────────┐
│ Meta                            │
├─────────────────────────────────┤
│ License: MIT                    │
│ Author: D&D Development Team    │
│ Maintainers: D&D Development... │
│                                 │
│ Project links                   │
├─────────────────────────────────┤
│ Homepage                        │
│ Documentation                   │
│ Source Code                     │
│ Issues                          │
│ Bug Tracker                     │
│ Changelog                       │
│ Quick Start                     │
│                                 │
│ Statistics                      │
├─────────────────────────────────┤
│ GitHub statistics               │
│                                 │
│ Maintainers                     │
├─────────────────────────────────┤
│ D&D Development Team            │
│                                 │
│ Classifiers                     │
├─────────────────────────────────┤
│ Development Status :: 3 - Alpha │
│ Intended Audience :: Developers │
│ License :: OSI Approved :: MIT  │
│ ... (17 total)                  │
└─────────────────────────────────┘
```

**Description**:
The complete README.md with:
- 📖 About section
- ✨ Features
- 🚀 Installation
- 📚 Usage examples
- Etc.

---

## 🚨 In Case of Problems

### Error: "File already exists"
➡️ Version 0.1.1 already exists, increment to 0.1.2

### Error: "Invalid token"
➡️ Verify token on https://pypi.org/manage/account/token/

### Error: "Invalid metadata"
➡️ Verify `pyproject.toml` with:
```bash
python -m build
```

---

## 📞 Support

- **PyPI Help**: https://pypi.org/help/
- **Packaging Guide**: https://packaging.python.org/
- **Twine Docs**: https://twine.readthedocs.io/

---

## ✨ Final Command

```bash
cd /Users/display/PycharmProjects/dnd-5e-core
twine upload dist/*
# Enter your PyPI token when prompted
```

**Good luck! 🎉**
