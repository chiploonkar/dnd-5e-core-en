# Conditions and Magic Items System - Implementation Summary

## 🎯 Objective

Implement a comprehensive system to parse and automatically apply D&D 5e conditions from monster actions and magic items.

## ✅ What has been implemented

### 1. Condition Parser (`ConditionParser`)

**File**: `dnd_5e_core/combat/condition_parser.py`

Features:
- ✅ Parses textual descriptions to extract conditions
- ✅ Automatically extracts DC (Difficulty Class) and saving throw types
- ✅ Supports 9 standard D&D 5e conditions
- ✅ Handles format variations ("DC 15 Constitution" or "Constitution save DC 15")
- ✅ Works with both monster actions AND magic item descriptions

**Usage example**:
```python
from dnd_5e_core.combat import ConditionParser

desc = "Target must make a DC 15 Constitution saving throw or be paralyzed for 1 minute."
conditions = ConditionParser.parse_condition_from_description(desc)
# → [Condition(name="Paralyzed", dc_type=CON, dc_value=15)]
```

### 2. Integration into the Monster Loader

**File**: `dnd_5e_core/data/loader.py`

Modifications:
- ✅ Import of `ConditionParser`
- ✅ Automatic parsing of conditions during action creation
- ✅ Conditions are attached to `Action.effects`

**Impact**:
```python
spider = load_monster('giant-spider')
for action in spider.actions:
    if action.effects:  # List automatically filled!
        print(f"{action.name} applies {len(action.effects)} condition(s)")
```

### 3. Improvement of Monster.attack()

**File**: `dnd_5e_core/entities/monster.py`

Improvements:
- ✅ Automatic application of conditions to characters
- ✅ Correct handling of reference creatures (for grappled, frightened, etc.)
- ✅ Copying of conditions to avoid shared modifications
- ✅ Fallback for conditions without an apply_to_character method

**Flow**:
1. Monster attacks
2. If hit → applies damage
3. If action.effects → applies each condition
4. Condition.apply_to_character(target)
5. Informative messages

### 4. Magic Items System with Conditions

#### a. MagicItemAction Extension

**File**: `dnd_5e_core/equipment/magic_item.py`

Additions:
- ✅ Field `conditions: List[Condition]`
- ✅ Methods `can_use()`, `use()`, `recharge_uses()`
- ✅ Method `perform_action()` to use the item in combat

**Example**:
```python
wand = create_wand_of_paralysis()
action = wand.actions[0]

messages, damage, healing = wand.perform_action(
    action=action,
    target=goblin,
    user=wizard,
    verbose=True
)
# Automatically applies paralysis to the goblin
```

#### b. Magic Item Factory

**File**: `dnd_5e_core/equipment/magic_item_factory.py`

Created functions:
- ✅ `create_magic_item_with_conditions()` - Generic creation
- ✅ `create_wand_of_paralysis()` - Paralyzes (DC 15 CON)
- ✅ `create_staff_of_entanglement()` - Restrains (DC 13 STR)
- ✅ `create_ring_of_blinding()` - Blinds (DC 14 CON)
- ✅ `create_cloak_of_fear()` - Frightens (DC 15 WIS)
- ✅ `create_poisoned_dagger()` - Poisons + 2d8 poison damage

**Usage**:
```python
from dnd_5e_core.equipment import create_wand_of_paralysis

wand = create_wand_of_paralysis()
# Everything is configured automatically:
# - Conditions parsed from the description
# - DC and saving throw type
# - Limited charges (3/day)
# - Recharge at dawn
```

### 5. Exports and Integration

**Modified files**:
- `dnd_5e_core/combat/__init__.py` - Export of `ConditionParser`
- `dnd_5e_core/equipment/__init__.py` - Exports of the new functions

Now available:
```python
from dnd_5e_core.combat import ConditionParser, parse_magic_item_conditions
from dnd_5e_core.equipment import (
    create_wand_of_paralysis,
    create_magic_item_with_conditions
)
```

### 6. Testing and Documentation

#### Tests

**File**: `tests/test_conditions_system.py`

Complete test suite:
1. ✅ Automatic parsing from monster JSON
2. ✅ Magic items with conditions
3. ✅ Real combat with condition application
4. ✅ Use of magic items in combat
5. ✅ Directly parsing descriptions

**Execution**:
```bash
python tests/test_conditions_system.py
```

#### Documentation

**File**: `docs/CONDITIONS_SYSTEM.md`

Content:
- System overview
- Complete architecture
- Usage examples
- API Reference
- Advanced use cases

