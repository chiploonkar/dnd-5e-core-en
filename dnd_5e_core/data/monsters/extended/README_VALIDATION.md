# Validation et Organisation des Monstres Extended

Ce document décrit le processus de validation et d'organisation des fichiers de monstres dans le répertoire `extended/`.

## 📋 Objectifs

1. ✅ Vérifier que tous les fichiers JSON contiennent des actions
2. ✅ Valider la structure des monstres (compatibilité Monster class)
3. ✅ Tester les fonctions de chargement (FiveEToolsMonsterLoader)
4. ✅ Archiver les fichiers invalides dans `invalid/`

## 🔧 Scripts Disponibles

### 1. validate_and_organize.py

Script rapide pour identifier et déplacer les fichiers sans actions.

**Utilisation:**
```bash
python3 validate_and_organize.py
```

**Fonctionnalités:**
- ✅ Analyse tous les fichiers JSON
- ✅ Identifie ceux sans actions
- ✅ Déplace vers `invalid/` (avec confirmation)

### 2. test_monster_loading.py

Script complet pour validation approfondie.

**Utilisation:**
```bash
python3 test_monster_loading.py
```

**Fonctionnalités:**
- ✅ Validation structure complète
- ✅ Test du FiveEToolsMonsterLoader
- ✅ Vérification champs requis
- ✅ Rapport détaillé
- ✅ Archivage automatique

### 3. validate_monsters.py

Script de validation simple (pré-existant).

**Utilisation:**
```bash
python3 validate_monsters.py
```

## 📊 Critères de Validation

### Champs Requis

Un monstre valide DOIT avoir:

- ✅ `name` - Nom du monstre
- ✅ `size` - Taille (T, S, M, L, H, G)
- ✅ `type` - Type de créature
- ✅ `action` - Liste d'actions (NON VIDE)

### Caractéristiques (Abilities)

Format 5e.tools - les 6 caractéristiques:

- `str` (Force)
- `dex` (Dextérité)
- `con` (Constitution)
- `int` (Intelligence)
- `wis` (Sagesse)
- `cha` (Charisme)

### Champs Recommandés

Pour une compatibilité complète:

- `ac` - Armor Class
- `hp` - Hit Points
- `speed` - Vitesse
- `cr` - Challenge Rating

## 🗂️ Structure des Fichiers

### Format 5e.tools

```json
{
  "name": "Acolyte",
  "size": ["M"],
  "type": "humanoid",
  "source": "MM",
  "ac": [{"ac": 10}],
  "hp": {"average": 9, "formula": "2d8"},
  "speed": {"walk": 30},
  "str": 10,
  "dex": 10,
  "con": 10,
  "int": 10,
  "wis": 14,
  "cha": 11,
  "cr": "1/4",
  "action": [
    {
      "name": "Club",
      "entries": [
        "{@atk mw} {@hit 2} to hit, reach 5 ft., one target. {@h}2 ({@damage 1d4}) bludgeoning damage."
      ]
    }
  ]
}
```

### Actions

Les actions sont dans la clé `action` (liste):

```json
{
  "action": [
    {
      "name": "Multiattack",
      "entries": ["The monster makes two attacks..."]
    },
    {
      "name": "Bite",
      "entries": ["{@atk mw} {@hit 5} to hit..."]
    }
  ]
}
```

## 📁 Répertoire `invalid/`

### Raisons d'Archivage

Les fichiers sont déplacés vers `invalid/` si:

1. ❌ **Pas d'actions** - Clé `action` absente ou vide
2. ❌ **JSON invalide** - Erreur de syntaxe
3. ❌ **Champs requis manquants** - name, size, type absents
4. ❌ **Structure incorrecte** - Ne peut pas être chargé

### Restauration

Pour restaurer un monstre depuis `invalid/`:

```bash
# Si le monstre a été corrigé
mv invalid/monstre.json .
```

## 🔄 Processus de Validation

### Étape 1: Analyse

```bash
cd dnd_5e_core/data/monsters/extended
python3 test_monster_loading.py
```

### Étape 2: Rapport

Le script affiche:
- Nombre total de fichiers
- Fichiers valides vs invalides
- Fichiers avec/sans actions
- Test du loader
- Groupement par type d'erreur

### Étape 3: Archivage

Avec confirmation utilisateur:
- Création du répertoire `invalid/`
- Déplacement des fichiers problématiques
- Rapport final

## 📊 Exemples de Rapport

```
================================================================================
📊 RAPPORT DE VALIDATION
================================================================================

📁 Fichiers analysés: 2228

✅ Fichiers valides: 2150
   • Avec actions: 2150
   • Sans actions: 0

❌ Fichiers invalides: 78

🔧 Test du loader:
   • Succès: 2150
   • Échecs: 0

⚠️  78 fichiers à archiver:

  Sans actions (45 fichiers):
    • animated-object
    • construct-spirit
    • elemental-spirit
    ... et 42 autres

  JSON invalide: (33 fichiers):
    • corrupted-file-1
    • corrupted-file-2
    ...

Déplacer les fichiers invalides vers invalid/ ? (oui/non): oui

📦 Archivage des fichiers...
✅ 78 fichiers archivés dans invalid/

================================================================================
📊 RÉSULTAT FINAL
================================================================================
📁 Fichiers restants dans extended/: 2150
📁 Fichiers archivés dans invalid/: 78
```

## 🔧 Intégration avec Monster Class

### Chargement d'un Monstre

```python
from dnd_5e_core.entities import FiveEToolsMonsterLoader

loader = FiveEToolsMonsterLoader()

# Charger depuis fichier individuel
monster_data = loader.get_monster_by_name("Acolyte")

# Le loader vérifie automatiquement:
# 1. Fichier individuel existe
# 2. Structure valide
# 3. Retourne les données 5e.tools
```

### Parsing des Actions

```python
from dnd_5e_core.entities import get_special_monster_actions

# Parser les actions avec définitions manuelles ou JSON
actions, abilities, spellcaster = get_special_monster_actions("Acolyte")
```

## 📝 Notes Importantes

### Format 5e.tools vs API Officielle

**5e.tools (extended/):**
```json
{
  "str": 10,
  "dex": 10,
  "ac": [{"ac": 10}]
}
```

**API Officielle (official/):**
```json
{
  "strength": 10,
  "dexterity": 10,
  "armor_class": 10
}
```

Le loader `FiveEToolsMonsterLoader` gère le format 5e.tools.

### Fichiers à Exclure

Certains fichiers ne doivent PAS être validés:

- `bestiary-sublist-data.json` - Archive source
- `bestiary-sublist-data-all-monsters.json` - Archive complète
- `*.py` - Scripts Python

## 🚀 Prochaines Étapes

1. ✅ Valider tous les monstres
2. ✅ Archiver les invalides
3. ⏳ Améliorer le parsing des actions
4. ⏳ Ajouter support spellcasting
5. ⏳ Parser les dégâts depuis JSON

## 📚 Références

- [Format 5e.tools](https://5e.tools)
- [Monster Class Documentation](../../docs/MONSTER_CLASS.md)
- [Special Monster Actions](../../docs/SPECIAL_MONSTER_ACTIONS.md)

---

**Version:** dnd-5e-core v0.4.0  
**Date:** 20 Janvier 2026  
**Statut:** ✅ Production Ready
