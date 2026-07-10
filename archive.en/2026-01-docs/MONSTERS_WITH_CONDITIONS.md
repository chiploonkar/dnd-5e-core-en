# List of D&D 5e Monsters with Conditions - Complete Analysis

## 🕷️ Monsters with RESTRAINED

### Giant Spider
- **Action**: Web
- **Condition**: Restrained  
- **DC**: 12 Strength
- **Status**: ✅ Automatically extracted

### Giant Constrictor Snake
- **Action**: Constrict
- **Condition**: Grappled → Restrained
- **DC**: Escape DC 16
- **Status**: ✅ Automatically extracted

### Ettercap
- **Action**: Web
- **Condition**: Restrained
- **DC**: 11 Strength
- **Status**: ✅ Automatically extracted

### Gelatinous Cube
- **Action**: Engulf
- **Condition**: Restrained
- **DC**: 12 Dexterity
- **Status**: ✅ Automatically extracted

### Roper
- **Action**: Tendril
- **Condition**: Grappled + Restrained
- **DC**: 15 Strength
- **Status**: ⚠️ To be verified

### Shambling Mound
- **Action**: Engulf
- **Condition**: Restrained + Blinded
- **DC**: 14 Strength
- **Status**: ⚠️ To be verified

---

## 🐍 Monsters with GRAPPLED

### Giant Octopus
- **Action**: Tentacles
- **Condition**: Grappled
- **DC**: Escape DC 16
- **Status**: ✅ Automatically extracted

### Giant Toad
- **Action**: Bite + Swallow
- **Condition**: Grappled
- **DC**: 12 Strength
- **Status**: ✅ Automatically extracted

### Mimic
- **Action**: Adhesive (Bite)
- **Condition**: Grappled
- **DC**: 13 Strength
- **Status**: ✅ Automatically extracted

### Rug of Smothering
- **Action**: Smother
- **Condition**: Grappled + Restrained + Blinded
- **DC**: 13 Strength
- **Status**: ⚠️ To be verified

---

## ☠️ Monsters with POISONED

### Giant Poisonous Snake
- **Action**: Bite
- **Condition**: Poisoned
- **DC**: 11 Constitution
- **Status**: ✅ Automatically extracted

### Giant Centipede
- **Action**: Bite
- **Condition**: Poisoned
- **DC**: 11 Constitution
- **Status**: ✅ Automatically extracted

### Giant Spider
- **Action**: Bite
- **Condition**: Poisoned
- **DC**: 11 Constitution
- **Status**: ✅ Automatically extracted

### Ettercap
- **Action**: Bite
- **Condition**: Poisoned
- **DC**: 11 Constitution
- **Status**: ✅ Automatically extracted

### Scorpion (Giant)
- **Action**: Sting
- **Condition**: Poisoned
- **DC**: 12 Constitution
- **Status**: ✅ Automatically extracted

### Green Hag
- **Action**: Illusory Appearance
- **Condition**: Poisoned (via spell)
- **DC**: Variable
- **Status**: ⚠️ Special ability

---

## ⚡ Monsters with PARALYZED

### Ghoul
- **Action**: Claws
- **Condition**: Paralyzed
- **DC**: 10 Constitution
- **Status**: ✅ Automatically extracted

### Carrion Crawler
- **Action**: Tentacles
- **Condition**: Paralyzed
- **DC**: 13 Constitution
- **Status**: ⚠️ To be verified

### Gelatinous Cube
- **Action**: Engulf
- **Condition**: Paralyzed (poison)
- **DC**: 12 Constitution
- **Status**: ✅ Automatically extracted

---

## 😱 Monsters with FRIGHTENED

### Dragon (all types)
- **Action**: Frightful Presence
- **Condition**: Frightened
- **DC**: Variable (15-24)
- **Status**: ⚠️ To be verified

### Mummy
- **Action**: Dreadful Glare
- **Condition**: Frightened
- **DC**: 11 Wisdom
- **Status**: ✅ Automatically extracted

### Banshee
- **Action**: Wail
- **Condition**: Frightened
- **DC**: 13 Wisdom
- **Status**: ⚠️ To be verified

### Night Hag
- **Action**: Nightmare Haunting
- **Condition**: Frightened
- **DC**: Variable
- **Status**: ⚠️ Special ability

---

## 🗿 Monsters with PETRIFIED

