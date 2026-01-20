# Parsing Avancé des Monstres Extended

Ce document décrit le système de parsing avancé pour extraire les informations des monstres au format 5e.tools.

## 🎯 Objectif

Parser automatiquement depuis le format 5e.tools:
1. **Actions** - Extraction attack_bonus, damage, DC, etc.
2. **Spells** - Extraction des sorts depuis spellcasting
3. **Enrichissement** - Créer fichiers avec données parsées

## 📝 Scripts

### 1. improved_converter.py

Convertisseur intelligent avec parsing regex.

**Classes:**

#### FiveEToolsActionParser

Parse les actions au format 5e.tools.

**Patterns regex utilisés:**
```python
ATTACK_PATTERN = r'\{@atk (mw|rw|ms|rs)\}'  # Type d'attaque
HIT_PATTERN = r'\{@hit (\d+)\}'             # Bonus d'attaque
DAMAGE_PATTERN = r'\{@damage ([\dd\+\-\s]+)\}'  # Dégâts
DC_PATTERN = r'\{@dc (\d+)\}'                # Difficulty Class
```

**Exemple d'extraction:**
```
Texte 5e.tools:
"{@atk mw} {@hit 5} to hit, reach 5 ft. {@h}7 ({@damage 1d8 + 3}) slashing damage"

Extrait:
{
  "attack_type": "melee_weapon",
  "attack_bonus": 5,
  "damages": [
    {
      "formula": "1d8 + 3",
      "dice_count": 1,
      "dice_sides": 8,
      "bonus": 3
    }
  ]
}
```

#### FiveEToolsSpellParser

Parse le spellcasting et extrait les sorts.

**Pattern regex:**
```python
SPELL_PATTERN = r'\{@spell ([^}|]+)(?:\|[^}]*)?\}'
```

**Extraction depuis:**
- `spells` (par niveau)
- `daily` (fréquence quotidienne)
- `will` (à volonté)

**Exemple:**
```json
Input 5e.tools:
{
  "spellcasting": [{
    "spells": {
      "0": {
        "spells": ["{@spell fire bolt}", "{@spell mage hand}"]
      },
      "1": {
        "spells": ["{@spell magic missile}", "{@spell shield}"]
      }
    }
  }]
}

Output parsé:
{
  "spells_by_level": {
    "0": ["fire bolt", "mage hand"],
    "1": ["magic missile", "shield"]
  }
}
```

### 2. enrich_monsters.py

Script d'enrichissement automatique.

**Fonctionnalités:**
- Analyse tous les fichiers extended/
- Applique improved_converter
- Crée fichiers enrichis dans enriched/
- Rapport détaillé

**Utilisation:**
```bash
python3 enrich_monsters.py
```

## 🔍 Format 5e.tools - Tags Spéciaux

### Actions

#### Types d'attaque

- `{@atk mw}` - Melee Weapon (arme de mêlée)
- `{@atk rw}` - Ranged Weapon (arme à distance)
- `{@atk ms}` - Melee Spell (sort de mêlée)
- `{@atk rs}` - Ranged Spell (sort à distance)

#### Dégâts

- `{@damage 2d6}` - Dégâts de dés
- `{@damage 2d6 + 4}` - Dégâts avec bonus
- `{@h}` - Hit (coup qui touche)

#### Autres

- `{@dc 15}` - Difficulty Class (jet de sauvegarde)
- `{@hit 5}` - Bonus d'attaque
- `{@spell fireball}` - Référence à un sort

### Spellcasting

Structure typique:
```json
{
  "spellcasting": [
    {
      "name": "Spellcasting",
      "headerEntries": [
        "The wizard is a 5th-level spellcaster. save {@dc 13}"
      ],
      "ability": "int",
      "spells": {
        "0": {
          "spells": [
            "{@spell fire bolt}",
            "{@spell light}",
            "{@spell mage hand}",
            "{@spell prestidigitation}"
          ]
        },
        "1": {
          "slots": 4,
          "spells": [
            "{@spell detect magic}",
            "{@spell mage armor}",
            "{@spell magic missile}",
            "{@spell shield}"
          ]
        }
      }
    }
  ]
}
```

## 📊 Extraction des Sorts

### Depuis data/spells

Le SpellParser charge les sorts connus depuis:
```
dnd_5e_core/data/spells/*.json
```

**Validation:**
- Compare sorts extraits avec liste connue
- Normalise les noms (lowercase)
- Signale sorts inconnus

### Pattern Matching

**Simple:**
```
"{@spell fireball}" → "fireball"
```

**Avec variante:**
```
"{@spell fireball|phb}" → "fireball"
```

**Dans texte:**
```
"The wizard can cast {@spell mage armor} and {@spell shield}"
→ ["mage armor", "shield"]
```

## 🔄 Pipeline de Conversion

