# Modules: races, classes, abilities

## Module: races

### Overview
Management of D&D 5e character races and sub-races.

### Race

**Import:**
```python
from dnd_5e_core.races import Race
```

**Available Races:**
- Dwarf
- Elf
- Halfling
- Human
- Dragonborn
- Gnome
- Half-Elf
- Half-Orc
- Tiefling

**Usage:**
```python
from dnd_5e_core.races import Race

# Load a race
elf_race = Race.load_from_json("elf")
dwarf_race = Race.load_from_json("dwarf")

print(f"{elf_race.name}")
print(f"  Bonus: +{elf_race.ability_bonuses}")
print(f"  Speed: {elf_race.speed} feet")
print(f"  Languages: {elf_race.languages}")
```

### SubRace

**Sub-races:**
- High Elf / Wood Elf
- Mountain Dwarf / Hill Dwarf
- Lightfoot Halfling / Stout Halfling

### Trait

Special racial traits.

**Example:**
```python
# Traits are automatically loaded with the race
elf = Race.load_from_json("elf")
for trait in elf.traits:
    print(f"- {trait.name}: {trait.desc}")
```

### Language

Known languages.

**Standard Languages:**
- Common
- Elvish
- Dwarvish
- Draconic
- etc.

---

## Module: classes

### Overview
Character classes with level progression.

### ClassType

**Import:**
```python
from dnd_5e_core.classes import ClassType
```

**Available Classes:**
- Barbarian
- Bard
- Cleric
- Druid
- Fighter
- Monk
- Paladin
- Ranger
- Rogue
- Sorcerer
- Warlock
- Wizard

**Usage:**
```python
from dnd_5e_core.classes import ClassType

# Load a class
fighter = ClassType.load_from_json("fighter")
wizard = ClassType.load_from_json("wizard")

print(f"{fighter.name}")
print(f"  Hit Die: d{fighter.hit_die}")
print(f"  Proficiencies: {fighter.proficiencies}")
```

### Proficiency

Proficiencies and skills.

**Types:**
```python
from dnd_5e_core.classes import ProfType

ProfType.ARMOR     # Armor
ProfType.WEAPON    # Weapons
ProfType.TOOL      # Tools
ProfType.SKILL     # Skills
ProfType.SAVING_THROW  # Saving throws
```

**Example:**
```python
fighter = ClassType.load_from_json("fighter")

# Armor proficiencies
armor_profs = [p for p in fighter.proficiencies if p.type == ProfType.ARMOR]
print("Armor proficiencies:")
for prof in armor_profs:
    print(f"  - {prof.name}")
```

### Multiclass

Multiclassing management.

**Example:**
```python
from dnd_5e_core.entities import Character

# Create a multiclassed character
hero = Character.generate_random_character(level=3, class_name="fighter")

# Add a level in another class
# (To be implemented according to your specific needs)
```

---

## Module: abilities

### Overview
The six core ability scores and their modifiers.

### Abilities

**Import:**
```python
from dnd_5e_core.abilities import Abilities, AbilityType
```

**Creation:**
```python
# Method 1: Specific values
abilities = Abilities(
    str=16,  # Strength
    dex=14,  # Dexterity
    con=13,  # Constitution
    int=12,  # Intelligence
    wis=10,  # Wisdom
    cha=8    # Charisma
)

# Method 2: Random rolling
abilities = Abilities.roll_abilities()

# Access to values
print(f"Strength: {abilities.str}")
print(f"Strength modifier: {abilities.str_mod}")

# All modifiers
print(f"STR: {abilities.str} ({abilities.str_mod:+d})")
print(f"DEX: {abilities.dex} ({abilities.dex_mod:+d})")
print(f"CON: {abilities.con} ({abilities.con_mod:+d})")
print(f"INT: {abilities.int} ({abilities.int_mod:+d})")
print(f"WIS: {abilities.wis} ({abilities.wis_mod:+d})")
print(f"CHA: {abilities.cha} ({abilities.cha_mod:+d})")
```

### AbilityType

Ability score types.

```python
from dnd_5e_core.abilities import AbilityType

AbilityType.STRENGTH      # Strength
AbilityType.DEXTERITY     # Dexterity
AbilityType.CONSTITUTION  # Constitution
AbilityType.INTELLIGENCE  # Intelligence
AbilityType.WISDOM        # Wisdom
AbilityType.CHARISMA      # Charisma
```

### Skill

Skills based on ability scores.

**Skills by Ability Score:**

**Strength:**
- Athletics

**Dexterity:**
- Acrobatics
- Sleight of Hand
- Stealth

**Intelligence:**
- Arcana
- History
- Investigation
- Nature
- Religion

**Wisdom:**
- Animal Handling
- Insight
- Medicine
- Perception
- Survival

**Charisma:**
- Deception
- Intimidation
- Performance
- Persuasion

**Example:**
```python
from dnd_5e_core.entities import Character

hero = Character.generate_random_character(level=5, class_name="rogue")

# Skill check
perception_bonus = hero.abilities.wis_mod + hero.proficiency_bonus
perception_roll = randint(1, 20) + perception_bonus

if perception_roll >= 15:
    print("You spot the ambush!")
```

### Saving Throw

Saving throws.

**Example:**
```python
from dnd_5e_core.entities import Character

hero = Character.generate_random_character(level=5, class_name="wizard")

# Saving throw
dc_value = 15
success = hero.saving_throw(dc_type="dex", dc_value=dc_value)

if success:
    print("Saving throw succeeded!")
else:
    print("Saving throw failed!")
```

---

## Complete Examples

### Create a Complete Character

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.abilities import Abilities
from dnd_5e_core.races import Race
from dnd_5e_core.classes import ClassType

# Create the components
abilities = Abilities(str=16, dex=14, con=15, int=8, wis=10, cha=12)
race = Race.load_from_json("dwarf")
char_class = ClassType.load_from_json("fighter")

# Create the character
hero = Character(
    id=1,
    name="Thorin Oakenshield",
    abilities=abilities,
    race=race,
    classe=char_class,
    level=5
)

print(f"{hero.name}")
print(f"  Race: {hero.race.name}")
print(f"  Class: {hero.classe.name} level {hero.level}")
print(f"  HP: {hero.max_hit_points}")
print(f"  AC: {hero.armor_class}")
```

### Display All Races

```python
from dnd_5e_core.races import Race

races = ["dwarf", "elf", "halfling", "human", "dragonborn", 
         "gnome", "half-elf", "half-orc", "tiefling"]

print("AVAILABLE RACES:\n")
for race_name in races:
    race = Race.load_from_json(race_name)
    print(f"{race.name}")
    print(f"  Speed: {race.speed} feet")
    print(f"  Languages: {len(race.languages)}")
    print(f"  Traits: {len(race.traits)}")
    print()
```

### Display All Classes

```python
from dnd_5e_core.classes import ClassType

classes = ["barbarian", "bard", "cleric", "druid", "fighter",
           "monk", "paladin", "ranger", "rogue", "sorcerer",
           "warlock", "wizard"]

print("AVAILABLE CLASSES:\n")
for class_name in classes:
    char_class = ClassType.load_from_json(class_name)
    print(f"{char_class.name}")
    print(f"  Hit Die: d{char_class.hit_die}")
    print(f"  Primary Ability: {char_class.primary_ability}")
    print()
```

---

## See Also

- [entities](./entities.md) - Characters using races and classes
- [mechanics](./mechanics.md) - Modifier calculations
- [combat](./combat.md) - Use of skills in combat
