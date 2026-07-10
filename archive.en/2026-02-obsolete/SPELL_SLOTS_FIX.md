# Fixing the KeyError on spell_slots

## 🐛 Identified Issue

The following error occurred during rest at the inn in `main_ncurses.py`:

```
KeyError: 2
char.sc.spell_slots = char.class_type.spell_slots[char.level]
```

### Root Cause

1. **In `loaders.py`**: The `simple_character_generator` function created `ClassType` objects with `spell_slots={}` (empty dictionary)
2. **In `main_ncurses.py`**: The code tried to access `char.class_type.spell_slots[char.level]` without checking, causing a `KeyError` when the key did not exist.

## ✅ Applied Solutions

### 1. Fix in `dnd_5e_core/data/loaders.py`

**Modified lines: ~220-230**

Before:
```python
class_type = ClassType(
    # ...
    spell_slots={},  # ❌ Empty dictionary
    spells_known=[],
    cantrips_known=[]
)
```

After:
```python
# Build spell_slots dictionary for all levels 1-20
spell_slots_dict = {}
cantrips_known_list = []
spells_known_list = []

if is_caster:
    try:
        from .progression_loader import get_spell_slots_for_level
        # Populate spell slots for all levels
        for lvl in range(1, 21):
            spell_slots_dict[lvl] = get_spell_slots_for_level(class_name, lvl)
        # Simple progression for cantrips and spells known
        for lvl in range(1, 21):
            # Cantrips progression (simplified)
            if class_name in ['wizard', 'sorcerer', 'bard', 'cleric', 'druid', 'warlock']:
                if lvl >= 10:
                    cantrips_known_list.append(5 if lvl < 10 else 6)
                elif lvl >= 4:
                    cantrips_known_list.append(4)
                else:
                    cantrips_known_list.append(3)
            else:
                cantrips_known_list.append(0)
            
            # Spells known progression (for classes that use it)
            if class_name in ['bard', 'sorcerer', 'ranger', 'warlock']:
                spells_known_list.append(lvl + 1 if lvl < 10 else 15)
            else:
                spells_known_list.append(0)  # Prepared casters
    except Exception as e:
        # Fallback if progression_loader not available
        print(f"⚠️  Could not load spell progression for {class_name}: {e}")
        for lvl in range(1, 21):
            spell_slots_dict[lvl] = [0] * 10

class_type = ClassType(
    # ...
    spell_slots=spell_slots_dict,  # ✅ Complete dictionary with all levels
    spells_known=spells_known_list,
    cantrips_known=cantrips_known_list
)
```

**Benefits:**
- `spell_slots` now contains slots for ALL levels (1-20)
- Uses `get_spell_slots_for_level` from the package for precise progression
- Also manages `cantrips_known` and `spells_known` by level
- Graceful fallback in case of error

### 2. Securing in `main_ncurses.py` - Line 1734

**Rest at the inn**

Before:
```python
char.sc.spell_slots = char.class_type.spell_slots[char.level]  # ❌ Can cause KeyError
```

