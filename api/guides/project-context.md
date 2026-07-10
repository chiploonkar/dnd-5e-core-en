# CONTEXT SUMMARY - D&D 5e Projects

**Date:** December 23, 2025
**Analyst:** GitHub Copilot

---

## Overview

### 3 Interconnected Projects

1. **dnd-5e-core** - Python package with all D&D 5e logic (UI-agnostic)
2. **DnD-5th-Edition-API** - Multiple game interfaces (Console, PyQt5, Pygame, Ncurses, 3D)
3. **DnD-5e-ncurses** - Simplified ncurses game with dungeons and combats

---

## 📦 1. dnd-5e-core (Core Package)

### Description
Standalone Python package containing **all D&D 5e business logic**, without UI dependencies.

### Main Content
- **Python Code:**
  - `entities/` - Monster, Character, Sprite
  - `classes/` - Character classes (Wizard, Fighter, etc.)
  - `races/` - Races and subraces
  - `equipment/` - Weapons, armors, potions
  - `spells/` - Spell system and slots
  - `combat/` - Combat system and actions
  - `abilities/` - Ability scores and saving throws
  - `mechanics/` - Basic mechanics (dice, etc.)
  - `data/` - Data loading modules

- **JSON Data (8.7 MB, 2000+ files):**
  - `data/monsters/` - 332 monsters
  - `data/spells/` - 319 spells
  - `data/weapons/` - 65 weapons
  - `data/armors/` - 30 armors
  - `data/equipment/` - 237 equipment items
  - And 22+ other categories

- **Collections (26 files):**
  - `collections/` - D&D 5e API index
  - ~2800+ indexed entries
  - `data/collections.py` module for loading

### Key Features
- Auto-detection of `data/` and `collections/` directories
- `populate()` function compatible with old code
- Convenience functions (`get_monsters_list()`, etc.)
- Automatic fallback to `DnD-5th-Edition-API`
- 100% backward compatible

### Current Status
- Code migration COMPLETED (December 2024)
- Data migration COMPLETED (December 2024)
- Collections migration COMPLETED (December 2025)
- Tests 7/7 PASSED
- Version 0.1.0 in preparation

---

## 🎮 2. DnD-5th-Edition-API (Game Interfaces)

### Description
Main project containing **7 different interfaces** to play D&D 5e, using the `dnd-5e-core` package.

### Available Interfaces

#### a) Console Version (main.py)
- Full text version with all D&D 5e rules
- Character creation, combat, exploration
- **Files:** `main.py`, `main_v2.py`

#### b) PyQt5 Version (pyQTApp/wizardry.py)
- Qt Designer graphical interface
- All features except training grounds
- **Files:** `pyQTApp/wizardry.py`, `pyQTApp/wizardry_v2.py`

#### c) Ncurses Version (main_ncurses_v2_FULL.py)
- Complete textual interface (2783 lines)
- Castle, inn, temple, shop, dungeons
- Inventory, combat, character creation
- **Files:** `main_ncurses.py`, `main_ncurses_v2.py`, `main_ncurses_v2_FULL.py`

#### d) Pygame Dungeon Explorer
- Dungeon exploration with a 2D view
- Spells, inventory, combat (D&D 5e rules)
- **Files:** `dungeon_pygame.py`, `dungeon_pygame_v2.py`, `dungeon_menu_pygame.py`, `dungeon_menu_pygame_v2.py`

#### e) 3D Dungeon Explorer (dungeon_3d.py)
- First-person 3D raycasting
- Procedural dungeon generation
- Real-time combat with projectiles
- Mini-map, potions, enemy AI
- **File:** `tools/dungeon_perl/dungeon_3d.py`

#### f) RPG Pygame Demo (rpg_pygame.py)
- Basic demo with collision detection
- Inspired by Simplon gamejam

#### g) Tkinter Version (dungeon_tk.py)
- Simplified arena with basic D&D rules
- One character, multi-level exploration

### Key Files Modified
- **populate_functions.py** - Updated to use `dnd-5e-core`
  - `populate()` function with automatic fallback
  - Import of `dnd_5e_core.data.populate` if available
  - Tests: `test_populate_migration.py`

### Current Status
- 7 functional game versions
- v2 versions use `dnd-5e-core`
- `populate_functions.py` adapted
- Migration tests passed
- Local collections kept (fallback)

---

## 🏰 3. DnD-5e-ncurses (Simplified Game)

### Description
Standalone and simple ncurses game with heroes, dungeons, combat, and shop.

### Features
- **Main menu:** Castle or Dungeon
- **Dungeon:** Random encounters, turn-based combat
- **Castle (Shop):** Buying/selling weapons and armor
- **Inventory:** Weapons, armors, potions
  - Key `e`: equip/unequip
  - Key `p`: drink potion
- **Save:** Automatic JSON save (`save_player.json`)

