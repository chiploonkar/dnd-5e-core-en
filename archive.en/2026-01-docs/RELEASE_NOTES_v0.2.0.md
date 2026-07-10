# 🎉 dnd-5e-core v0.2.0 - Magic Items & Defensive Spells

## 📅 Release date: January 18, 2026

## 🌟 Major new features

### 1. 🪄 Complete Magic Items System

The package now includes a complete **magic items** system usable in combat:

#### Features
- ✅ **Passive bonuses**: AC, saving throws, ability scores
- ✅ **Active abilities**: Combat actions (attacks, healing, defense)
- ✅ **Attunement system**: Max 3 items attuned per character
- ✅ **Charges/Uses tracking**: Limited uses per day with recharge
- ✅ **Rarity system**: Common, Uncommon, Rare, Very Rare, Legendary, Artifact

#### Main classes
```python
from dnd_5e_core.equipment import MagicItem, MagicItemAction, MagicItemRarity

# Creating a magic item
ring = MagicItem(
    index="ring-of-protection",
    name="Ring of Protection",
    rarity=MagicItemRarity.RARE,
    ac_bonus=1,
    saving_throw_bonus=1,
    requires_attunement=True
)
```

#### 8 Predefined Magic Items

```python
from dnd_5e_core.equipment import (
    create_ring_of_protection,      # +1 AC, +1 saves
    create_cloak_of_protection,     # +1 AC, +1 saves
    create_wand_of_magic_missiles,  # 7 charges/day
    create_staff_of_healing,        # 10 charges/day
    create_belt_of_giant_strength,  # STR 21
    create_amulet_of_health,        # CON 19
    create_bracers_of_defense,      # +2 AC
    create_necklace_of_fireballs    # 6 beads
)Base
# Usage
ring = create_ring_of_protection()
ring.attune(character)
ring.equipped = True
ring.apply_to_character(character)
```

#### Magic items loader

```python
from dnd_5e_core.data import load_magic_item

# Load from JSON
ring = load_magic_item("ring-of-protection")
staff = load_magic_item("staff-of-healing")
```

### 2. 🛡️ Defensive spells and buffs

Spells can now provide **defensive bonuses** and **buffs**:

#### New Spell properties
```python
@dataclass
class Spell:
    # ... existing properties ...
    
    # 🆕 New properties
    duration: Optional[str]              # "1 round", "8 hours", etc.
    concentration: bool                  # Requires concentration
    ac_bonus: Optional[int]             # AC bonus
    saving_throw_bonus: Optional[int]   # Saving throw bonus
    ability_bonuses: Optional[Dict]     # Ability score bonuses
    damage_resistance: Optional[List]    # Damage types resisted
    damage_immunity: Optional[List]      # Damage types immune
    conditions_immunity: Optional[List]  # Conditions prevented
```

#### New methods
```python
# Check spell type
shield = load_spell("shield")
print(shield.is_defensive)  # True
print(shield.is_damaging)   # False
print(shield.is_healing)    # False
print(shield.is_buff)       # False

# Properties
print(shield.ac_bonus)      # 5
print(shield.duration)      # "1 round"
print(shield.concentration) # False
```

#### Parsed defensive spells

The following spells are automatically parsed from JSON:

| Spell | Level | AC Bonus | Duration | Concentration |
|------|--------|----------|-------|---------------|
| **Shield** | 1 | +5 | 1 round | No |
| **Mage Armor** | 1 | +3 | 8 hours | No |
| **Shield of Faith** | 1 | +2 | 10 minutes | Yes |
| **Protection from Energy** | 3 | - | 1 hour | Yes |

```python
from dnd_5e_core.data import load_spell

# Shield (+5 AC, 1 round)
shield = load_spell("shield")
print(f"{shield.name}: +{shield.ac_bonus} AC for {shield.duration}")

# Mage Armor (AC 13 + DEX)
mage_armor = load_spell("mage-armor")
print(f"{mage_armor.name}: +{mage_armor.ac_bonus} AC for {mage_armor.duration}")

# Shield of Faith (+2 AC, concentration)
shield_of_faith = load_spell("shield-of-faith")
print(f"{shield_of_faith.name}: +{shield_of_faith.ac_bonus} AC")
print(f"Concentration: {shield_of_faith.concentration}")
```

