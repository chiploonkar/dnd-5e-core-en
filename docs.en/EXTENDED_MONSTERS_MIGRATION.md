# Migration of 5e.tools Monsters to dnd-5e-core

This document describes the migration of features related to 5e.tools monsters from DnD-5th-Edition-API to dnd-5e-core.

## Overview

The 5e.tools monsters are creatures that are not included in the official D&D 5e API but are available on the https://5e.tools/ website. These monsters have a slightly different JSON structure and require special handling.

## Migrated Modules

### 1. `dnd_5e_core/entities/extended_monsters.py`

**Main class:** `FiveEToolsMonsterLoader`

This module handles loading and searching monsters from the 5e.tools JSON files.

**Features:**
- Loading implemented monsters (`bestiary-sublist-data.json`)
- Loading all available monsters (`bestiary-sublist-data-all-monsters.json`)
- Searching monsters by name, source, CR, type
- Statistics on loaded monsters

**Usage example:**
```python
from dnd_5e_core.entities import get_extended_monster_loader

loader = get_extended_monster_loader()

# Get a monster
orc = loader.get_monster_by_name("Orc Eye of Gruumsh")

# Search for monsters
goblins = loader.search_monsters(name_contains="goblin", min_cr=1, max_cr=3)

# Get statistics
stats = loader.get_stats()
print(f"Total: {stats['total']} monsters")
```

### 2. `dnd_5e_core/entities/special_monster_actions.py`

**Main class:** `SpecialMonsterActionsBuilder`

This module encapsulates the construction logic of actions and special abilities for each 5e.tools monster. It replaces the large `get_special_monster_actions()` function in `populate_functions.py` with a more modular architecture.

**Features:**
- Builder pattern architecture for monster actions
- 47 implemented monsters with their complete actions
- Verification of monster implementation
- List of implemented monsters

**Note:** Individual construction functions raise `NotImplementedError` because they must be called from `populate_functions.py` with the correct dependencies (request_damage_type, request_spell, etc.).

**Usage example:**
```python
from dnd_5e_core.entities import get_special_actions_builder

builder = get_special_actions_builder()

# Check if a monster is implemented
if builder.is_implemented("Orc Eye of Gruumsh"):
    print("This monster has its actions implemented")

# List all implemented monsters
implemented = builder.get_implemented_monsters()
print(f"{len(implemented)} monsters with actions")
```

### 3. `dnd_5e_core/utils/token_downloader.py`

**Main functions:**
- `download_image()`: Downloads an image from a URL
- `download_monster_token()`: Downloads a monster token from 5e.tools
- `download_tokens_batch()`: Downloads tokens for multiple monsters

This module replaces the `tools/download_tokens.py` script in DnD-5th-Edition-API.

**Usage example:**
```python
from dnd_5e_core.utils import download_monster_token, download_tokens_batch

# Download a single token
download_monster_token("Orc Eye of Gruumsh", source="MM", save_folder="tokens")

# Download multiple tokens
monsters = [
    ("Orc Eye of Gruumsh", "MM"),
    ("Goblin Boss", "MM"),
    ("Hobgoblin Captain", "MM"),
]
results = download_tokens_batch(monsters, save_folder="tokens")
```

### 4. JSON Data

**Location:** `dnd_5e_core/data/monsters/`

Two JSON files:
- `bestiary-sublist-data.json`: 89 implemented monsters with actions
- `bestiary-sublist-data-all-monsters.json`: All available monsters on 5e.tools

## Migration from populate_functions.py

### Before (DnD-5th-Edition-API)

```python
# In populate_functions.py (lines 488-1400+)
def get_special_monster_actions(name: str) -> tuple[List[Action], List[SpecialAbility], SpellCaster]:
    actions: List[Action] = []
    special_abilities: List[SpecialAbility] = []
    spell_caster: SpellCaster = None
    
    if name == "Orc Eye of Gruumsh":
        # 100+ lines of code for this monster...
    elif name == "Ogre Bolt Launcher":
        # 50+ lines of code...
    # ... 40+ other elifs with 900+ lines in total
    
    return actions, special_abilities, spell_caster
```

