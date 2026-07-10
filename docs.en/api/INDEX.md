# API Documentation dnd-5e-core

## Overview

`dnd-5e-core` is a complete Python package implementing the core rules of D&D 5th Edition.
The package is independent of any user interface and can be used with pygame, ncurses, web, or any other interface.

**Version:** 0.1.7  
**Author:** D&D Development Team  
**License:** MIT

## Installation

```bash
pip install dnd-5e-core
```

## Quick Start

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.mechanics import DamageDice
from dnd_5e_core.data import load_monster

# Load a monster
goblin = load_monster("goblin")

# Create a character
hero = Character.generate_random_character(level=5, class_name="fighter")

# Roll dice
damage = DamageDice("2d6+3")
result = damage.roll()
```

## Package Structure

The package is organized into logical modules:

### 📦 [entities](./entities.md)
Core classes for characters and monsters.
- `Sprite` - Base class for all beings
- `Character` - Player characters
- `Monster` - Creatures and monsters

### ⚔️ [combat](./combat.md)
Complete combat system.
- `CombatSystem` - Combat management
- `Action` - Combat actions
- `Damage` - Damage calculation
- `Condition` - States and conditions

### 🎲 [mechanics](./mechanics.md)
Game rules and mechanics.
- `DamageDice` - Dice rolling system
- `experience` - XP management
- `challenge_rating` - CR calculation
- `encounter_builder` - Encounter builder
- `level_up` - Level up

### 🎒 [equipment](./equipment.md)
Equipment and items.
- `Weapon` - Weapons
- `Armor` - Armors
- `Equipment` - General equipment
- `HealingPotion`, `SpeedPotion`, `StrengthPotion` - Potions

### ✨ [spells](./spells.md)
Magic and spells.
- `Spell` - Spells
- `SpellCaster` - Spellcasters
- `spell_slots` - Spell slots
- `cantrips` - Cantrips

### 👤 [races](./races.md)
Races and sub-races.
- `Race` - Character races
- `SubRace` - Sub-races
- `Trait` - Racial traits
- `Language` - Languages

### 🎓 [classes](./classes.md)
Character classes.
- `ClassType` - Character classes
- `Proficiency` - Proficiencies
- `multiclass` - Multiclassing

### 💪 [abilities](./abilities.md)
Ability scores and skills.
- `Abilities` - Six core ability scores
- `AbilityType` - Ability score types
- `skill` - Skills
- `saving_throw` - Saving throws

### 📊 [data](./data.md)
Data loading and management.
- `load_monster()` - Load a monster
- `load_spell()` - Load a spell
- `load_weapon()` - Load a weapon
- `load_armor()` - Load an armor
- `api_client` - D&D 5e API client
- `serialization` - Save/load

### 🎨 [ui](./ui.md)
UI utilities.
- `Color` - Colors
- `color()` - Text colorization
- `cprint()` - Colored printing

### 🔧 [utils](./utils.md)
Miscellaneous utilities.
- `constants` - Game constants
- `helpers` - Utility functions
- `token_downloader` - Token downloader

## Usage Examples

### Create a Character

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.races import Race
from dnd_5e_core.classes import ClassType
from dnd_5e_core.abilities import Abilities

# Method 1: Random generation
hero = Character.generate_random_character(level=3, class_name="wizard")

# Method 2: Manual creation
abilities = Abilities(str=10, dex=14, con=12, int=16, wis=13, cha=8)
race = Race.load_from_json("elf")
char_class = ClassType.load_from_json("wizard")

wizard = Character(
    id=1,
    name="Gandalf",
    abilities=abilities,
    race=race,
    classe=char_class,
    level=5
)
```

### Load a Monster

```python
from dnd_5e_core.data import load_monster

# Load from API
dragon = load_monster("ancient-red-dragon")

# Display statistics
print(f"CR: {dragon.challenge_rating}")
print(f"HP: {dragon.hit_points}")
print(f"AC: {dragon.armor_class}")
```

### Manage Combat

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Create the party
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="cleric"),
]

# Load monsters
monsters = [
    load_monster("goblin"),
    load_monster("goblin"),
    load_monster("goblin"),
]

# Initialize combat
combat = CombatSystem(party, monsters)

# Player turn
target = monsters[0]
combat.player_turn(party[0], target, action_type="melee")

# Monster turn
combat.monster_turn(monsters[0], party)
```

### Roll Dice

```python
from dnd_5e_core.mechanics import DamageDice

# Damage dice
damage = DamageDice("2d6+3")
result = damage.roll()
print(f"Damage: {result}")

# Multiple dice
dice = DamageDice("3d8+2d6+5")
total = dice.roll()
```

### Calculate Encounter

```python
from dnd_5e_core.mechanics import generate_encounter_cr

# Party of 4 level 5 characters
party_levels = [5, 5, 5, 5]

# Calculate appropriate CR
min_cr, max_cr = generate_encounter_cr(party_levels, difficulty="medium")
print(f"Recommended CR: {min_cr} - {max_cr}")
```

## Example Projects

### DnD5e-Scenarios
Examples of complete scenarios using the package.
- Narrative scenarios with combat
- Multi-character party management
- Game save/load
- https://github.com/codingame-team/DnD5e-Scenarios

### DnD-5th-Edition-API
Graphical frontends (PyQt, Pygame, ncurses).
- PyQt interface with tavern manager
- Pygame version with dungeon
- ncurses version for terminal
- https://github.com/codingame-team/DnD-5th-Edition-API

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](../../CONTRIBUTING.md) for more details.

## License

MIT License - see [LICENSE](../../LICENSE) for more details.

## Support

- Issues: https://github.com/codingame-team/dnd-5e-core/issues
- Documentation: https://github.com/codingame-team/dnd-5e-core/docs
