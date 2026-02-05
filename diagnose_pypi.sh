#!/bin/bash
# Script de diagnostic pour les problèmes d'authentification PyPI

echo "=========================================="
echo "DIAGNOSTIC PyPI Authentication"
echo "=========================================="
echo ""

# 1. Vérifier le fichier .pypirc
echo "1. Vérification du fichier ~/.pypirc"
echo "--------------------------------------"
if [ -f ~/.pypirc ]; then
    echo "✅ Fichier existe"
    ls -l ~/.pypirc
    echo ""
    echo "Permissions: $(stat -f '%Lp' ~/.pypirc 2>/dev/null || stat -c '%a' ~/.pypirc 2>/dev/null)"
    echo ""
    echo "Contenu (masqué):"
    cat ~/.pypirc | sed 's/pypi-[A-Za-z0-9_-]*/pypi-***MASKED***/g'
else
    echo "❌ Fichier n'existe pas"
fi
echo ""

# 2. Vérifier les variables d'environnement
echo "2. Variables d'environnement"
echo "--------------------------------------"
if [ -n "$TWINE_USERNAME" ]; then
    echo "✅ TWINE_USERNAME: $TWINE_USERNAME"
else
    echo "❌ TWINE_USERNAME non définie"
fi

if [ -n "$TWINE_PASSWORD" ]; then
    echo "✅ TWINE_PASSWORD: $(echo $TWINE_PASSWORD | cut -c1-10)...***"
else
    echo "❌ TWINE_PASSWORD non définie"
fi
echo ""

# 3. Vérifier les packages nécessaires
echo "3. Packages PyPI"
echo "--------------------------------------"
python3 -c "import twine; print(f'✅ twine version: {twine.__version__}')" 2>/dev/null || echo "❌ twine non installé"
python3 -c "import build; print(f'✅ build version: {build.__version__}')" 2>/dev/null || echo "❌ build non installé"
echo ""

# 4. Vérifier le package
echo "4. Validation du package"
echo "--------------------------------------"
if [ -d dist ]; then
    echo "Fichiers dans dist/:"
    ls -lh dist/dnd_5e_core-0.4.4* 2>/dev/null || echo "❌ Pas de fichiers 0.4.4"
    echo ""
    echo "Test twine check:"
    python3 -m twine check dist/dnd_5e_core-0.4.4* 2>&1
else
    echo "❌ Dossier dist/ n'existe pas"
fi
echo ""

# 5. Causes possibles de l'erreur 403
echo "5. Causes possibles de l'erreur 403"
echo "--------------------------------------"
echo "a) Token invalide/expiré"
echo "b) Token n'a pas les permissions sur le projet 'dnd-5e-core'"
echo "c) Le fichier .pypirc a des caractères invisibles/formatage incorrect"
echo "d) Conflit entre .pypirc et variables d'environnement"
echo "e) Le token est pour TestPyPI au lieu de PyPI"
echo ""

# 6. Solutions recommandées
echo "6. Solutions recommandées"
echo "--------------------------------------"
echo "1. Vérifier sur PyPI que le token est bien pour 'dnd-5e-core'"
echo "   → https://pypi.org/manage/account/token/"
echo ""
echo "2. Vérifier que vous êtes bien propriétaire/mainteneur du projet"
echo "   → https://pypi.org/project/dnd-5e-core/"
echo ""
echo "3. Régénérer un nouveau token avec scope 'Project: dnd-5e-core'"
echo ""
echo "4. Tester avec TestPyPI d'abord:"
echo "   export TWINE_REPOSITORY=testpypi"
echo "   python3 -m twine upload --repository testpypi dist/*"
echo ""
echo "=========================================="
