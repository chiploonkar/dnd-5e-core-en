# Contributing to dnd-5e-core

Thank you for your interest in contributing!

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```
3. Install in development mode:
   ```bash
   pip install -e .[dev]
   ```

## Coding Standards

- Follow PEP 8 style guide
- Use type hints for all function signatures
- Write docstrings for all public functions/classes (Google style)
- Keep UI logic OUT of this package (this is core logic only)
- Add tests for new features

## Type Hints Example

```python
from typing import List, Optional
from dnd_5e_core.entities import Character, Monster

def attack(attacker: Character, defender: Monster, action_index: int = 0) -> int:
    """
    Perform an attack from attacker to defender.

    Args:
        attacker: The character performing the attack
        defender: The target monster
        action_index: Index of action to use (default: 0)

    Returns:
        Total damage dealt to defender

    Raises:
        ValueError: If action_index is invalid
    """
    pass
```

## Testing

Run tests before submitting:
```bash
pytest tests/ -v
```

Check coverage:
```bash
pytest tests/ --cov=dnd_5e_core --cov-report=html
```

## Adding New Features

1. Create feature branch: `git checkout -b feature/my-feature`
2. Implement feature with tests
3. Ensure all tests pass
4. Run linting: `black dnd_5e_core/` and `flake8 dnd_5e_core/`
5. Update documentation if needed
6. Submit pull request

## Project Structure

```
dnd_5e_core/
├── entities/       # Monster, Character, Sprite
├── races/          # Race, SubRace, Trait, Language
├── classes/        # ClassType, Proficiency
├── equipment/      # Weapon, Armor, Potion, Inventory
├── spells/         # Spell, SpellCaster, SpellSlots
├── combat/         # Action, SpecialAbility, Condition, CombatSystem
├── abilities/      # Abilities, SavingThrow, Skill
├── mechanics/      # Dice, CR, XP, LevelUp
├── data/           # API loader, serialization
└── utils/          # Helpers, constants
```

## Pull Request Process

1. Create a feature branch
2. Make your changes
3. Add/update tests
4. Run tests and linting
5. Update CHANGELOG.md
6. Submit pull request with clear description


## CHANGELOG & Release checklist

Please update `CHANGELOG.md` for every release. This repository follows the "Keep a Changelog" format. The CI will enforce that the changelog contains an entry for the version declared in `pyproject.toml` before merging/publishing.

What to do before publishing:

- Bump the version in `pyproject.toml`, `setup.py` (if used), and `dnd_5e_core/__init__.py` to the same value.
- Add a section in `CHANGELOG.md` for the new version using the format below.
- Commit the changes and open a PR. The GitHub Actions workflow `.github/workflows/check-changelog.yml` will verify the changelog entry automatically.

Example changelog entry (copy/paste):

```
## [0.4.2] - 2026-01-22

### Added
- Short description of the change.

### Fixed
- Short description of the fix.
```

If the release contains no notable changes, add a short note under the version header (e.g. "No notable changes").

Local checks you can run:

```bash
# Verify the changelog contains an entry for the current version
python3 scripts/check_changelog.py

# Build and test locally before publishing
./build_package.sh --clean --build
```

Notes:

- The scripts `build_package.sh` and `publish_final.sh` also run the changelog check and will fail if the changelog does not contain the expected version header.
- The CI workflow will block merges to `main` if the changelog check fails; please ensure your PR updates the changelog accordingly.

## Code of Conduct

Be respectful and inclusive. We welcome contributions from everyone.

## Questions?

Open an issue for discussion before starting major changes.
