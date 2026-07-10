# Collections Migration - dnd-5e-core

## 📚 Summary

The `collections/` folder has been migrated from `DnD-5th-Edition-API` to `dnd-5e-core` to centralize all D&D 5e data into a single package.

**Migration date:** December 23, 2025

---

## 🎯 Objective

Centralize the D&D 5e API index collection files in the `dnd-5e-core` package to:
- ✅ Avoid data duplication between projects
- ✅ Facilitate maintenance and updates
- ✅ Allow for better code reusability
- ✅ Create a standalone and complete Python package

---

## 📁 Before/After Structure

### Before Migration

```
DnD-5th-Edition-API/
├── collections/
│   ├── ability-scores.json
│   ├── alignments.json
│   ├── monsters.json
│   ├── spells.json
│   └── ... (26 files)
└── populate_functions.py  # Uses collections/

dnd-5e-core/
└── (no collections)
```

### After Migration

```
dnd-5e-core/
├── collections/                    # ✅ NEW
│   ├── README.md                   # Collections documentation
│   ├── ability-scores.json
│   ├── alignments.json
│   ├── monsters.json
│   ├── spells.json
│   └── ... (26 files)
└── dnd_5e_core/
    └── data/
        ├── collections.py          # ✅ NEW MODULE
        ├── loader.py
        └── __init__.py             # Updated

DnD-5th-Edition-API/
├── collections/                    # Kept for compatibility
└── populate_functions.py           # Can now import from dnd-5e-core
```

---

## 🔧 New Module: `collections.py`

A new module `dnd_5e_core/data/collections.py` has been created to manage collections.

### Main Functions

```python
from dnd_5e_core.data import (
    populate,                    # Function compatible with old code
    load_collection,             # Load a complete collection
    get_collection_count,        # Get the number of items
    get_collection_item,         # Get a specific item
    list_all_collections,        # List all available collections
)

# Convenience functions
from dnd_5e_core.data import (
    get_monsters_list,
    get_spells_list,
    get_classes_list,
    get_races_list,
    get_equipment_list,
    get_weapons_list,
    get_armors_list,
    get_magic_items_list,
)
```

---

## 📝 Code Migration Guide

### Old Code (DnD-5th-Edition-API)

```python
from populate_functions import populate

# Load the list of monsters
monsters = populate(collection_name='monsters', key_name='results')

# With URLs
monsters_with_urls = populate(
    collection_name='monsters', 
    key_name='results', 
    with_url=True
)
```

### New Code (dnd-5e-core)

```python
from dnd_5e_core.data import populate, get_monsters_list

# Option 1: Use populate() (compatible)
monsters = populate('monsters', 'results')
monsters_with_urls = populate('monsters', 'results', with_url=True)

# Option 2: Use the convenience function (recommended)
monsters = get_monsters_list()
monsters_with_urls = get_monsters_list(with_url=True)
```

### Advanced Example

```python
from dnd_5e_core.data import (
    load_collection,
    get_collection_count,
    get_collection_item,
    list_all_collections
)

# List all available collections
collections = list_all_collections()
print(f"Available collections: {collections}")

# Get the number of monsters
monster_count = get_collection_count('monsters')
print(f"Number of monsters: {monster_count}")

# Load the entire collection
monsters_data = load_collection('monsters')
print(f"Count: {monsters_data['count']}")
print(f"Results: {len(monsters_data['results'])}")

# Get a specific monster
goblin = get_collection_item('monsters', 'goblin')
print(f"Goblin: {goblin['name']}, URL: {goblin['url']}")
```

---

## 🔄 Path Configuration

The `collections.py` module automatically detects the collections path. You can also define it manually:

```python
from dnd_5e_core.data import set_collections_directory

# Define a custom path
set_collections_directory('/path/to/collections')
```

The module automatically searches in:
1. `dnd-5e-core/collections/` (preferred)
2. `DnD-5th-Edition-API/collections/` (fallback)
3. `./collections/` (current directory)

---

## 📊 Migrated Files

26 JSON files have been migrated:

| Collection | Items | Description |
|------------|-------|-------------|
| ability-scores | 6 | STR, DEX, CON, INT, WIS, CHA |
| alignments | 9 | Alignment types |
| armors | 30 | Armor types |
| backgrounds | - | Character backgrounds |
| classes | 12 | Character classes |
| conditions | 15 | Status conditions |
| damage-types | 13 | Damage types |
| equipment | 237 | General equipment |
| equipment-categories | 39 | Equipment categories |
| feats | - | Special feats |
| features | 377 | Class/racial features |
| languages | 16 | Languages |
| magic-items | 239 | Magic items |
| magic-schools | 8 | Magic schools |
| monsters | 332 | Monsters (CR 0-30) |
| proficiencies | 117 | Skills and tools |
| races | 9 | Playable races |
| rule-sections | 30 | Rule sections |
| rules | - | Basic rules |
| skills | 18 | Skills |
| spells | 319 | Spells (cantrips to level 9) |
| subclasses | 12 | Subclass options |
| subraces | 4 | Racial variants |
| traits | 38 | Racial/background traits |
| weapon-properties | 11 | Weapon properties |
| weapons | 65 | Simple and martial weapons |

---

## ✅ Benefits of the Migration

### For dnd-5e-core
- ✅ Complete and standalone package
- ✅ All D&D 5e data centralized
- ✅ Facilitates installation and distribution
- ✅ Consistent API for data access

### For DnD-5th-Edition-API
- ✅ Can import directly from dnd-5e-core
- ✅ Less code duplication
- ✅ Automatic updates when dnd-5e-core is updated
- ✅ More maintainable code

### For Developers
- ✅ Single place to manage collections
- ✅ Clear and complete documentation
- ✅ Convenience functions for easy usage
- ✅ Compatibility with old code

---

## 🚀 Next Steps

### 1. Update DnD-5th-Edition-API

Modify `populate_functions.py` to use dnd-5e-core:

```python
# Option 1: Direct import (recommended)
from dnd_5e_core.data import populate

# Option 2: Wrapper for compatibility
def populate(collection_name: str, key_name: str, with_url=False, collection_path: str = None):
    from dnd_5e_core.data import populate as core_populate
    return core_populate(collection_name, key_name, with_url, collection_path)
```

### 2. Add dnd-5e-core to Dependencies

In `DnD-5th-Edition-API/requirements.txt`:

```
-e ../dnd-5e-core
```

### 3. Test the Migration

```bash
cd /Users/display/PycharmProjects/dnd-5e-core
python -m dnd_5e_core.data.collections
```

### 4. Update Documentation

- ✅ README.md in collections/
- ✅ Documented collections.py module
- ✅ This migration guide

---

## 🧪 Tests

```python
# Basic test
from dnd_5e_core.data import get_monsters_list, populate

monsters = get_monsters_list()
assert len(monsters) > 0
print(f"✅ {len(monsters)} monsters loaded")

# Test with populate
spells = populate('spells', 'results')
assert len(spells) > 0
print(f"✅ {len(spells)} spells loaded")

# Test with URLs
weapons = populate('weapons', 'results', with_url=True)
assert all(isinstance(w, tuple) and len(w) == 2 for w in weapons)
print(f"✅ {len(weapons)} weapons with URLs loaded")
```

---

## 📖 Documentation

- **Collections README:** `/collections/README.md`
- **Python module:** `/dnd_5e_core/data/collections.py`
- **This guide:** `/docs/COLLECTIONS_MIGRATION.md`

---

## ✅ Migration Checklist

- [x] Create the `collections/` folder in dnd-5e-core
- [x] Copy all JSON files
- [x] Create `collections/README.md`
- [x] Create `dnd_5e_core/data/collections.py`
- [x] Update `dnd_5e_core/data/__init__.py`
- [x] Create this migration guide
- [ ] Update `populate_functions.py` in DnD-5th-Edition-API
- [ ] Test import in DnD-5th-Edition-API
- [ ] Update CHANGELOG.md

---

## 🔍 Troubleshooting

### Error: "Collections directory not found"

**Solution:**
```python
from dnd_5e_core.data import set_collections_directory
set_collections_directory('/path/to/dnd-5e-core/collections')
```

### Import Error

**Solution:**
```bash
# Install dnd-5e-core in development mode
cd /Users/display/PycharmProjects/dnd-5e-core
pip install -e .
```

### Collections Not Loading

**Verification:**
```python
from dnd_5e_core.data import get_collections_directory
print(get_collections_directory())
```

---

**Status:** ✅ **MIGRATION COMPLETED**

**Next step:** Update DnD-5th-Edition-API to use collections from dnd-5e-core
