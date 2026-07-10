# 🚀 Quick Commands - dnd-5e-core Publishing

## ⚡ Direct Copy-Paste

### 🏗️ Package Build
```bash
cd /Users/display/PycharmProjects/dnd-5e-core
rm -rf dist/ build/ *.egg-info/
pip install --upgrade build twine
python -m build
twine check dist/*
```

### 📦 PyPI Publication (Production)
```bash
twine upload dist/*
```

### 🧪 TestPyPI Publication (Test First)
```bash
twine upload --repository testpypi dist/*
```

### 🐙 GitHub Tag & Release
```bash
git tag -a v0.1.1 -m "Version 0.1.1 - Complete D&D 5e Rules Engine"
git push origin v0.1.1
```

### ✅ Local Installation Test
```bash
python -m venv test-env
source test-env/bin/activate
pip install dist/dnd_5e_core-0.1.1-py3-none-any.whl
python -c "from dnd_5e_core.data import load_monster; print(load_monster('goblin')['name'])"
deactivate
rm -rf test-env/
```

### 🧹 Cleaning
```bash
rm -rf dist/ build/ *.egg-info/ __pycache__/ .pytest_cache/
```

---

## 📋 Initial Configuration (One-time)

### Create ~/.pypirc
```bash
cat > ~/.pypirc << 'EOF'
[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE

[testpypi]
username = __token__
password = pypi-YOUR_TESTPYPI_TOKEN_HERE
EOF

chmod 600 ~/.pypirc
```

### Get Tokens
- PyPI: https://pypi.org/manage/account/token/
- TestPyPI: https://test.pypi.org/manage/account/token/

---

## 🔍 Verification Commands

### Check version
```bash
grep "version = " pyproject.toml
```

### List package files
```bash
tar -tzf dist/dnd-5e-core-0.1.1.tar.gz | head -20
```

### View metadata
```bash
python -m build && tar -xzf dist/dnd-5e-core-0.1.1.tar.gz -O dnd-5e-core-0.1.1/PKG-INFO
```

### Count monsters
```bash
python -c "from dnd_5e_core.data import list_monsters; print(len(list_monsters()))"
```

---

## 📊 Important URLs

### After Publication
- **PyPI:** https://pypi.org/project/dnd-5e-core/
- **GitHub:** https://github.com/codingame-team/dnd-5e-core
- **Releases:** https://github.com/codingame-team/dnd-5e-core/releases

### For Configuration
- **PyPI Account:** https://pypi.org/account/
- **PyPI Tokens:** https://pypi.org/manage/account/token/
- **TestPyPI:** https://test.pypi.org/
- **GitHub Releases:** https://github.com/codingame-team/dnd-5e-core/releases/new

---

## 🎯 Complete Workflow in One Command

```bash
cd /Users/display/PycharmProjects/dnd-5e-core && \
rm -rf dist/ build/ *.egg-info/ && \
python -m build && \
twine check dist/* && \
echo "✅ Build complete! Now: twine upload dist/*"
```

---

## 📚 Detailed Guides

For more information, check:
- `PUBLICATION_CHECKLIST.md` - Complete checklist
- `PUBLICATION_EXPLAINED.md` - Detailed explanations
- `SUMMARY_SOLUTIONS.md` - Answers to your questions

---

**Last updated:** January 5, 2026
