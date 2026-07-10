# Update of the Loader Module - Object Return Instead of Dictionaries

## Date: January 17, 2026

## Major Change

The `dnd_5e_core.data.loader` module has been updated to return **class objects** instead of **JSON dictionaries**.

### Before (v0.1.0 - v0.1.6)

```python
from dnd_5e_core.data import load_monster

goblin = load_monster("goblin")
print(goblin["name"])  # Dict access
print(goblin.get("challenge_rating"))  # Usage of .get()
```

### After (v0.1.7+)

```python
from dnd_5e_core.data import load_monster

goblin = load_monster("goblin")  # Returns a Monster object
print(goblin.name)  # Property access
print(goblin.challenge_rating)  # Direct access
print(goblin.is_alive)  # Usage of object methods
```

## Modified Functions

### `load_monster(index: str) -> Optional[Monster]`

- **Before**: Returned `Dict[str, Any]`
- **After**: Returns `Monster` (object of the `Monster` class)
- **Benefit**: Direct access to methods like `hp_roll()`, `saving_throw()`, `is_spell_caster`, etc.

### `load_spell(index: str) -> Optional[Spell]`

- **Before**: Returned `Dict[str, Any]`
- **After**: Returns `Spell` (object of the `Spell` class)
- **Benefit**: Access to properties like `is_cantrip`, `is_damaging`, `requires_save`, etc.

### `load_weapon(index: str) -> Optional[Weapon]`

- **Before**: Returned `Dict[str, Any]`
- **After**: Returns `Weapon` (object of the `Weapon` class)
- **Benefit**: Access to properties like `is_melee`, `is_ranged`, `has_property()`, etc.

### `load_armor(index: str) -> Optional[Armor]`

- **Before**: Returned `Dict[str, Any]`
- **After**: Returns `Armor` (object of the `Armor` class)
- **Benefit**: Direct access to properties like `armor_class`, `stealth_disadvantage`, etc.

## New Internal Functions

Two new helper functions were added to convert JSON data to objects:

- `_create_monster_from_data(index: str, data: Dict) -> Monster`
- `_create_spell_from_data(index: str, data: Dict) -> Spell`

These functions handle:
- Conversion of JSON data to Python objects
- Creation of sub-objects (Abilities, Actions, Damages, etc.)
- Handling of special cases (Spellcasting, Multiattack, Special Abilities)

## Compatibility

### Code to Update

If your code used the old functions that returned dictionaries:

```python
# BEFORE - TO BE REPLACED
monster_data = load_monster("goblin")
name = monster_data.get("name")
cr = monster_data.get("challenge_rating")

# AFTER - NEW CODE
monster = load_monster("goblin")
name = monster.name
cr = monster.challenge_rating
```

### Automatic Migration

For projects using the package, search and replace:

```bash
# Search for usages of .get() on load_* results
grep -r "load_monster.*\.get\|load_spell.*\.get" .
```

## Advantages of This Change

1. **Strong typing**: IDEs can now auto-complete properties
2. **Fewer errors**: No more unexpected `KeyError` or `None`
3. **Better documentation**: Function signatures are clearer
4. **Utility methods**: Direct access to the methods of each class
5. **Consistency**: Same interface as the other modules of the package

## Impact on Projects

### DnD5e-Scenarios
✅ Scenarios already use `Monster` and `Spell` - no impact

### DnD-5th-Edition-API
⚠️ Some scripts use `populate_functions.request_monster()` which already returns objects
- Scripts migrating to `dnd_5e_core` will benefit from this change

## Tests

The functions were tested successfully:

```bash
# Works:
✅ load_monster works:
   Name: Goblin
   CR: 0.25
   HP: 7
   Type: Monster

✅ load_spell works:
   Name: Fireball
   Level: 3
   School: evocation
   Type: Spell
```

## Updated Documentation

- ✅ `dnd_5e_core/data/loader.py` - Updated docstrings
- ✅ `docs/api/data.md` - Complete documentation with examples
- ✅ Type signatures added for all returns

## Next Steps

1. Test scenarios with the new functions
2. Migrate remaining scripts from DnD-5th-Edition-API
3. Publish version 0.1.7 of the package
4. Update the main README.md with examples
