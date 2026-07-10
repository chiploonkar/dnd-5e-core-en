#!/bin/bash
# Simplified script to publish dnd-5e-core v0.2.6

echo "════════════════════════════════════════════════════════════════"
echo "📦 PUBLISHING dnd-5e-core v0.2.6"
echo "════════════════════════════════════════════════════════════════"

# Verify version
echo ""
echo "📋 Verifying the version..."
VERSION=$(grep 'version=' setup.py | head -1 | cut -d'"' -f2)
echo "Current version: $VERSION"

if [ "$VERSION" != "0.2.6" ]; then
    echo "❌ ERROR: The version is not 0.2.6!"
    echo "Modify setup.py to set version='0.2.6'"
    exit 1
fi

# Clean up
echo ""
echo "🧹 Cleaning..."
rm -rf dist/ build/ *.egg-info dnd_5e_core.egg-info/
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Install tools
echo ""
echo "📦 Installing tools..."
python3 -m pip install --upgrade pip setuptools wheel build twine --quiet

# Build
echo ""
echo "🔨 Building package v$VERSION..."
python3 -m build

# Verify
echo ""
echo "🔍 Verification..."
python3 -m twine check dist/*

# List files
echo ""
echo "📦 Generated files:"
ls -lh dist/

# Publish
echo ""
echo "════════════════════════════════════════════════════════════════"
echo "⚠️  PUBLISHING TO PyPI (PRODUCTION)"
echo "════════════════════════════════════════════════════════════════"
echo ""
read -p "Publish dnd-5e-core v$VERSION to PyPI? (yes/no): " confirm

if [ "$confirm" = "yes" ]; then
    echo ""
    echo "🚀 Publishing in progress..."
    python3 -m twine upload dist/*

    echo ""
    echo "════════════════════════════════════════════════════════════════"
    echo "✅ PUBLISHING SUCCESSFUL!"
    echo "════════════════════════════════════════════════════════════════"
    echo ""
    echo "Package available at: https://pypi.org/project/dnd-5e-core/"
    echo "To install: pip install dnd-5e-core==$VERSION"
    echo ""
else
    echo "❌ Publishing canceled"
fi