### After (with dnd-5e-core)

```python
# In populate_functions.py
from dnd_5e_core.entities import get_special_actions_builder, get_extended_monster_loader

# Get the instances
loader = get_extended_monster_loader()
builder = get_special_actions_builder()

# Use the loader to retrieve JSON data
monster_data = loader.get_monster_by_name("Orc Eye of Gruumsh")

# Check if actions are implemented
if builder.is_implemented("Orc Eye of Gruumsh"):
    # The construction logic remains in populate_functions.py
    # but the builder structures the architecture
    actions, special_abilities, spell_caster = get_special_monster_actions("Orc Eye of Gruumsh")
```

## Benefits of the Migration

1. **Separation of Concerns:**
   - Data loading → `extended_monsters.py`
   - Action construction → `special_monster_actions.py`
   - Image downloading → `token_downloader.py`

2. **Reusability:**
   - Modules can be used by all projects in the workspace
   - JSON data is centralized

3. **Maintainability:**
   - Modular architecture instead of a large function
   - Facilitates adding new monsters
   - Better code organization

4. **Testability:**
   - Unit tests possible for each module
   - Test script provided: `test_extended_monsters.py`

## Next Steps

### To integrate into DnD-5th-Edition-API

1. Modify `populate_functions.py` to use `dnd-5e-core`:
   ```python
   # Add at the top of the file
   from dnd_5e_core.entities import get_extended_monster_loader, get_special_actions_builder
   
   # Replace the get_special_monster_actions() function
   # with calls to the builder
   ```

2. Update scripts that use `tools/download_tokens.py`:
   ```python
   # Replace
   from archive.tools.download_tokens import download_image
   
   # With
   from dnd_5e_core.utils import download_monster_token
   ```

3. Remove obsolete files:
   - `maze/other_monsters/bestiary-sublist-data.json` (moved to dnd-5e-core)
   - `maze/other_monsters/bestiary-sublist-data-all-monsters.json` (moved to dnd-5e-core)
   - `tools/download_tokens.py` (replaced by `token_downloader.py`)

### To extend functionality

1. **Add a new implemented monster:**
   - Add its name in `_register_action_builders()` in `special_monster_actions.py`
   - Create a function `_build_new_monster()`
   - Implement it in `populate_functions.py`

2. **Download missing tokens:**
   ```python
   from dnd_5e_core.entities import get_extended_monster_loader
   from dnd_5e_core.utils import download_tokens_batch
   
   loader = get_extended_monster_loader()
   monsters = loader.load_implemented_monsters()
   
   # Create the list of tuples (name, source)
   monster_list = [(m['name'], m['source']) for m in monsters]
   
   # Download all tokens
   download_tokens_batch(monster_list, save_folder="images/monsters/tokens")
   ```

## Tests

Run tests:
```bash
cd /Users/display/PycharmProjects/dnd-5e-core
python test_extended_monsters.py
```

Expected results:
- ✓ Loading of 89 implemented monsters
- ✓ 47 monsters with actions implemented
- ✓ Functional searching and filtering
- ⚠ 3 monsters with actions but missing from JSON (normal, they are in the official API)

## Data Sources

- **5e.tools**: https://5e.tools/
- **JSON Files**: Extracted from the 5e.tools website
- **Images (tokens)**: https://5e.tools/img/bestiary/tokens/{SOURCE}/{MONSTER_NAME}.webp

## Statistics

- **Total monsters in the JSON**: 89
- **Monsters with actions implemented**: 47
- **Sources represented**: MM, MPMM, VGTM
- **Creature types**: 12 different types

## Support

For any questions or problems, consult:
- `dnd_5e_core/data/monsters/README.md` - Data documentation
- `test_extended_monsters.py` - Usage examples
- `populate_functions.py` - Actions implementation in DnD-5th-Edition-API