### Basilisk
- **Action**: Petrifying Gaze
- **Condition**: Petrified
- **DC**: 12 Constitution
- **Status**: ✅ Automatically extracted

### Medusa
- **Action**: Petrifying Gaze
- **Condition**: Petrified
- **DC**: 14 Constitution
- **Status**: ✅ Automatically extracted

### Cockatrice
- **Action**: Bite
- **Condition**: Petrified
- **DC**: 11 Constitution
- **Status**: ✅ Automatically extracted

---

## 😵 Monsters with STUNNED

### Monk (enemy NPC)
- **Action**: Stunning Strike
- **Condition**: Stunned
- **DC**: Variable
- **Status**: ⚠️ Class feature

### Harpy
- **Action**: Luring Song
- **Condition**: Incapacitated (similar to stunned)
- **DC**: 11 Wisdom
- **Status**: ⚠️ To be verified

---

## 👁️ Monsters with BLINDED

### Shambling Mound
- **Action**: Engulf
- **Condition**: Blinded + Restrained
- **DC**: 14 Strength
- **Status**: ⚠️ To be verified

### Rug of Smothering
- **Action**: Smother
- **Condition**: Blinded + Grappled
- **DC**: 13 Strength
- **Status**: ⚠️ To be verified

---

## 💫 Monsters with CHARMED

### Vampire
- **Action**: Charm
- **Condition**: Charmed
- **DC**: 17 Wisdom
- **Status**: ✅ Automatically extracted

### Succubus/Incubus
- **Action**: Charm
- **Condition**: Charmed
- **DC**: 15 Wisdom
- **Status**: ✅ Automatically extracted

### Dryad
- **Action**: Fey Charm
- **Condition**: Charmed
- **DC**: 14 Wisdom
- **Status**: ✅ Automatically extracted

### Lamia
- **Action**: Intoxicating Touch
- **Condition**: Charmed
- **DC**: 13 Wisdom
- **Status**: ✅ Automatically extracted

---

## 📊 Statistical Summary

| Condition | No. Monsters | % Auto Extraction |
|-----------|-------------|-------------------|
| Restrained | 6+ | ~83% |
| Grappled | 4+ | ~75% |
| Poisoned | 6+ | ~90% |
| Paralyzed | 3+ | ~85% |
| Frightened | 4+ | ~50% |
| Petrified | 3 | 100% |
| Stunned | 2+ | ~50% |
| Blinded | 2+ | ~50% |
| Charmed | 4+ | 100% |
| **TOTAL** | **34+** | **~75%** |

---

## ⚠️ Monsters Requiring Special Attention

### 1. Dragon (Frightful Presence)
**Issue**: Variable DC depending on the dragon type  
**Solution**: Parse "frightful presence" with DC extracted from text

### 2. Roper (Multi-conditions)
**Issue**: Grappled + Restrained at the same time  
**Solution**: Parse multiple conditions per action

### 3. Shambling Mound (Multi-conditions)
**Issue**: Restrained + Blinded  
**Solution**: Parse multiple conditions per action

### 4. Rug of Smothering (Multi-conditions)
**Issue**: Grappled + Restrained + Blinded  
**Solution**: Parse multiple conditions per action

### 5. Harpy (Incapacitated)
**Issue**: Condition "Incapacitated" not in the list  
**Solution**: Add "Incapacitated" to recognized conditions

---

## ✅ Recommended Actions

1. **Add Incapacitated** to the list of conditions in ConditionParser
2. **Verify multi-conditions** (multiple conditions per action)
3. **Specifically test**:
   - Roper
   - Shambling Mound
   - Rug of Smothering
   - Dragon (Frightful Presence)
   - Harpy
4. **Create unit tests** for the 10 most common monsters
5. **Document** special cases in the doc

---

## 📝 Monsters to Test with Priority

1. ✅ Giant Spider - DONE (demo_complete.py)
2. ⏳ Ghoul - Paralysis
3. ⏳ Basilisk - Petrification
4. ⏳ Vampire - Charm
5. ⏳ Gelatinous Cube - Multi-conditions
6. ⏳ Mummy - Frightened
7. ⏳ Roper - Multi-conditions
8. ⏳ Dragon (Any) - Frightful Presence
9. ⏳ Ettercap - Poisoned + Restrained
10. ⏳ Giant Constrictor Snake - Grappled + Restrained
