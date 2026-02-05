# 🚀 GUIDE RAPIDE - Publication dnd-5e-core

## ⚠️ PROBLÈME ACTUEL : Token PyPI invalide

Le token PyPI fourni précédemment est **invalide ou a expiré**.

## 📋 SOLUTION EN 3 ÉTAPES

### Étape 1 : Générer un nouveau token PyPI

1. **Connectez-vous sur PyPI** : https://pypi.org/
2. **Account Settings** → **API tokens** → **Add API token**
3. **Paramètres du token** :
   - Token name : `dnd-5e-core-publish`
   - Scope : `Project: dnd-5e-core` (ou `Entire account`)
4. **Créer le token** et **COPIER IMMÉDIATEMENT** (il ne sera plus affiché)

### Étape 2 : Configurer le token

**Option A : Script automatique (Recommandé)** ✅

```bash
./setup_pypi_token.sh
```

Le script vous demandera de coller le token et créera automatiquement le fichier `~/.pypirc`.

**Option B : Manuel**

Créer/éditer `~/.pypirc` :

```ini
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = pypi-VOTRE_TOKEN_ICI
```

Puis sécuriser :

```bash
chmod 600 ~/.pypirc
```

### Étape 3 : Publier

```bash
./publish_simple.sh
```

## ✅ VÉRIFICATION

Après publication réussie :

1. **Vérifier sur PyPI** : https://pypi.org/project/dnd-5e-core/
2. **Tester l'installation** :
   ```bash
   pip install --upgrade dnd-5e-core
   python -c "import dnd_5e_core; print(dnd_5e_core.__version__)"
   ```

## 📝 VERSIONS ACTUELLES

- **Version construite** : 0.4.4 (prête à publier)
- **Version sur PyPI** : 0.4.3 (dernière publiée)

## 🔧 DÉPANNAGE

### "403 Invalid authentication"

✅ **Cause** : Token invalide/expiré  
✅ **Solution** : Générer un nouveau token (voir Étape 1)

### "400 File already exists"

✅ **Cause** : La version 0.4.4 existe déjà  
✅ **Solution** : Bumper vers 0.4.5 (voir `PUBLICATION_PYPI.md`)

### Le build échoue

✅ **Vérifier** :
```bash
python3 -m build --version
pip list | grep -E "build|twine"
```

✅ **Installer/Mettre à jour** :
```bash
pip install --upgrade build twine
```

## 📚 DOCUMENTATION COMPLÈTE

- **Guide détaillé** : `PUBLICATION_PYPI.md`
- **CHANGELOG** : `CHANGELOG.md`

## 🎯 PROCHAINES ÉTAPES

1. ✅ Archivage fichiers obsolètes (fait)
2. ✅ Documentation IA complète (fait)
3. ✅ Bump version 0.4.4 (fait)
4. ✅ Build package (fait)
5. ⏳ **Configurer token PyPI** ← VOUS ÊTES ICI
6. ⏳ Publier sur PyPI
7. ⏳ Vérifier installation

---

**Note** : Le package est déjà construit dans `dist/`. Il suffit de configurer le token PyPI pour publier.
