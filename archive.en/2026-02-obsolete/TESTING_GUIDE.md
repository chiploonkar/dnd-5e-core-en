# Test and Validation Scripts - Spell Slots Fix

This directory contains several scripts to test and validate the fix for the `spell_slots` KeyError.

## 📋 Available Scripts

### 1. `validate_spell_slots_fix.py` ⭐ (RECOMMENDED)
**Quick validation script** - Run to check that everything is working.

```bash
# Quick validation (imports, basic access, documentation)
python3 validate_spell_slots_fix.py

# Full validation with all tests
python3 validate_spell_slots_fix.py --full
```

**Expected Output:**
```
✅ Imports                     : PASSED
✅ Quick validation            : PASSED  
✅ Documentation              : PASSED
🎉 FULL VALIDATION SUCCESSFUL!
```

---

### 2. `test_spell_slots_fix.py`
**Detailed spell_slots test** - Checks all classes and all levels.

```bash
python3 test_spell_slots_fix.py
```

**What it tests:**
- ✅ `spell_slots` exists for all spellcaster classes (wizard, cleric, druid, sorcerer, bard, warlock, paladin, ranger)
- ✅ All levels 1-20 are present in the dictionary
- ✅ Direct access to `char.class_type.spell_slots[char.level]` works
- ✅ `SpellCaster` is correctly initialized

**Duration:** ~5-10 seconds

---

### 3. `test_spell_slots_end_to_end.py`
**End-to-end test** - Creation, saving, reloading.

```bash
python3 test_spell_slots_end_to_end.py
```

**What it tests:**
- ✅ Creation of a character with `spell_slots`
- ✅ Saving with pickle
- ✅ Reloading and checking integrity
- ✅ Access to `spell_slots` after reloading
- ✅ Test with all caster classes at level 2

**Duration:** ~10-15 seconds

---

### 4. `test_game_integration.py`
**Integration test** - Simulates the game situations that caused the KeyError.

```bash
python3 test_game_integration.py
```

**What it tests:**
- ✅ **Resting at the inn** (main_ncurses.py line 1734)
  - Use of slots then restoration
  - 7 classes tested (wizard, cleric, sorcerer, bard, paladin, ranger, warlock)
  
- ✅ **Leveling up** (main_ncurses.py line 2415)
  - Moving from level 1→2, 2→3, etc.
  - Updating `spell_slots`
  
- ✅ **Edge cases**
  - Level 20 (maximum)
  - Level 1 Paladin (no spells yet)
  - Warlock level 5 (pact magic)

**Duration:** ~10-15 seconds

---

### 5. `migrate_spell_slots.py`
**Migration script** - For existing saved characters.

```bash
# Dry-run mode (analysis only, no modifications)
python3 migrate_spell_slots.py --dry-run

# Actual migration (creates backups automatically)
python3 migrate_spell_slots.py
```

**What it does:**
- 🔍 Searches for all .pkl files in `~/Saved_Games_DnD_5th/`
- 🔍 Checks if `spell_slots` is empty or malformed
- 🔧 Reconstructs `spell_slots` with `get_spell_slots_for_level()`
- 💾 Creates backups (.pkl.bak) before modification
- ✅ Updates `char.sc.spell_slots` if necessary

**When to use it:**
- If you have characters created BEFORE the fix
- If you still encounter KeyErrors with existing characters

---

## 🚀 Recommended Workflow

### After installation or update

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# 1. Quick validation
python3 validate_spell_slots_fix.py

# 2. If everything is OK, test the game
cd /Users/display/PycharmProjects/DnD-5th-Edition-API
python3 main_ncurses.py
```

### If you have existing characters

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# 1. Verify what will be modified
python3 migrate_spell_slots.py --dry-run

# 2. If necessary, migrate
python3 migrate_spell_slots.py

# 3. Validate
python3 validate_spell_slots_fix.py
```

### For development

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# Run all tests
python3 test_spell_slots_fix.py
python3 test_spell_slots_end_to_end.py
python3 test_game_integration.py

# Or full validation
python3 validate_spell_slots_fix.py --full
```

---

## 📊 Execution Time

| Script | Duration | When to use it |
|--------|-------|------------------|
| `validate_spell_slots_fix.py` | ~2 sec | ⭐ Always (quick validation) |
| `validate_spell_slots_fix.py --full` | ~30 sec | After modifying the code |
| `test_spell_slots_fix.py` | ~10 sec | Development |
| `test_spell_slots_end_to_end.py` | ~15 sec | Development |
| `test_game_integration.py` | ~15 sec | Development |
| `migrate_spell_slots.py` | Variable | Once for existing characters |

---

## ✅ What to do if a test fails?

### Import test fails
```
❌ Imports : FAILED
```
**Solution:** Check that you are in the correct directory and that the modified files are present.

### Quick validation fails
```
❌ Quick validation : FAILED
```
**Possible solutions:**
1. Check that `dnd_5e_core/data/loaders.py` contains the modifications
2. Check that `get_spell_slots_for_level` is accessible
3. Run again with `python3 validate_spell_slots_fix.py --full` for more details

### Full tests fail
```
❌ test_game_integration.py : FAILED
```
**Solutions:**
1. Check the detailed error messages
2. Refer to `SPELL_SLOTS_FIX.md` for complete documentation
3. Delete corrupted saved characters and recreate them

---

## 📚 Documentation

- **`SPELL_SLOTS_FIX.md`** - Complete technical documentation
- **`QUICKFIX_SPELL_SLOTS.md`** - Quick user guide
- **`SPELL_SLOTS_SUMMARY.md`** - One-page summary
- **`CHANGELOG.md`** - Changelog

---

## 🆘 Support

If you encounter persistent issues:

1. **Check versions**
   ```bash
   git status
   git log --oneline -5
   ```

2. **Clean up saves**
   ```bash
   # Back up your important characters elsewhere!
   rm -rf ~/Saved_Games_DnD_5th/*.pkl
   ```

3. **Recreate a test character**
   ```bash
   cd /Users/display/PycharmProjects/dnd-5e-core
   python3 -c "from dnd_5e_core.data.loaders import simple_character_generator; c = simple_character_generator(level=2, class_name='wizard'); print(c.class_type.spell_slots[2])"
   ```

If the last command displays `[0, 3, 0, 0, 0, 0, 0, 0, 0, 0]`, the fix works!

---

**Last updated:** February 3, 2026  
**Status:** ✅ All scripts work and are tested