## 📚 Usage examples

### Combat with Magic Items

```python
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.equipment import create_ring_of_protection, create_wand_of_magic_missiles
from dnd_5e_core.combat import CombatSystem

# Create a wizard
wizard = simple_character_generator(level=5, class_name='wizard', name='Gandalf')

# Equip Ring of Protection
ring = create_ring_of_protection()
ring.attune(wizard)
ring.equipped = True
ring.apply_to_character(wizard)

print(f"AC: {wizard.armor_class}")  # +1 from ring

# Equip Wand of Magic Missiles
wand = create_wand_of_magic_missiles()
wand.equipped = True

# Use the wand's action in combat
magic_missile_action = wand.actions[0]
if wand.can_perform_action(magic_missile_action):
    wand.use_action(magic_missile_action)
    print(f"Used Magic Missile! Remaining charges: {magic_missile_action.remaining_uses}")
```

### Using defensive spells

```python
from dnd_5e_core.data import load_spell

# Load defensive spells
shield = load_spell("shield")
mage_armor = load_spell("mage-armor")

# Apply in combat (conceptual)
if under_attack and wizard.can_cast_spell(shield.level):
    # Cast Shield as reaction
    wizard.cast_spell(shield.level)
    temporary_ac_bonus = shield.ac_bonus  # +5
    print(f"Shield cast! AC temporarily increased by {temporary_ac_bonus}")
```

## 🔧 Integration with the combat system

Magic items and defensive spells integrate perfectly with the existing `CombatSystem`:

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.data import load_monster

combat = CombatSystem(verbose=True)

# The wizard with Ring of Protection will automatically have +1 AC
# The combat system will take the modified AC into account
goblin = load_monster('goblin')

combat.character_turn(
    character=wizard,
    alive_chars=[wizard],
    alive_monsters=[goblin],
    party=[wizard]
)
```

## 📖 Documentation

### Added modules

- `dnd_5e_core.equipment.magic_item` - Magic items system
- `dnd_5e_core.equipment.predefined_magic_items` - 8 ready-to-use magic items

### Added functions

- `load_magic_item(index)` - Load a magic item from JSON
- `get_magic_item(index)` - Get a predefined magic item
- `create_*()` - 8 functions to create specific magic items

### Tests

A complete test script is available:

```bash
python tests/test_magic_items_and_defense.py
```

## 🚀 Migration from v0.1.9

No breaking changes! All existing features remain compatible.

### New features available

```python
# Before v0.2.0
from dnd_5e_core.data import load_spell
shield = load_spell("shield")
# shield.ac_bonus did not exist

# v0.2.0+
from dnd_5e_core.data import load_spell
shield = load_spell("shield")
print(shield.ac_bonus)      # 5
print(shield.is_defensive)  # True
print(shield.duration)      # "1 round"
```

## 📦 Installation

```bash
pip install dnd-5e-core==0.2.0
```

or

```bash
pip install --upgrade dnd-5e-core
```

## 🔗 Useful links

- **PyPI**: https://pypi.org/project/dnd-5e-core/0.2.0/
- **GitHub**: https://github.com/codingame-team/dnd-5e-core
- **Documentation**: https://github.com/codingame-team/dnd-5e-core/tree/main/docs
- **CHANGELOG**: https://github.com/codingame-team/dnd-5e-core/blob/main/CHANGELOG.md

## 🎮 Example projects

See how to use these features in real projects:

- **DnD5e-Scenarios**: https://github.com/codingame-team/DnD5e-Scenarios
- **DnD-5th-Edition-API**: https://github.com/codingame-team/DnD-5th-Edition-API

## 🙏 Contribution

Contributions are welcome! Feel free to:

- Open an issue to report a bug
- Propose new magic items
- Improve the documentation
- Add tests

## 📝 Complete changelog

See [CHANGELOG.md](https://github.com/codingame-team/dnd-5e-core/blob/main/CHANGELOG.md) for all details.
