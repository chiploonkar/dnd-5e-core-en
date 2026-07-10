# API Documentation - dnd-5e-core

Welcome to the complete documentation of the `dnd-5e-core` package.

## 📚 Table of Contents

### Main Documentation
- **[INDEX](./INDEX.md)** - Complete package overview

### Package Modules

#### Core Modules
1. **[entities](./entities.md)** - Characters and Monsters
   - `Sprite` - Base class
   - `Character` - Player characters
   - `Monster` - Creatures and monsters
   - `ExtendedMonsterLoader` - Extended monster loader

2. **[combat](./combat.md)** - Combat System
   - `CombatSystem` - Combat manager
   - `Action` - Combat actions
   - `Damage` - Damage calculation
   - `Condition` - States and conditions
   - `SpecialAbility` - Special abilities

3. **[mechanics](./mechanics.md)** - Game Rules
   - `DamageDice` - Dice system
   - `experience` - XP management
   - `challenge_rating` - CR calculation
   - `encounter_builder` - Encounter builder
   - `level_up` - Level up
   - `gold_rewards` - Gold rewards

4. **[equipment](./equipment.md)** - Equipment
   - `Weapon` - Weapons
   - `Armor` - Armors
   - `HealingPotion` - Healing potions
   - `SpeedPotion` - Speed potions
   - `StrengthPotion` - Strength potions
   - `Inventory` - Inventory management

5. **[spells](./spells.md)** - Magic
   - `Spell` - Spells
   - `SpellCaster` - Spellcasters
   - `spell_slots` - Spell slots
   - `cantrips` - Cantrips

6. **[data](./data.md)** - Data Loading
   - `load_monster()` - Load a monster
   - `load_spell()` - Load a spell
   - `load_weapon()` - Load a weapon
   - `load_armor()` - Load an armor
   - `api_client` - API client
   - `serialization` - Save/load

#### Customization Modules
7. **[races-classes-abilities](./races-classes-abilities.md)** - Characters
   - **races** - Races and sub-races
   - **classes** - Character classes
   - **abilities** - Ability scores and skills

#### Utility Modules
8. **[ui-utils](./ui-utils.md)** - UI and Utilities
   - **ui** - Colors and display
   - **utils** - Utility functions

## 🚀 Quick Start

### Installation
```bash
pip install dnd-5e-core
```

### Basic Example
```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster
from dnd_5e_core.combat import CombatSystem

# Create a hero
hero = Character.generate_random_character(level=5, class_name="fighter")

# Load a monster
goblin = load_monster("goblin")

# Initialize combat
combat = CombatSystem(verbose=True)

# Attack
combat.player_turn(hero, goblin, action_type="melee")
```

## 📖 Reading Guide

### Getting Started
1. Start with the [INDEX](./INDEX.md) for a general overview
2. Read [entities](./entities.md) to understand characters and monsters
3. Refer to [data](./data.md) to load data
4. Explore [combat](./combat.md) for combat mechanics

### Going Deeper
- [mechanics](./mechanics.md) - Understand D&D 5e rules
- [spells](./spells.md) - Complete magic system
- [equipment](./equipment.md) - Weapons, armors, and items

### Customizing
- [races-classes-abilities](./races-classes-abilities.md) - Create unique characters
- [ui-utils](./ui-utils.md) - Customize the display

## 🎯 Use Cases

### Create a Scenario
```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster
from dnd_5e_core.mechanics import generate_encounter_cr

# Create the party
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=5, class_name="cleric"),
]

# Generate an appropriate encounter
party_levels = [c.level for c in party]
min_cr, max_cr = generate_encounter_cr(party_levels, difficulty="medium")

# Load monsters
monsters = [
    load_monster("orc"),
    load_monster("orc"),
    load_monster("ogre"),
]
```

### Save a Game
```python
import json
from dnd_5e_core.entities import Character

# Create and save
hero = Character.generate_random_character(level=5, class_name="wizard")
with open("hero.json", "w") as f:
    json.dump(hero.to_dict(), f, indent=2)

# Load
with open("hero.json", "r") as f:
    data = json.load(f)
loaded_hero = Character.from_dict(data)
```

### Graphical Interface
```python
from dnd_5e_core.combat import CombatSystem

# Callback for custom interface
def display_message(msg):
    # Your display logic (pygame, tkinter, etc.)
    print(msg)

combat = CombatSystem(verbose=False, message_callback=display_message)
```

## 🔗 Useful Links

### Example Projects
- **DnD5e-Scenarios** - Complete narrative scenarios
  - https://github.com/codingame-team/DnD5e-Scenarios
  
- **DnD-5th-Edition-API** - Graphical frontends (PyQt, Pygame, ncurses)
  - https://github.com/codingame-team/DnD-5th-Edition-API

### D&D 5e Resources
- Official API: https://www.dnd5eapi.co
- SRD Rules: https://dnd.wizards.com/resources/systems-reference-document

## 📝 Notes

- All classes are documented with examples
- Examples are tested and functional
- The package is independent of any UI
- Compatible with Python 3.8+

## 🤝 Contribution

To contribute to the documentation:
1. Create an issue to discuss changes
2. Fork the repository
3. Create a pull request

See [CONTRIBUTING.md](https://github.com/codingame-team/dnd-5e-core/blob/main/CONTRIBUTING.md) for more details.

## 📄 License

MIT License - see [LICENSE](../../LICENSE)
