# 🚨 ERREUR 403 PyPI - SOLUTION RAPIDE

## Le Problème
```
ERROR: 403 Forbidden - Invalid or non-existent authentication information
```

## La Cause la Plus Probable

**Votre token PyPI n'a PAS les bonnes permissions** ou **vous n'êtes pas mainteneur du projet**.

## ✅ SOLUTION EN 5 MINUTES

### Étape 1 : Vérifier que vous êtes mainteneur

Ouvrir : https://pypi.org/project/dnd-5e-core/

**Regarder la section "Maintainers"** :
- ✅ Si votre nom y est → Continuer étape 2
- ❌ Si votre nom n'y est PAS → **VOUS NE POUVEZ PAS PUBLIER**

**Si vous n'êtes pas mainteneur** :
- Contacter le propriétaire actuel
- OU publier sous un autre nom de package

### Étape 2 : Créer un NOUVEAU token avec le bon scope

1. **Supprimer l'ancien token** :
   - https://pypi.org/manage/account/token/
   - Supprimer tous les tokens pour dnd-5e-core

2. **Créer un nouveau token** :
   - Cliquer "Add API token"
   - Token name : `dnd-5e-core-feb-2026`
   - **Scope : sélectionner "Project: dnd-5e-core"** ← IMPORTANT !
   - Cliquer "Add token"
   - **COPIER le token** (commence par `pypi-...`)

### Étape 3 : Reconfigurer proprement

**Option A** - Script automatique :
```bash
cd /Users/display/PycharmProjects/dnd-5e-core
./setup_pypi_token.sh
# Coller le nouveau token quand demandé
```

**Option B** - Manuel :
```bash
# Créer le fichier .pypirc
cat > ~/.pypirc << 'EOF'
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = COLLER_LE_TOKEN_ICI
EOF

# Sécuriser
chmod 600 ~/.pypirc

# Nettoyer les variables d'environnement
unset TWINE_USERNAME
unset TWINE_PASSWORD
```

### Étape 4 : Publier

```bash
cd /Users/display/PycharmProjects/dnd-5e-core
./publish_simple.sh
```

## 🔍 Si ça ne marche TOUJOURS pas

### Vérification 1 : Le fichier .pypirc est-il correct ?

```bash
cat ~/.pypirc
```

Doit ressembler EXACTEMENT à :
```ini
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = pypi-Ag...très long token...
```

**Erreurs courantes** :
- ❌ Espaces avant/après le token
- ❌ Guillemets autour du token
- ❌ Retours à la ligne dans le token

### Vérification 2 : Le token vient-il du bon site ?

- ✅ Doit venir de : https://pypi.org/ (production)
- ❌ PAS de : https://test.pypi.org/ (test)

### Vérification 3 : Le projet existe-t-il déjà ?

```bash
curl -I https://pypi.org/project/dnd-5e-core/
```

- Si **404** → Le projet n'existe pas encore → Utilisez un token "Entire account"
- Si **200** → Le projet existe → Utilisez un token "Project: dnd-5e-core"

## 💡 ASTUCE : Tester l'authentification

```bash
./test_pypi_auth.sh
```

Ce script teste l'authentification sans risque de dupliquer la version.

## 📞 Besoin d'aide ?

1. **Lire le guide complet** : `TROUBLESHOOTING_403.md`
2. **Documentation PyPI** : https://pypi.org/help/#apitoken
3. **Support PyPI** : https://pypi.org/help/

---

**TL;DR** : 99% du temps c'est soit :
1. Le token n'a pas le bon scope ("Project: dnd-5e-core")
2. Vous n'êtes pas mainteneur du projet sur PyPI
3. Le fichier .pypirc a des espaces ou caractères invisibles
