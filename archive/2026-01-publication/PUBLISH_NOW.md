# 🚀 GUIDE DE PUBLICATION RAPIDE - Version 0.2.6

## ⚡ Publication Immédiate

```bash
cd /Users/display/PycharmProjects/dnd-5e-core
./publish.sh
```

Répondez **yes** quand demandé.

---

## 📋 Ce Que Fait le Script

1. ✅ Vérifie que la version est bien 0.2.6
2. 🧹 Nettoie dist/, build/, *.egg-info
3. 📦 Installe/met à jour build et twine
4. 🔨 Construit le package (wheel + source)
5. 🔍 Vérifie avec twine check
6. 📦 Liste les fichiers générés
7. 🚀 Publie sur PyPI (après confirmation)

---

## ✅ Prérequis

Assurez-vous que `~/.pypirc` est configuré :

```ini
[pypi]
username = __token__
password = pypi-VOTRE_TOKEN_ICI
```

---

## 🔧 Résolution de Problèmes

### Si le script publish.sh ne fonctionne pas

Exécutez manuellement :

```bash
# 1. Nettoyer
rm -rf dist/ build/ *.egg-info dnd_5e_core.egg-info/

# 2. Vérifier la version
grep 'version=' setup.py
# Doit afficher: version="0.2.6"

# 3. Installer les outils
python3 -m pip install --upgrade build twine

# 4. Construire
python3 -m build

# 5. Vérifier
python3 -m twine check dist/*

# 6. Voir les fichiers
ls -lh dist/
# Doit afficher: dnd_5e_core-0.2.6.tar.gz et dnd_5e_core-0.2.6-py3-none-any.whl

# 7. Publier
python3 -m twine upload dist/*
```

---

## ❌ Erreur Courante

### "File already exists"

Si vous voyez :
```
ERROR: File already exists ('dnd_5e_core-0.2.4-py3-none-any.whl')
```

**Cause** : Anciens fichiers dans dist/

**Solution** :
```bash
rm -rf dist/
python3 -m build
python3 -m twine upload dist/*
```

---

## ✅ Vérification Post-Publication

```bash
# Attendre 2-3 minutes

# Installer depuis PyPI
pip install dnd-5e-core==0.2.6 --upgrade

# Tester
python3 -c "
from dnd_5e_core import ClassAbilities, RacialTraits
from dnd_5e_core.data.loaders import simple_character_generator
print('✅ Package dnd-5e-core v0.2.6 fonctionne!')
"
```

---

## 🎯 Commande Ultra-Rapide

```bash
cd /Users/display/PycharmProjects/dnd-5e-core && ./publish.sh
```

C'est tout ! 🎉

---

**Date** : 18 Janvier 2026  
**Version** : 0.2.6  
**Status** : ✅ Prêt à publier