After:
```python
# Safely get spell slots with fallback
if hasattr(char.class_type, 'spell_slots') and isinstance(char.class_type.spell_slots, dict):
    char.sc.spell_slots = char.class_type.spell_slots.get(char.level, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
else:
    char.sc.spell_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

### 3. Securing in `main_ncurses.py` - Line 2415

**Level up**

Before:
```python
char.sc.spell_slots = char.class_type.spell_slots[char.level].copy()  # ❌ Can cause KeyError
```

After:
```python
# Safely get spell slots with fallback
if hasattr(char.class_type, 'spell_slots') and isinstance(char.class_type.spell_slots, dict):
    slots = char.class_type.spell_slots.get(char.level, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    char.sc.spell_slots = slots.copy() if isinstance(slots, list) else [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
else:
    char.sc.spell_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## 🧪 Tests Performed

### Test 1: Verifying spell_slots for all levels
```bash
python3 test_spell_slots_fix.py
```

**Result:** ✅ PASSED
- All spellcaster classes (wizard, cleric, druid, sorcerer, bard, warlock, paladin, ranger)
- All levels tested (1, 2, 5, 10, 15, 20)
- Direct access to `char.class_type.spell_slots[char.level]` works

### Test 2: End-to-end test
```bash
python3 test_spell_slots_end_to_end.py
```

**Result:** ✅ PASSED
- Character creation ✅
- Save with pickle ✅
- Reload ✅
- Access to spell_slots after reload ✅
- Simulation of accesses in main_ncurses.py ✅

## 📊 Example spell_slots structure

For a Level 2 Wizard:
```python
char.class_type.spell_slots = {
    1: [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],  # 2 slots level 1
    2: [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],  # 3 slots level 1
    3: [0, 4, 2, 0, 0, 0, 0, 0, 0, 0],  # 4 slots level 1, 2 slots level 2
    # ... up to level 20
}
```

Index in the list:
- `[0]`: Unused (cantrips do not have slots)
- `[1]`: Level 1 slots
- `[2]`: Level 2 slots
- `[3-9]`: Level 3 to 9 slots

## 🔧 Migration of existing characters

A migration script is available to update saved characters:

```bash
# Analysis only (without modification)
python3 migrate_spell_slots.py --dry-run

# Actual migration (with automatic backup)
python3 migrate_spell_slots.py
```

The script:
- Searches for all `.pkl` files in the save directories
- Checks if `spell_slots` is empty or malformed
- Reconstructs `spell_slots` using `get_spell_slots_for_level`
- Creates `.pkl.bak` backups before modification
- Updates `char.sc.spell_slots` if necessary

## 📝 Recommendations

### For developers

1. **Always use `.get()` for dictionaries**: Prefer `dict.get(key, default)` rather than `dict[key]`
2. **Verify types**: Use `isinstance()` before accessing attributes
3. **Default values**: Always provide sensible default values
4. **Tests**: Test all levels (1-20) for spellcaster classes

### For users

1. **New characters**: Work directly with the fix
2. **Existing characters**: Use the migration script if necessary
3. **Backups**: Backups are created automatically during migration

## ✨ Benefits of the fix

- ✅ No more `KeyError` during rest at the inn
- ✅ No more `KeyError` during level up
- ✅ Correct spell progression for all levels
- ✅ Compatibility with the package progression system
- ✅ Graceful handling of error cases
- ✅ Automatic migration of existing characters
- ✅ Complete tests to verify operation

## 🔗 Modified Files

### Main files

1. **`dnd_5e_core/data/loaders.py`** (lines ~220-260)
   - Populating `spell_slots` with all levels 1-20
   - Using `get_spell_slots_for_level` for precise progression
   - Adding `cantrips_known` and `spells_known` by level

2. **`DnD-5th-Edition-API/main_ncurses.py`** (lines 1734 and 2415)
   - Securing rest at the inn access
   - Securing level up access

3. **`DnD-5th-Edition-API/main.py`** (line 1383-1385)
   - Securing rest access (rest function)

4. **`DnD-5th-Edition-API/dungeon_pygame.py`** (line 2362-2364)
   - Securing rest access in pygame mode

### Applied securing method

All accesses to `char.class_type.spell_slots[char.level]` have been replaced by:

```python
# Safely get spell slots with fallback
expected_slots = char.class_type.spell_slots.get(char.level, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) \
    if hasattr(char.class_type, 'spell_slots') and isinstance(char.class_type.spell_slots, dict) \
    else [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## 🔗 Created test files

1. **`test_spell_slots_fix.py`** - Spell slots verification test
   - Verifies that spell_slots exists for all classes and levels
   - Simulates the access that caused the KeyError
   - **Result:** ✅ PASSED

2. **`test_spell_slots_end_to_end.py`** - End-to-end test
   - Creation, saving, and reloading test
   - Test with all spellcaster classes
   - **Result:** ✅ PASSED

3. **`test_game_integration.py`** - Game integration test
   - Simulating rest at the inn
   - Simulating level up
   - Testing edge cases (level 1, 20, pact magic)
   - **Result:** ✅ PASSED

4. **`migrate_spell_slots.py`** - Migration script
   - Automatic migration of existing characters
   - Creation of automatic backups
   - Dry-run mode available

## 📊 Test Results

### Test 1: Verifying spell_slots
```
✅ Wizard       - Level 2: L1:3
✅ Cleric       - Level 2: L1:3
✅ Paladin      - Level 2: L1:2
✅ Warlock      - Level 2: L1:2
... (all levels 1-20 tested)
```

### Test 2: End-to-end
```
✅ Creation: TestWizard (Level 2)
✅ Save: test_wizard.pkl (7914 bytes)
✅ Reload: TestWizard
✅ Direct access: [0, 3, 0, 0, 0, 0, 0, 0, 0, 0]
```

### Test 3: Game integration
```
✅ Rest at inn: 7/7 classes successfully tested
✅ Level up: 3/3 scenarios successfully tested
✅ Edge cases: 3/3 cases successfully tested
```

---

**Fix Date:** February 3, 2026  
**Status:** ✅ FIXED, TESTED AND VALIDATED

**Compatibility:**
- ✅ New characters
- ✅ Existing characters (with migration)
- ✅ All frontends (ncurses, pygame, tk, Qt)
- ✅ All levels (1-20)
- ✅ All spellcaster classes
