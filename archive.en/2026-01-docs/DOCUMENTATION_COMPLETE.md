# 📚 dnd-5e-core - Complete Documentation

## Overview

`dnd-5e-core` is a comprehensive Python package implementing the rules of Dungeons & Dragons 5th edition, including:

- ✅ Complete combat system with conditions
- ✅ Character and monster management
- ✅ Spells and spellcasting system
- ✅ Equipment and magic items
- ✅ **Class progression by level (1-20)** ✨ NEW
- ✅ Initiative system
- ✅ Automatic encounter calculation

---

## 🚀 Installation

```bash
pip install dnd-5e-core
```

Or from source:

```bash
cd dnd-5e-core
pip install -e .
```

---

## 📖 Quickstart Guide

### 1. Create a Character

```python
from dnd_5e_core.data.loaders import simple_character_generator

# Create a level 5 wizard
gandalf = simple_character_generator(
    level=5,
    race_name='elf',
    class_name='wizard',
    name='Gandalf'
)

print(f"{gandalf.name}: Level {gandalf.level} {gandalf.class_type.name}")
print(f"HP: {gandalf.hit_points}/{gandalf.max_hit_points}")
print(f"AC: {gandalf.armor_class}")

# Spell slots are automatically configured!
if gandalf.sc:
    print(f"Spell slots: {gandalf.sc.spell_slots[1:6]}")
    # Displays: [4, 3, 2, 0, 0] for a level 5 wizard
```

### 2. Level Up a Character

```python
from dnd_5e_core.data.loaders import level_up_character

# Level up to level 6
gandalf = level_up_character(gandalf, 6, verbose=True)

# Will display:
# 🎉 Gandalf levels up from level 5 to level 6!
#    ❤️  HP: +5 (38 total)
#    🔮 Spell slots updated
#    ✨ New features:
#       - [level 6 features]
```

### 3. Load a Monster

```python
from dnd_5e_core import load_monster

# Load a monster with its capabilities
dragon = load_monster('adult-red-dragon')

print(f"{dragon.name}: CR {dragon.challenge_rating}")
print(f"HP: {dragon.hit_points}, AC: {dragon.armor_class}")

# Display actions with conditions
for action in dragon.actions:
    if hasattr(action, 'effects') and action.effects:
        print(f"  {action.name}: {[e.name for e in action.effects]}")
```

### 4. Complete Combat

```python
from dnd_5e_core.combat import CombatSystem

# Create the combat system
combat = CombatSystem(verbose=True)

# Party and monsters
party = [gandalf, conan, gimli, bilbo]
monsters = [dragon, goblin1, goblin2]

# Initiative (as in main.py)
from random import randint

initiative_order = []
for char in party:
    dex_mod = char.abilities.get_modifier('dex')
    roll = randint(1, 20) + dex_mod
    initiative_order.append((char, roll))

for monster in monsters:
    dex_mod = monster.abilities.get_modifier('dex')
    roll = randint(1, 20) + dex_mod
    initiative_order.append((monster, roll))

initiative_order.sort(key=lambda x: x[1], reverse=True)
combatants = [c for c, _ in initiative_order]

# Combat round by round
for combatant in combatants:
    if combatant in party:
        combat.character_turn(combatant, party, monsters, party)
    else:
        combat.monster_turn(combatant, monsters, party, party, round_num=1)
```

---

## 🎓 Advanced Features

### Level Progression System

The package now includes a complete progression system using official data from the D&D 5e API.

#### Load Class Progression

```python
from dnd_5e_core.data.progression_loader import load_class_progression

wizard_prog = load_class_progression('wizard')

# Get info for level 5
level_5 = wizard_prog.get_level(5)

print(f"Proficiency bonus: +{level_5.prof_bonus}")
print(f"Features: {[f.name for f in level_5.features]}")
print(f"Spell slots: {level_5.spellcasting.spell_slots}")
```

#### Retrieve Spell Slots

