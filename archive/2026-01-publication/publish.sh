#!/bin/bash
# Script simplifié pour publier dnd-5e-core v0.2.6

echo "════════════════════════════════════════════════════════════════"
echo "📦 PUBLICATION dnd-5e-core v0.2.6"
echo "════════════════════════════════════════════════════════════════"

# Vérifier la version
echo ""
echo "📋 Vérification de la version..."
VERSION=$(grep 'version=' setup.py | head -1 | cut -d'"' -f2)
echo "Version actuelle: $VERSION"

if [ "$VERSION" != "0.2.6" ]; then
    echo "❌ ERREUR: La version n'est pas 0.2.6!"
    echo "Modifiez setup.py pour mettre version='0.2.6'"
    exit 1
fi

# Nettoyer
echo ""
echo "🧹 Nettoyage..."
rm -rf dist/ build/ *.egg-info dnd_5e_core.egg-info/
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Installer les outils
echo ""
echo "📦 Installation des outils..."
python3 -m pip install --upgrade pip setuptools wheel build twine --quiet

# Build
echo ""
echo "🔨 Construction du package v$VERSION..."
python3 -m build

# Vérifier
echo ""
echo "🔍 Vérification..."
python3 -m twine check dist/*

# Lister les fichiers
echo ""
echo "📦 Fichiers générés:"
ls -lh dist/

# Publier
echo ""
echo "════════════════════════════════════════════════════════════════"
echo "⚠️  PUBLICATION SUR PyPI (PRODUCTION)"
echo "════════════════════════════════════════════════════════════════"
echo ""
read -p "Publier dnd-5e-core v$VERSION sur PyPI? (yes/no): " confirm

if [ "$confirm" = "yes" ]; then
    echo ""
    echo "🚀 Publication en cours..."
    python3 -m twine upload dist/*

    echo ""
    echo "════════════════════════════════════════════════════════════════"
    echo "✅ PUBLICATION RÉUSSIE!"
    echo "════════════════════════════════════════════════════════════════"
    echo ""
    echo "Package disponible sur: https://pypi.org/project/dnd-5e-core/"
    echo "Pour installer: pip install dnd-5e-core==$VERSION"
    echo ""
else
    echo "❌ Publication annulée"
fi
