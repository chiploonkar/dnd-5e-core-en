# Extraction des Monstres 5e.tools

Ce répertoire contient les scripts pour extraire et convertir les 2228 monstres de 5e.tools vers le format compatible avec la classe `Monster` de dnd-5e-core.

## 📋 Fichiers

- `extract_5etools_monsters.py` - Script d'extraction principal
- `validate_monsters.py` - Script de validation des fichiers générés
- `bestiary-sublist-data.json` - Fichier source (2228 monstres)
- `*.json` - Fichiers individuels de monstres (générés)

## 🚀 Utilisation

### 1. Extraction

```bash
cd dnd_5e_core/data/monsters/extended
python3 extract_5etools_monsters.py
```

**Ce que fait le script:**
- ✅ Lit `bestiary-sublist-data.json` (2228 monstres)
- ✅ Convertit chaque monstre au format Monster class
- ✅ Extrait chaque monstre en fichier JSON individuel
- ✅ Génère un rapport de conversion

**Format de sortie:**
```
nom-du-monstre.json  (ex: ancient-red-dragon.json)
```

### 2. Validation

```bash
python3 validate_monsters.py
```

**Ce que fait le script:**
- ✅ Vérifie que tous les JSON sont valides
- ✅ Valide la structure (champs requis)
- ✅ Vérifie la compatibilité avec Monster class
- ✅ Génère un rapport de validation

## 📊 Conversion 5e.tools → Monster

### Champs Mappés

| 5e.tools | Monster Class | Notes |
|----------|---------------|-------|
| `name` | `name` | Direct |
| `size` | `size` | Prend premier élément si liste |
| `type` | `type` | Direct ou depuis dict |
| `ac` | `armor_class` | Prend première valeur si liste |
| `hp` | `hit_points` | Convertit en {average, formula} |
| `speed` | `speed` | Convertit en dict {walk, fly, etc.} |
| `str, dex, con, int, wis, cha` | `abilities` | Direct |
| `cr` | `challenge_rating` | Convertit fractions (1/8 → 0.125) |
| `save` | `saving_throws` | Direct |
| `skill` | `skills` | Direct |
| `vulnerable` | `damage_vulnerabilities` | Direct |
| `resist` | `damage_resistances` | Direct |
| `immune` | `damage_immunities` | Direct |
| `conditionImmune` | `condition_immunities` | Direct |
| `senses` | `senses` | Direct |
| `languages` | `languages` | Direct |
| `trait` | `trait` | Préservé (format 5e.tools) |
| `action` | `action` | Préservé (format 5e.tools) |
| `reaction` | `reaction` | Préservé (format 5e.tools) |
| `legendary` | `legendary` | Préservé (format 5e.tools) |
| `spellcasting` | `spellcasting` | Préservé (format 5e.tools) |

### Métadonnées 5e.tools

Les données spécifiques à 5e.tools sont préservées dans `_5etools`:

```json
{
  "_5etools": {
    "page": 123,
    "otherSources": [...],
    "environment": [...],
    "soundClip": {...},
    "isNpc": false
  }
}
```

## 🔧 Conversions Spéciales

### Challenge Rating (CR)

```python
# Fractions → nombres décimaux
"1/8" → 0.125
"1/4" → 0.25
"1/2" → 0.5
1     → 1.0
```

### Vitesse (Speed)

```python
# 5e.tools
{"walk": 30, "fly": {"number": 60, "condition": "..."}}

# Converti en
{"walk": 30, "fly": 60}
```

### Armor Class (AC)

```python
# 5e.tools (peut être liste)
[{"ac": 18, "from": ["natural armor"]}, {"ac": 15}]

# Converti en (prend premier)
18
```

### Hit Points (HP)

```python
# 5e.tools
{"average": 136, "formula": "16d10 + 48"}

# Converti en
{"average": 136, "formula": "16d10 + 48"}
```

## 📝 Actions et Capacités

Les actions, traits, réactions, etc. sont préservés au format 5e.tools pour permettre un parsing ultérieur plus sophistiqué:

