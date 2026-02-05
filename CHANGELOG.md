# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.4] - 2026-02-05

### Added
- **DOCUMENTATION**: Complete AI Agent integration guide
  - New `AI_AGENT_GUIDE.md` - Comprehensive guide for AI agents (100+ code examples)
  - New `.copilot-instructions.md` - Quick reference for GitHub Copilot
  - New `QUICK_START_AI.md` - Quick start guide for AI agents
  - New `archive/AI_DOCUMENTATION_SUMMARY.md` - Documentation summary and metrics
  - Updated README.md with AI agent section
  - Updated INDEX.md with AI documentation links
  - Updated docs/README.md with AI documentation section
  - Covers: Installation, patterns, error handling, integration, debugging
  - 8 modules documented (100%), 100+ code examples, 10 patterns, 7 error solutions
  - 3 advanced use cases (GameEngine, DungeonGenerator, CampaignManager)
  - 3 UI integrations (PyQt, Pygame, Flask)
  - Optimized for AI-assisted development and automated code generation

### Changed
- Archived obsolete documentation files to `archive/2026-02-obsolete/`
  - QUICKFIX_SPELL_SLOTS.md, SPELL_SLOTS_FIX.md, SPELL_SLOTS_SUMMARY.md
  - TESTING_GUIDE.md, GIT_COMMIT_EQUIPMENT_EXPANSION.txt
- Archived obsolete test scripts to `archive/2026-02-obsolete/`
  - test_spell_slots_*.py, validate_spell_slots_fix.py, migrate_spell_slots.py
  - test_game_integration.py, test_new_loaders.py, test_special_monster_actions.py

## [0.4.3] - 2026-02-03

### Fixed
- **CRITICAL**: Fixed KeyError on `spell_slots` during inn rest and level up (2026-02-03)
  - `class_type.spell_slots` now properly initialized with all levels 1-20 in `simple_character_generator()`
  - All spell slot accesses secured with `.get()` and fallback values
  - Affects: main_ncurses.py, main.py, dungeon_pygame.py
  - Migration script available for existing saved characters (`migrate_spell_slots.py`)
  - All tests passing (48 class/level combinations, end-to-end, game integration)
  - See `SPELL_SLOTS_FIX.md` for complete documentation

### Added
- **MAJOR**: Integrated D&D 5e API Collections directory (26 index files)
  - All collection indexes from DnD-5th-Edition-API migrated to dnd-5e-core
  - New `dnd_5e_core.data.collections` module for managing collections
  - Auto-detection of collections directory (no manual configuration needed)
  - Compatible `populate()` function for backward compatibility
  - Convenience functions: `get_monsters_list()`, `get_spells_list()`, etc.
  - Collections README with documentation and examples
- **MAJOR**: Integrated D&D 5e JSON data directory (8.7 MB, 2000+ files)
  - All monster, spell, weapon, armor, class, and race data now included in package
  - Auto-detection of data directory (no manual configuration needed)
  - 27 categories of D&D 5e content (monsters, spells, weapons, etc.)
- Initial package structure
- Entity system (Monster, Character, Sprite)
- Race and SubRace system
- Class system with proficiencies
- Equipment system (Weapon, Armor, Potion)
- Spellcasting system with spell slots
- Combat system with actions and special abilities
- Abilities and saving throws
- Dice mechanics
- Data loader from local JSON files (migrated from API)
- JSON serialization

### Changed
- **BREAKING**: Data loader now auto-detects `dnd-5e-core/data` directory
- **IMPROVED**: `set_data_directory()` is now optional (auto-detection first)
- **IMPROVED**: Collections loader auto-detects `dnd-5e-core/collections` directory
- Data loader priority: 1) dnd-5e-core/data, 2) DnD-5th-Edition-API/data (fallback), 3) ./data
- Collections loader priority: 1) dnd-5e-core/collections, 2) DnD-5th-Edition-API/collections (fallback), 3) ./collections

### Migration Notes
- See `DATA_MIGRATION_COMPLETE.md` for full migration documentation
- All v2 game files updated to use auto-detection
- Backward compatibility maintained with fallback to old data location

## [0.1.0] - 2025-01-XX

### Added
- First alpha release
- Core D&D 5e mechanics implementation
