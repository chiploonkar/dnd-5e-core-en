# 🔍 RÉSOLUTION ERREUR 403 PyPI

## ❌ Problème Actuel

```
HTTPError: 403 Forbidden from https://upload.pypi.org/legacy/
Invalid or non-existent authentication information.
```

Malgré un token qui semble valide, l'authentification échoue.

## 🎯 CAUSES POSSIBLES ET SOLUTIONS

### Cause 1 : Le token n'a pas les permissions sur le projet

**Vérification** :
1. Aller sur https://pypi.org/manage/account/token/
2. Trouver le token utilisé
3. Vérifier le **Scope** :
   - ❌ Si "Entire account" → Peut ne pas fonctionner selon la config PyPI
   - ✅ Doit être "Project: dnd-5e-core"

**Solution** :
```bash
# 1. Supprimer l'ancien token sur PyPI
# 2. Créer un nouveau token avec scope: "Project: dnd-5e-core"
# 3. Reconfigurer
./setup_pypi_token.sh
```

### Cause 2 : Vous n'êtes pas mainteneur du projet

**Vérification** :
1. Aller sur https://pypi.org/project/dnd-5e-core/
2. Vérifier que votre compte PyPI est listé dans "Maintainers"

**Solution** :
Si vous n'êtes pas mainteneur, demander à être ajouté par un mainteneur existant.

### Cause 3 : Le token est pour TestPyPI au lieu de PyPI

**Vérification** :
Le token vient-il de https://test.pypi.org/ au lieu de https://pypi.org/ ?

**Solution** :
Créer un token sur le bon site : https://pypi.org/manage/account/

### Cause 4 : Formatage incorrect du fichier .pypirc

**Vérification** :
```bash
cat ~/.pypirc
```

**Format correct** :
```ini
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = pypi-VOTRE_TOKEN_EXACT_SANS_ESPACES
```

**Problèmes fréquents** :
- ❌ Espaces avant/après le token
- ❌ Retours à la ligne dans le token
- ❌ Guillemets autour du token
- ❌ Caractères invisibles copiés-collés

**Solution** :
Recréer le fichier manuellement avec un éditeur de texte :
```bash
nano ~/.pypirc
# Coller le contenu correct
# Ctrl+O pour sauvegarder, Ctrl+X pour quitter
chmod 600 ~/.pypirc
```

### Cause 5 : Conflit entre .pypirc et variables d'environnement

**Vérification** :
```bash
echo $TWINE_USERNAME
echo $TWINE_PASSWORD
```

Si elles sont définies, elles ont la priorité sur .pypirc.

**Solution A** : Utiliser uniquement les variables d'environnement
```bash
unset TWINE_USERNAME
unset TWINE_PASSWORD
# Puis utiliser uniquement ~/.pypirc
```

**Solution B** : Utiliser uniquement .pypirc
```bash
# S'assurer que .pypirc est correct et faire :
python3 -m twine upload dist/* --config-file ~/.pypirc
```

### Cause 6 : Le projet dnd-5e-core n'existe pas encore sur PyPI

**Vérification** :
```bash
curl -I https://pypi.org/project/dnd-5e-core/
# Si 404 → Le projet n'existe pas
# Si 200 → Le projet existe
```

**Solution** :
Si c'est la première publication, il faut utiliser un token avec scope "Entire account" ou créer le projet d'abord.

## 🔧 SOLUTION ÉTAPE PAR ÉTAPE

### Méthode 1 : Nouveau token avec scope projet (Recommandé)

```bash
# 1. Aller sur PyPI
open https://pypi.org/manage/account/token/

# 2. Supprimer tous les anciens tokens pour dnd-5e-core

# 3. Créer un nouveau token
# - Token name: dnd-5e-core-publish-2026
# - Scope: "Project: dnd-5e-core"
# - COPIER le token

# 4. Reconfigurer
./setup_pypi_token.sh
# Coller le nouveau token

# 5. Tester
./publish_simple.sh
```

### Méthode 2 : Utilisation manuelle de twine

```bash
# 1. Supprimer les variables d'environnement
unset TWINE_USERNAME
unset TWINE_PASSWORD

# 2. Recréer .pypirc proprement
cat > ~/.pypirc << 'EOF'
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = pypi-VOTRE_TOKEN_ICI
EOF

chmod 600 ~/.pypirc

# 3. Publier manuellement
cd /Users/display/PycharmProjects/dnd-5e-core
python3 -m twine upload dist/dnd_5e_core-0.4.4* --verbose
```

### Méthode 3 : Test avec TestPyPI d'abord

```bash
# 1. Créer un compte sur TestPyPI
open https://test.pypi.org/account/register/

# 2. Créer un token sur TestPyPI
open https://test.pypi.org/manage/account/token/

# 3. Modifier .pypirc pour ajouter testpypi
cat > ~/.pypirc << 'EOF'
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-VOTRE_TOKEN_PYPI

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-VOTRE_TOKEN_TESTPYPI
EOF

chmod 600 ~/.pypirc

# 4. Tester sur TestPyPI
python3 -m twine upload --repository testpypi dist/*

# 5. Si ça marche, publier sur PyPI
python3 -m twine upload dist/*
```

## 📝 CHECKLIST DE VÉRIFICATION

Avant de republier, vérifier :

- [ ] Vous êtes connecté sur https://pypi.org/ avec le bon compte
- [ ] Votre compte est mainteneur de dnd-5e-core
- [ ] Le token est bien pour PyPI (pas TestPyPI)
- [ ] Le token a le scope "Project: dnd-5e-core" ou "Entire account"
- [ ] Le fichier ~/.pypirc a le bon format (pas d'espaces, pas de guillemets)
- [ ] Les permissions de ~/.pypirc sont 600
- [ ] Les variables TWINE_USERNAME et TWINE_PASSWORD sont soit vides, soit correctes
- [ ] Le package est bien construit (dist/dnd_5e_core-0.4.4*)
- [ ] twine check ne retourne pas d'erreur

## 🆘 SI RIEN NE FONCTIONNE

### Option A : Contacter PyPI Support

Si vous êtes le propriétaire légitime du projet mais ne pouvez pas publier :
- Email : https://pypi.org/help/
- Expliquer la situation avec le nom du projet et votre compte

### Option B : Créer un nouveau projet

Si dnd-5e-core ne vous appartient pas :
- Publier sous un nom différent (ex: dnd-5e-core-yourname)
- Ou demander à être ajouté comme mainteneur

### Option C : Utiliser GitHub Actions

Automatiser la publication avec GitHub Actions (qui a ses propres tokens PyPI).

## 📞 RESSOURCES

- **PyPI Help** : https://pypi.org/help/
- **Twine Docs** : https://twine.readthedocs.io/
- **Token Info** : https://pypi.org/help/#apitoken

---

**Dernière mise à jour** : 5 février 2026
