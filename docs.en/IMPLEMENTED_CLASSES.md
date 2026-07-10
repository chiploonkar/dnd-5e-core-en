# Implemented Classes in dnd-5e-core

This document lists all classes and functions implemented in the `dnd-5e-core` package that have been migrated from `dao_classes.py`.

## Migration Summary

All domain classes from `dao_classes.py` have been migrated to `dnd-5e-core` by separating the business logic from the presentation (UI).

### Main Classes Already Migrated

#### Entities (entities/)
- ✅ `Sprite` - Base class for entities with coordinates/position
- ✅ `Monster` - Class representing monsters
- ✅ `Character` - Class representing player characters

#### Equipment (equipment/)
- ✅ `Cost` - Cost of an item
- ✅ `Equipment` - Base class for equipment
- ✅ `EquipmentCategory` - Equipment category
- ✅ `Weapon` / `WeaponData` - Weapons
- ✅ `Armor` / `ArmorData` - Armor
- ✅ `Potion` - Base class for potions
- ✅ `HealingPotion` - Healing potion
- ✅ `SpeedPotion` - Speed potion
- ✅ `StrengthPotion` - Strength potion
- ✅ `PotionRarity` - Potion rarity
- ✅ `Inventory` - **NEWLY IMPLEMENTED**

#### Races (races/)
- ✅ `Language` - Languages
- ✅ `Trait` - Racial traits
- ✅ `SubRace` - Subraces
- ✅ `Race` - Races

#### Classes (classes/)
- ✅ `ProfType` - Proficiency types
- ✅ `Proficiency` - Proficiencies
- ✅ `ClassType` - Character classes
- ✅ `Feature` - Class features
- ✅ `Level` - Class level
- ✅ `BackGround` - Backgrounds
- ✅ **Multiclassing** - **NEWLY IMPLEMENTED**
  - `MulticlassRequirements`
  - `MULTICLASS_PREREQUISITES`
  - `can_multiclass_into()`
  - `can_multiclass_from()`
  - `calculate_spell_slots_multiclass()`
  - `get_multiclass_proficiencies()`
  - `calculate_hit_points_multiclass()`

#### Abilities (abilities/)
- ✅ `AbilityType` - Ability types
- ✅ `Abilities` - The 6 abilities
- ✅ **Skills** - **NEWLY IMPLEMENTED**
  - `SkillType` - Skill types
  - `Skill` - Skills
  - `get_all_skills()`
- ✅ **Saving Throws** - **NEWLY IMPLEMENTED**
  - `SavingThrowType` - Saving throw types
  - `SavingThrow` - Saving throws
  - `make_saving_throw()`

#### Spells (spells/)
- ✅ `Spell` - Spells
- ✅ `SpellCaster` - Spellcaster
- ✅ `AreaOfEffect` - Area of effect
- ✅ **Spell Slots** - **NEWLY IMPLEMENTED**
  - `SpellSlots` - Spell slot management
  - `get_spell_slots_by_level()`
- ✅ **Cantrips** - **NEWLY IMPLEMENTED**
  - `is_cantrip()`
  - `get_cantrip_damage_scaling()`
  - `get_cantrip_damage()`
  - `filter_cantrips()`
  - `get_cantrips_known_by_level()`
  - `DAMAGE_CANTRIPS`
  - `UTILITY_CANTRIPS`

#### Combat (combat/)
- ✅ `Damage` - Damage
- ✅ `DamageType` - Damage types
- ✅ `Condition` - Conditions/states
- ✅ `ActionType` - Action types
- ✅ `Action` - Actions
- ✅ `SpecialAbility` - Special abilities
- ✅ `RangeType` - Range types
- ✅ `CategoryType` - Category types

#### Game Mechanics (mechanics/)
- ✅ `DamageDice` - Damage dice
- ✅ **Experience System** - **NEWLY IMPLEMENTED**
  - `XP_LEVELS` - XP thresholds per level
  - `get_level_from_xp()`
  - `get_xp_for_level()`
  - `get_xp_to_next_level()`
  - `should_level_up()`
  - `calculate_proficiency_bonus()`
  - `get_cr_xp()`
- ✅ **Level Up System** - **NEWLY IMPLEMENTED**
  - `LevelUpResult` - Level up result
  - `calculate_hp_gain()`
  - `can_level_up()`
  - `get_ability_score_improvement_levels()`
  - `is_ability_score_improvement_level()`
  - `perform_level_up()`
- ✅ **Challenge Rating** - **NEWLY IMPLEMENTED**
  - `ChallengeRating` - Challenge rating
  - `EncounterDifficulty` - Encounter difficulty
  - `get_xp_thresholds_for_level()`
  - `calculate_encounter_difficulty()`
  - `get_appropriate_cr_range()`

