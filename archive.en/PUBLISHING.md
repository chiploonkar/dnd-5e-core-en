# Package Publishing

## 📋 Project Metadata

### ⚠️ About the `.egg-info` directory

The `dnd_5e_core.egg-info/` directory is an automatically generated **build artifact**:
- ❌ **Do NOT version it** on Git (already in `.gitignore`)
- ✅ **Automatically created** during build
- 📦 **Used by pip/setuptools** for local installation
- 🗑️ **Automatically deleted** by `./build.sh`

### 📝 PyPI Metadata (in `pyproject.toml`)

All metadata for PyPI are defined in `pyproject.toml`:
- ✅ **Description & About**: Short description and complete README
- ✅ **Authors & Maintainers**: Contact information
- ✅ **Keywords**: Keywords for PyPI search
- ✅ **Classifiers**: Package categorization
- ✅ **Links**: Homepage, Documentation, Issues, Changelog, etc.
- ✅ **License**: MIT License

This information will automatically appear in the **PyPI sidebar** upon publication.

### 🌐 Publishing Platforms

#### 1. **GitHub** (Current)
```bash
pip install git+https://github.com/codingame-team/dnd-5e-core.git
```
- ✅ Free and simple
- ✅ Perfect for open source projects
- ✅ No PyPI account needed
- ❌ Requires Git to install

#### 2. **PyPI** (Python Package Index)
```bash
pip install dnd-5e-core
```
- ✅ Standard installation with pip
- ✅ Easy discovery by the community
- ✅ Version and dependency management
- ✅ Download statistics
- ⚠️ Requires a PyPI account
- ⚠️ Package name must be unique

#### 3. **TestPyPI** (Test before production)
```bash
pip install --index-url https://test.pypi.org/simple/ dnd-5e-core
```
- ✅ Test before official publication
- ✅ Test environment identical to PyPI

## ⚡ Quick Installation

### For users (GitHub only)
```bash
pip install git+https://github.com/codingame-team/dnd-5e-core.git
```

### For developers
```bash
git clone https://github.com/codingame-team/dnd-5e-core.git
cd dnd-5e-core
pip install -e ".[dev]"
```

## 📦 Build and Publication

### Local Build
```bash
./build.sh
```

Or manually:
```bash
rm -rf build/ dist/ *.egg-info/
python -m build
```

### Publishing on PyPI

1. **Create a PyPI account** on https://pypi.org/account/register/

2. **Configure API tokens** (recommended):
```bash
# Create a token on https://pypi.org/manage/account/token/
# Then in ~/.pypirc:
[pypi]
username = __token__
password = pypi-<your-token-here>
```

3. **Test on TestPyPI** (recommended first)
```bash
twine upload --repository testpypi dist/*
```

4. **Production on PyPI**
```bash
twine upload dist/*
```

## 📂 Files to NOT version

These folders are build artifacts and are automatically excluded by `.gitignore`:
- `*.egg-info/` ❌ (local build artifact)
- `build/` ❌ (compilation files)
- `dist/` ❌ (distributed packages)
- `__pycache__/` ❌ (Python bytecode)

## 🎯 GitHub Sidebar

To configure the GitHub sidebar, see the detailed guide: `.github/GITHUB_ABOUT_SETUP.md`

**Quick summary**:
1. Go to the GitHub repository
2. Click on **⚙️** next to "About"
3. Fill in:
   - **Description**: Copy from `.github/DESCRIPTION.txt`
   - **Website**: `https://github.com/codingame-team/dnd-5e-core`
   - **Topics**: See `.github/TOPICS.md`

## 📊 PyPI Sidebar

PyPI metadata is in `pyproject.toml`:
- ✅ **Authors & Maintainers** with emails
- ✅ **Keywords** for search
- ✅ **Classifiers** complete
- ✅ **URLs** (Homepage, Documentation, Issues, Changelog, etc.)
- ✅ **License** (MIT)

This information will automatically appear on PyPI after publication.

## 📖 Complete documentation

See the following files for more details:
- **Publishing**: [docs/GUIDE_PUBLICATION.md](docs/GUIDE_PUBLICATION.md)
- **Metadata**: [METADATA_SUMMARY.md](METADATA_SUMMARY.md)
- **GitHub About**: [.github/GITHUB_ABOUT_SETUP.md](.github/GITHUB_ABOUT_SETUP.md)
