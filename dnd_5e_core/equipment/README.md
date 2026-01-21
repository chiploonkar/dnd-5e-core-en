# Equipment Module

This module contains all equipment-related classes and factory functions for D&D 5e.

## Structure

### Core Classes
- **`equipment.py`** - Base equipment class and inventory system
- **`weapon.py`** - Weapon data structures and types
- **`armor.py`** - Armor data structures
- **`potion.py`** - Potion classes (healing, enhancement, etc.)
- **`magic_item.py`** - Magic item system with actions and effects

### Factory Modules
- **`armor_factory.py`** - Special and magical armors (16 items + variants)
- **`weapon_factory.py`** - Legendary and magical weapons (19 items)
- **`magic_item_factory.py`** - Comprehensive magic items collection (49 items)
  - Rings, wands, staves, wondrous items, potions
  - Merged from `predefined_magic_items.py` (now deprecated)

### Deprecated
- **`predefined_magic_items.py`** - ⚠️ DEPRECATED - Merged into `magic_item_factory.py`

## Usage

### Import from Package Level (Recommended)

```python
from dnd_5e_core.equipment import (
    # Armors
    create_dwarven_plate,
    create_dragon_scale_mail,
    get_special_armor,
    SPECIAL_ARMORS,
    
    # Weapons
    create_flame_tongue,
    create_holy_avenger,
    get_special_weapon,
    SPECIAL_WEAPONS,
    
    # Magic Items
    create_ring_of_protection,
    create_belt_of_giant_strength,
    create_potion_of_healing,
    get_magic_item,
    MAGIC_ITEMS_REGISTRY,
)
```

### Create Equipment

```python
# Armors
armor = create_dwarven_plate()  # AC 20, +2 bonus
dragon_mail = create_dragon_scale_mail("red")  # Fire resistance
mithral = create_mithral_armor("plate")  # No stealth disadvantage

# Weapons
sword = create_flame_tongue()  # +2d6 fire damage
bow = create_oathbow()  # +3d6 vs sworn enemy
holy = create_holy_avenger()  # Legendary paladin weapon

# Magic Items
ring = create_ring_of_protection()  # +1 AC and saves
belt = create_belt_of_giant_strength("storm")  # STR 29
wand = create_wand_of_magic_missiles()  # 7 charges

# Potions
healing = create_potion_of_healing()  # 2d4+2 HP
antitoxin = create_antitoxin()  # Advantage vs poison
elixir = create_elixir_of_health()  # Cure disease & poison
```

### Access by Index

```python
# Get items from registry
armor = get_special_armor("elven-chain")
weapon = get_special_weapon("sun-blade")
item = get_magic_item("ring-of-regeneration")

# List all available
print(f"Armors: {len(SPECIAL_ARMORS)}")
print(f"Weapons: {len(SPECIAL_WEAPONS)}")
print(f"Magic Items: {len(MAGIC_ITEMS_REGISTRY)}")
```

## Equipment Counts

| Category | Count | Description |
|----------|-------|-------------|
| **Special Armors** | 16 base + variants | Legendary to Uncommon |
| **Special Weapons** | 19 | Legendary to Uncommon |
| **Magic Items** | 49 | Rings, wands, staves, wondrous items, potions |
| **Total** | 84+ | Complete D&D 5e equipment collection |

## Registries

### SPECIAL_ARMORS (16 items)
- Legendary: Armor of Invulnerability, Plate Armor of Etherealness, Spellguard Shield
- Very Rare: Demon Armor, Dragon Scale Mail, Dwarven Plate, Animated Shield
- Rare: Elven Chain, Armor of Resistance, Arrow-Catching Shield
- Uncommon: Mithral Armor, Adamantine Armor

### SPECIAL_WEAPONS (19 items)
- Legendary: Holy Avenger, Vorpal Sword, Luck Blade, Defender, Hammer of Thunderbolts
- Very Rare: Frost Brand, Sword of Sharpness, Nine Lives Stealer, Oathbow, Dwarven Thrower, Scimitar of Speed
- Rare: Flame Tongue, Sun Blade, Giant Slayer, Dragon Slayer, Mace of Disruption, Mace of Smiting
- Uncommon: Javelin of Lightning, Trident of Fish Command

### MAGIC_ITEMS_REGISTRY (49 items)
- **Rings** (5): Protection, Free Action, Regeneration, Spell Storing, Blinding
- **Wands** (3): Magic Missiles, Fireballs, Paralysis
- **Staves** (2): Healing, Entanglement
- **Wondrous Items** (21): Belts, Cloaks, Boots, Gauntlets, Amulets, etc.
- **Potions** (17): Healing (4 tiers), Giant Strength (6 types), Speed, Flying, Invisibility, etc.
- **Weapons** (1): Poisoned Dagger

## Documentation

For complete documentation, see:
- **`/docs/EQUIPMENT_GUIDE.md`** - Full equipment reference with stats and examples
- **`/CHANGELOG.md`** - Version history and changes
- **`/EQUIPMENT_EXPANSION_SUMMARY.md`** - Detailed expansion report

## Testing

Run equipment tests:
```bash
python test/test_equipment_factories.py
```

List all equipment:
```bash
python scripts/list_all_equipment.py
```

## Notes

- All factory functions return fully configured equipment objects
- Equipment can be used immediately in combat and character creation
- Magic items with actions integrate with the combat system
- Potions can be consumed for various effects
- All items follow official D&D 5e rules and pricing

## Version

Equipment expansion added in version 0.3.0 (January 2026)