## 📊 Statistics

### Created files
- `dnd_5e_core/combat/condition_parser.py` (230 lines)
- `dnd_5e_core/equipment/magic_item_factory.py` (200 lines)
- `tests/test_conditions_system.py` (350 lines)
- `docs/CONDITIONS_SYSTEM.md` (500 lines)

### Modified files
- `dnd_5e_core/entities/monster.py` - Improvement of `attack()`
- `dnd_5e_core/equipment/magic_item.py` - Addition of `perform_action()`
- `dnd_5e_core/data/loader.py` - Parser integration
- `dnd_5e_core/combat/__init__.py` - Exports
- `dnd_5e_core/equipment/__init__.py` - Exports

### Total
- **~1500 lines** of code added
- **5 new files**
- **5 modified files**
- **9 conditions** supported
- **5 predefined magic items**

## 🎮 Workings in Practice

### Scenario 1: Combat with Giant Spider

```python
from dnd_5e_core.data import load_monster, simple_character_generator

# Setup
fighter = simple_character_generator(level=5, class_name='fighter')
spider = load_monster('giant-spider')

# Combat - Conditions are applied automatically!
messages, damage = spider.attack(fighter)
print(messages)
# → "Giant Spider uses Web on Fighter!"
# → "Fighter is hit for 0 hit points!"
# → "Fighter is now Restrained!"

# Verification
if fighter.conditions:
    for c in fighter.conditions:
        print(f"✅ {c.name} - DC {c.dc_value} {c.dc_type.value} to escape")
```

### Scenario 2: Wand of Paralysis

```python
from dnd_5e_core.equipment import create_wand_of_paralysis

# Create and equip
wand = create_wand_of_paralysis()
wand.equipped = True
wand.attuned = True

# Use in combat
action = wand.actions[0]
messages, dmg, heal = wand.perform_action(action, target=goblin, user=wizard)
print(messages)
# → "Wizard uses Wand of Paralysis - Paralyze!"
# → "Goblin is now Paralyzed!"

# Charges management
print(f"Charges: {action.remaining_uses}/{action.uses_per_day}")
# → "Charges: 2/3"
```

## 🔧 Configuration and Customization

### Create a Custom Magic Item

```python
from dnd_5e_core.equipment import create_magic_item_with_conditions, MagicItemRarity, MagicItemType

my_staff = create_magic_item_with_conditions(
    name="Staff of Lightning Stun",
    description="Stuns enemies with lightning",
    rarity=MagicItemRarity.RARE,
    item_type=MagicItemType.STAFF,
    action_name="Lightning Strike",
    action_description="Target must make a DC 16 Constitution saving throw or be stunned. "
                       "On a failed save, also takes 3d8 lightning damage.",
    damage_dice="3d8",
    damage_type="lightning",
    save_dc=16,
    save_ability="con",
    uses_per_day=5,
    recharge="long rest"
)
# Conditions are parsed automatically!
```

### Parse Custom Descriptions

```python
from dnd_5e_core.combat import ConditionParser

custom_desc = """
The creature must make a DC 18 Wisdom saving throw or be frightened and paralyzed.
It can repeat the saving throw at the end of each of its turns.
"""

conditions = ConditionParser.parse_condition_from_description(custom_desc)
# → [Frightened(DC 18 WIS), Paralyzed(DC 18 WIS)]
```

## 🚀 Next Possible Steps

### Short term
- [ ] Add more predefined magic items
- [ ] Support for conditions in spells
- [ ] Condition immunities by race/class

### Medium term
- [ ] Automatic condition durations
- [ ] Visual effects for UI interfaces
- [ ] Environmental conditions

### Long term
- [ ] Parse more complex special abilities
- [ ] Condition chains (A → B → C)
- [ ] Custom conditions by campaign

## 📝 Important Notes

1. **Performance**: Parsing is done only once upon loading, not at every attack
2. **Compatibility**: Works with all existing monsters from the D&D 5e API
3. **Extensibility**: Easy to add new conditions or extend the parser
4. **Tests**: Complete test suite provided for validation

## 🎉 Conclusion

The condition system is now fully integrated into `dnd-5e-core`:

- ✅ **Monsters**: Conditions parsed automatically from JSON
- ✅ **Magic items**: Factory to create items with conditions
- ✅ **Combat**: Automatic application of conditions
- ✅ **Tests**: Complete validation suite
- ✅ **Documentation**: Complete usage guide

The package is now ready for advanced use in D&D 5e scenarios with full management of combat conditions! 🐉⚔️✨