### Architecture
- `entities.py` - Entity, Player, Monster, weapons, armors, potions
- `game.py` - Game logic, combat, encounters
- `ui_curses.py` - Ncurses interface (menus, inventory, shop)
- `main.py` - Entry point
- `starter.py` - POC/demo

### Current Status
- Functional and complete game
- Inventory system with equipment
- Shop with buying/selling
- Automatic save
- Independent of `dnd-5e-core` (for now)

---

## Development History

### December 2024
1. **Code Migration** - Extraction of `dao_classes` to `dnd-5e-core`
2. **Data Migration** - 2000+ JSON files to `dnd-5e-core`
3. **v2 Versions Creation** - 7 games migrated to `dnd-5e-core`
4. **Bug Fixes** - Combat messages, empty corridor, shop items
5. **Documentation Archival** - 51 archived files

### December 2025
6. **Collections Migration** - 26 JSON files to `dnd-5e-core`
7. **`collections.py` Module** - New module with `populate()`
8. **`populate_functions.py` Adaptation** - Use of `dnd-5e-core`
9. **Tests & Documentation** - 7/7 tests passed, complete docs

---

## Statistics

### dnd-5e-core
- **Code:** ~5000+ Python lines
- **Data:** 8.7 MB, 2000+ JSON files
- **Collections:** 26 files, ~2800 entries
- **Tests:** 7/7 passed

### DnD-5th-Edition-API
- **Interfaces:** 7 different versions
- **Python Files:** 50+ files
- **Documentation:** 60+ markdown files

### DnD-5e-ncurses
- **Files:** 5 main files
- **Lines:** ~1500 Python lines
- **Save:** JSON

---

## Current Development Status

### Completed
- [x] Code migration to `dnd-5e-core`
- [x] JSON data migration to `dnd-5e-core`
- [x] Collections migration to `dnd-5e-core`
- [x] `populate_functions.py` adaptation
- [x] Auto-detection of directories
- [x] Validation tests (7/7)
- [x] Complete documentation

### In Progress
- [ ] Automated unit tests (pytest)
- [ ] `dnd-5e-core` package publication
- [ ] CI/CD integration

### Next Steps
- [ ] Test all games with the new `populate()`
- [ ] Deprecate local collections
- [ ] `dnd-5e-core` version 0.1.0
- [ ] `DnD-5e-ncurses` integration with `dnd-5e-core` (optional)

---

## 🔧 Technical Structure

### Dependencies
```
DnD-5e-ncurses (standalone)
    └── curses, json

DnD-5th-Edition-API
    └── dnd-5e-core (optional, with fallback)
        └── Python stdlib + JSON data

dnd-5e-core (standalone)
    └── Python stdlib
```

### Data Flow
```
1. Collections (dnd-5e-core/collections/)
   → collections.py module
   → populate() function
   → DnD-5th-Edition-API (via populate_functions.py)

2. Data (dnd-5e-core/data/)
   → loader.py module
   → load_monster(), load_spell(), etc.
   → DnD-5th-Edition-API (via direct imports)

3. Game Logic (dnd-5e-core/entities/, classes/, etc.)
   → Character, Monster, Weapon, etc.
   → DnD-5th-Edition-API (v2 versions)
```

---

## Available Documentation

### dnd-5e-core
- `README.md` - Overview and quick start
- `CHANGELOG.md` - Version history
- `QUICK_START_DATA.md` - Data guide
- `data/README.md` - Data documentation
- `collections/README.md` - Collections documentation
- `docs/COLLECTIONS_MIGRATION.md` - Migration guide
- `docs/COLLECTIONS_COMPLETE.md` - Migration summary
- `docs/PROJETS_ADAPTATION.md` - Project adaptation
- `docs/archive/` - Historical documentation

### DnD-5th-Edition-API
- `README.md` - 7 versions overview
- `CHANGELOG.md` - History (updated)
- `HISTORIQUE_DEVELOPPEMENT.md` - Detailed history
- `manual/` - Manuals for each version
- `docs/archive/` - 51 archived files

### DnD-5e-ncurses
- `README.md` - Description and gameplay
- `CONTRIBUTING.md` - Contribution guide
- Specific markdown files (navigation, inventory, etc.)

---

## Conclusion

### Strengths
- Modular and clear architecture
- Successful UI/Logic separation
- Reusable `dnd-5e-core` package
- 7 different functional interfaces
- Robust auto-detection and fallbacks
- Exhaustive documentation
- Validation tests passed

### Recommended Next Actions
1. Test all games with migrated `populate()`
2. Create automated unit tests (pytest)
3. Publish `dnd-5e-core` v0.1.0
4. Clean up local collections (after transition)
5. Consider integrating `DnD-5e-ncurses` with `dnd-5e-core`

---

**Summary:** Complete D&D 5e ecosystem with a reusable core package, multiple game interfaces, complete integrated data, and successful collections migration. Ready for use and evolution!

---

**Summary date:** December 23, 2025
**Status:** **COMPLETE CONTEXT ANALYZED**
