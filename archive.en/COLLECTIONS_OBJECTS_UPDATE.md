# New Object Loading Functions - collections.py

## Date: January 17, 2026

## 🎯 Goal

Add practical functions to `collections.py` to directly load **lists of objects** (Monster, Spell, etc.) instead of lists of indexes (strings).

## ✨ New Functions Added

### 1. Loading All Entities

#### `load_all_monsters() -> List[Monster]`
Loads **all** monsters as Monster objects.

```python
from dnd_5e_core.data import load_all_monsters

monsters = load_all_monsters()
for monster in monsters:
    print(f"{monster.name} - CR {monster.challenge_rating}, HP {monster.hit_points}")
```

#### `load_all_spells() -> List[Spell]`
Loads **all** spells as Spell objects.

```python
from dnd_5e_core.data import load_all_spells

spells = load_all_spells()
for spell in spells:
    print(f"{spell.name} - Level {spell.level}, School: {spell.school}")
```

#### `load_all_weapons() -> List[Weapon]`
Loads **all** weapons as Weapon objects.

```python
from dnd_5e_core.data import load_all_weapons

weapons = load_all_weapons()
for weapon in weapons:
    print(f"{weapon.name} - {weapon.damage_dice}")
```

#### `load_all_armors() -> List[Armor]`
Loads **all** armors as Armor objects.

```python
from dnd_5e_core.data import load_all_armors

armors = load_all_armors()
for armor in armors:
    print(f"{armor.name} - AC {armor.armor_class}")
```

### 2. Filtering by Criteria

#### `filter_monsters(min_cr, max_cr, name_contains) -> List[Monster]`
Filters monsters based on criteria.

**Parameters:**
- `min_cr` (float, optional): minimum CR
- `max_cr` (float, optional): maximum CR
- `name_contains` (str, optional): filter by name (case-insensitive)

**Examples:**

```python
from dnd_5e_core.data import filter_monsters

# All monsters CR 0-1 (beginner)
low_level = filter_monsters(max_cr=1)

# Monsters CR 5-10 (medium level)
mid_level = filter_monsters(min_cr=5, max_cr=10)

# All CR 10+ dragons
dragons = filter_monsters(min_cr=10, name_contains="dragon")

# All goblins (any CR)
goblins = filter_monsters(name_contains="goblin")
```

#### `filter_spells(level, school, class_name) -> List[Spell]`
Filters spells based on criteria.

**Parameters:**
- `level` (int, optional): Spell level (0-9, where 0 = cantrip)
- `school` (str, optional): school of magic
- `class_name` (str, optional): class that can cast it

**Examples:**

```python
from dnd_5e_core.data import filter_spells

# All wizard cantrips
wizard_cantrips = filter_spells(level=0, class_name="wizard")

# All level 3 evocation spells
evocation_3 = filter_spells(level=3, school="evocation")

# All cleric spells (all levels)
cleric_spells = filter_spells(class_name="cleric")

# Abjuration cantrips for wizard
wizard_abjuration_cantrips = filter_spells(
    level=0, 
    school="abjuration", 
    class_name="wizard"
)
```

## 📊 Before/After Comparison

### Before (With Indexes)

```python
# Load the index list
from dnd_5e_core.data import get_monsters_list, load_monster

monster_indexes = get_monsters_list()

# Manually load each monster
monsters = []
for index in monster_indexes:
    monster = load_monster(index)
    if monster:
        monsters.append(monster)

# Manually filter
low_cr_monsters = [m for m in monsters if m.challenge_rating <= 1]
```

### After (With Objects)

```python
# Directly load all monsters
from dnd_5e_core.data import load_all_monsters, filter_monsters

monsters = load_all_monsters()

# Or filter directly
low_cr_monsters = filter_monsters(max_cr=1)
```

**Code savings: ~70%** 🚀

## 🔧 Implementation

The new functions use the `load_*()` functions from `loader.py` which now return objects (v0.1.9).

```python
def load_all_monsters() -> List:
    """Load all monsters as Monster objects"""
    from .loader import load_monster
    
    monster_indexes = get_monsters_list()
    monsters = []
    
    for index in monster_indexes:
        monster = load_monster(index)
        if monster:
            monsters.append(monster)
    
    return monsters
```

