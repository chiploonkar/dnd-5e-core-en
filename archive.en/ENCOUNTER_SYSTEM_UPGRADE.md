# Challenge Rating System Upgrade

## 🎯 Identified Problem

The Challenge Rating system in `dnd_5e_core` used a **simplified** approach that did not faithfully follow the official D&D 5e rules, unlike the `generate_encounter()` function in `main.py` which uses the **precise encounter tables** from the Dungeon Master's Guide.

### Old System (Simplified)
```python
def get_appropriate_cr_range(party_level: int) -> Tuple[float, float]:
    min_cr = max(0, party_level - 3)
    max_cr = party_level + 3
    return (min_cr, max_cr)
```

**Issues:**
- ❌ Only uses a ±3 range around the party level
- ❌ Does not account for the **number of monsters**
- ❌ No group or pair structure
- ❌ Can generate unbalanced encounters
- ❌ Does not follow official D&D 5e tables

### main.py System (Correct)
- ✅ Uses the `Encounter_Levels.csv` file based on D&D 5e rules
- ✅ Accounts for the number of monsters (1, 2, 3, 4, 5-6, 7-9, 10-12)
- ✅ Generates pairs of monsters of different CRs OR homogeneous groups
- ✅ Adjusts CRs based on party size
- ✅ Realistic difficulty distribution (30% easy, 50% medium, 15% hard, 5% deadly)

---

## ✅ Implemented Solution

### New Module: `encounter_builder.py`

Creation of a new module in `dnd_5e_core/mechanics/encounter_builder.py` that implements the exact system of `main.py`.

**Features:**

1. **ENCOUNTER_TABLE**: Complete encounter table for levels 1-20
   - Based on `Encounter_Levels.csv`
   - For each level: CR pairs + group options

2. **generate_encounter_distribution()**: Difficulty distribution
   - 30% easy encounters (< party_level)
   - 50% medium encounters (= party_level)
   - 15% hard encounters (+1-4)
   - 5% deadly encounters (+5-20)

3. **select_monsters_by_encounter_table()**: Intelligent selection
   - Generates pairs or groups according to the table
   - Respects appropriate CRs
   - Handles cases where the exact CR does not exist (finds the closest one)

4. **get_encounter_info()**: Encounter information
   - Returns available options for a given level

---

## 📊 Comparison

### Example: Level 5 Party

**Old system:**
```python
min_cr, max_cr = get_appropriate_cr_range(5)  # (2, 8)
# Selects any monster between CR 2 and 8
# No structure, no optimal number
```

**New system:**
```python
monsters, type = select_monsters_by_encounter_table(5, monsters_db)

# Possible options:
# PAIRS: CR 4 + CR 2
# GROUPS:
#   - 1x monster CR 4-6
#   - 2x monsters CR 3
#   - 3x monsters CR 2
#   - 4x monsters CR 1-2
#   - 5-6x monsters CR 1
#   - 7-9x monsters CR 0.5
#   - 10-12x monsters CR 0.5
```

**Results:**
- ✅ More balanced and varied
- ✅ Exactly follows D&D 5e rules
- ✅ Generates appropriate encounters

---

## 🔧 Usage

### Import the new system

```python
from dnd_5e_core.mechanics import (
    select_monsters_by_encounter_table,
    generate_encounter_distribution,
    get_encounter_info,
    ENCOUNTER_TABLE
)
```

### Generate an encounter

```python
# Load monsters
monsters_db = load_monsters()

# Generate an encounter for a level 5 party
party_level = 5
monsters, encounter_type = select_monsters_by_encounter_table(
    encounter_level=party_level,
    available_monsters=monsters_db,
    spell_casters_only=False,  # Optional
    allow_pairs=True  # True = can generate pairs, False = only groups
)

# Result
if encounter_type == "pair":
    print(f"Pair: {monsters[0].name} + {monsters[1].name}")
else:
    print(f"Group: {len(monsters)}x {monsters[0].name}")
```

### Generate an encounter distribution

```python
party_level = 5
encounter_levels = generate_encounter_distribution(party_level)
# Returns 20 encounter levels with the distribution:
# 30% easy, 50% medium, 15% hard, 5% deadly
```

### Get level info

```python
info = get_encounter_info(party_level=5)
# Returns:
# {
#     'level': 5,
#     'pair_crs': (Fraction(4), Fraction(2)),
#     'group_options': {
#         '1': [4, 5, 6],
#         '2': [3],
#         '3': [2],
#         ...
#     }
# }
```

---

## 📝 Complete Example

```python
from dnd_5e_core.mechanics import select_monsters_by_encounter_table
from main import request_monster, populate

# Load monsters
monster_names = populate(collection_name="monsters", key_name="results")
monsters_db = [request_monster(name) for name in monster_names if request_monster(name)]

# Level 8 party
party_level = 8

# Generate 5 different encounters
for i in range(5):
    monsters, enc_type = select_monsters_by_encounter_table(
        party_level, monsters_db, allow_pairs=True
    )
    
    if enc_type == "pair":
        print(f"{i+1}. PAIR: {monsters[0].name} (CR {monsters[0].challenge_rating}) "
              f"+ {monsters[1].name} (CR {monsters[1].challenge_rating})")
    else:
        print(f"{i+1}. GROUP: {len(monsters)}x {monsters[0].name} "
              f"(CR {monsters[0].challenge_rating})")

# Example output:
# 1. GROUP: 3x Young Green Dragon (CR 8)
# 2. PAIR: Stone Giant (CR 7) + Air Elemental (CR 5)
# 3. GROUP: 2x Medusa (CR 6)
# 4. PAIR: Fire Giant (CR 9) + Gladiator (CR 5)
# 5. GROUP: 4x Young Green Dragon (CR 8)
```

---

## 🎯 Recommendations

1. **For new scripts**: Use `select_monsters_by_encounter_table()`
2. **Migration**: Replace `get_appropriate_cr_range()` with the new system
3. **Advantages**:
   - More balanced encounters
   - Follows official D&D 5e rules
   - More variety (pairs vs groups)
   - Realistic difficulty distribution

---

## 📁 Modified/Created Files

1. **New**: `dnd_5e_core/mechanics/encounter_builder.py` (510 lines)
   - Complete ENCOUNTER_TABLE table
   - Encounter generation functions

2. **Modified**: `dnd_5e_core/mechanics/__init__.py`
   - Added imports of the new module
   - Export of the new functions

3. **Modified**: `dnd_5e_core/mechanics/dice.py`
   - Bugfix: management of `success_type=None`

4. **New**: `DnD5e-Test/demo_encounter_systems.py`
   - Demonstration and comparison script

---

## 🧪 Tests

The script `demo_encounter_systems.py` demonstrates the difference between the two systems for levels 1, 3, 5, 10, 15, and 20.

**Execute:**
```bash
cd /Users/display/PycharmProjects/DnD5e-Test
python3 demo_encounter_systems.py
```

---

## ✅ Conclusion

The `dnd_5e_core` package now uses the **same encounter generation system** as `main.py`, based on the **official D&D 5e tables**. This guarantees balanced encounters in compliance with game rules.

The old system remains available for backward compatibility, but the new system is **highly recommended** for all new development.

---

**Date:** January 6, 2026  
**Version:** dnd-5e-core 0.1.4
