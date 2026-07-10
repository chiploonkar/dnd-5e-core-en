# ⚡ Quick Start - Conditions System v0.2.4

## 🎯 In 30 Seconds

### Monsters apply conditions automatically
```python
from dnd_5e_core.data import load_monster

spider = load_monster('giant-spider')
spider.attack(fighter)  # ← Applies "Restrained" automatically!
```

### Magic items with conditions
```python
from dnd_5e_core.equipment import create_wand_of_paralysis

wand = create_wand_of_paralysis()
wand.perform_action(wand.actions[0], target=goblin, user=wizard)
# ← Goblin is paralyzed!
```

### Parse custom descriptions
```python
from dnd_5e_core.combat import ConditionParser

conditions = ConditionParser.parse_condition_from_description(
    "DC 15 Constitution save or be paralyzed"
)
# ← [Condition(Paralyzed, DC 15 CON)]
```

## 📚 Documentation

- **Complete Summary**: `FINAL_SUMMARY_v0.2.4.md`
- **Detailed Guide**: `docs/CONDITIONS_SYSTEM.md`
- **Index**: `INDEX_v0.2.4.md`

## 🧪 Tests

```bash
python quick_validate_conditions.py
```

## ✨ What's New

- ✅ 9 D&D 5e conditions supported
- ✅ Automatic parsing of monsters
- ✅ 5 predefined magic items
- ✅ Automatic application in combat
- ✅ ~1500 lines of code
- ✅ ~2000 lines of documentation

**Version**: 0.2.4 | **Date**: January 18, 2026 | **Status**: ✅ Production Ready
