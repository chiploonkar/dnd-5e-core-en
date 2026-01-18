#!/bin/bash
# Script de build pour dnd-5e-core
# Usage: ./build.sh

set -e  # Arrêter en cas d'erreur

echo "🧹 Nettoyage des anciens builds..."
rm -rf build/ dist/ *.egg-info/

echo "📦 Création du package..."
python -m build

echo ""
echo "✅ Build terminé avec succès!"
echo ""
echo "📂 Fichiers créés dans dist/ :"
ls -lh dist/

echo ""
echo "📋 Prochaines étapes :"
echo "   1. Pour tester sur TestPyPI :"
echo "      twine upload --repository testpypi dist/*"
echo ""
echo "   2. Pour publier sur PyPI :"
echo "      twine upload dist/*"
echo ""
echo "   3. Pour installer localement :"
echo "      pip install dist/dnd_5e_core-0.1.0-py3-none-any.whl"

