#!/bin/bash
# Script de publication final pour dnd-5e-core
# Utilise pyproject.toml (moderne) et gère les erreurs correctement

set -e  # Arrêter en cas d'erreur

# Couleurs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonction d'affichage coloré
print_header() {
    echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Fonction de nettoyage
clean_build() {
    print_info "Nettoyage des fichiers de build..."
    rm -rf dist/ build/ *.egg-info dnd_5e_core.egg-info/
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -name "*.pyc" -delete 2>/dev/null || true
    print_success "Nettoyage terminé"
}

# Fonction de vérification des versions
check_versions() {
    print_info "Vérification des versions..."

    # Vérifier pyproject.toml (priorité)
    if [ -f "pyproject.toml" ]; then
        PYPROJECT_VERSION=$(grep '^version =' pyproject.toml | head -1 | cut -d'"' -f2)
        print_info "pyproject.toml: $PYPROJECT_VERSION"
    else
        print_error "pyproject.toml introuvable!"
        exit 1
    fi

    # Vérifier setup.py
    if [ -f "setup.py" ]; then
        SETUP_VERSION=$(grep 'version=' setup.py | head -1 | cut -d'"' -f2)
        print_info "setup.py: $SETUP_VERSION"
    fi

    # Vérifier __init__.py
    if [ -f "dnd_5e_core/__init__.py" ]; then
        INIT_VERSION=$(grep '__version__' dnd_5e_core/__init__.py | head -1 | cut -d"'" -f2)
        print_info "__init__.py: $INIT_VERSION"
    fi

    # Vérifier cohérence
    if [ "$PYPROJECT_VERSION" != "$SETUP_VERSION" ] || [ "$PYPROJECT_VERSION" != "$INIT_VERSION" ]; then
        print_error "Versions incohérentes!"
        print_error "pyproject.toml: $PYPROJECT_VERSION"
        print_error "setup.py: $SETUP_VERSION"
        print_error "__init__.py: $INIT_VERSION"
        exit 1
    fi

    VERSION="$PYPROJECT_VERSION"
    print_success "Version $VERSION cohérente dans tous les fichiers"
}

# Fonction de build
build_package() {
    print_info "Construction du package v$VERSION..."

    # Vérifier que les outils sont installés
    if ! command -v python3 &> /dev/null; then
        print_error "python3 n'est pas installé"
        exit 1
    fi

    # Installer les outils de build
    print_info "Installation des outils de build..."
    python3 -m pip install --upgrade pip setuptools wheel build twine --quiet

    # Build
    python3 -m build

    # Vérifier que les fichiers ont été créés
    if [ ! -d "dist" ]; then
        print_error "Le répertoire dist n'a pas été créé"
        exit 1
    fi

    print_success "Package construit"
    echo ""
    echo "📦 Fichiers générés:"
    ls -lh dist/
}

# Fonction de vérification
verify_package() {
    print_info "Vérification du package..."

    # Vérifier avec twine
    python3 -m twine check dist/*

    # Vérifier le contenu
    print_info "Contenu du package:"
    tar -tzf dist/dnd-5e-core-$VERSION.tar.gz | head -10

    print_success "Vérification terminée"
}

# Fonction de publication
publish_package() {
    print_header "PUBLICATION SUR PyPI (PRODUCTION)"

    print_warning "ATTENTION: Cette action ne peut PAS être annulée!"
    echo ""
    echo "Package: dnd-5e-core v$VERSION"
    echo "Fichiers à publier:"
    ls -lh dist/
    echo ""

    read -p "Confirmer la publication sur PyPI? (yes/no): " confirm

    if [ "$confirm" != "yes" ]; then
        print_info "Publication annulée"
        exit 0
    fi

    print_info "Publication en cours..."
    python3 -m twine upload dist/*

    print_success "PUBLICATION RÉUSSIE!"
    echo ""
    echo "📦 Package disponible sur:"
    echo "   https://pypi.org/project/dnd-5e-core/$VERSION/"
    echo ""
    echo "📦 Pour installer:"
    echo "   pip install dnd-5e-core==$VERSION"
}

# Fonction principale
main() {
    print_header "PUBLICATION dnd-5e-core"

    # Étape 1: Nettoyer
    clean_build
    echo ""

    # Étape 2: Vérifier versions
    check_versions
    echo ""

    # Étape 3: Build
    build_package
    echo ""

    # Étape 4: Vérifier
    verify_package
    echo ""

    # Étape 5: Publier
    publish_package
}

# Exécuter
main "$@"
