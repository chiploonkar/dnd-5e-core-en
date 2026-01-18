#!/bin/bash
# Script de build et publication du package dnd-5e-core sur PyPI
# Date: 18 Janvier 2026

set -e  # Arrêter en cas d'erreur

echo "════════════════════════════════════════════════════════════════"
echo "📦 BUILD & PUBLISH - dnd-5e-core"
echo "════════════════════════════════════════════════════════════════"
echo ""

# Couleurs pour l'affichage
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Fonction d'aide
show_help() {
    echo "Usage: ./build_package.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --clean      Nettoyer les fichiers de build précédents"
    echo "  --build      Construire le package"
    echo "  --test       Publier sur TestPyPI"
    echo "  --publish    Publier sur PyPI (production)"
    echo "  --all        Tout faire (clean + build + publish)"
    echo "  --help       Afficher cette aide"
    echo ""
    echo "Exemples:"
    echo "  ./build_package.sh --clean --build"
    echo "  ./build_package.sh --test"
    echo "  ./build_package.sh --all"
}

# Fonction de nettoyage
clean_build() {
    echo -e "${YELLOW}🧹 Nettoyage des fichiers de build...${NC}"

    rm -rf build/
    rm -rf dist/
    rm -rf *.egg-info
    rm -rf dnd_5e_core.egg-info/

    # Nettoyer les __pycache__
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true

    echo -e "${GREEN}✅ Nettoyage terminé${NC}"
    echo ""
}

# Fonction de build
build_package() {
    echo -e "${YELLOW}🔨 Construction du package...${NC}"

    # Vérifier que setup.py existe
    if [ ! -f "setup.py" ]; then
        echo -e "${RED}❌ Erreur: setup.py introuvable${NC}"
        exit 1
    fi

    # Installer/mettre à jour les outils de build
    echo "📦 Installation des outils de build..."
    pip install --upgrade pip setuptools wheel build twine

    # Construire le package
    echo "🔨 Build du package..."
    python -m build

    # Vérifier que les fichiers ont été créés
    if [ ! -d "dist" ]; then
        echo -e "${RED}❌ Erreur: Le répertoire dist n'a pas été créé${NC}"
        exit 1
    fi

    echo -e "${GREEN}✅ Package construit avec succès${NC}"
    echo ""
    echo "📦 Fichiers générés:"
    ls -lh dist/
    echo ""
}

# Fonction de vérification
check_package() {
    echo -e "${YELLOW}🔍 Vérification du package...${NC}"

    # Vérifier avec twine
    twine check dist/*

    echo -e "${GREEN}✅ Vérification terminée${NC}"
    echo ""
}

# Fonction de publication sur TestPyPI
publish_test() {
    echo -e "${YELLOW}🚀 Publication sur TestPyPI...${NC}"

    check_package

    echo "⚠️  Publication sur TestPyPI (test)"
    echo "Vous devez avoir un compte sur https://test.pypi.org"
    echo ""

    twine upload --repository testpypi dist/*

    echo -e "${GREEN}✅ Publié sur TestPyPI${NC}"
    echo ""
    echo "Pour installer depuis TestPyPI:"
    echo "pip install --index-url https://test.pypi.org/simple/ dnd-5e-core"
    echo ""
}

# Fonction de publication sur PyPI
publish_pypi() {
    echo -e "${YELLOW}🚀 Publication sur PyPI (PRODUCTION)...${NC}"

    check_package

    echo "⚠️  ATTENTION: Publication sur PyPI PRODUCTION"
    echo "Cette action ne peut PAS être annulée!"
    echo ""
    read -p "Êtes-vous sûr de vouloir publier? (yes/no): " confirm

    if [ "$confirm" != "yes" ]; then
        echo "❌ Publication annulée"
        exit 0
    fi

    twine upload dist/*

    echo -e "${GREEN}✅ Publié sur PyPI${NC}"
    echo ""
    echo "Package disponible sur: https://pypi.org/project/dnd-5e-core/"
    echo "Pour installer: pip install dnd-5e-core"
    echo ""
}

# Fonction pour tout faire
do_all() {
    clean_build
    build_package
    publish_pypi
}

# Parser les arguments
if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

while [[ $# -gt 0 ]]; do
    case $1 in
        --clean)
            clean_build
            shift
            ;;
        --build)
            build_package
            shift
            ;;
        --test)
            publish_test
            shift
            ;;
        --publish)
            publish_pypi
            shift
            ;;
        --all)
            do_all
            shift
            ;;
        --help)
            show_help
            exit 0
            ;;
        *)
            echo -e "${RED}Option inconnue: $1${NC}"
            show_help
            exit 1
            ;;
    esac
done

echo "════════════════════════════════════════════════════════════════"
echo -e "${GREEN}✅ TERMINÉ${NC}"
echo "════════════════════════════════════════════════════════════════"
