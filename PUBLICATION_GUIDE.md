# 📤 Guide de Publication - Version 0.1.1

## ✅ Étape actuelle : PRÊT À PUBLIER

La version 0.1.1 est construite et prête à être publiée sur PyPI.

---

## 🔑 Publication sur PyPI

### Méthode 1 : Avec token API (recommandé)

```bash
cd /Users/display/PycharmProjects/dnd-5e-core
twine upload dist/*
```

Lorsque demandé :
```
Enter your API token: [Coller votre token PyPI ici]
```

### Méthode 2 : Avec configuration ~/.pypirc

Créez/éditez `~/.pypirc` :
```ini
[pypi]
username = __token__
password = pypi-VOTRE_TOKEN_ICI
```

Puis :
```bash
twine upload dist/*
```

---

## 🎯 Après la publication

### 1. Vérifier sur PyPI
- URL : https://pypi.org/project/dnd-5e-core/
- Version 0.1.1 devrait apparaître
- Vérifier les métadonnées dans la barre latérale

### 2. Tester l'installation
```bash
# Dans un nouvel environnement
pip install dnd-5e-core==0.1.1

# Vérifier
python -c "import dnd_5e_core; print(dnd_5e_core.__version__ if hasattr(dnd_5e_core, '__version__') else 'Package imported successfully')"
```

### 3. Créer un tag Git
```bash
git add pyproject.toml setup.py CHANGELOG.md
git commit -m "Release version 0.1.1 - Enhanced PyPI metadata"
git tag v0.1.1
git push origin main
git push origin v0.1.1
```

### 4. Créer une Release GitHub
1. Aller sur : https://github.com/codingame-team/dnd-5e-core/releases/new
2. Tag : `v0.1.1`
3. Title : `v0.1.1 - Enhanced PyPI Metadata`
4. Description :
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

## 📊 Vérifications finales

Avant de publier, vérifiez :

✅ Version mise à jour : 0.1.1
```bash
grep "version = " pyproject.toml
# Devrait afficher : version = "0.1.1"
```

✅ Build réussi :
```bash
ls -lh dist/
# Devrait montrer :
# dnd_5e_core-0.1.1-py3-none-any.whl
# dnd_5e_core-0.1.1.tar.gz
```

✅ Métadonnées présentes :
```bash
python -m zipfile -l dist/dnd_5e_core-0.1.1-py3-none-any.whl | grep METADATA
# Devrait afficher le fichier METADATA
```

✅ CHANGELOG mis à jour :
```bash
head -20 CHANGELOG.md
# Devrait montrer [0.1.1] - 2026-01-03
```

---

## 🎉 Résultat attendu

### Sur PyPI (https://pypi.org/project/dnd-5e-core/)

La page affichera :

**Barre latérale** :
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
│ ... (17 au total)               │
└─────────────────────────────────┘
```

**Description** :
Le README.md complet avec :
- 📖 About section
- ✨ Features
- 🚀 Installation
- 📚 Usage examples
- Etc.

---

## 🚨 En cas de problème

### Erreur : "File already exists"
➡️ La version 0.1.1 existe déjà, incrémenter à 0.1.2

### Erreur : "Invalid token"
➡️ Vérifier le token sur https://pypi.org/manage/account/token/

### Erreur : "Invalid metadata"
➡️ Vérifier `pyproject.toml` avec :
```bash
python -m build
```

---

## 📞 Support

- **PyPI Help** : https://pypi.org/help/
- **Packaging Guide** : https://packaging.python.org/
- **Twine Docs** : https://twine.readthedocs.io/

---

## ✨ Commande finale

```bash
cd /Users/display/PycharmProjects/dnd-5e-core
twine upload dist/*
# Entrez votre token PyPI quand demandé
```

**Bonne chance ! 🎉**

