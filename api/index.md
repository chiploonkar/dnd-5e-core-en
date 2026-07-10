# 📚 dnd-5e-core Documentation

Welcome to the **dnd-5e-core** package documentation!

## 📖 Main Documentation

### Essentials
- **[README.md](../README.md)** - Package overview and usage guide
- **[AI_AGENT_GUIDE.md](https://github.com/codingame-team/dnd-5e-core/blob/main/AI_AGENT_GUIDE.md)** - 🤖 **Complete guide for agentic AIs**
- **[CHANGELOG.md](https://github.com/codingame-team/dnd-5e-core/blob/main/CHANGELOG.md)** - Version history and changes
- **[CONTRIBUTING.md](https://github.com/codingame-team/dnd-5e-core/blob/main/CONTRIBUTING.md)** - Guide to contributing to the project
- **[QUICK_START_DATA.md](https://github.com/codingame-team/dnd-5e-core/blob/main/archive/QUICK_START_DATA.md)** - Quick start with data

### AI Documentation
- **[AI_AGENT_GUIDE.md](https://github.com/codingame-team/dnd-5e-core/blob/main/AI_AGENT_GUIDE.md)** - Complete guide for AI integration (100+ examples)
- **[.copilot-instructions.md](https://github.com/codingame-team/dnd-5e-core/blob/main/archive/2026-02-obsolete/copilot-instructions.md)** - Instructions for GitHub Copilot

### Data
- **[data/README.md](https://github.com/codingame-team/dnd-5e-core/tree/main/dnd_5e_core/data)** - JSON data content documentation (2000+ files)
- **[collections/README.md](https://github.com/codingame-team/dnd-5e-core/blob/main/collections/README.md)** - API index collections documentation

---

## 🔄 Migration Documentation

### Collections Migration (December 2025)
- **[COLLECTIONS_MIGRATION.md](../docs.en/COLLECTIONS_MIGRATION.md)** - Collections migration guide
- **[COLLECTIONS_COMPLETE.md](../docs.en/COLLECTIONS_COMPLETE.md)** - Complete migration summary

### Data Migration (December 2024)
See the `archive/migration/` directory for historical data migration documentation.

---

## 📁 Package Structure

```
dnd-5e-core/
├── collections/              # D&D 5e API collections index
│   ├── README.md            # Collections documentation
│   └── *.json               # 26 index files (monsters, spells, etc.)
│
├── data/                    # D&D 5e JSON data (2000+ files)
│   ├── README.md            # Data documentation
│   ├── monsters/            # 332 monsters
│   ├── spells/              # 319 spells
│   ├── weapons/             # 65 weapons
│   └── ...                  # 24+ other categories
│
├── dnd_5e_core/             # Package source code
│   ├── abilities/           # Ability score system
│   ├── classes/             # Character classes
│   ├── combat/              # Combat system
│   ├── data/                # Data loading
│   │   ├── loader.py        # Loading data/ files
│   │   ├── collections.py   # Loading collections/ files
│   │   └── __init__.py      # Public API
│   ├── entities/            # Entities (Monster, Character, etc.)
│   ├── equipment/           # Equipment and items
│   ├── mechanics/           # Game mechanics (dice, etc.)
│   ├── races/               # Races and subraces
│   ├── spells/              # Spell system
│   └── utils/               # Utilities
│
├── tests/                   # Unit tests
│
└── docs/                    # Documentation (you are here!)
    ├── README.md            # This file
    ├── COLLECTIONS_MIGRATION.md
    ├── COLLECTIONS_COMPLETE.md
    └── archive/             # Historical documentation
```

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd dnd-5e-core

# Install in development mode
pip install -e .
```

### Basic Usage

```python
# Load data
from dnd_5e_core.data import load_monster, load_spell

goblin = load_monster('goblin')
fireball = load_spell('fireball')

# Load collections
from dnd_5e_core.data import get_monsters_list, get_spells_list

all_monsters = get_monsters_list()
all_spells = get_spells_list()

# Create entities
from dnd_5e_core.entities import Monster, Character
from dnd_5e_core.races import Race

monster = Monster.from_json_data(goblin)
character = Character(name="Aragorn", race=Race(...))
```

---

## 📊 Package Content

### Collections (26 files)
- **332 monsters** indexed
- **319 spells** indexed
- **12 character** classes
- **9 playable** races
- **237 equipment** items indexed
- And much more...

### Data (2000+ JSON files)
- Full details of all monsters
- Full descriptions of all spells
- Statistics for all weapons and armor
- Full game rules
- And much more...

### Python Code
- **Entities** - Complete entity system
- **Combat** - Combat system with actions
- **Spells** - Spell system and slots
- **Equipment** - Equipment management
- **Mechanics** - Core mechanics (dice, checks, etc.)
- **Data Loaders** - Automatic data loading

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run a specific test
pytest tests/test_data_loader.py

# With coverage
pytest --cov=dnd_5e_core
```

---

## 📝 Guides and Tutorials

### For Developers
- **[CONTRIBUTING.md](https://github.com/codingame-team/dnd-5e-core/blob/main/CONTRIBUTING.md)** - How to contribute
- **Migration from DnD-5th-Edition-API** - See `COLLECTIONS_MIGRATION.md`

### For Users
- **[QUICK_START_DATA.md](https://github.com/codingame-team/dnd-5e-core/blob/main/archive/QUICK_START_DATA.md)** - Quick start guide
- **[data/README.md](https://github.com/codingame-team/dnd-5e-core/tree/main/dnd_5e_core/data)** - Data documentation
- **[collections/README.md](https://github.com/codingame-team/dnd-5e-core/blob/main/collections/README.md)** - Collections documentation

---

## 🗂️ Archive

Historical development documentation is archived in `archive/`:

### Migrations
- **DATA_MIGRATION_COMPLETE.md** - JSON data migration
- **MIGRATION_COMPLETE.md** - Migration finalization
- **MIGRATION_GUIDE.md** - Migration guide
- **MIGRATION_STATUS.md** - Migration status

### Progression
- **PROJECT_COMPLETE.md** - Project completion
- **COMBAT_SPELLS_COMPLETE.md** - Combat system and spells
- **DATA_LOADERS_CORRECTED.md** - Loader corrections

See **[archive/README.md](../docs.en/archive/README.md)** for more details.

---

## 🔗 Useful Links

### D&D 5e Resources
- [D&D 5e API](https://www.dnd5eapi.co/) - Source of data
- [Open Gaming License](https://dnd.wizards.com/resources/systems-reference-document) - OGL License

### Related Projects
- **DnD-5th-Edition-API** - Project using dnd-5e-core
- **DnD-5e-ncurses** - ncurses interface for D&D 5e

---

## 📅 Version History

See **[CHANGELOG.md](https://github.com/codingame-team/dnd-5e-core/blob/main/CHANGELOG.md)** for full version history.

### Current Version: Unreleased

Latest features:
- ✅ Collections migration (December 2025)
- ✅ `collections.py` module to manage indexes
- ✅ Convenience functions for quick access
- ✅ Automatic path detection

---

## 🤝 Contributing

Contributions are welcome! See **[CONTRIBUTING.md](https://github.com/codingame-team/dnd-5e-core/blob/main/CONTRIBUTING.md)** for more details.

### Contribution Process
1. Fork the project
2. Create a branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project uses data under the **Open Gaming License (OGL)** and **System Reference Document (SRD)**.

---

## 📧 Contact

For any questions or suggestions, please feel free to open an issue on the GitHub repository.

---

**Last Updated:** December 23, 2025