```
Fichier 5e.tools
        ↓
FiveEToolsActionParser
        ↓
    Actions parsées
    (attack_bonus, damage, dc)
        ↓
FiveEToolsSpellParser
        ↓
    Sorts extraits
    (par niveau, daily, at-will)
        ↓
ImprovedMonsterConverter
        ↓
    Monstre enrichi
    (original + parsed)
        ↓
  enriched/*.json
```

## 📝 Exemple Complet

### Input (5e.tools)

```json
{
  "name": "Archmage",
  "action": [
    {
      "name": "Dagger",
      "entries": [
        "{@atk mw,rw} {@hit 6} to hit, reach 5 ft. or range 20/60 ft. {@h}4 ({@damage 1d4 + 2}) piercing damage."
      ]
    }
  ],
  "spellcasting": [
    {
      "name": "Spellcasting",
      "ability": "int",
      "headerEntries": [
        "The archmage casts one of the following spells, using Intelligence as the spellcasting ability (spell save {@dc 17}):"
      ],
      "will": [
        "{@spell light}",
        "{@spell mage hand}",
        "{@spell prestidigitation}"
      ],
      "daily": {
        "3e": [
          "{@spell detect magic}",
          "{@spell dispel magic}"
        ],
        "1e": [
          "{@spell time stop}"
        ]
      }
    }
  ]
}
```

### Output (enrichi)

```json
{
  "name": "Archmage",
  "action": [...],
  "actions_parsed": [
    {
      "name": "Dagger",
      "attack_type": "melee_weapon",
      "attack_bonus": 6,
      "damages": [
        {
          "formula": "1d4 + 2",
          "dice_count": 1,
          "dice_sides": 4,
          "bonus": 2
        }
      ],
      "description": "{@atk mw,rw} {@hit 6} to hit..."
    }
  ],
  "spellcasting": [...],
  "spellcasting_parsed": {
    "ability": "int",
    "dc": 17,
    "at_will": ["light", "mage hand", "prestidigitation"],
    "daily": {
      "3e": ["detect magic", "dispel magic"],
      "1e": ["time stop"]
    }
  }
}
```

## 🧪 Tests

### Test du Parser d'Actions

```python
from improved_converter import FiveEToolsActionParser

parser = FiveEToolsActionParser()

action_data = {
    "name": "Longsword",
    "entries": [
        "{@atk mw} {@hit 5} to hit, reach 5 ft. {@h}7 ({@damage 1d8 + 3}) slashing damage"
    ]
}

parsed = parser.parse_action(action_data)
print(parsed)
# {
#   'name': 'Longsword',
#   'attack_type': 'melee_weapon',
#   'attack_bonus': 5,
#   'damages': [{'formula': '1d8 + 3', ...}],
#   ...
# }
```

### Test du Parser de Sorts

```python
from improved_converter import FiveEToolsSpellParser

parser = FiveEToolsSpellParser()

spellcasting_data = [{
    "will": ["{@spell light}", "{@spell mage hand}"],
    "daily": {
        "3e": ["{@spell fireball}"]
    }
}]

parsed = parser.parse_spellcasting(spellcasting_data)
print(parsed)
# {
#   'at_will': ['light', 'mage hand'],
#   'daily': {'3e': ['fireball']},
#   ...
# }
```

## 📚 Références

### Tags 5e.tools

Documentation complète: https://5e.tools

**Tags courants:**
- `{@atk ...}` - Type d'attaque
- `{@hit ...}` - Bonus d'attaque
- `{@damage ...}` - Dégâts
- `{@dc ...}` - Difficulty Class
- `{@spell ...}` - Sort
- `{@creature ...}` - Créature
- `{@item ...}` - Objet
- `{@condition ...}` - Condition

### Regex Python

Documentation: https://docs.python.org/3/library/re.html

**Patterns utilisés:**
- `\d+` - Un ou plusieurs chiffres
- `[^}]+` - Tout sauf }
- `(?:...)` - Groupe non-capturant
- `\s*` - Espaces optionnels

## ⚠️ Limitations Actuelles

1. **Dégâts multiples** - Parse le premier uniquement
2. **Conditions complexes** - Pas toutes extraites
3. **Sorts inconnus** - Acceptés mais pas validés
4. **Effets spéciaux** - Non parsés (paralysie, etc.)

## 🔧 Améliorations Futures

1. Parser TOUS les dégâts d'une attaque
2. Extraire conditions (poison, paralysie, etc.)
3. Valider tous les sorts contre data/spells
4. Parser les effets spéciaux (reach, etc.)
5. Gérer les variantes d'attaque
6. Extraire portées (range)

---

**Version:** dnd-5e-core v0.4.0  
**Date:** 20 Janvier 2026  
**Statut:** ✅ Fonctionnel