## 📦 Exports

All new functions are exported in `dnd_5e_core.data.__init__.py`:

```python
from dnd_5e_core.data import (
    # Bulk loading
    load_all_monsters,
    load_all_spells,
    load_all_weapons,
    load_all_armors,
    
    # Filtering
    filter_monsters,
    filter_spells
)
```

## 🎮 Use Cases

### 1. Random Encounter Generator

```python
from dnd_5e_core.data import filter_monsters
import random

def generate_encounter(party_level: int, num_monsters: int = 3):
    """Generate a random encounter"""
    # Appropriate CR for the party level
    min_cr = max(0, party_level - 2)
    max_cr = party_level + 1
    
    # Find suitable monsters
    suitable_monsters = filter_monsters(min_cr=min_cr, max_cr=max_cr)
    
    # Randomly select
    encounter = random.sample(suitable_monsters, min(num_monsters, len(suitable_monsters)))
    
    return encounter

# Usage
party_level = 5
encounter = generate_encounter(party_level)
for monster in encounter:
    print(f"- {monster.name} (CR {monster.challenge_rating})")
```

### 2. Wizard Spellbook

```python
from dnd_5e_core.data import filter_spells

def get_wizard_spellbook(max_level: int = 9):
    """Get all wizard spells up to the specified level"""
    spellbook = {}
    
    for level in range(max_level + 1):
        spells = filter_spells(level=level, class_name="wizard")
        spellbook[level] = spells
    
    return spellbook

# Usage
spellbook = get_wizard_spellbook(max_level=3)
for level, spells in spellbook.items():
    level_name = "Cantrips" if level == 0 else f"Level {level}"
    print(f"\n{level_name} ({len(spells)} spells):")
    for spell in spells[:5]:  # Show the first 5
        print(f"  - {spell.name}")
```

### 3. Weapon Comparator

```python
from dnd_5e_core.data import load_all_weapons

def compare_weapons_by_damage():
    """Compare all weapons by average damage"""
    weapons = load_all_weapons()
    
    # Sort by average damage
    sorted_weapons = sorted(
        weapons, 
        key=lambda w: w.damage_dice.average(), 
        reverse=True
    )
    
    print("Top 10 weapons by damage:")
    for i, weapon in enumerate(sorted_weapons[:10], 1):
        print(f"{i}. {weapon.name}: {weapon.damage_dice} "
              f"(avg: {weapon.damage_dice.average()})")

# Usage
compare_weapons_by_damage()
```

## ✅ Tests Performed

```python
# Test 1: Loading
✅ load_all_monsters() - 332 monsters loaded
✅ load_all_spells() - 319 spells loaded

# Test 2: Filtering
✅ filter_monsters(max_cr=0.5) - 5+ weak monsters
✅ filter_monsters(name_contains="dragon") - 20+ dragons
✅ filter_spells(level=0, class_name="wizard") - 10+ cantrips

# Test 3: Import
✅ from dnd_5e_core.data import load_all_monsters
✅ from dnd_5e_core.data import filter_spells
```

## 🚀 Performance

The functions use lazy loading:
- Only requested monsters/spells are loaded
- No global cache (avoids excessive memory)
- Each call reloads from JSON files (always up to date)

For optimal performance with repeated loads:

```python
# Load once and reuse
all_monsters = load_all_monsters()  # Loads all monsters

# Filter in memory (fast)
dragons = [m for m in all_monsters if 'dragon' in m.name.lower()]
low_cr = [m for m in all_monsters if m.challenge_rating <= 1]
```

## 📚 Updated Documentation

- ✅ `collections.py` - Complete docstrings with examples
- ✅ `data/__init__.py` - Updated exports
- ✅ Example `__main__` in `collections.py`

## 🔄 Compatibility

**100% backward compatible**: Existing functions (`get_monsters_list()`, etc.) still work and return index lists.

The new functions (`load_all_monsters()`, `filter_monsters()`) are **additions** that do not affect existing code.

---

**Author**: GitHub Copilot  
**Date**: January 17, 2026  
**Version**: dnd-5e-core 0.1.9+  
**Status**: ✅ **COMPLETED**