```json
{
  "action": [
    {
      "name": "Multiattack",
      "entries": [
        "The dragon makes three attacks: one with its bite and two with its claws."
      ]
    },
    {
      "name": "Bite",
      "entries": [
        "{@atk mw} {@hit 17} to hit, reach 15 ft., one target. {@h}21 ({@damage 2d10 + 10}) piercing damage plus 14 ({@damage 4d6}) fire damage."
      ]
    }
  ]
}
```

**Note:** Le parsing détaillé des actions (extraction attack_bonus, damage, etc.) peut être fait ultérieurement avec le module `special_monster_actions.py`.

## 🎯 Exemple de Monstre Converti

```json
{
  "name": "Ancient Red Dragon",
  "size": "G",
  "type": "dragon",
  "alignment": "CE",
  "armor_class": 22,
  "hit_points": {
    "average": 546,
    "formula": "28d20 + 252"
  },
  "speed": {
    "walk": 40,
    "climb": 40,
    "fly": 80
  },
  "abilities": {
    "str": 30,
    "dex": 10,
    "con": 29,
    "int": 18,
    "wis": 15,
    "cha": 23
  },
  "challenge_rating": 24.0,
  "source": "MM",
  "saving_throws": {
    "dex": 7,
    "con": 16,
    "wis": 9,
    "cha": 13
  },
  "skills": {
    "perception": 16,
    "stealth": 7
  },
  "damage_immunities": ["fire"],
  "senses": ["blindsight 60 ft.", "darkvision 120 ft."],
  "languages": ["Common", "Draconic"],
  "trait": [...],
  "action": [...],
  "legendary": [...]
}
```

## ✅ Validation

Le script `validate_monsters.py` vérifie:

1. **JSON valide** - Syntaxe correcte
2. **Champs requis** - name, size, type, armor_class, hit_points, abilities
3. **Structure abilities** - Les 6 caractéristiques (str, dex, con, int, wis, cha)
4. **Types corrects** - Entiers pour AC, abilities, etc.

## 🐛 Gestion des Erreurs

### Erreurs Communes

**Monstre sans nom:**
- Fallback: `Unknown-{index}`

**CR invalide:**
- Fallback: `0.0`

**HP manquant:**
- Fallback: `{"average": 10, "formula": "2d8"}`

**AC manquant:**
- Fallback: `10`

**Vitesse manquante:**
- Fallback: `{"walk": 30}`

### Logs

Les erreurs et avertissements sont affichés dans le rapport final:

```
❌ Erreurs (3):
  • Erreur conversion Zombie: KeyError 'name'
  • Erreur écriture goblin.json: Permission denied
  
⚠️  Avertissements (15):
  • ancient-dragon.json: hit_points.formula manquant
  • goblin-boss.json: speed devrait être un dictionnaire
```

## 📊 Statistiques Attendues

- **Total de monstres:** 2228
- **Convertis avec succès:** ~2200+
- **Fichiers créés:** ~2200+ fichiers .json
- **Taille moyenne par fichier:** 2-5 KB
- **Taille totale:** ~10-20 MB

## 🔄 Maintenance

### Ajouter un Monstre

1. Créer `nom-monstre.json` dans ce répertoire
2. Suivre la structure décrite ci-dessus
3. Valider avec `validate_monsters.py`

### Mettre à Jour les Monstres

1. Télécharger nouveau `bestiary-sublist-data.json` depuis 5e.tools
2. Relancer `extract_5etools_monsters.py`
3. Valider avec `validate_monsters.py`

### Synchroniser avec Monster Class

Si la classe `Monster` change:

1. Mettre à jour `extract_5etools_monsters.py`
2. Relancer l'extraction
3. Mettre à jour les tests

## 🔗 Intégration

### Charger un Monstre

```python
from dnd_5e_core.entities import FiveEToolsMonsterLoader

loader = FiveEToolsMonsterLoader()
dragon = loader.get_monster_by_name("Ancient Red Dragon")
```

### Parser les Actions

```python
from dnd_5e_core.entities import get_special_monster_actions

actions, abilities, spellcaster = get_special_monster_actions("Ancient Red Dragon")
```

---

**Version:** dnd-5e-core v0.4.0  
**Date:** 20 Janvier 2026  
**Format source:** 5e.tools JSON  
**Monstres:** 2228
