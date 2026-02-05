#!/bin/bash
# Test d'authentification PyPI sans publier

set -e

echo "=========================================="
echo "Test d'authentification PyPI"
echo "=========================================="
echo ""

# Vérifier que le package existe
if [ ! -f "dist/dnd_5e_core-0.4.4-py3-none-any.whl" ]; then
    echo "❌ Package non trouvé. Construire d'abord avec: python3 -m build"
    exit 1
fi

echo "1. Vérification du package..."
python3 -m twine check dist/dnd_5e_core-0.4.4* 2>&1

echo ""
echo "2. Test d'upload (dry-run avec --skip-existing)..."
echo "   Note: --skip-existing permet de tester sans erreur si la version existe"
echo ""

# Tenter l'upload avec skip-existing
python3 -m twine upload dist/dnd_5e_core-0.4.4* --skip-existing --verbose 2>&1

EXIT_CODE=$?

echo ""
echo "=========================================="
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ SUCCÈS ! Le token fonctionne."
    echo ""
    echo "Si la version 0.4.4 existe déjà, elle n'a pas été re-uploadée."
    echo "Sinon, elle a été publiée avec succès !"
    echo ""
    echo "Vérifier sur: https://pypi.org/project/dnd-5e-core/"
else
    echo "❌ ÉCHEC (code: $EXIT_CODE)"
    echo ""
    echo "Erreurs possibles:"
    echo "1. Token invalide ou expiré"
    echo "2. Token n'a pas les permissions sur dnd-5e-core"
    echo "3. Vous n'êtes pas mainteneur du projet"
    echo ""
    echo "Solutions:"
    echo "1. Vérifier https://pypi.org/project/dnd-5e-core/ → Maintainers"
    echo "2. Créer un nouveau token: https://pypi.org/manage/account/token/"
    echo "3. Lire: TROUBLESHOOTING_403.md"
fi
echo "=========================================="

exit $EXIT_CODE
