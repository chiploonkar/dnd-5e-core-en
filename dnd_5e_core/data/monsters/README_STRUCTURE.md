# Structure des Données de Monstres

Ce répertoire contient les données JSON des monstres pour D&D 5e, organisées en deux catégories principales.

## 📁 Structure

```
monsters/
├── official/          # Monstres de l'API officielle D&D 5e  
│   ├── goblin.json
│   ├── orc.json
│   ├── dragon.json
│   └── ... (300+ fichiers individuels)
│
├── extended/          # Monstres étendus (5e.tools)
│   ├── goblin-boss.json                     # Fichiers individuels (47+)
│   ├── orc-eye-of-gruumsh.json
│   ├── hobgoblin-captain.json
│   ├── ... (tous les monstres en fichiers séparés)
│   ├── bestiary-sublist-data.json           # Archive (conservé)
│   └── bestiary-sublist-data-all-monsters.json  # Archive (conservé)
│
└── README_STRUCTURE.md  # Ce fichier
```

---

## 🎯 Catégories

### Official (Monstres Officiels)

**Source:** API officielle D&D 5e (https://www.dnd5eapi.co/)

**Format:** Un fichier JSON par monstre

**Caractéristiques:**
- ✅ Complet et standardisé
- ✅ Directement de l'API officielle
- ✅ Utilisé par `dnd_5e_core.data.loaders.request_monster()`
- ✅ ~300 monstres du Monster Manual

**Exemple de fichier:** `official/goblin.json`
```json
{
  "index": "goblin",
  "name": "Goblin",
  "size": "Small",
  "type": "humanoid",
  "alignment": "neutral evil",
  "armor_class": 15,
  "hit_points": 7,
  "hit_dice": "2d6",
  "speed": {
    "walk": "30 ft."
  },
  "strength": 8,
  "dexterity": 14,
  ...
}
```

### Extended (Monstres Étendus)

**Source:** 5e.tools (format JSON étendu)

**Format:** ⭐ **NOUVEAU** - Un fichier JSON par monstre

**Changement Important:**
- ✅ **Avant:** 2 fichiers agrégés (bestiary-sublist-data.json + all-monsters)
- ✅ **Maintenant:** Fichiers individuels + archives conservées

**Fichiers:**

1. **Fichiers Individuels** (NOUVEAU)
   - Un fichier par monstre étendu
   - Nommage: lowercase, tirets (ex: `goblin-boss.json`)
   - ~300+ fichiers individuels
   - Facilite la recherche et modification

2. **Archives** (conservées pour compatibilité)
   - `bestiary-sublist-data.json` - 47 monstres implémentés
   - `bestiary-sublist-data-all-monsters.json` - Tous les monstres

**Caractéristiques:**
- ✅ Plus détaillé que l'API officielle
- ✅ Extraction automatique des actions depuis JSON
- ✅ Un fichier = un monstre (plus facile à gérer)
- ✅ Utilisé par `FiveEToolsMonsterLoader`
- ✅ Archives conservées pour rétro-compatibilité

**Exemple de fichier:** `extended/goblin-boss.json`
```json
{
  "name": "Goblin Boss",
  "source": "MM",
  "cr": "1",
  "trait": [
    {
      "name": "Nimble Escape",
      "entries": ["The goblin can take the Disengage or Hide action as a bonus action..."]
    }
  ],
  "action": [
    {
      "name": "Multiattack",
      "entries": ["The goblin makes two attacks with its scimitar..."]
    },
    {
      "name": "Scimitar",
      "entries": ["{@atk mw} {@hit 4} to hit, reach 5 ft., one target..."]
    }
  ]
}
```

---

## 🔧 Utilisation

### Charger un Monstre Officiel

```python
from dnd_5e_core.data.loaders import request_monster

# Charge depuis official/goblin.json
goblin = request_monster("goblin")
```

### Charger un Monstre Étendu (Fichier Individuel)

```python
from dnd_5e_core.entities import FiveEToolsMonsterLoader

loader = FiveEToolsMonsterLoader()

# NOUVEAU: Charge depuis extended/goblin-boss.json
goblin_boss = loader.get_monster_by_name("Goblin Boss")

# OU depuis les archives (compatibilité)
goblin_boss_archive = loader.get_monster_by_name("Goblin Boss", use_all=True)
```

### Récupérer Actions Spéciales

```python
from dnd_5e_core.entities import get_special_monster_actions

# Fonctionne avec fichiers individuels ou archives
actions, abilities, spellcaster = get_special_monster_actions("Goblin Boss")
```

---

## 📊 Statistiques

| Catégorie | Format | Monstres | Source |
|-----------|--------|----------|--------|
| **Official** | Fichiers individuels | ~300 | API D&D 5e |
| **Extended (individuels)** | Fichiers individuels | ~300+ | 5e.tools |
| **Extended (archives)** | 2 fichiers agrégés | ~300+ | 5e.tools |
| **TOTAL** | **~600+ fichiers** | **~600+** | - |

---

## 🆕 Nouveau: Fichiers Individuels Extended

### Avantages

✅ **Recherche Facile**
- Un monstre = un fichier
- Pas besoin de parser un gros JSON

✅ **Modification Simple**
- Éditer directement le fichier du monstre
- Pas de risque de corruption du fichier global

✅ **Performance**
- Chargement sélectif
- Pas besoin de charger 300+ monstres

✅ **Git-Friendly**
- Changements isolés par monstre
- Meilleur historique Git

✅ **Compatibilité**
- Archives conservées
- Aucun breaking change

### Nommage des Fichiers

Pattern: `lowercase-with-dashes.json`

Exemples:
- `Goblin Boss` → `goblin-boss.json`
- `Orc Eye of Gruumsh` → `orc-eye-of-gruumsh.json`
- `Hobgoblin Captain` → `hobgoblin-captain.json`

Règles:
- Tout en minuscules
- Espaces → tirets
- Apostrophes supprimées
- Virgules supprimées
- Parenthèses supprimées

---

## 🔄 Migration depuis Ancienne Structure

**Avant (Archives uniquement):**
```
extended/
├── bestiary-sublist-data.json           (47 monstres)
└── bestiary-sublist-data-all-monsters.json  (300+ monstres)
```

**Maintenant (Fichiers individuels + Archives):**
```
extended/
├── goblin-boss.json                     ← NOUVEAU
├── orc-eye-of-gruumsh.json              ← NOUVEAU
├── hobgoblin-captain.json               ← NOUVEAU
├── ... (300+ fichiers individuels)      ← NOUVEAU
├── bestiary-sublist-data.json           (conservé)
└── bestiary-sublist-data-all-monsters.json  (conservé)
```

**Impact sur le Code:**

✅ **Aucun breaking change** - Les loaders fonctionnent toujours avec les archives
✅ **Nouveau:** Peut aussi charger depuis fichiers individuels
✅ **Performance:** Chargement plus rapide avec fichiers individuels

---

## 🎯 Cas d'Usage

### Développeur: Ajouter un Monstre

**Avant:**
1. Ouvrir bestiary-sublist-data.json (300+ monstres)
2. Trouver le bon endroit dans le tableau
3. Ajouter le monstre
4. Risque d'erreur JSON

**Maintenant:**
1. Créer `extended/mon-nouveau-monstre.json`
2. Écrire les données du monstre
3. Terminé!

### Développeur: Modifier un Monstre

**Avant:**
1. Ouvrir bestiary-sublist-data.json
2. Chercher le monstre (CTRL+F)
3. Modifier
4. Sauvegarder tout le fichier

**Maintenant:**
1. Ouvrir `extended/goblin-boss.json`
2. Modifier
3. Sauvegarder

### Utilisateur: Charger un Monstre

**Code identique:**
```python
# Fonctionne avec archives OU fichiers individuels
loader = FiveEToolsMonsterLoader()
monster = loader.get_monster_by_name("Goblin Boss")
```

---

## 📝 Notes Techniques

### Paths

- **Official:** `dnd_5e_core/data/monsters/official/*.json`
- **Extended (individuels):** `dnd_5e_core/data/monsters/extended/*.json`
- **Extended (archives):** `dnd_5e_core/data/monsters/extended/bestiary-*.json`

### Loaders

Les loaders ont été mis à jour pour:
1. Chercher d'abord dans les fichiers individuels
2. Fallback sur les archives si nécessaire
3. Maintenir la rétro-compatibilité

### Format JSON

- **Official**: Format API D&D 5e standard
- **Extended**: Format 5e.tools avec tags spéciaux (`{@atk mw}`, `{@hit 4}`, etc.)
- **Identique** que ce soit fichier individuel ou archive

---

## ✨ Extraction Automatique

### Script d'Extraction

Les fichiers individuels ont été créés automatiquement depuis les archives:

```python
# Script utilisé pour extraction
import json
from pathlib import Path

with open('bestiary-sublist-data.json', 'r') as f:
    monsters = json.load(f)

for monster in monsters:
    name = monster['name']
    filename = name.lower().replace(' ', '-').replace("'", '').replace(',', '')
    
    with open(f'{filename}.json', 'w') as f:
        json.dump(monster, f, indent=2, ensure_ascii=False)
```

### Maintenir la Synchronisation

**Important:** Les fichiers individuels ET les archives peuvent coexister.

**Recommandation:** Utiliser les fichiers individuels pour modifications, régénérer les archives périodiquement si nécessaire.

---

**Version:** dnd-5e-core v0.4.0  
**Date:** 20 Janvier 2026  
**Statut:** ✅ Production Ready  
**Format:** ⭐ Fichiers Individuels (NOUVEAU)

---

## 🎯 Catégories

### Official (Monstres Officiels)

**Source:** API officielle D&D 5e (https://www.dnd5eapi.co/)

**Format:** Un fichier JSON par monstre

**Caractéristiques:**
- ✅ Complet et standardisé
- ✅ Directement de l'API officielle
- ✅ Utilisé par `dnd_5e_core.data.loaders.request_monster()`
- ✅ ~300 monstres du Monster Manual

**Exemple de fichier:** `official/goblin.json`
```json
{
  "index": "goblin",
  "name": "Goblin",
  "size": "Small",
  "type": "humanoid",
  "alignment": "neutral evil",
  "armor_class": 15,
  "hit_points": 7,
  "hit_dice": "2d6",
  "speed": {
    "walk": "30 ft."
  },
  "strength": 8,
  "dexterity": 14,
  ...
}
```

### Extended (Monstres Étendus)

**Source:** 5e.tools (format JSON étendu)

**Format:** 2 fichiers JSON agrégés

**Fichiers:**

1. **bestiary-sublist-data.json**
   - Monstres avec implémentations manuelles
   - Actions détaillées définies dans `special_monster_actions.py`
   - ~47 monstres
   - Exemples: Orc Eye of Gruumsh, Goblin Boss, Hobgoblin Captain

2. **bestiary-sublist-data-all-monsters.json**
   - Tous les monstres étendus
   - Extraction automatique des actions
   - ~300+ monstres
   - Format 5e.tools complet

**Caractéristiques:**
- ✅ Plus détaillé que l'API officielle
- ✅ Extraction automatique des actions depuis JSON
- ✅ Utilisé par `FiveEToolsMonsterLoader`
- ✅ Fallback automatique pour actions spéciales

**Exemple de structure:**
```json
[
  {
    "name": "Goblin Boss",
    "source": "MM",
    "cr": "1",
    "trait": [
      {
        "name": "Nimble Escape",
        "entries": ["The goblin can take the Disengage or Hide action as a bonus action..."]
      }
    ],
    "action": [
      {
        "name": "Multiattack",
        "entries": ["The goblin makes two attacks with its scimitar..."]
      },
      {
        "name": "Scimitar",
        "entries": ["{@atk mw} {@hit 4} to hit, reach 5 ft., one target..."]
      }
    ]
  }
]
```

---

## 🔧 Utilisation

### Charger un Monstre Officiel

```python
from dnd_5e_core.data.loaders import request_monster

# Charge depuis official/goblin.json
goblin = request_monster("goblin")
```

### Charger un Monstre Étendu

```python
from dnd_5e_core.entities import FiveEToolsMonsterLoader

loader = FiveEToolsMonsterLoader()

# Charge depuis extended/bestiary-sublist-data.json
goblin_boss = loader.get_monster_by_name("Goblin Boss")

# Ou depuis extended/bestiary-sublist-data-all-monsters.json
goblin_boss_all = loader.get_monster_by_name("Goblin Boss", use_all=True)
```

### Récupérer Actions Spéciales

```python
from dnd_5e_core.entities import get_special_monster_actions

# Essaie d'abord définitions manuelles, puis extraction JSON
actions, abilities, spellcaster = get_special_monster_actions("Goblin Boss")
```

---

## 📊 Statistiques

| Catégorie | Fichiers | Monstres | Source |
|-----------|----------|----------|--------|
| **Official** | ~300 | ~300 | API D&D 5e |
| **Extended (implémentés)** | 1 | ~47 | 5e.tools |
| **Extended (tous)** | 1 | ~300+ | 5e.tools |
| **TOTAL** | ~302 | **~600+** | - |

---

## 🔄 Migration depuis Ancienne Structure

**Avant:**
```
monsters/
├── goblin.json
├── orc.json
├── bestiary-sublist-data.json
└── bestiary-sublist-data-all-monsters.json
```

**Après:**
```
monsters/
├── official/
│   ├── goblin.json
│   └── orc.json
└── extended/
    ├── bestiary-sublist-data.json
    └── bestiary-sublist-data-all-monsters.json
```

**Impact sur le Code:**

Les loaders ont été mis à jour automatiquement pour chercher dans les bons répertoires. Aucune modification de code utilisateur nécessaire.

---

## 🎯 Avantages de cette Structure

1. **Organisation Claire**
   - Séparation officiel vs étendu
   - Facile de trouver les monstres

2. **Maintenance Simplifiée**
   - Mise à jour sélective par source
   - Pas de conflit de noms

3. **Performance**
   - Chargement sélectif selon la source
   - Réduction du temps de recherche

4. **Extensibilité**
   - Facile d'ajouter de nouvelles sources
   - Structure modulaire

---

## 📝 Notes Techniques

### Paths

- **Official:** `dnd_5e_core/data/monsters/official/*.json`
- **Extended:** `dnd_5e_core/data/monsters/extended/*.json`

### Loaders

- **request_monster()**: Cherche dans `official/`
- **FiveEToolsMonsterLoader**: Cherche dans `extended/`
- **get_special_monster_actions()**: Utilise les deux

### Format JSON

- **Official**: Format API D&D 5e standard
- **Extended**: Format 5e.tools avec tags spéciaux (`{@atk mw}`, `{@hit 4}`, etc.)

---

**Version:** dnd-5e-core v0.4.0  
**Date:** 20 Janvier 2026  
**Statut:** ✅ Production Ready
