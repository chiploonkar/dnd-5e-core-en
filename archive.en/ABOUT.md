# About dnd-5e-core

## 📖 Description

**dnd-5e-core** is a comprehensive Python package that implements all core mechanics of Dungeons & Dragons 5th Edition. It provides a complete rules engine that is UI-agnostic, allowing you to build any type of D&D application (web, desktop, CLI, game) on top of it.

## 🎯 Key Features

- **Complete D&D 5e Implementation**: All core rules, mechanics, and calculations
- **8.7 MB of Bundled Data**: 332 monsters, 319 spells, equipment, and more
- **Offline-Ready**: No external APIs or databases required
- **UI-Agnostic**: Use with pygame, web frameworks, CLI, or any interface
- **Type-Annotated**: Full type hints for better IDE support
- **Well-Tested**: Comprehensive test suite

## 📦 What's Included

### Game Data (2000+ JSON Files)
- 🐉 **332 Monsters** - Complete stat blocks with actions and abilities
- ✨ **319 Spells** - All spell details, ranges, and effects
- ⚔️ **65 Weapons** - With properties, damage, and ranges
- 🛡️ **30 Armors** - AC calculations and armor types
- 🎒 **237 Equipment Items** - Adventuring gear and tools
- 🏃 **16 Races & 24 Subraces** - With traits and ability bonuses
- 👤 **13 Classes & 46 Subclasses** - With features and spellcasting
- 🎲 **Complete Rules** - Skills, conditions, damage types, etc.

### Core Modules
- **Entities**: Monster and Character classes
- **Combat**: Actions, attacks, damage, conditions
- **Spells**: Spellcasting system with spell slots
- **Equipment**: Weapons, armor, potions, magic items
- **Abilities**: Six core abilities with modifiers
- **Mechanics**: Dice rolling, XP, challenge rating
- **Data**: JSON loading and serialization

## 🚀 Installation

```bash
pip install dnd-5e-core
```

## 💻 Quick Start

```python
from dnd_5e_core.data import load_monster, load_spell

# Load a monster
goblin = load_monster('goblin')
print(f"{goblin['name']} - HP: {goblin['hit_points']}, CR: {goblin['challenge_rating']}")

# Load a spell
fireball = load_spell('fireball')
print(f"{fireball['name']} - Level {fireball['level']}, {fireball['damage']['damage_type']['name']}")
```

## 🎮 Use Cases

- **Game Development**: Build D&D video games or digital tools
- **Virtual Tabletops**: Create online D&D platforms
- **Character Managers**: Build character sheet applications
- **Combat Trackers**: Develop initiative and combat tools
- **DM Tools**: Create dungeon master aids and generators
- **Discord Bots**: Make D&D-themed bots
- **Educational**: Learn Python and game development

## 🛠️ Technology

- **Language**: Python 3.10+
- **Dependencies**: numpy, requests
- **License**: MIT
- **Type Hints**: Full type annotations
- **Testing**: pytest with comprehensive coverage

## 👥 Target Audience

- **Game Developers** building D&D applications
- **Python Developers** interested in RPG mechanics
- **Dungeon Masters** creating digital tools
- **Students** learning game programming
- **Hobbyists** exploring tabletop RPG systems

## 📚 Documentation

- [README.md](README.md) - Full documentation
- [QUICK_START_DATA.md](QUICK_START_DATA.md) - Data usage guide
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

## 🔗 Links

- **PyPI**: https://pypi.org/project/dnd-5e-core/
- **Repository**: https://github.com/codingame-team/dnd-5e-core
- **Issues**: https://github.com/codingame-team/dnd-5e-core/issues
- **Discussions**: https://github.com/codingame-team/dnd-5e-core/discussions

## 🏷️ Topics

`python` `dnd` `dungeons-dragons` `5e` `rpg` `game-engine` `tabletop` `monsters` `spells` `character-sheet` `combat` `dice-roller` `game-development`

## ⚖️ Legal

This project is **not affiliated** with Wizards of the Coast. D&D, Dungeons & Dragons, and their respective logos are trademarks of Wizards of the Coast LLC.

All game data is sourced from the D&D 5e SRD (System Reference Document), which is released under the Open Gaming License v1.0a.

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Made with ❤️ for the D&D community**