#### Utilities (utils/)
- ✅ `token_downloader` - Token downloader
- ✅ **Helpers** - **NEWLY IMPLEMENTED**
  - `roll_dice()`
  - `roll_with_advantage()`
  - `roll_with_disadvantage()`
  - `calculate_modifier()`
  - `calculate_ac()`
  - `calculate_attack_bonus()`
  - `calculate_save_dc()`
  - `is_critical_hit()`
  - `is_critical_fail()`
  - `apply_resistance()`
  - `apply_vulnerability()`
  - `calculate_spell_attack_bonus()`
  - `get_random_ability_scores()`
  - `get_standard_array()`
  - `calculate_carrying_capacity()`
  - `calculate_jump_distance()`
  - `format_modifier()`
  - `format_dice()`
- ✅ **Constants** - **NEWLY IMPLEMENTED**
  - Game constants for D&D 5e
  - Default values
  - Reference tables

#### Data (data/)
- ✅ `loader` - Data loading
- ✅ `collections` - Data collections
- ✅ **API Client** - **NEWLY IMPLEMENTED**
  - `DndApiClient` - Client to access the D&D 5e API
  - `get_default_client()`
  - `set_default_client()`
- ✅ **Serialization** - **NEWLY IMPLEMENTED**
  - `DndJSONEncoder` - Custom JSON encoder
  - `to_json()`
  - `from_json()`
  - `save_to_file()`
  - `load_from_file()`
  - `serialize_character()`
  - `deserialize_character()`
  - `save_character()`
  - `load_character()`
  - `save_party()`
  - `load_party()`
  - `create_backup()`

## Separated UI Classes

The following classes have been removed from the domain package and must be managed by the frontends (pygame, ncurses, etc.):

- `color` - Terminal colors → in `dnd_5e_core.ui`
- `draw()` and `draw_effect()` methods of `Sprite` → to be managed in the frontend's `game_entity.py`

## Usage

### Importing new classes

```python
# Experience and Level Up
from dnd_5e_core.mechanics import (
    get_level_from_xp,
    should_level_up,
    perform_level_up,
    calculate_proficiency_bonus
)

# Skills and Saving Throws
from dnd_5e_core.abilities import (
    Skill,
    SkillType,
    SavingThrow,
    make_saving_throw
)

# Spell Slots
from dnd_5e_core.spells import (
    SpellSlots,
    get_spell_slots_by_level
)

# Cantrips
from dnd_5e_core.spells import (
    is_cantrip,
    get_cantrip_damage_scaling
)

# Multiclassing
from dnd_5e_core.classes import (
    can_multiclass_into,
    calculate_spell_slots_multiclass
)

# Challenge Rating
from dnd_5e_core.mechanics import (
    ChallengeRating,
    calculate_encounter_difficulty
)

# Helpers
from dnd_5e_core.utils import (
    roll_with_advantage,
    calculate_modifier,
    calculate_ac
)

# Constants
from dnd_5e_core.utils import constants

# Serialization
from dnd_5e_core.data.serialization import (
    save_character,
    load_character,
    save_party
)

# API Client
from dnd_5e_core.data.api_client import (
    DndApiClient,
    get_default_client
)
```

### Usage Examples

```python
# Check if a character can level up
from dnd_5e_core.mechanics import should_level_up, perform_level_up

if should_level_up(character.xp, character.level):
    result = perform_level_up(character, available_spells)
    for msg in result.messages:
        print(msg)
    
    character.level = result.new_level
    character.max_hit_points = result.new_max_hp

# Make a saving throw
from dnd_5e_core.abilities import make_saving_throw

total, success = make_saving_throw(
    dc=15,
    ability_type="dex",
    abilities=character.abilities,
    proficiency_bonus=character.proficiency_bonus,
    proficiencies=character.saving_throw_proficiencies,
    advantage=True
)

# Calculate spell slots for multiclassing
from dnd_5e_core.classes import calculate_spell_slots_multiclass

class_levels = {"wizard": 3, "cleric": 2}
spell_slots = calculate_spell_slots_multiclass(class_levels)

# Use the API client
from dnd_5e_core.data.api_client import get_default_client

client = get_default_client()
monster_data = client.get_monster("adult-black-dragon")
```

## Migration Notes

1. **UI/Domain Separation**: All display functions (cprint, draw, etc.) have been removed from the domain classes.

2. **Message Format**: Methods now return tuples `(messages: List[str], result)` allowing frontends to manage display.

3. **GameEntity**: For pygame games, use `GameEntity` from `game_entity.py` which encapsulates domain classes and adds positioning/display features.

4. **Imports**: Verify that all imports use the `dnd_5e_core` package instead of `dao_classes`.

## Next Steps

- ✅ All empty classes have been implemented
- ✅ Module exports have been updated
- ✅ Documentation created
- 🔄 Tests to be added for new features
- 🔄 Full integration into frontends (main.py, main_ncurses.py, wizardry.py)

## Migration Date

Migration completed on: January 5, 2026
Package version: 0.1.2
