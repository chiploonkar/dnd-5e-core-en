# 📚 D&D 5e Class Progression System

## 🎯 Overview

This system implements the complete progression of D&D 5e classes, including:
- Progression by level (1-20)
- Spell slots for spellcasters
- Class features by level
- Class-specific bonuses
- Race traits
- Ability score improvements

## 📥 Data Downloaded from the API

### Source
Official D&D 5e API: https://www.dnd5eapi.co

### Used endpoints

#### 1. Class Levels
```
GET /api/classes/{index}/levels
```
**Example**: `/api/classes/wizard/levels`

**Retrieved data**:
- Proficiency bonus by level
- Features obtained at each level
- Spell slots for spellcasters
- Class-specific data (rage, ki points, etc.)

#### 2. Features
```
GET /api/features/{index}
```
**Examples**:
- `/api/features/spellcasting-wizard`
- `/api/features/rage`
- `/api/features/extra-attack`

#### 3. Traits
```
GET /api/traits/{index}
```
**Examples**:
- `/api/traits/darkvision`
- `/api/traits/fey-ancestry`
- `/api/traits/dwarven-resilience`

## 🏗️ Architecture

### 1. Main Classes

#### `ClassLevelProgression`
Represents the progression at a specific level.

```python
@dataclass
class ClassLevelProgression:
    level: int
    class_index: str
    ability_score_bonuses: int
    prof_bonus: int
    features: List[ClassFeature]
    spellcasting: Optional[SpellcastingInfo]
    class_specific: Dict[str, Any]
```

**Example for level 1 Wizard**:
```python
{
    "level": 1,
    "prof_bonus": 2,
    "features": ["Spellcasting", "Arcane Recovery"],
    "spellcasting": {
        "cantrips_known": 3,
        "spell_slots_level_1": 2
    }
}
```

#### `SpellcastingInfo`
Information on spells at a given level.

```python
@dataclass
class SpellcastingInfo:
    level: int
    cantrips_known: int
    spells_known: int
    spell_slots_level_1: int
    spell_slots_level_2: int
    # ... up to level 9
```

**Property `spell_slots`**:
```python
>>> wizard_lvl5 = progression.get_spellcasting(5)
>>> wizard_lvl5.spell_slots
[0, 4, 3, 2, 0, 0, 0, 0, 0, 0]
#    L1 L2 L3 L4 L5 L6 L7 L8 L9
```

#### `ClassProgression`
Complete progression over 20 levels.

```python
@dataclass
class ClassProgression:
    class_index: str
    class_name: str
    hit_die: int
    levels: Dict[int, ClassLevelProgression]
    saving_throws: List[str]
    skills: List[str]
```

### 2. Data Files

#### Directory Structure
```
dnd_5e_core/data/
├── class_levels/
│   ├── barbarian_levels.json
│   ├── bard_levels.json
│   ├── cleric_levels.json
│   ├── druid_levels.json
│   ├── fighter_levels.json
│   ├── monk_levels.json
│   ├── paladin_levels.json
│   ├── ranger_levels.json
│   ├── rogue_levels.json
│   ├── sorcerer_levels.json
│   ├── warlock_levels.json
│   └── wizard_levels.json
├── features/
│   ├── spellcasting-wizard.json
│   ├── rage.json
│   ├── extra-attack.json
│   └── ...
└── traits/
    ├── darkvision.json
    ├── fey-ancestry.json
    └── ...
```

## 🔧 Usage

### 1. Load a Class Progression

```python
from dnd_5e_core.data.progression_loader import load_class_progression

wizard_progression = load_class_progression('wizard')

# Get info for a level
level_5_data = wizard_progression.get_level(5)
print(f"Prof bonus: +{level_5_data.prof_bonus}")
print(f"Features: {[f.name for f in level_5_data.features]}")
```

### 2. Retrieve Spell Slots

```python
from dnd_5e_core.data.progression_loader import get_spell_slots_for_level

# For a level 5 Wizard
spell_slots = get_spell_slots_for_level('wizard', 5)
# Returns: [0, 4, 3, 2, 0, 0, 0, 0, 0, 0]
#            ^  ^  ^  ^
#            |  |  |  Level 3: 2 slots
#            |  |  Level 2: 3 slots
#            |  Level 1: 4 slots
#            Level 0 (unused)
```

### 3. Apply a Level Up

```python
from dnd_5e_core.data.progression_loader import apply_level_up_benefits

# When a character levels up
character.level = 5
apply_level_up_benefits(character, 5)

# Will display:
#    ❤️  HP: +6 (38 total)
#    🔮 Spell slots updated
#    ✨ New features:
#       - Extra Attack
```

### 4. Class-Specific Bonuses

