# 🚀 QUICK PUBLICATION GUIDE - Version 0.2.6

## ⚡ Immediate Publication

```bash
cd /Users/display/PycharmProjects/dnd-5e-core
./publish.sh
```

Answer **yes** when prompted.

---

## 📋 What the Script Does

1.  Verifies that the version is indeed 0.2.6
2.  Cleans dist/, build/, *.egg-info
3.  Installs/updates build and twine
4.  Builds the package (wheel + source)
5.  Verifies with twine check
6.  Lists the generated files
7.  Publishes to PyPI (after confirmation)

---

## ✅ Prerequisites

Make sure `~/.pypirc` is configured:

```ini
[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE
```

---

## 🔧 Troubleshooting

### If the publish.sh script does not work

Run manually:

```bash
# 1. Clean
rm -rf dist/ build/ *.egg-info dnd_5e_core.egg-info/

# 2. Verify version
grep 'version=' setup.py
# Should display: version="0.2.6"

# 3. Install tools
python3 -m pip install --upgrade build twine

# 4. Build
python3 -m build

# 5. Verify
python3 -m twine check dist/*

# 6. View files
ls -lh dist/
# Should display: dnd_5e_core-0.2.6.tar.gz and dnd_5e_core-0.2.6-py3-none-any.whl

# 7. Publish
python3 -m twine upload dist/*
```

---

## ❌ Common Error

### "File already exists"

If you see:
```
ERROR: File already exists ('dnd_5e_core-0.2.4-py3-none-any.whl')
```

**Cause**: Old files in dist/

**Solution**:
```bash
rm -rf dist/
python3 -m build
python3 -m twine upload dist/*
```

---

## ✅ Post-Publication Verification

```bash
# Wait 2-3 minutes

# Install from PyPI
pip install dnd-5e-core==0.2.6 --upgrade

# Test
python3 -c "
from dnd_5e_core import ClassAbilities, RacialTraits
from dnd_5e_core.data.loaders import simple_character_generator
print('✅ Package dnd-5e-core v0.2.6 works!')
"
```

---

## 🎯 Ultra-Fast Command

```bash
cd /Users/display/PycharmProjects/dnd-5e-core && ./publish.sh
```

That's all! 🎉

---

**Date**: January 18, 2026  
**Version**: 0.2.6  
**Status**: ✅ Ready to publish
