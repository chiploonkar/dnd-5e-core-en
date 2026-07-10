#!/bin/bash
# Build script for dnd-5e-core
# Usage: ./build.sh

set -e  # Stop in case of error

echo "🧹 Cleaning old builds..."
rm -rf build/ dist/ *.egg-info/

echo "📦 Creating the package..."
python -m build

echo ""
echo "✅ Build completed successfully!"
echo ""
echo "📂 Files created in dist/:"
ls -lh dist/

echo ""
echo "📋 Next steps:"
echo "   1. To test on TestPyPI:"
echo "      twine upload --repository testpypi dist/*"
echo ""
echo "   2. To publish on PyPI:"
echo "      twine upload dist/*"
echo ""
echo "   3. To install locally:"
echo "      pip install dist/dnd_5e_core-0.1.0-py3-none-any.whl"
