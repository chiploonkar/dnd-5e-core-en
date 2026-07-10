# Release Update Summary v0.1.3

## Issue Resolved

The `dnd-5e-core` package version 0.1.2 installed from PyPI did not contain the file `bestiary-sublist-data.json`, causing a `FileNotFoundError` when using the `search_monsters()` function.

## Solution Applied

### 1. Fixed Data Packaging
- **Issue**: The MANIFEST.in referenced only `data/` at the root, but the files are in `dnd_5e_core/data/`
- **Solution**: Added `recursive-include dnd_5e_core/data *.json` in MANIFEST.in
- **Result**: The file `bestiary-sublist-data.json` (422 KB) is now included in the distributed package

### 2. Optimized Package Size
- **Issue**: The package was 107 MB (PyPI limit: 100 MB) due to image tokens (102 MB)
- **Solution**: Excluded the `dnd_5e_core/data/monsters/tokens/` directory from the PyPI package
- **Result**: Package size reduced to 1.3 MB ✓

### 3. Documentation Added
- Created `dnd_5e_core/data/monsters/tokens/README.md` explaining how to download the tokens
- Updated CHANGELOG.md with v0.1.3 changes

## Successful Publication

✅ **Package published on PyPI**: https://pypi.org/project/dnd-5e-core/0.1.3/
✅ **Final size**: 1.3 MB (wheel) / 1.8 MB (source)
✅ **Tests passed**: The script `create_monster.py` runs correctly

## Answers to Initial Questions

### 1. Is the `dnd_5e_core.egg-info` directory necessary?
**No**, this directory is automatically generated during the build. It should **not** be committed to Git (already in .gitignore) and is **not necessary** for publication. It is recreated on each build.

### 2. Where to publish the package?
- **PyPI** (https://pypi.org/): For Python package distribution ✓ (done)
- **GitHub**: For source code, issues, and documentation
- The `.egg-info` file is unrelated to GitHub

### 3. PyPI Metadata
Your metadata in `pyproject.toml` is **complete and well-configured**:
- ✓ Detailed description
- ✓ Author and email
- ✓ Links (Homepage, Documentation, Repository, Issues, Changelog)
- ✓ Appropriate classifiers
- ✓ Relevant keywords

Everything is ready for a beautiful PyPI page!

## Modified Files

1. `MANIFEST.in` - Added the inclusion of `dnd_5e_core/data/` and excluded tokens
2. `setup.py` - Version 0.1.2 → 0.1.3
3. `pyproject.toml` - Version 0.1.2 → 0.1.3
4. `CHANGELOG.md` - Added v0.1.3 entry
5. `dnd_5e_core/data/monsters/tokens/README.md` - New file created

## Recommended Next Steps

1. **Commit and push to GitHub**:
   ```bash
   git add .
   git commit -m "Release v0.1.3: Fix package data inclusion and optimize size"
   git push
   ```

2. **Create a release tag**:
   ```bash
   git tag -a v0.1.3 -m "Version 0.1.3"
   git push origin v0.1.3
   ```

3. **Create a GitHub Release** with the CHANGELOG

4. **Download tokens** (optional for users):
   ```python
   from dnd_5e_core.utils.token_downloader import download_all_tokens
   download_all_tokens()
   ```
