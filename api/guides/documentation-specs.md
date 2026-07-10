# Documentation dnd-5e-core - Complete Guide

## Created Documentation Files

This complete documentation covers all modules of the `dnd-5e-core` package.

### Documentation Structure

```
docs/api/
├── README.md                        # Entry point of the documentation
├── INDEX.md                         # Overview and quick start
├── entities.md                      # Characters and monsters
├── combat.md                        # Combat system
├── mechanics.md                     # Game rules (dice, XP, CR)
├── equipment.md                     # Weapons, armors, potions
├── spells.md                        # Magic system
├── data.md                          # Data loading
├── races-classes-abilities.md       # Races, classes, ability scores
└── ui-utils.md                      # UI and utilities
```

## Content by File

### README.md (Entry Point)
- Complete table of contents
- Reading guide
- Quick start
- Use cases
- Links to example projects

### INDEX.md (Overview)
- Complete package description
- Installation
- Quick start
- Package structure
- Usage examples
- Example projects

### entities.md
**Classes:**
- `Sprite` - Base class
- `Character` - Player characters
  - Creation (random, manual)
  - Combat (attacks, spells)
  - Equipment
  - Resting
  - Serialization
- `Monster` - Creatures
- `ExtendedMonsterLoader` - Extended bestiary

**Examples:**
- Creating an adventurer party
- Simple combat
- Save/load

### combat.md
**Classes:**
- `CombatSystem` - Combat manager
  - Player turn
  - Monster turn
  - Rewards
- `Action` - Actions of combat
- `Damage` - Damage calculation
- `Condition` - States (poisoned, paralyzed, etc.)
- `SpecialAbility` - Special abilities

**Examples:**
- Turn-based combat
- Combat with spells
- Combat with positioning (front/back)
- Condition management

**Implemented Rules:**
- Attacks (melee, ranged)
- Damage and critical hits
- Spells and saving throws
- Monster AI
- Rewards (XP, gold)

### mechanics.md
**Classes and Functions:**
- `DamageDice` - Dice system
  - Dice rolling
  - Max/average values
  - Comparison
- `experience` - XP management
  - XP by CR
  - Level calculation
  - XP thresholds
- `challenge_rating` - Power factor
  - Encounter generation
  - Party strength calculation
- `encounter_builder` - Encounter builder
- `level_up` - Level up
- `gold_rewards` - Gold rewards

**Examples:**
- Complete dice system
- XP and level management
- Encounter builder
- Reward system

**Constants:**
- XP by CR (0-30)
- XP thresholds by level (1-20)

### equipment.md
**Classes:**
- `Weapon` - Weapons
  - Properties (damage, range)
  - Equipment
- `Armor` - Armors
  - Categories (light, medium, heavy)
  - AC calculation
- `HealingPotion` - Healing potions
  - Rarities (common → supreme)
- `SpeedPotion` - Speed potions
- `StrengthPotion` - Strength potions
- `Inventory` - Inventory management
- `Equipment` - General equipment

**Examples:**
- Equipping a character
- Weapons by category
- Armors by category
- Potion system

### spells.md
**Classes:**
- `Spell` - Spells
  - Properties (level, school, etc.)
  - Damage by level
  - Healing by level
- `SpellCaster` - Spellcasters
  - Spell slots
  - Known/prepared spells
  - Spell save DC and attack bonus
- `spell_slots` - Slot management
- `cantrips` - Cantrips

**Examples:**
- Complete spellcaster
- School of magic
- Magical healing system
- Area of effect (AOE) spells

**Spells by Level:**
- Level 0 (cantrips)
- Levels 1-9 with examples

### data.md
**Loading Functions:**
- `load_monster()` - Load a monster
- `load_spell()` - Load a spell
- `load_weapon()` - Load a weapon
- `load_armor()` - Load an armor

**Collections:**
- `ExtendedMonsterLoader` - Complete bestiary
  - Monster search
  - Filtering by CR
  - Statistics

**Serialization:**
- Save/load characters
- Save/load parties
- JSON format

**Examples:**
- Loading all data for a scenario
- Building a bestiary
- Caching system

**Data Sources:**
- Official D&D 5e API
- Enriched local data
- Collections

### races-classes-abilities.md

