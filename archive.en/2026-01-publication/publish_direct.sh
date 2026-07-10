#!/bin/bash
# Publishing dnd-5e-core v0.2.6 - Direct script

set -e  # Stop on error

echo "════════════════════════════════════════"
echo "📦 Publishing dnd-5e-core v0.2.6"
echo "════════════════════════════════════════"
echo ""

# 1. Clean completely
echo "🧹 Complete cleanup..."
rm -rf dist/ build/ *.egg-info dnd_5e_core.egg-info/
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true

# 2. Verify versions
echo ""
echo "📋 Verifying versions..."
echo "setup.py:"
grep 'version=' setup.py | head -1
echo "pyproject.toml:"
grep 'version =' pyproject.toml | head -1

# 3. Build
echo ""
echo "🔨 Building the package..."
python3 -m build

# 4. Verify
echo ""
echo "🔍 Verification..."
python3 -m twine check dist/*

# 5. List
echo ""
echo "📦 Generated files:"
ls -lh dist/

# 6. Publish
echo ""
echo "════════════════════════════════════════"
echo "🚀 Ready to publish on PyPI"
echo "════════════════════════════════════════"
echo ""
python3 -m twine upload dist/*
