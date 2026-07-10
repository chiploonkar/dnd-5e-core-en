#!/usr/bin/env bash
# Build and publication script for the dnd-5e-core package on PyPI
# Date: January 18, 2026

set -e  # Stop on error

echo "════════════════════════════════════════════════════════════════"
echo "📦 BUILD & PUBLISH - dnd-5e-core"
echo "════════════════════════════════════════════════════════════════"
echo ""

# Display colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Help function
show_help() {
    echo "Usage: ./build_package.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --clean      Clean previous build files"
    echo "  --build      Build the package"
    echo "  --test       Publish to TestPyPI"
    echo "  --publish    Publish to PyPI (production)"
    echo "  --all        Do everything (clean + build + publish)"
    echo "  --help       Show this help"
    echo ""
    echo "Examples:"
    echo "  ./build_package.sh --clean --build"
    echo "  ./build_package.sh --test"
    echo "  ./build_package.sh --all"
}

# Clean function
clean_build() {
    echo -e "${YELLOW}🧹 Cleaning build files...${NC}"

    rm -rf build/
    rm -rf dist/
    rm -rf *.egg-info
    rm -rf dnd_5e_core.egg-info/

    # Clean __pycache__
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true

    echo -e "${GREEN}✅ Cleaning completed${NC}"
    echo ""
}

# Build function
build_package() {
    echo -e "${YELLOW}🔨 Building package...${NC}"

    # Check that setup.py exists
    if [ ! -f "setup.py" ]; then
        echo -e "${RED}❌ Error: setup.py not found${NC}"
        exit 1
    fi

    # Install/update build tools
    echo "📦 Installing build tools..."
    pip install --upgrade pip setuptools wheel build twine

    # Building package
    echo "🔨 Building package..."
    python -m build

    # Check that files were created
    if [ ! -d "dist" ]; then
        echo -e "${RED}❌ Error: The dist directory was not created${NC}"
        exit 1
    fi

    echo -e "${GREEN}✅ Package built successfully${NC}"
    echo ""
    echo "📦 Generated files:"
    ls -lh dist/
    echo ""
}

# Verification function
check_package() {
    echo -e "${YELLOW}🔍 Verifying package...${NC}"

    # Verify with twine
    twine check dist/*

    echo -e "${GREEN}✅ Verification completed${NC}"
    echo ""
}

# TestPyPI publication function
publish_test() {
    echo -e "${YELLOW}🚀 Publishing to TestPyPI...${NC}"

    check_package

    echo "⚠️  Publishing to TestPyPI (test)"
    echo "You must have an account on https://test.pypi.org"
    echo ""

    twine upload --repository testpypi dist/*

    echo -e "${GREEN}✅ Published to TestPyPI${NC}"
    echo ""
    echo "To install from TestPyPI:"
    echo "pip install --index-url https://test.pypi.org/simple/ dnd-5e-core"
    echo ""
}

# PyPI publication function
publish_pypi() {
    echo -e "${YELLOW}🚀 Publishing to PyPI (PRODUCTION)...${NC}"

    check_package

    echo "⚠️  WARNING: Publishing to PyPI PRODUCTION"
    echo "This action CANNOT be undone!"
    echo ""
    read -p "Are you sure you want to publish? (yes/no): " confirm

    if [ "$confirm" != "yes" ]; then
        echo "❌ Publication canceled"
        exit 0
    fi

    twine upload dist/*

    echo -e "${GREEN}✅ Published to PyPI${NC}"
    echo ""
    echo "Package available at: https://pypi.org/project/dnd-5e-core/"
    echo "To install: pip install dnd-5e-core"
    echo ""
}

# Function to do everything
do_all() {
    clean_build
    build_package
    publish_pypi
}

# Parse arguments
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
            echo -e "${RED}Unknown option: $1${NC}"
            show_help
            exit 1
            ;;
    esac
done

echo "════════════════════════════════════════════════════════════════"
echo -e "${GREEN}✅ COMPLETED${NC}"
echo "════════════════════════════════════════════════════════════════"