**Races Module:**
- `Race` - Character races
  - Standard races (elf, dwarf, etc.)
  - Ability score increases
  - Racial traits
- `SubRace` - Sub-races
- `Trait` - Racial traits
- `Language` - Languages

**Classes Module:**
- `ClassType` - Character classes
  - 12 standard classes
  - Hit dice
  - Proficiencies
- `Proficiency` - Proficiencies
  - Types (armor, weapons, skills)
- `multiclass` - Multiclassing

**Abilities Module:**
- `Abilities` - Six ability scores
  - Values and modifiers
  - Random rolling
- `AbilityType` - Ability score types
- `Skill` - Skills
  - By ability score
- `Saving Throw` - Saving throws

**Examples:**
- Creating a complete character
- Displaying all races
- Displaying all classes

### ui-utils.md

**UI Module:**
- `Color` - ANSI colors
  - Standard colors
  - Bright colors
  - Background colors
  - Styles
- `color()` - Text colorization
- `cprint()` - Colored printing

**Utils Module:**
- `constants` - Game constants
  - Creature sizes
  - Creature types
  - Alignments
- `helpers` - Utility functions
  - Calculating modifiers
  - Formatting numbers
  - Validating dice
- `token_downloader` - Token downloader

**Examples:**
- Colored combat display
- Colored hit point bar
- Formatted character sheet
- Colored menu system
- Combat logger

## Using the Documentation

### For Beginners
1. Read `README.md` to understand the organization
2. Consult `INDEX.md` for the quick start
3. Follow the examples in `entities.md`
4. Experiment with `data.md`

### For Developers
1. Consult the specific module documentation
2. Use the examples as a base
3. Reference the constants and rules

### For Integrators
1. Read `combat.md` for the combat system
2. Consult `ui-utils.md` for the interface
3. Adapt the examples to your UI

## Documentation Statistics

- **10 Markdown files** complete
- **8 modules** documented
- **50+ classes and functions** explicated
- **100+ examples** of code
- **All D&D 5e rules** covered

## Quick Links

### Documentation
- [Entry Point](../index.md)
- [Overview](../index.md)

### Core Modules
- [Characters and Monsters](../core/entities.md)
- [Combat](../core/combat.md)
- [Game Rules](../core/rules-mechanics.md)

### Secondary Modules
- [Equipment](../core/equipment.md)
- [Spells](../core/magic-spells.md)
- [Data](../core/data-loading.md)

### Customization
- [Races, Classes, Abilities](../core/customization.md)
- [UI and Utilities](../core/ui-utilities.md)

## Reading Checklist

- [ ] README.md - Understand the structure
- [ ] INDEX.md - Quick start
- [ ] entities.md - Characters and monsters
- [ ] data.md - Load data
- [ ] combat.md - Combat system
- [ ] mechanics.md - Game rules
- [ ] spells.md - Magic system
- [ ] equipment.md - Weapons and armors
- [ ] races-classes-abilities.md - Customization
- [ ] ui-utils.md - Interface

## Level of Detail by File

| File | Lines | Classes | Examples | Level |
|---------|--------|---------|----------|--------|
| README.md | ~150 | - | 3 | Beginner |
| INDEX.md | ~250 | 10+ | 10+ | Beginner |
| entities.md | ~400 | 3 | 10+ | Intermediate |
| combat.md | ~450 | 5 | 12+ | Intermediate |
| mechanics.md | ~350 | 1+API | 15+ | Advanced |
| equipment.md | ~300 | 6 | 8+ | Beginner |
| spells.md | ~250 | 3 | 10+ | Intermediate |
| data.md | ~300 | 1+API | 8+ | Beginner |
| races-classes-abilities.md | ~300 | 9 | 6+ | Intermediate |
| ui-utils.md | ~250 | 2+API | 10+ | Beginner |

## Maintenance

To keep the documentation updated:

1. **New modules**: Create a new `.md` file in `docs/api/`
2. **New classes**: Add to the corresponding module file
3. **New examples**: Test and add to the appropriate sections
4. **Updates**: Synchronize with code changes

## Contributing

To contribute to the documentation:
1. Verify that all examples work
2. Maintain the same format as existing files
3. Add concrete and tested examples
4. Update this table of contents

---

**Documentation generated for dnd-5e-core v0.1.7+**
Last updated: January 2026
