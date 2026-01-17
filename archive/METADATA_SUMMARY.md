# ✅ Métadonnées PyPI - Configuration Complète

## 📋 Résumé des changements

Les métadonnées de publication pour PyPI et GitHub ont été complétées dans le fichier `pyproject.toml`.

### ✨ Nouvelles informations ajoutées :

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

#### 3. **Keywords** (pour la recherche PyPI)
```toml
keywords = [
    "dnd", "dungeons-dragons", "d&d", "5e", "rpg", "tabletop",
    "game-engine", "character-sheet", "combat-engine", "spells", "monsters"
]
```

#### 4. **Classifiers complets**
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

#### 5. **URLs supplémentaires** (pour la barre latérale PyPI)
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

## 📂 Nouveaux fichiers créés

### 1. `.github/ABOUT.md`
Description complète du projet pour la section "About" de GitHub.

### 2. `.github/DESCRIPTION.txt`
Description courte (1 ligne) pour la barre latérale GitHub.

### 3. `.github/TOPICS.md`
Liste des topics/tags recommandés pour GitHub.

## 🎯 Configuration GitHub

Pour configurer la barre latérale GitHub :

1. **Aller dans Settings** → **General** du repository
2. **Cliquer sur ⚙️** à côté de "About"
3. **Remplir** :
   - **Description** : Copier depuis `.github/DESCRIPTION.txt`
   - **Website** : `https://github.com/codingame-team/dnd-5e-core`
   - **Topics** : Copier depuis `.github/TOPICS.md`

## 📦 Publication PyPI

### Étape 1 : Build
```bash
./build.sh
```

### Étape 2 : Test sur TestPyPI
```bash
twine upload --repository testpypi dist/*
```

### Étape 3 : Production sur PyPI
```bash
twine upload dist/*
```

## ✅ Vérifications

- ✅ `pyproject.toml` contient toutes les métadonnées requises
- ✅ Description courte dans `description`
- ✅ Description longue dans `README.md` (via `readme = "README.md"`)
- ✅ Authors et maintainers avec emails
- ✅ License correctement spécifiée
- ✅ Keywords pour la recherche
- ✅ Classifiers complets
- ✅ URLs pour la barre latérale

## 📊 Résultat attendu sur PyPI

Quand vous publierez sur PyPI, la barre latérale affichera :

- **Meta** : License, Authors, Maintainers
- **Project Links** : Homepage, Documentation, Source Code, Issues, Changelog, Quick Start
- **Classifiers** : Development Status, Audience, License, Language, OS, Topics
- **Keywords** : dnd, dungeons-dragons, 5e, rpg, etc.

## ❓ FAQ

### Le dossier `.egg-info` est-il nécessaire ?

**Non**, le dossier `dnd_5e_core.egg-info/` est un **artefact de build** :
- ❌ **Ne PAS le versionner** sur Git (déjà dans `.gitignore`)
- ✅ **Automatiquement créé** lors du build
- 📦 **Utilisé par pip/setuptools** pour l'installation locale
- 🗑️ **Supprimé automatiquement** par `./build.sh`

### Où publier le package ?

1. **GitHub** (actuel) : Installation via `pip install git+https://github.com/...`
2. **PyPI** (recommandé) : Installation via `pip install dnd-5e-core`
3. **TestPyPI** (test) : Pour tester avant publication officielle

### Que contient `pyproject.toml` ?

Toutes les métadonnées nécessaires pour PyPI :
- Description du projet
- Informations de contact (authors, maintainers)
- License
- Mots-clés (keywords)
- Catégorisation (classifiers)
- Liens (homepage, documentation, issues, etc.)

Ces informations apparaissent automatiquement dans la **barre latérale PyPI** lors de la publication.

---

**Prochaines étapes** :
1. ✅ Vérifier que tout fonctionne : `./build.sh`
2. ✅ Tester sur TestPyPI : `twine upload --repository testpypi dist/*`
3. ✅ Publier sur PyPI : `twine upload dist/*`
4. ✅ Configurer la section "About" sur GitHub

