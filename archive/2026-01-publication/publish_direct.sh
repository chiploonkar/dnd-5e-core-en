#!/bin/bash
# Publication dnd-5e-core v0.2.6 - Script direct

set -e  # Arrêter en cas d'erreur

echo "════════════════════════════════════════"
echo "📦 Publication dnd-5e-core v0.2.6"
echo "════════════════════════════════════════"
echo ""

# 1. Nettoyer complètement
echo "🧹 Nettoyage complet..."
rm -rf dist/ build/ *.egg-info dnd_5e_core.egg-info/
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true

# 2. Vérifier les versions
echo ""
echo "📋 Vérification des versions..."
echo "setup.py:"
grep 'version=' setup.py | head -1
echo "pyproject.toml:"
grep 'version =' pyproject.toml | head -1

# 3. Build
echo ""
echo "🔨 Construction du package..."
python3 -m build

# 4. Vérifier
echo ""
echo "🔍 Vérification..."
python3 -m twine check dist/*

# 5. Lister
echo ""
echo "📦 Fichiers générés:"
ls -lh dist/

# 6. Publier
echo ""
echo "════════════════════════════════════════"
echo "🚀 Prêt à publier sur PyPI"
echo "════════════════════════════════════════"
echo ""
python3 -m twine upload dist/*