```python
from dnd_5e_core.data.progression_loader import get_spell_slots_for_level

# For a level 7 Cleric
slots = get_spell_slots_for_level('cleric', 7)
# Returns: [0, 4, 3, 3, 1, 0, 0, 0, 0, 0]
#              ^  L1 L2 L3 L4
```

#### Class-Specific Features

```python
from dnd_5e_core.data.progression_loader import get_class_specific_value

# Barbarian - Number of rages at level 5
rage_count = get_class_specific_value('barbarian', 5, 'rage_count')
# Returns: 3

# Monk - Ki points at level 8
ki_points = get_class_specific_value('monk', 8, 'ki_points')
# Returns: 8

# Rogue - Sneak attack dice at level 7
sneak_attack = get_class_specific_value('rogue', 7, 'sneak_attack')
# Returns: {'dice_count': 4, 'dice_value': 6} (4d6)
```

### Defense and Attack Spells

```python
# Shield (+5 temporary AC)
from dnd_5e_core.combat import cast_shield
cast_shield(wizard)

# Hold Person (paralyze a humanoid)
from dnd_5e_core.combat import cast_hold_person, create_paralyzed_condition
cast_hold_person(wizard, ghoul)  # Paralyzes the ghoul if save failed
```

### Magic Items

```python
from dnd_5e_core.equipment import (
    create_ring_of_protection,
    create_wand_of_paralysis,
    HealingPotion,
    PotionRarity
)

# Ring of protection (+1 AC, +1 saves)
ring = create_ring_of_protection()
ring.attune(gandalf)
ring.apply_to_character(gandalf)

# Wand of paralysis
wand = create_wand_of_paralysis()
# 3 charges per day

# Healing potion
potion = HealingPotion("Potion of Healing", PotionRarity.COMMON, "2d4", 2, 50, 50)
# Heals 2d4+2 HP
```

### Conditions System

```python
from dnd_5e_core.combat import (
    create_paralyzed_condition,
    create_restrained_condition,
    create_poisoned_condition
)

# Apply a condition to a character
poisoned = create_poisoned_condition(dc_value=13, dc_type=AbilityType.CON)
poisoned.apply_to_character(conan)

# Apply a condition to a monster
paralyzed = create_paralyzed_condition(dc_value=15, dc_type=AbilityType.WIS)
paralyzed.apply_to_monster(goblin)

# Attempt to break free
if poisoned.attempt_save(conan):
    print(f"{conan.name} breaks free from the condition!")
```

### Encounter Generation

```python
from dnd_5e_core.mechanics.encounter_builder import select_monsters_by_encounter_table
from dnd_5e_core.data.collections import load_all_monsters

# Load all monsters
all_monsters = load_all_monsters()

# Generate an encounter for a level 5 group
monsters, encounter_type = select_monsters_by_encounter_table(
    encounter_level=5,
    available_monsters=all_monsters,
    allow_pairs=True
)

print(f"Type: {encounter_type}")
print(f"Monsters: {[m.name for m in monsters]}")
```

---

## 📊 Supported Classes

All 12 official D&D 5e classes are supported with full progression:

| Class | Hit Die | Spellcaster | Special Features |
|--------|---------|-------------|-------------------|
| **Barbarian** | d12 | No | Rage, Brutal Critical |
| **Bard** | d8 | Full | Bardic Inspiration |
| **Cleric** | d8 | Full | Channel Divinity |
| **Druid** | d8 | Full | Wild Shape |
| **Fighter** | d10 | No | Action Surge, Extra Attack |
| **Monk** | d8 | No | Ki Points, Martial Arts |
| **Paladin** | d10 | Half | Lay on Hands, Smite |
| **Ranger** | d10 | Half | Favored Enemy, Hunter's Mark |
| **Rogue** | d8 | No | Sneak Attack, Cunning Action |
| **Sorcerer** | d6 | Full | Sorcery Points, Metamagic |
| **Warlock** | d8 | Pact | Eldritch Invocations |
| **Wizard** | d6 | Full | Arcane Recovery, Spellbook |

