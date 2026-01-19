# ⚡ Quick Start - Conditions System v0.2.4

## 🎯 En 30 Secondes

### Monstres appliquent des conditions automatiquement
```python
from dnd_5e_core.data import load_monster

spider = load_monster('giant-spider')
spider.attack(fighter)  # ← Applique "Restrained" automatiquement !
```

### Objets magiques avec conditions
```python
from dnd_5e_core.equipment import create_wand_of_paralysis

wand = create_wand_of_paralysis()
wand.perform_action(wand.actions[0], target=goblin, user=wizard)
# ← Goblin est paralysé !
```

### Parser des descriptions personnalisées
```python
from dnd_5e_core.combat import ConditionParser

conditions = ConditionParser.parse_condition_from_description(
    "DC 15 Constitution save or be paralyzed"
)
# ← [Condition(Paralyzed, DC 15 CON)]
```

## 📚 Documentation

- **Résumé complet**: `FINAL_SUMMARY_v0.2.4.md`
- **Guide détaillé**: `docs/CONDITIONS_SYSTEM.md`
- **Index**: `INDEX_v0.2.4.md`

## 🧪 Tests

```bash
python quick_validate_conditions.py
```

## ✨ Nouveautés

- ✅ 9 conditions D&D 5e supportées
- ✅ Parsing automatique des monstres
- ✅ 5 objets magiques prédéfinis
- ✅ Application automatique en combat
- ✅ ~1500 lignes de code
- ✅ ~2000 lignes de documentation

**Version**: 0.2.4 | **Date**: 18 Jan 2026 | **Status**: ✅ Production Ready
