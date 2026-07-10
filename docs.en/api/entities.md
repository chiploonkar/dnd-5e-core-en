# Module: entities

## Overview

The `entities` module contains the core classes to represent player characters and monsters in D&D 5e.

## Core Classes

### Sprite

Base class for all living beings (characters and monsters).

**Import:**
```python
from dnd_5e_core.entities import Sprite
```

**Properties:**
- `id: int` - Unique identifier
- `name: str` - Entity name
- `position: tuple[int, int]` - Position (x, y) for UI
- `hit_points: int` - Current hit points
- `max_hit_points: int` - Maximum hit points
- `armor_class: int` - Armor class
- `speed: int` - Movement speed

**Methods:**
- `is_alive() -> bool` - Checks if the entity is alive
- `take_damage(amount: int)` - Deals damage
- `heal(amount: int)` - Heals the entity

---

### Character

Represents a player character with all their D&D 5e attributes.

**Import:**
```python
from dnd_5e_core.entities import Character
```

**Creation:**

```python
# Method 1: Random generation
hero = Character.generate_random_character(
    level=5,
    class_name="wizard"
)

# Method 2: Manual creation
from dnd_5e_core.abilities import Abilities
from dnd_5e_core.races import Race
from dnd_5e_core.classes import ClassType

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

**Main Properties:**
- `name: str` - Character name
- `level: int` - Character level
- `race: Race` - Character race
- `classe: ClassType` - Character class
- `abilities: Abilities` - The 6 ability scores (STR, DEX, CON, INT, WIS, CHA)
- `hit_points: int` - Current hit points
- `max_hit_points: int` - Maximum hit points
- `armor_class: int` - Armor class
- `proficiency_bonus: int` - Proficiency bonus
- `experience_points: int` - Experience points
- `inventory: Inventory` - Equipment inventory

**Core Methods:**

#### Creation and Management
```python
# Generate a random character
char = Character.generate_random_character(level=3, class_name="fighter")

# Level up
char.level_up()

# Gain XP
char.gain_xp(300)
```

#### Combat
```python
# Attack
char.melee_attack(monster)
char.ranged_attack(monster)

# Cast a spell
char.cast_spell(spell, target)

# Saving throws
success = char.saving_throw(dc_type="dex", dc_value=15)
```

#### Equipment
```python
# Equip a weapon
from dnd_5e_core.data import load_weapon
weapon = load_weapon("longsword")
char.equip_weapon(weapon)

# Equip an armor
from dnd_5e_core.data import load_armor
armor = load_armor("chain-mail")
char.equip_armor(armor)

# Use a potion
from dnd_5e_core.equipment import HealingPotion, PotionRarity
potion = HealingPotion(
    id=1,
    name="Potion of Healing",
    rarity=PotionRarity.COMMON,
    hit_dice="2d4",
    bonus=2,
    min_cost=50,
    max_cost=50
)
hp_gained = char.drink_potion(potion)
```

#### Spells (for spellcasters)
```python
# Prepare spells
char.prepare_spells([spell1, spell2, spell3])

# Cast a spell
char.cast_spell(spell, target, slot_level=1)

# Check available spell slots
slots = char.spell_slots
```

#### Resting
```python
# Short rest
char.short_rest()

# Long rest
char.long_rest()
```

#### Serialization
```python
# Save
char_data = char.to_dict()
with open("character.json", "w") as f:
    json.dump(char_data, f)

# Load
with open("character.json", "r") as f:
    char_data = json.load(f)
char = Character.from_dict(char_data)
```

---

### Monster

Represents a creature or a monster.

**Import:**
```python
from dnd_5e_core.entities import Monster
from dnd_5e_core.data import load_monster
```

**Creation:**

```python
# Load from data
goblin = load_monster("goblin")
dragon = load_monster("ancient-red-dragon")

# Create a copy
goblin2 = copy(goblin)
goblin2.hp_roll()  # Reroll HP
```

**Main Properties:**
- `index: str` - API identifier (e.g. "goblin")
- `name: str` - Display name
- `abilities: Abilities` - The 6 ability scores
- `armor_class: int` - AC
- `hit_points: int` - Current HP
- `max_hit_points: int` - Maximum HP
- `hit_dice: str` - Hit dice (e.g. "2d8+2")
- `challenge_rating: float` - Challenge rating
- `xp: int` - XP awarded on defeat
- `speed: int` - Speed
- `actions: List[Action]` - Combat actions
- `sc: SpellCaster` - Spellcaster (optional)
- `sa: List[SpecialAbility]` - Special abilities (optional)

**Core Methods:**

```python
# Check state
if monster.is_alive:
    print(f"{monster.name} is alive")

# Reroll HP
monster.hp_roll()

# Saving throws
success = monster.saving_throw(dc_type="con", dc_value=14)

# Cast a healing spell (if spellcaster)
if monster.is_spell_caster:
    hp_gained = monster.cast_heal(spell, slot_level=1, targets=[ally])

# Cast an attack spell
if monster.is_spell_caster:
    messages, damage = monster.cast_attack(target, spell)
```

**Calculated Properties:**

```python
# Effective level
effective_level = monster.level

# Spell DC
if monster.is_spell_caster:
    dc = monster.dc_value
```

---

## Utility Classes

### ExtendedMonsterLoader

Loader for extended monsters (complete bestiary).

**Import:**
```python
from dnd_5e_core.entities import ExtendedMonsterLoader
```

**Usage:**

```python
loader = ExtendedMonsterLoader()

# Load all implemented monsters
monsters = loader.load_implemented_monsters()

# Search for monsters
goblins = loader.search_monsters(
    name_contains="goblin",
    min_cr=0,
    max_cr=2
)

# Load a specific monster
goblin_boss = loader.load_monster_by_index("goblin-boss")

# Get stats
stats = loader.get_monster_stats()
print(f"Total: {stats['total']}")
print(f"Implemented: {stats['implemented']}")
```

---

## Complete Examples

### Create a Party of Adventurers

```python
from dnd_5e_core.entities import Character

party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=5, class_name="cleric"),
    Character.generate_random_character(level=5, class_name="rogue"),
]

# Display the party
for hero in party:
    print(f"{hero.name} - {hero.classe.name} level {hero.level}")
    print(f"  HP: {hero.hit_points}/{hero.max_hit_points}")
    print(f"  AC: {hero.armor_class}")
```

### Simple Combat

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Create the combatants
hero = Character.generate_random_character(level=3, class_name="fighter")
goblin = load_monster("goblin")

# Combat
while hero.is_alive and goblin.is_alive:
    # Hero's turn
    damage = hero.melee_attack(goblin)
    print(f"{hero.name} deals {damage} damage to {goblin.name}")
    
    if not goblin.is_alive:
        print(f"{goblin.name} is defeated!")
        break
    
    # Monster's turn (simplified)
    from random import randint
    action = goblin.actions[0]
    attack_roll = randint(1, 20) + action.attack_bonus
    
    if attack_roll >= hero.armor_class:
        damage = action.damage.roll()
        hero.hit_points -= damage
        print(f"{goblin.name} deals {damage} damage to {hero.name}")
    
    if not hero.is_alive:
        print(f"{hero.name} is defeated!")
```

### Save and Load

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

print(f"Loaded hero: {loaded_hero.name}")
```

---

## See Also

- [combat](./combat.md) - Combat system
- [mechanics](./mechanics.md) - Game rules
- [equipment](./equipment.md) - Equipment
- [spells](./spells.md) - Spells
- [data](./data.md) - Data loading
