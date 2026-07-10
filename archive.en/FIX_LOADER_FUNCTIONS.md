# ✅ Fix: All load_*() Functions Return Objects

## Date: January 17, 2026

## 🎯 Identified Issue

Some `load_*()` functions in `loader.py` were still returning **dictionaries** instead of **objects**:

- ❌ `load_race()` returned `Dict[str, Any]`
- ❌ `load_class()` returned `Dict[str, Any]`
- ❌ `load_equipment()` returned `Dict[str, Any]`

## ✨ Implemented Solution

### New Helper Functions

1. **`_create_race_from_data(index, data) -> Race`**
   - Converts JSON → Race object
   - Manages: ability bonuses, languages, traits, proficiencies
   - Parses proficiency options

2. **`_create_class_from_data(index, data) -> ClassType`**
   - Converts JSON → ClassType object
   - Manages: hit die, proficiencies, saving throws, spellcasting
   - Parses spell slots and proficiency choices

### Modified Functions

#### `load_race(index: str) -> Optional[Race]`

**Before:**
```python
def load_race(index: str) -> Optional[Dict[str, Any]]:
    return load_json_file("races", index)
```

**After:**
```python
def load_race(index: str) -> Optional['Race']:
    data = load_json_file("races", index)
    if data is None:
        return None
    return _create_race_from_data(index, data)
```

**Usage example:**
```python
from dnd_5e_core.data import load_race

elf = load_race("elf")
print(elf.name)                    # "Elf"
print(elf.speed)                   # 30
print(elf.ability_bonuses)         # {"dex": 2}
print(elf.size)                    # "Medium"
print(len(elf.languages))          # Number of languages
```

#### `load_class(index: str) -> Optional[ClassType]`

**Before:**
```python
def load_class(index: str) -> Optional[Dict[str, Any]]:
    return load_json_file("classes", index)
```

**After:**
```python
def load_class(index: str) -> Optional['ClassType']:
    data = load_json_file("classes", index)
    if data is None:
        return None
    return _create_class_from_data(index, data)
```

**Usage example:**
```python
from dnd_5e_core.data import load_class

fighter = load_class("fighter")
print(fighter.name)                # "Fighter"
print(fighter.hit_die)             # 10
print(fighter.can_cast)            # False
print(len(fighter.proficiencies))  # Number of proficiencies
print([st.name for st in fighter.saving_throws])  # ["STR", "CON"]
```

#### `load_equipment(index: str) -> Weapon | Armor | Equipment`

**Before:**
```python
def load_equipment(index: str) -> Optional[Dict[str, Any]]:
    return load_json_file("equipment", index)
```

**After:**
```python
def load_equipment(index: str):
    data = load_json_file("equipment", index)
    if data is None:
        return None
    
    category = data.get('equipment_category', {}).get('index', '')
    
    if category == 'weapon':
        return load_weapon(index)
    elif category == 'armor':
        return load_armor(index)
    else:
        return Equipment(...)  # Generic Equipment object
```

**Usage example:**
```python
from dnd_5e_core.data import load_equipment

# Weapon
longsword = load_equipment("longsword")
print(type(longsword).__name__)    # "WeaponData"
print(longsword.damage_dice)       # DamageDice("1d8")

# Armor
chain_mail = load_equipment("chain-mail")
print(type(chain_mail).__name__)   # "ArmorData"
print(chain_mail.armor_class)      # {'base': 16, ...}

# Other equipment
rope = load_equipment("rope-hempen-50-feet")
print(type(rope).__name__)         # "Equipment"
print(rope.weight)                 # 10
```

## ✅ Final State: All Functions Return Objects

| Function | Return Type | Status |
|----------|----------------|--------|
| `load_monster()` | `Monster` | ✅ v0.1.9 |
| `load_spell()` | `Spell` | ✅ v0.1.9 |
| `load_weapon()` | `Weapon` | ✅ v0.1.9 |
| `load_armor()` | `Armor` | ✅ v0.1.9 |
| `load_race()` | `Race` | ✅ **NEW** |
| `load_class()` | `ClassType` | ✅ **NEW** |
| `load_equipment()` | `Weapon` \| `Armor` \| `Equipment` | ✅ **NEW** |

## 🧪 Tests Performed

```bash
✅ Test of all load_* functions
==================================================
load_race("elf"): Race
load_class("fighter"): ClassType
load_equipment("longsword"): WeaponData
load_equipment("chain-mail"): ArmorData

✅ All functions return objects!
```

## 🔧 Technical Details

### Race Object Creation

The `_create_race_from_data()` function manages:

- **Ability Bonuses**: `{"dex": 2, "int": 1}`
- **Languages**: Language objects with index, name, desc, type, speakers, script
- **Traits**: Trait objects with index, name, desc
- **Proficiencies**: Proficiency objects with auto-detected type (SKILL, WEAPON, ARMOR, etc.)
- **Proficiency Options**: Tuples `(choose, [Proficiency])` for choices

### ClassType Object Creation

The `_create_class_from_data()` function manages:

- **Proficiencies**: Auto-detection of type (SKILL, ST, WEAPON, ARMOR, TOOLS)
- **Proficiency Choices**: Tuples `(choose, [Proficiency])`
- **Saving Throws**: List of `AbilityType` (STR, DEX, CON, INT, WIS, CHA)
- **Spellcasting**: Automatic detection of whether the class can cast spells
- **Spell Slots**: Dictionary by level if spellcaster class

### Equipment Smart Loading

The `load_equipment()` function automatically detects:

- **Weapon**: Returns `load_weapon(index)` → `WeaponData` object
- **Armor**: Returns `load_armor(index)` → `ArmorData` object
- **Other**: Creates a generic `Equipment` object

## 💡 Benefits

1. **Consistency**: All `load_*()` functions return objects
2. **Strong Typing**: No more `KeyError` errors, IDE auto-completion
3. **Utility Methods**: Direct access to properties and methods
4. **More Readable Code**: `elf.speed` instead of `elf_data.get('speed', 30)`

## 📦 Git Commit

- **Commit**: `184aa28`
- **Message**: Fix: load_race, load_class and load_equipment now return objects
- **Status**: ✅ Pushed to GitHub

## 🎉 Summary

**All `load_*()` functions in `loader.py` now return objects instead of dictionaries!**

This completes the migration to an object-oriented API for the `dnd-5e-core` package.

---

**Author**: GitHub Copilot  
**Date**: January 17, 2026  
**Version**: dnd-5e-core 0.1.9+  
**Status**: ✅ **COMPLETED**
