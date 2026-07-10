# ✅ PyPI Metadata - Complete Configuration

## 📋 Summary of Changes

Publication metadata for PyPI and GitHub has been completed in the `pyproject.toml` file.

### ✨ New Information Added:

#### 1. **Authors & Maintainers**
```toml
authors = [
    { name = "D&D Development Team", email = "dev@codingame-team.com" }
]
maintainers = [
    { name = "D&D Development Team", email = "dev@codingame-team.com" }
]
```

#### 2. **License**
```toml
license = { text = "MIT" }
```

#### 3. **Keywords** (for PyPI search)
```toml
keywords = [
    "dnd", "dungeons-dragons", "d&d", "5e", "rpg", "tabletop",
    "game-engine", "character-sheet", "combat-engine", "spells", "monsters"
]
```

#### 4. **Complete Classifiers**
```toml
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Games/Entertainment :: Role-Playing",
    "Topic :: Games/Entertainment :: Turn Based Strategy",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Typing :: Typed",
]
```

#### 5. **Additional URLs** (for PyPI sidebar)
```toml
[project.urls]
Homepage = "https://github.com/codingame-team/dnd-5e-core"
Documentation = "https://github.com/codingame-team/dnd-5e-core/blob/main/README.md"
Repository = "https://github.com/codingame-team/dnd-5e-core"
"Source Code" = "https://github.com/codingame-team/dnd-5e-core"
Issues = "https://github.com/codingame-team/dnd-5e-core/issues"
"Bug Tracker" = "https://github.com/codingame-team/dnd-5e-core/issues"
Changelog = "https://github.com/codingame-team/dnd-5e-core/blob/main/CHANGELOG.md"
"Quick Start" = "https://github.com/codingame-team/dnd-5e-core/blob/main/QUICK_START_DATA.md"
```

## 📂 New Files Created

### 1. `.github/ABOUT.md`
Complete project description for the GitHub "About" section.

### 2. `.github/DESCRIPTION.txt`
Short description (1 line) for the GitHub sidebar.

### 3. `.github/TOPICS.md`
List of recommended topics/tags for GitHub.

## 🎯 GitHub Configuration

To configure the GitHub sidebar:

1. **Go to Settings** → **General** of the repository
2. **Click on ⚙️** next to "About"
3. **Fill in**:
   - **Description**: Copy from `.github/DESCRIPTION.txt`
   - **Website**: `https://github.com/codingame-team/dnd-5e-core`
   - **Topics**: Copy from `.github/TOPICS.md`

## 📦 PyPI Publication

### Step 1: Build
```bash
./build.sh
```

### Step 2: Test on TestPyPI
```bash
twine upload --repository testpypi dist/*
```

### Step 3: Production on PyPI
```bash
twine upload dist/*
```

## ✅ Verifications

- ✅ `pyproject.toml` contains all required metadata
- ✅ Short description in `description`
- ✅ Long description in `README.md` (via `readme = "README.md"`)
- ✅ Authors and maintainers with emails
- ✅ License correctly specified
- ✅ Keywords for search
- ✅ Complete classifiers
- ✅ URLs for the sidebar

## 📊 Expected Result on PyPI

When you publish on PyPI, the sidebar will display:

- **Meta**: License, Authors, Maintainers
- **Project Links**: Homepage, Documentation, Source Code, Issues, Changelog, Quick Start
- **Classifiers**: Development Status, Audience, License, Language, OS, Topics
- **Keywords**: dnd, dungeons-dragons, 5e, rpg, etc.

## ❓ FAQ

### Is the `.egg-info` folder necessary?

**No**, the `dnd_5e_core.egg-info/` folder is a **build artifact**:
- ❌ **Do NOT version it** on Git (already in `.gitignore`)
- ✅ **Automatically created** during the build
- 📦 **Used by pip/setuptools** for local installation
- 🗑️ **Automatically deleted** by `./build.sh`

### Where to publish the package?

1. **GitHub** (current): Installation via `pip install git+https://github.com/...`
2. **PyPI** (recommended): Installation via `pip install dnd-5e-core`
3. **TestPyPI** (test): To test before official publication

### What does pyproject.toml contain?

All metadata necessary for PyPI:
- Project description
- Contact information (authors, maintainers)
- License
- Keywords
- Categorization (classifiers)
- Links (homepage, documentation, issues, etc.)

This information automatically appears in the **PyPI sidebar** upon publication.

---

**Next Steps**:
1. ✅ Verify that everything works: `./build.sh`
2. ✅ Test on TestPyPI: `twine upload --repository testpypi dist/*`
3. ✅ Publish on PyPI: `twine upload dist/*`
4. ✅ Configure the "About" section on GitHub
