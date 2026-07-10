# 🚀 Migration Plan - dao_classes.py → dnd-5e-core

## ✅ Progress

Start date: December 23, 2024
Total estimated time: 11-15 hours

---

## 📊 Phase 1: Base Classes Extraction (IN PROGRESS)

### ✅ Entities

- [x] **Sprite** → `dnd_5e_core/entities/sprite.py` ✅ DONE
  - Base class for Monster and Character
  - pygame code removed (draw, draw_effect)
  - Base methods preserved (pos, check_collision, move)

- [ ] **Monster** → `dnd_5e_core/entities/monster.py` 🔄 IN PROGRESS
  - Depends on: Sprite, Abilities, Proficiency, Action, SpecialAbility, SpellCaster
  - ~150 lines of code
  - Clean cprint()

- [ ] **Character** → `dnd_5e_core/entities/character.py`
  - Depends on: Sprite, Race, ClassType, Abilities, Equipment, SpellCaster, Condition
  - ~600 lines of code
  - Clean cprint()

### 📋 Equipment (High Priority - Heavily Used)

- [ ] **EquipmentCategory** → `dnd_5e_core/equipment/equipment.py`
- [ ] **Cost** → `dnd_5e_core/equipment/equipment.py`
- [ ] **Equipment** → `dnd_5e_core/equipment/equipment.py`
  - Base class for Weapon, Armor, Potion

- [ ] **Weapon** → `dnd_5e_core/equipment/weapon.py`
  - Depends on: Equipment, WeaponProperty, DamageType, DamageDice, WeaponRange
  - ~50 lines
  
- [ ] **Armor** → `dnd_5e_core/equipment/armor.py`
  - Depends on: Equipment
  - ~30 lines

- [ ] **Potion** → `dnd_5e_core/equipment/potion.py`
  - HealingPotion, SpeedPotion, StrengthPotion
  - ~100 lines total

- [ ] **Inventory** → `dnd_5e_core/equipment/inventory.py`

---

## 📊 Phase 2: Support Classes

### 🧬 Abilities

- [ ] **Abilities** → `dnd_5e_core/abilities/abilities.py`
  - STR, DEX, CON, INT, WIS, CHA
  - ~50 lines

### 🎲 Mechanics  

- [ ] **DamageDice** → `dnd_5e_core/mechanics/dice.py`
  - Used everywhere
  - ~30 lines

### 🏛️ Races

- [ ] **Language** → `dnd_5e_core/races/language.py`
- [ ] **Trait** → `dnd_5e_core/races/trait.py`
- [ ] **SubRace** → `dnd_5e_core/races/subrace.py`
- [ ] **Race** → `dnd_5e_core/races/race.py`

### 🎓 Classes

- [ ] **ProfType** (Enum) → `dnd_5e_core/classes/proficiency.py`
- [ ] **Proficiency** → `dnd_5e_core/classes/proficiency.py`
- [ ] **ClassType** → `dnd_5e_core/classes/class_type.py`
- [ ] **MultiClassing** → `dnd_5e_core/classes/multiclass.py`

---

## 📊 Phase 3: Combat System

### ⚔️ Combat

- [ ] **ActionType** (Enum) → `dnd_5e_core/combat/action.py`
- [ ] **Damage** → `dnd_5e_core/combat/damage.py`
- [ ] **DamageType** → `dnd_5e_core/combat/damage.py`
- [ ] **Action** → `dnd_5e_core/combat/action.py`
- [ ] **SpecialAbility** → `dnd_5e_core/combat/special_ability.py`
- [ ] **Condition** → `dnd_5e_core/combat/condition.py`

---

## 📊 Phase 4: Spellcasting System

### ✨ Spells

- [ ] **Spell** → `dnd_5e_core/spells/spell.py`
- [ ] **SpellCaster** → `dnd_5e_core/spells/spellcaster.py`
- [ ] **SpellSlot** → `dnd_5e_core/spells/spell_slots.py`

---

## 📊 Phase 5: Extraction of populate_functions.py

### 📦 Data Loaders