---

## 🎮 Complete Examples

### Example 1: Character Creation and Progression

```python
from dnd_5e_core.data.loaders import simple_character_generator, level_up_character

# Create a level 1 Fighter
fighter = simple_character_generator(1, 'human', 'fighter', 'Conan')
print(f"{fighter.name}: {fighter.hit_points} HP, AC {fighter.armor_class}")

# Level up character
for level in range(2, 6):
    fighter = level_up_character(fighter, level, verbose=True)

# Level 5 Fighter with Extra Attack
print(f"Final: {fighter.name} level {fighter.level}")
```

### Example 2: Combat with Conditions

```python
# See: test_complete_combat_v4.py
# Complete script demonstrating:
# - Initiative
# - Defense spells (Shield, Mage Armor)
# - Attack spells (Hold Person, Entangle)
# - Bidirectional conditions (characters ↔ monsters)
# - Magic items
# - Healing potions
```

### Example 3: Automatic Progression

```python
# See: demo_progression_integration.py
# Demonstration of:
# - Creation with automatic spell slots
# - Level up with features
# - Test of all classes
```

---

## 📚 API Documentation

### Main Modules

- `dnd_5e_core.entities` - Character, Monster, Sprite
- `dnd_5e_core.combat` - CombatSystem, Conditions
- `dnd_5e_core.equipment` - Weapons, Armor, Magic Items, Potions
- `dnd_5e_core.spells` - Spell, SpellCaster
- `dnd_5e_core.mechanics` - Dice, Encounter Builder, Class Progression
- `dnd_5e_core.data` - Data loaders

### Detailed Documentation

- **CLASS_PROGRESSION_SYSTEM.md** - Class progression system
- **COMBAT_V4_GUIDE.md** - Combat system v4.0 guide
- **ENCOUNTER_BUILDER_IMPROVEMENTS.md** - Encounter system
- **CONDITIONS_SYSTEM.md** - Conditions system

---

## 🛠️ Useful Scripts

### Download Progression Data

```bash
cd dnd-5e-core
python download_class_progression.py
```

### Test Progression System

```bash
python test_class_progression.py
```

### Integration Demo

```bash
python demo_progression_integration.py
```

### Complete Combat Test

```bash
cd ../DnD5e-Scenarios
python test_complete_combat_v4.py
```

---

## 📝 Changelog

### v0.2.5 (January 2026) - Progression System ✨

**New Features**:
- ✨ Complete class progression system (levels 1-20)
- ✨ Spell slots based on official API data
- ✨ Class features by level
- ✨ Automatic `level_up_character()` function
- ✨ Support for class-specific features (rage, ki, sneak attack, etc.)
- ✨ Integration into `simple_character_generator()`

**Improvements**:
- 📈 Spell slots dynamically calculated from the API
- 📈 Correct proficiency bonuses by level
- 📈 HP gains based on the class's hit die

### v0.2.4 (January 2026) - Advanced Combat

**Features**:
- ⚔️ Initiative system (1d20 + DEX)
- ⚔️ Magic weapons with bonuses
- 🛡️ Defense spells (Shield, Mage Armor)
- ⚡ Spells affecting monsters (Hold Person, Entangle)
- 🔴 Bidirectional conditions (characters ↔ monsters)
- 💊 Magic items and healing potions

---

## 🤝 Contributing

To contribute to the project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🙏 Acknowledgements

- **D&D 5e API**: https://www.dnd5eapi.co
- **Wizards of the Coast**: For the D&D 5e SRD
- **Contributors**: Thanks to everyone who contributed!

---

## 📧 Contact

For questions or suggestions:
- GitHub Issues: https://github.com/votre-repo/dnd-5e-core/issues
- Documentation: https://github.com/votre-repo/dnd-5e-core/wiki

---

**Version**: 0.2.5  
**Date**: January 18, 2026  
**Status**: ✅ Production Ready

🎲 Happy gaming! ⚔️🐉✨
