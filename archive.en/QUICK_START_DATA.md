# 🚀 Quick Start - D&D 5e Data
The `dnd-5e-core` package now includes **all D&D 5e data**!
## ✅ No More Configuration Needed
Before, you had to manually configure the data directory:
```python
# ❌ OLD CODE - No longer necessary!
from dnd_5e_core.data import set_data_directory
set_data_directory('/path/to/data')
```
Now, everything works **automatically**:
```python
# ✅ NEW CODE - Works out of the box!
from dnd_5e_core.data import load_monster
goblin = load_monster('goblin')
```
---
## 📖 Usage Examples
### Load a Monster
```python
from dnd_5e_core.data import load_monster
goblin = load_monster('goblin')
print(f"Name: {goblin['name']}")           # Goblin
print(f"HP: {goblin['hit_points']}")      # 7
print(f"AC: {goblin['armor_class']}")     # 15
print(f"CR: {goblin['challenge_rating']}")# 0.25
print(f"XP: {goblin['xp']}")              # 50
```
### List All Monsters
```python
from dnd_5e_core.data import list_monsters
monsters = list_monsters()
print(f"Total: {len(monsters)} monsters")  # 332
# Display the first 10
for monster_index in monsters[:10]:
    print(f"- {monster_index}")    print(f"- {monster_index}")    print(f"- {monster_indimport load_spell
fireball = load_spell('fireball')
print(f"Spell: {fireball['name']}")       # Fireball
print(f"Level: {fireball['level']}")    # 3
print(f"School: {fireball['school']['name']}")  # Evocation
print(f"Range: {fireball['range']}")    # 150 feet
```
### Load a Weapon
```python
from dnd_5e_core.data import load_weapon
longsword = load_weapon('longsword')
print(f"Weapon: {longsword['name']}")      # Longsword
print(f"Damage: {longsword['damage']['damage_dice']}")  # 1d8
print(f"Type: {longsword['damaprint(f"Type: {longsword['damaprint(f"Type:```
### Load an Armor
```python
from dnd_5e_core.data import load_armor
plate = load_armor('plate-armor')
print(f"Armor: {plate['name']}")        # Plate Armor
print(f"AC: {plate['armor_class']['base']}")  # 18
print(f"Category: {plate['armor_category']}")  # Heavy
```
### Load a Race
```python
from dnd_5e_core.data import load_race
elf = load_race('elf')
print(f"Race: {elf['name']}")            # Elf
print(f"Speed: {elf['speed']}")        # 30
print(f"Bonus: {elf['ability_bonuses']}")
```
### Load a Class
```python
from dnd_5e_core.datfrom dnd_5e_core.datfrom dnd_5e_core.datf'figfrom dnd_5e_core.datfrom dnd_5e_core.datfrom dnd_5e_core.dprint(f"HD: {fighter['hit_die']}")       # 10
print(f"Proficiencies: {fighter['proficiencies']}")
```
---
## 📊 Available Data## 📊 Available Data## 📊```python
from dnd_5e_core.data import (
    list_monsters, list_spells, list_weapons, list_armors,
    list_equipment, list_races, list_classes
)
print(f"Monsters: {len(list_monsters())}")      # 332
print(f"Spells: {len(list_spells())}")           # 319
print(f"Weapons: {len(list_weapons())}")          print(f"Weapons: {len(list_weapons())}")               # 30
print(f"Equipment: {len(list_equipment())}")  # 237
print(f"Races: {len(list_races())}")            # 9
print(f"Classes: {len(list_classes())}")        # 12
```
---
## 🎮 Complete Example: Create a## 🎮 Complete Example: Create a## 🎮 mport## 🎮 Complete Example: Create a## 🎮 Egoblin = load_monster('goblin')
orc = load_monster('orc')
dragon = load_monster('ancient-red-dragon')
# Display statistics
monsters = [goblin, orc, dragon]
for monster in monsters:
    print(f"\n{monster['name']}:")
    print(f"  HP: {monster['hit_points']}")
    print(f"  AC: {monster['armor_class']}")
    print(f"  CR: {monster['challenge_rating']}")
    # Available actions
    if 'actions' in monster:
        print("  Actions:")
        for action in monster['actions']:
            print(f"    - {acti            print(f"    - {acti            print(f"```
---
## 🔍 Advanced Search
### Filter Monsters by CR
```python
from dnd_5e_core.data import list_monsters, load_monster
# Find all monsters with CR <= 2
low_cr_monsters = []
for monster_index in list_monsters():
    monster = load_monster(monster_ind    monster = load_monster(monster_ind    monsng'] <= 2:
        low_cr_monsters.append(monster)
print(f"Monsters CR ≤ 2: {len(low_cr_monsters)}")
for m in low_cr_monsters[:5]:
    print(f"  - {m['name']} (CR {m['ch    print(f"  - {m['n```
### Find All Spells of a Level
```python
from dnd_5e_core.data import list_spells, load_spell
# All level 3 spells
level3_spells = []
for spell_index in list_spells():
    spell = load_spell(spell_index)
    if spell and spell['level'] == 3:
        level3_spells.append(spell)
print(f"Spells level 3: {len(level3_spells)}")
for s in level3_spells[:5]:
    print(f"  - {s[    print(f"  - {s[    print(f"  - {s[ ---
## 🛠️ Customization (Optional)
If you have a custom location for your data:
```python
from dnd_5e_core.data import set_data_directory
# Define a custom directory
set_data_directory('/custom/path/to/data')
# Then, use normally
# Then, use normallyoad_monster
goblin = load_monster('goblin')
```
**Note:** This is **only** necessary if you have a custom data source.
---
## 📖 More Information
- **Full content:** See `data/README.md`
- **Migration:** See `DATA_MIGRATION_COMPLETE.md`
- **API Documentation- **API Documentation- **Documentatio---
## ✅ Quick Test
Validate that everything works:
```bash
python test_migration.py
```
YouYouYouYouYou```
🎉 ALL TESTS PASSED - MIGRATION VALIDATED!
```
---
**Have fun with D&D 5e!** 🎲🐉