#### Barbarian
```python
from dnd_5e_core.data.progression_loader import get_class_specific_value

# Rage count at level 3
rage_count = get_class_specific_value('barbarian', 3, 'rage_count')
# Returns: 3

# Rage damage bonus
rage_damage = get_class_specific_value('barbarian', 3, 'rage_damage_bonus')
# Returns: 2
```

#### Monk
```python
# Ki points at level 5
ki_points = get_class_specific_value('monk', 5, 'ki_points')
# Returns: 5

# Martial arts dice
martial_arts = get_class_specific_value('monk', 5, 'martial_arts', {'dice_count': 1, 'dice_value': 6})
# Returns: {'dice_count': 1, 'dice_value': 6} (1d6)
```

#### Rogue
```python
# Sneak attack dice at level 5
sneak_attack = get_class_specific_value('rogue', 5, 'sneak_attack', {'dice_count': 3, 'dice_value': 6})
# Returns: {'dice_count': 3, 'dice_value': 6} (3d6)
```

## 📊 Data Examples

### Wizard Level 1-3

```json
[
  {
    "level": 1,
    "prof_bonus": 2,
    "features": [
      {
        "index": "spellcasting-wizard",
        "name": "Spellcasting"
      },
      {
        "index": "arcane-recovery",
        "name": "Arcane Recovery"
      }
    ],
    "spellcasting": {
      "cantrips_known": 3,
      "spell_slots_level_1": 2
    }
  },
  {
    "level": 2,
    "prof_bonus": 2,
    "features": [
      {
        "index": "arcane-tradition",
        "name": "Arcane Tradition"
      }
    ],
    "spellcasting": {
      "cantrips_known": 3,
      "spell_slots_level_1": 3
    }
  },
  {
    "level": 3,
    "prof_bonus": 2,
    "features": [],
    "spellcasting": {
      "cantrips_known": 3,
      "spell_slots_level_1": 4,
      "spell_slots_level_2": 2
    }
  }
]
```

### Barbarian class_specific

```json
{
  "class_specific": {
    "rage_count": 3,
    "rage_damage_bonus": 2,
    "brutal_critical_dice": 0
  }
}
```

### Fighter class_specific

```json
{
  "class_specific": {
    "action_surge_count": 1,
    "indomitable_uses": 0,
    "extra_attacks": 1
  }
}
```

## 🎮 Integration with Character

### Character Class Extension

Progression data is automatically used in:

#### 1. Character Creation
```python
from dnd_5e_core.data.loaders import simple_character_generator

wizard = simple_character_generator(5, 'elf', 'wizard', 'Gandalf')
# Spell slots are automatically configured for level 5
```

#### 2. Level Up
```python
wizard.level = 6
apply_level_up_benefits(wizard, 6)
# Applies all benefits of level 6
```

#### 3. Spell Casting
```python
# Spell slots are retrieved from progression
if hasattr(wizard, 'sc') and wizard.sc:
    wizard.sc.spell_slots = get_spell_slots_for_level('wizard', wizard.level)
```

## 🔍 Verification of Existing Implementations

### Traits and Features already implemented

✅ **Race Traits** (already in Character)
- Darkvision
- Ability bonuses
- Proficiencies

✅ **Class Features** (partially implemented)
- Spellcasting (via SpellCaster class)
- Proficiencies (weapons, armor, saves)

⚠️ **To implement**
- Specific class features (Rage, Ki, etc.)
- Subclass choices
- Feat selection

### Skills System

✅ **Already implemented**
```python
# Character already has a skill system
character.proficiencies  # List of proficiencies
character.class_type.index  # Class index
```

## 📝 TODO List

### Short Term
- [x] Download progression data
- [x] Create data classes
- [x] Implement the loader
- [ ] Test with all classes
- [ ] Integrate into simple_character_generator
- [ ] Document examples

### Medium Term
- [ ] Implement subclasses
- [ ] Feature choice system
- [ ] Multiclassing support
- [ ] Feats system

### Long Term
- [ ] UI for level up
- [ ] Choice validation
- [ ] Export/Import of characters

## 🚀 Useful Scripts

### 1. Download Data
```bash
cd /Users/display/PycharmProjects/dnd-5e-core
python download_class_progression.py
```

### 2. Test the System
```python
from dnd_5e_core.data.progression_loader import load_class_progression

# Test for all classes
classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 
           'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 
           'warlock', 'wizard']

for class_index in classes:
    prog = load_class_progression(class_index)
    if prog:
        print(f"✅ {class_index}: {prog.class_name}")
    else:
        print(f"❌ {class_index}: Failed to load")
```

## 📚 References

- **API Documentation**: https://5e-bits.github.io/docs/api
- **D&D 5e SRD**: https://dnd.wizards.com/resources/systems-reference-document
- **Class Levels**: https://5e-bits.github.io/docs/api/get-all-level-resources-for-a-class

---

**Version**: 1.0  
**Date**: January 18, 2026  
**Status**: 🚧 In development  
**Compatibility**: dnd-5e-core v0.2.4+
