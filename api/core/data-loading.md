# Module: data

## Overview

The `data` module provides loading and serialization functions for all game data: monsters, spells, weapons, armors, races, classes.

**Important:** All `load_*()` functions now return class objects (Monster, Spell, Weapon, Armor) instead of JSON dictionaries. This allows direct use of the methods and properties of these objects.

## Loading Functions

### load_monster()

Loads a monster from JSON data and returns a `Monster` object.

**Import:**
```python
from dnd_5e_core.data import load_monster
```

**Signature:**
```python
def load_monster(index: str) -> Optional[Monster]
```

**Usage:**
```python
# Load a base monster
goblin = load_monster("goblin")
print(f"{goblin.name} - CR {goblin.challenge_rating}")
print(f"HP: {goblin.hit_points}/{goblin.max_hit_points}")
print(f"AC: {goblin.armor_class}")

# Use the methods of the Monster object
goblin.hp_roll()  # Reroll HP for variation
if goblin.is_spell_caster:
    print(f"DC: {goblin.dc_value}")

# Powerful monsters
dragon = load_monster("ancient-red-dragon")
lich = load_monster("lich")
```

**Returns:**
- A `Monster` object with all its properties and methods
- `None` if the monster is not found

**Available Monsters:**
- Low-level creatures: goblin, kobold, orc, skeleton, zombie
- Medium creatures: ogre, troll, owlbear, wyvern
- Powerful creatures: giant, dragon, beholder, lich

---

### load_spell()

Loads a spell from JSON data and returns a `Spell` object.

**Import:**
```python
from dnd_5e_core.data import load_spell
```

**Signature:**
```python
def load_spell(index: str) -> Optional[Spell]
```

**Usage:**
```python
# Combat spells
fireball = load_spell("fireball")
print(f"{fireball.name} - Level {fireball.level}")
print(f"School: {fireball.school}")
print(f"Range: {fireball.range} ft")

# Check properties
if fireball.is_damaging:
    print("This spell deals damage")
if fireball.requires_save:
    print(f"Saving throw: {fireball.dc_type}")

# Other spells
magic_missile = load_spell("magic-missile")
cure_wounds = load_spell("cure-wounds")
shield = load_spell("shield")
```

**Returns:**
- A `Spell` object with all its properties and methods
- `None` if the spell is not found

---

### load_weapon()

Loads a weapon from JSON data and returns a `Weapon` object.

**Import:**
```python
from dnd_5e_core.data import load_weapon
```

**Signature:**
```python
def load_weapon(index: str) -> Optional[Weapon]
```

**Usage:**
```python
# Melee weapons
longsword = load_weapon("longsword")
print(f"{longsword.name} - {longsword.damage_dice}")
print(f"Type: {longsword.damage_type}")

# Check properties
if longsword.is_melee:
    print("Melee weapon")
if longsword.is_martial:
    print("Martial weapon")

# Ranged weapons
longbow = load_weapon("longbow")
if longbow.weapon_range:
    print(f"Range: {longbow.weapon_range}")
```

**Returns:**
- A `Weapon` object with all its properties and methods
- `None` if the weapon is not found

---

### load_armor()

Loads an armor from JSON data and returns an `Armor` object.

**Import:**
```python
from dnd_5e_core.data import load_armor
```

**Signature:**
```python
def load_armor(index: str) -> Optional[Armor]
```

**Usage:**
```python
# Light armors
leather = load_armor("leather-armor")
studded = load_armor("studded-leather-armor")

# Medium armors
chain_shirt = load_armor("chain-shirt")
scale_mail = load_armor("scale-mail")

# Heavy armors
chain_mail = load_armor("chain-mail")
plate = load_armor("plate-armor")
```

---

## Loading by Collections

### Monster Collections

**Import:**
```python
from dnd_5e_core.entities import ExtendedMonsterLoader
```

**Usage:**
```python
loader = ExtendedMonsterLoader()

# Load all implemented monsters
all_monsters = loader.load_implemented_monsters()
print(f"Available monsters: {len(all_monsters)}")

# Search for monsters
goblins = loader.search_monsters(
    name_contains="goblin",
    min_cr=0,
    max_cr=2
)

dragons = loader.search_monsters(
    name_contains="dragon",
    min_cr=10,
    max_cr=30
)

# Load a specific monster
boss = loader.load_monster_by_index("ancient-red-dragon")

# Get statistics
stats = loader.get_monster_stats()
print(f"Total monsters: {stats['total']}")
print(f"Implemented: {stats['implemented']}")
```

---

## Serialization

### Save and Load Characters

**Import:**
```python
from dnd_5e_core.entities import Character
import json
```

