# Guide de Publication sur PyPI

## Prérequis

### 1. Créer un token API sur PyPI

1. Se connecter sur https://pypi.org/
2. Aller dans Account Settings → API tokens
3. Créer un nouveau token avec le scope "Entire account" ou limité au projet "dnd-5e-core"
4. **IMPORTANT** : Copier le token immédiatement (il ne sera plus affiché)

### 2. Configurer le token PyPI

#### Option A : Fichier ~/.pypirc (Recommandé)

Créer ou éditer le fichier `~/.pypirc` :

```ini
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = pypi-VOTRE_TOKEN_ICI
```

**Permissions** : `chmod 600 ~/.pypirc`

#### Option B : Variables d'environnement (Session temporaire)

```bash
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="pypi-VOTRE_TOKEN_ICI"
```

## Processus de Publication

### Étape 1 : Préparer la nouvelle version

1. **Mettre à jour le CHANGELOG.md**
   - Déplacer les changements de `[Unreleased]` vers une nouvelle version `[X.Y.Z]`
   - Ajouter la date de publication

2. **Bumper la version** dans 3 fichiers :
   - `pyproject.toml` : `version = "X.Y.Z"`
   - `dnd_5e_core/__init__.py` : `__version__ = 'X.Y.Z'`
   - `setup.py` : `version="X.Y.Z"`

3. **Committer les changements**
   ```bash
   git add CHANGELOG.md pyproject.toml setup.py dnd_5e_core/__init__.py
   git commit -m "chore: Release version X.Y.Z"
   git push origin main
   ```

### Étape 2 : Construire et publier

```bash
# S'assurer que build et twine sont installés
pip install --upgrade build twine

# Exécuter le script de publication
./publish_simple.sh
```

## Vérification

Après publication, vérifier sur :
- https://pypi.org/project/dnd-5e-core/
- Tester l'installation : `pip install dnd-5e-core==X.Y.Z`

## Dépannage

### Erreur 403 : Invalid authentication

**Cause** : Token invalide, expiré ou mal configuré

**Solutions** :
1. Vérifier que le token commence bien par `pypi-`
2. Vérifier le fichier `~/.pypirc` (pas d'espaces, bon format)
3. Régénérer un nouveau token sur PyPI
4. Vérifier les permissions : `chmod 600 ~/.pypirc`

### Erreur 400 : File already exists

**Cause** : La version existe déjà sur PyPI

**Solutions** :
1. Bumper la version (impossible de remplacer une version existante)
2. Vérifier que vous avez bien mis à jour tous les fichiers de version

### Le build échoue

**Causes possibles** :
- Fichiers manquants dans MANIFEST.in
- Erreurs de syntaxe dans le code
- Dépendances manquantes

**Solution** : Vérifier les logs de build et corriger les erreurs

## Versions Sémantiques

- **X.0.0** : Changements majeurs (breaking changes)
- **0.X.0** : Nouvelles fonctionnalités (features)
- **0.0.X** : Corrections de bugs (bugfixes)

## Historique des versions

- **0.4.4** (2026-02-05) : Documentation IA complète, archivage fichiers obsolètes
- **0.4.3** (2026-02-03) : Fix spell_slots KeyError, intégration data/collections
- **0.4.2** : [À documenter]
- **0.4.1** : [À documenter]