- [ ] **populate()** → `dnd_5e_core/data/loader.py`
- [ ] **request_monster()** → `dnd_5e_core/data/loader.py`
- [ ] **request_weapon()** → `dnd_5e_core/data/loader.py`
- [ ] **request_armor()** → `dnd_5e_core/data/loader.py`
- [ ] **request_spell()** → `dnd_5e_core/data/loader.py`
- [ ] All other request_* functions

---

## 📊 Phase 6: Updating Imports

### Files to Modify (15+)

#### Games
- [ ] `main.py`
- [ ] `main_ncurses.py`
- [ ] `dungeon_pygame.py`
- [ ] `dungeon_menu_pygame.py`
- [ ] `boltac_tp_pygame.py`
- [ ] `pyQTApp/wizardry.py`
- [ ] `pyQTApp/common.py`
- [ ] `pyQTApp/Castle/Boltac_module.py`
- [ ] `pyQTApp/Castle/Cant_module.py`
- [ ] `pyQTApp/Castle/Inn_module.py`
- [ ] `pyQTApp/EdgeOfTown/Combat_module.py`

#### Support
- [ ] `populate_functions.py`
- [ ] `populate_rpg_functions.py`

---

## 📊 Phase 7: Testing and Validation

- [ ] Unit tests for Sprite
- [ ] Unit tests for Monster
- [ ] Unit tests for Character
- [ ] Unit tests for Weapon/Armor
- [ ] Unit tests for Combat system
- [ ] Unit tests for Spell system
- [ ] Integration tests for main.py
- [ ] Integration tests for main_ncurses.py
- [ ] Integration tests for dungeon_pygame.py
- [ ] Integration tests for pyQTApp/wizardry.py

---

## 🎯 Current Status

**Date**: December 23, 2024, 17:30

### ✅ Done
1. dnd-5e-core structure created ✅
2. Sprite extracted and cleaned ✅

### 🔄 In Progress
3. Creation of the migration plan (this document)

### 📋 To Do
4. Extract base classes (Equipment, DamageDice, Abilities)
5. Extract Monster
6. Extract Character
7. Extract other classes
8. Update imports
9. Test

---

## 📝 Notes

### Priority Classes (Most Used)

According to DEPENDENCY_MAP.md:

1. **Character** - 8+ uses
2. **Weapon** - 6+ uses
3. **Armor** - 6+ uses
4. **Monster** - 5+ uses
5. **Equipment** - 4+ uses
6. **HealingPotion** - 4+ uses

### Strategy

1. ✅ Start with Sprite (base class)
2. Extract Equipment, Weapon, Armor, Potion (heavily used, relatively simple)
3. Extract DamageDice, Abilities (dependencies of Monster/Character)
4. Extract Monster (complex but essential)
5. Extract Character (most complex)
6. Extract the rest (Races, Classes, Spells, Combat)
7. Extract populate_functions.py
8. Update all imports
9. Test each game

---

## 🚧 Potential Problems

### Circular Dependencies

- Monster imports Character (for attack)
- Character imports Monster (for kills list)
- Solution: Use `from __future__ import annotations` and quotes for types

### Mixed UI Code

- cprint() everywhere
- color.RED, color.END
- pygame.mixer.Sound
- Solution: Remove or comment out, only return data

### Relative Imports

- from tools.common import cprint
- Solution: Remove UI imports, keep only data imports

---

## ⏱️ Revised Time Estimation

| Phase | Initial Estimate | Real Time | Status |
|-------|---------------------|------------|--------|
| Phase 1: Base classes | 3-4h | ? | 🔄 |
| Phase 2: Support classes | 2h | ? | ⏸️ |
| Phase 3: Combat system | 2h | ? | ⏸️ |
| Phase 4: Spell system | 2h | ? | ⏸️ |
| Phase 5: Data loaders | 2h | ? | ⏸️ |
| Phase 6: Update imports | 2-3h | ? | ⏸️ |
| Phase 7: Tests | 2-3h | ? | ⏸️ |
| **TOTAL** | **15-17h** | **?** | 🔄 |

---

## 📞 Next Action

✅ Continue extracting classes in this order:

1. Equipment (base class)
2. DamageDice
3. Weapon
4. Armor
5. Potion (Healing, Speed, Strength)
6. Abilities
7. Monster
8. Character

Each class will be cleaned (UI code removed) and documented.