**Save:**
```python
# Create a character
hero = Character.generate_random_character(level=5, class_name="wizard")

# Convert to dictionary
char_data = hero.to_dict()

# Save to a JSON file
with open("hero.json", "w") as f:
    json.dump(char_data, f, indent=2)

print("Character saved!")
```

**Load:**
```python
# Load from a JSON file
with open("hero.json", "r") as f:
    char_data = json.load(f)

# Create the character from the data
hero = Character.from_dict(char_data)

print(f"Character loaded: {hero.name} - {hero.classe.name} level {hero.level}")
```

---

### Save a Party

```python
import json
from dnd_5e_core.entities import Character

# Create a party
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=5, class_name="cleric"),
    Character.generate_random_character(level=5, class_name="rogue"),
]

# Save
party_data = {
    "party": [char.to_dict() for char in party]
}

with open("party.json", "w") as f:
    json.dump(party_data, f, indent=2)

# Load
with open("party.json", "r") as f:
    party_data = json.load(f)

loaded_party = [Character.from_dict(char_data) for char_data in party_data["party"]]

print(f"Loaded party: {len(loaded_party)} members")
for hero in loaded_party:
    print(f"  - {hero.name} ({hero.classe.name} {hero.level})")
```

---

## API Client

Direct access to the D&D 5e API.

**Import:**
```python
from dnd_5e_core.data import api_client
```

**Usage:**
```python
# Direct query to the API
monster_data = api_client.get_monster("goblin")
spell_data = api_client.get_spell("fireball")

# Note: The load_* functions are recommended because they include
# enriched local data and manage cache
```

---

## Complete Examples

### Load all data for a scenario

```python
from dnd_5e_core.data import load_monster, load_spell, load_weapon, load_armor
from dnd_5e_core.entities import Character

# Create the party
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=5, class_name="cleric"),
]

# Equip the party
longsword = load_weapon("longsword")
party[0].equip_weapon(longsword)

plate = load_armor("plate-armor")
party[0].equip_armor(plate)

# Prepare spells
fireball = load_spell("fireball")
party[1].prepare_spells([fireball])

cure_wounds = load_spell("cure-wounds")
party[2].prepare_spells([cure_wounds])

# Load monsters
encounter = [
    load_monster("orc"),
    load_monster("orc"),
    load_monster("ogre"),
]

print("Party ready for adventure!")
print(f"  {len(party)} heroes")
print(f"  {len(encounter)} monsters")
```

### Build a bestiary

```python
from dnd_5e_core.entities import ExtendedMonsterLoader

loader = ExtendedMonsterLoader()

# Load by category
categories = {
    "Weak (CR 0-1)": loader.search_monsters(min_cr=0, max_cr=1),
    "Medium (CR 2-5)": loader.search_monsters(min_cr=2, max_cr=5),
    "Strong (CR 6-10)": loader.search_monsters(min_cr=6, max_cr=10),
    "Very Strong (CR 11+)": loader.search_monsters(min_cr=11, max_cr=30),
}

print("📚 D&D 5e BESTIARY")
for category, monsters in categories.items():
    print(f"\n{category}:")
    for monster in sorted(monsters, key=lambda m: m.challenge_rating):
        print(f"  - {monster.name} (CR {monster.challenge_rating}, {monster.xp} XP)")
```

### Cache System

```python
from dnd_5e_core.data import load_monster
import time

# First load (from file/API)
start = time.time()
dragon1 = load_monster("ancient-red-dragon")
first_load = time.time() - start

# Second load (from cache)
start = time.time()
dragon2 = load_monster("ancient-red-dragon")
cached_load = time.time() - start

print(f"First load: {first_load:.4f}s")
print(f"Load from cache: {cached_load:.4f}s")
print(f"Speedup: {first_load / cached_load:.1f}x")
```

---

## Data Sources

The package uses several sources:

### 1. Official D&D 5e API
- URL: https://www.dnd5eapi.co
- Base data for monsters, spells, equipment
- Local cache for performance

### 2. Enriched Local Data
- Extended monsters (complete bestiary)
- Custom statistics
- JSON files in `data/`

### 3. Collections
- Lists of monsters by category
- Character templates
- Pre-configured equipment

---

## Data Files

Directory structure of `data/`:

```
data/
├── monsters/
│   ├── monsters.json           # Base monsters
│   └── bestiary-sublist-data.json  # Extended monsters
├── spells/
│   └── spells.json
├── equipment/
│   ├── weapons.json
│   └── armor.json
├── races/
│   └── races.json
└── classes/
    └── classes.json
```

---

## See Also

- [entities](entities.md) - Characters and monsters
- [equipment](equipment.md) - Weapons and armors
- [spells](magic-spells.md) - Spells
- [combat](combat.md) - Combat system
