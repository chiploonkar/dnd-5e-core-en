#!/bin/bash
# Script de configuration du token PyPI pour dnd-5e-core

set -e

PYPIRC_FILE="$HOME/.pypirc"

echo "=========================================="
echo "Configuration du token PyPI"
echo "=========================================="
echo ""
echo "Ce script va configurer votre token PyPI pour publier dnd-5e-core."
echo ""
echo "Étapes à suivre :"
echo "1. Connectez-vous sur https://pypi.org/"
echo "2. Allez dans Account Settings → API tokens"
echo "3. Créez un nouveau token (scope: 'Entire account' ou 'dnd-5e-core')"
echo "4. Copiez le token (il commence par 'pypi-')"
echo ""

# Vérifier si le fichier existe déjà
if [ -f "$PYPIRC_FILE" ]; then
    echo "⚠️  Le fichier $PYPIRC_FILE existe déjà."
    echo ""
    cat "$PYPIRC_FILE"
    echo ""
    read -p "Voulez-vous le remplacer ? (yes/no): " REPLACE
    if [ "$REPLACE" != "yes" ]; then
        echo "❌ Configuration annulée."
        exit 0
    fi
    # Backup de l'ancien fichier
    cp "$PYPIRC_FILE" "$PYPIRC_FILE.backup.$(date +%Y%m%d_%H%M%S)"
    echo "✅ Backup créé : $PYPIRC_FILE.backup.*"
fi

# Demander le token
echo ""
read -p "Entrez votre token PyPI (commence par 'pypi-'): " PYPI_TOKEN

# Vérifier que le token commence par 'pypi-'
if [[ ! "$PYPI_TOKEN" =~ ^pypi- ]]; then
    echo "❌ Erreur : Le token doit commencer par 'pypi-'"
    exit 1
fi

# Créer le fichier .pypirc
cat > "$PYPIRC_FILE" << EOF
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = $PYPI_TOKEN
EOF

# Sécuriser les permissions
chmod 600 "$PYPIRC_FILE"

echo ""
echo "✅ Configuration terminée !"
echo ""
echo "Le fichier $PYPIRC_FILE a été créé avec les bonnes permissions."
echo ""
echo "Vous pouvez maintenant publier avec :"
echo "  ./publish_simple.sh"
echo ""
echo "Pour tester la configuration :"
echo "  python3 -m twine check dist/*"
echo ""
