# Guide de Publication - dnd-5e-core

## 📦 Options de Publication

### Option 1 : GitHub uniquement (Simple)

Votre package est déjà utilisable directement depuis GitHub :

```bash
pip install git+https://github.com/codingame-team/dnd-5e-core.git
```

**Avantages :**
- Aucune configuration supplémentaire nécessaire
- Gratuit et immédiat
- Parfait pour les projets internes ou en développement

**Inconvénients :**
- Moins de visibilité
- Pas de versioning facile
- Nécessite Git installé

---

### Option 2 : PyPI (Python Package Index) - RECOMMANDÉ

PyPI est le registre officiel de packages Python. C'est là que se trouvent tous les packages installables via `pip install`.

#### Étapes pour publier sur PyPI :

#### 1. Créer un compte PyPI
- Production : https://pypi.org/account/register/
- Test (recommandé pour débuter) : https://test.pypi.org/account/register/

#### 2. Installer les outils de build
```bash
pip install --upgrade build twine
```

#### 3. Créer le package
```bash
# Nettoyer les anciens builds
rm -rf dist/ build/ *.egg-info/

# Créer les distributions
python -m build
```

Cela créera deux fichiers dans `dist/` :
- `dnd-5e-core-0.1.0.tar.gz` (source distribution)
- `dnd_5e_core-0.1.0-py3-none-any.whl` (wheel distribution)

#### 4. Tester sur TestPyPI (RECOMMANDÉ d'abord)
```bash
# Upload sur TestPyPI
twine upload --repository testpypi dist/*

# Tester l'installation
pip install --index-url https://test.pypi.org/simple/ dnd-5e-core
```

#### 5. Publier sur PyPI (production)
```bash
twine upload dist/*
```

#### 6. Installation par les utilisateurs
```bash
pip install dnd-5e-core
```

---

## 🔧 Migration vers pyproject.toml

J'ai créé un fichier `pyproject.toml` moderne qui remplace `setup.py`. C'est le nouveau standard Python (PEP 517/518).

### Avantages :
- ✅ Compatible avec Python 3.13
- ✅ Plus simple et déclaratif
- ✅ Standard moderne
- ✅ Évite les erreurs de setuptools obsolètes

### Que faire avec setup.py ?

Vous avez **deux options** :

**Option A : Garder les deux (compatibilité maximale)**
- Conservez `setup.py` ET `pyproject.toml`
- `pyproject.toml` sera utilisé en priorité
- Ancien setup.py reste pour compatibilité ascendante

**Option B : Utiliser seulement pyproject.toml (moderne)**
- Supprimez `setup.py`
- Plus propre, mais nécessite setuptools>=61.0

Je recommande l'**Option B** pour un nouveau projet.

---

## 📝 Fichiers à exclure de Git

Votre `.gitignore` est déjà bien configuré. Ces fichiers NE DOIVENT PAS être versionnés :

- ❌ `*.egg-info/` - Artefacts de build local
- ❌ `build/` - Dossier de build temporaire
- ❌ `dist/` - Distributions créées (tar.gz, whl)
- ❌ `__pycache__/` - Cache Python

Ces fichiers sont déjà exclus dans votre `.gitignore` ✅

---

## 🚀 Workflow de Publication Recommandé

### 1. Développement
```bash
# Installation en mode développement
pip install -e .

# Ou avec les dépendances de dev
pip install -e ".[dev]"
```

### 2. Tests
```bash
pytest
```

### 3. Mise à jour de version
Éditez `pyproject.toml` :
```toml
version = "0.1.1"  # Incrémentez la version
```

### 4. Build et publication
```bash
# Nettoyer
rm -rf dist/ build/ *.egg-info/

# Build
python -m build

# Publier (TestPyPI d'abord pour tester)
twine upload --repository testpypi dist/*

# Puis PyPI si tout est OK
twine upload dist/*
```

### 5. Tag Git
```bash
git tag v0.1.1
git push origin v0.1.1
```

---

## 🔐 Sécurité - Tokens PyPI

**N'utilisez jamais votre mot de passe directement avec twine !**

### Créer un API Token :
1. Connectez-vous sur PyPI
2. Account Settings > API Tokens
3. Créez un token pour votre projet
4. Utilisez-le lors de l'upload :

```bash
# Twine vous demandera :
# Username: __token__
# Password: pypi-AgEIcHlwaS5vcmc... (votre token)
```

Ou configurez `~/.pypirc` :
```ini
[testpypi]
username = __token__
password = pypi-AgEI...

[pypi]
username = __token__
password = pypi-AgEI...
```

---

## 📊 Résumé

| Aspect | GitHub | PyPI |
|--------|--------|------|
| **Installation** | `pip install git+https://...` | `pip install dnd-5e-core` |
| **Visibilité** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Setup** | Aucun | Compte + upload |
| **Coût** | Gratuit | Gratuit |
| **Recommandé pour** | Projets internes | Projets publics |

---

## ❓ Questions Fréquentes

### Dois-je supprimer setup.py ?
Optionnel. `pyproject.toml` suffit pour les nouvelles installations.

### Le dossier .egg-info est-il nécessaire ?
**NON**. Il est généré automatiquement et ne doit PAS être versionné.

### Quelle version Python minimum ?
Votre projet spécifie `>=3.10`. C'est bien pour un projet moderne en 2026.

### Puis-je publier sur GitHub ET PyPI ?
**OUI !** C'est même recommandé. GitHub pour le code source, PyPI pour la distribution.

---

## 📚 Ressources

- Documentation PyPI : https://packaging.python.org/
- Guide packaging : https://packaging.python.org/tutorials/packaging-projects/
- Twine : https://twine.readthedocs.io/

