# Combat Examples - dnd-5e-core

This document contains complete combat examples using the `dnd-5e-core` package.

## Table of Contents

1. [Simple Combat with Spellcasting](#simple-combat-with-spellcasting)
2. [Combat with Equipment](#combat-with-equipment)
3. [Combat Spellcaster vs Spellcaster](#combat-spellcaster-vs-spellcaster)
4. [Combat with Monster Special Attacks](#combat-with-special-attacks)
5. [Party Formation and Positioning](#party-formation)

---

## Simple Combat with Spellcasting

### Complete Code

```python
from dnd_5e_core import load_monster
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.combat import CombatSystem

# Create a wizard
wizard = simple_character_generator(level=5, race_name='elf', class_name='wizard', name='Gandalf')

# Create fighters for the front
fighter1 = simple_character_generator(level=5, class_name='fighter', name='Conan')
fighter2 = simple_character_generator(level=5, class_name='fighter', name='Aragorn')
fighter3 = simple_character_generator(level=5, class_name='fighter', name='Beorn')

# Load a monster
ogre = load_monster('ogre')

# Formation: fighters in front (0-2), wizard in back (3) to cast spells
party = [fighter1, fighter2, fighter3, wizard]

print(f"📖 {wizard.name}'s Spells:")
if hasattr(wizard, 'sc') and wizard.sc:
    print(f"   Spells Known: {len(wizard.sc.learned_spells)}")
    print(f"   Spell Slots: {wizard.sc.spell_slots[1:6]}")
    for spell in wizard.sc.learned_spells[:5]:
        spell_type = "Cantrip" if spell.level == 0 else f"Level {spell.level}"
        print(f"      - {spell.name} ({spell_type})")

# Start combat
combat = CombatSystem(verbose=True)
alive_chars = [c for c in party if c.hit_points > 0]
alive_monsters = [ogre]

round_num = 1
max_rounds = 10

print(f"\n⚔️ Starting combat!")

while alive_chars and alive_monsters and round_num <= max_rounds:
    print(f"\n=== Round {round_num} ===")
    
    # Character turns
    for char in alive_chars[:]:
        if not alive_monsters:
            break
        if char.hit_points <= 0:
            if char in alive_chars:
                alive_chars.remove(char)
            continue
        
        combat.character_turn(
            character=char,
            alive_chars=alive_chars,
            alive_monsters=alive_monsters,
            party=party
        )
    
    # Monster turns
    for monster in alive_monsters[:]:
        if not alive_chars:
            break
        if monster.hit_points <= 0:
            if monster in alive_monsters:
                alive_monsters.remove(monster)
            continue
        
        combat.monster_turn(
            monster=monster,
            alive_monsters=alive_monsters,
            alive_chars=alive_chars,
            party=party,
            round_num=round_num
        )
    
    round_num += 1

# Results
if alive_chars:
    print(f"\n✅ VICTORY!")
    if hasattr(wizard, 'sc') and wizard.sc:
        print(f"\n{wizard.name}'s Spell Usage:")
        print(f"   Spell Slots After:  {wizard.sc.spell_slots[1:6]}")
```

### Expected Output

```
📖 Gandalf's Spells:
   Spells Known: 10
   Spell Slots: [4, 3, 2, 0, 0]
      - Fire Bolt (Cantrip)
      - Shocking Grasp (Cantrip)
      - Ice Storm (Level 4)
      - Black Tentacles (Level 4)
      - Scorching Ray (Level 2)

⚔️ Starting combat!

=== Round 1 ===
Conan attacks Ogre!
Conan punches Ogre for 2 hit points!
Aragorn attacks Ogre!
Aragorn punches Ogre for 1 hit points!
Beorn attacks Ogre!
Beorn punches Ogre for 1 hit points!
Gandalf attacks Ogre!
Gandalf CAST SPELL ** ICE STORM ** on Ogre
Ogre is hit for 18 hit points!
Ogre bludgeones Conan for 12 hit points!

=== Round 2 ===
...

✅ VICTORY!
Gandalf's Spell Usage:
   Spell Slots After: [4, 0, 0, 0, 0]
```

---

## Combat with Equipment

### Complete Code

```python
from dnd_5e_core import load_monster
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.data import load_weapon, load_armor
from dnd_5e_core.combat import CombatSystem

# Create characters
fighter1 = simple_character_generator(level=5, class_name='fighter', name='Conan')
fighter2 = simple_character_generator(level=5, class_name='fighter', name='Aragorn')
fighter3 = simple_character_generator(level=5, class_name='fighter', name='Beorn')
wizard = simple_character_generator(level=5, class_name='wizard', name='Gandalf')

# Load equipment
longsword = load_weapon("longsword")
battleaxe = load_weapon("battleaxe")
greatsword = load_weapon("greatsword")

chain_mail = load_armor("chain-mail")
scale_mail = load_armor("scale-mail")
ring_mail = load_armor("ring-mail")

# Equip Fighter1 with longsword and chain mail
if fighter1.inventory and longsword:
    for i, item in enumerate(fighter1.inventory):
        if item is None:
            fighter1.inventory[i] = longsword
            break
    fighter1.equip(longsword)
    
if fighter1.inventory and chain_mail:
    for i, item in enumerate(fighter1.inventory):
        if item is None:
            fighter1.inventory[i] = chain_mail
            break
    fighter1.equip(chain_mail)
    print(f"✅ {fighter1.name}: {longsword.name} + {chain_mail.name} (AC {chain_mail.armor_class['base']})")

# Equip Fighter2
if fighter2.inventory and battleaxe:
    for i, item in enumerate(fighter2.inventory):
        if item is None:
            fighter2.inventory[i] = battleaxe
            break
    fighter2.equip(battleaxe)

if fighter2.inventory and scale_mail:
    for i, item in enumerate(fighter2.inventory):
        if item is None:
            fighter2.inventory[i] = scale_mail
            break
    fighter2.equip(scale_mail)
    print(f"✅ {fighter2.name}: {battleaxe.name} + {scale_mail.name} (AC {scale_mail.armor_class['base']})")

# Equip Fighter3
if fighter3.inventory and greatsword:
    for i, item in enumerate(fighter3.inventory):
        if item is None:
            fighter3.inventory[i] = greatsword
            break
    fighter3.equip(greatsword)

if fighter3.inventory and ring_mail:
    for i, item in enumerate(fighter3.inventory):
        if item is None:
            fighter3.inventory[i] = ring_mail
            break
    fighter3.equip(ring_mail)
    print(f"✅ {fighter3.name}: {greatsword.name} + {ring_mail.name} (AC {ring_mail.armor_class['base']})")

# Load monster
ogre = load_monster('ogre')

# Party formation
party = [fighter1, fighter2, fighter3, wizard]

# Combat (same code as before)
# ...
```

### Expected Output

```
✅ Conan: Longsword + Chain Mail (AC 16)
✅ Aragorn: Battleaxe + Scale Mail (AC 14)
✅ Beorn: Greatsword + Ring Mail (AC 14)

=== Round 1 ===
Conan attacks Ogre!
Conan slashes Ogre for 5 hit points!     ← Uses the longsword!
Aragorn attacks Ogre!
Aragorn slashes Ogre for 6 hit points!   ← Uses the axe!
Beorn attacks Ogre!
Beorn slashes Ogre for 10 hit points!    ← Uses the greatsword!
Gandalf CAST SPELL ** ICE STORM ** on Ogre
Ogre is hit for 18 hit points!
Ogre bludgeones Conan for 7 hit points!  ← Reduced damage thanks to armor AC 16
```

**Notable Difference:**
- Without equipment: "punches" for 1-2 damage
- With equipment: "slashes" for 5-10 damage
- Improved AC: 10 → 14-16

---

## Combat Spellcaster vs Spellcaster

### Complete Code

```python
from dnd_5e_core import load_monster
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.combat import CombatSystem

# Create two wizards
wizard = simple_character_generator(level=5, class_name='wizard', name='Gandalf')

# Load a spellcaster monster
mage = load_monster('mage')

print(f"✨ {wizard.name} (Player)")
if hasattr(wizard, 'sc') and wizard.sc:
    print(f"   Spells: {len(wizard.sc.learned_spells)}")

print(f"\n✨ {mage.name} (Monster)")
if hasattr(mage, 'is_spell_caster') and mage.is_spell_caster:
    print(f"   Spellcaster: Yes")
    if hasattr(mage, 'sc'):
        print(f"   Spells: {len(mage.sc.learned_spells)}")

# Add guards to position the wizards in the back row
guard1 = simple_character_generator(level=5, class_name='fighter', name='Guard1')
guard2 = simple_character_generator(level=5, class_name='fighter', name='Guard2')
guard3 = simple_character_generator(level=5, class_name='fighter', name='Guard3')

party = [guard1, guard2, guard3, wizard]
monsters = [mage]

# Combat
combat = CombatSystem(verbose=True)
alive_chars = [c for c in party if c.hit_points > 0]
alive_monsters = monsters.copy()

round_num = 1
while alive_chars and alive_monsters and round_num <= 10:
    print(f"\n=== Round {round_num} ===")
    
    for char in alive_chars[:]:
        if not alive_monsters:
            break
        combat.character_turn(char, alive_chars, alive_monsters, party)
    
    for monster in alive_monsters[:]:
        if not alive_chars:
            break
        combat.monster_turn(monster, alive_monsters, alive_chars, party, round_num)
    
    round_num += 1
```

### Expected Output

```
✨ Gandalf (Player)
   Spells: 10

✨ Mage (Monster)
   Spellcaster: Yes
   Spells: 16

=== Round 1 ===
Guard1 attacks Mage!
Guard1 punches Mage for 2 hit points!
Guard2 attacks Mage!
Guard2 punches Mage for 1 hit points!
Guard3 attacks Mage!
Guard3 punches Mage for 1 hit points!
Gandalf attacks Mage!
Gandalf CAST SPELL ** BLACK TENTACLES ** on Mage
Mage is hit for 12 hit points!
Mage casts CONE OF COLD on Gandalf!      ← The Mage counters with a spell!
Gandalf is hit for 27 hit points!
```

---

## Combat with Special Attacks

### Complete Code

```python
from dnd_5e_core import load_monster
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.combat import CombatSystem

# Create a party
party = [
    simple_character_generator(level=5, class_name='fighter', name='Tank1'),
    simple_character_generator(level=5, class_name='fighter', name='Tank2'),
    simple_character_generator(level=5, class_name='fighter', name='Tank3'),
    simple_character_generator(level=5, class_name='wizard', name='Merlin')
]

# Load a monster with special attacks
try:
    dragon = load_monster('young-red-dragon')
    print(f"✨ Loaded: {dragon.name}")
    
    if hasattr(dragon, 'sa') and dragon.sa:
        print(f"   Special Attacks: {[sa.name for sa in dragon.sa]}")
        # Output: Multi-attack, Breath Weapon
except:
    dragon = load_monster('ogre')

# Combat
combat = CombatSystem(verbose=True)
alive_chars = [c for c in party if c.hit_points > 0]
alive_monsters = [dragon]

round_num = 1
while alive_chars and alive_monsters and round_num <= 5:
    print(f"\n=== Round {round_num} ===")
    
    for char in alive_chars[:]:
        if not alive_monsters:
            break
        combat.character_turn(char, alive_chars, alive_monsters, party)
    
    for monster in alive_monsters[:]:
        if not alive_chars:
            break
        combat.monster_turn(monster, alive_monsters, alive_chars, party, round_num)
    
    round_num += 1
```

### Expected Output

```
✨ Loaded: Young Red Dragon
   Special Attacks: ['Multi-attack', 'Breath Weapon']

=== Round 1 ===
Tank1 attacks Young Red Dragon!
Tank1 punches Young Red Dragon for 1 hit points!
Tank2 attacks Young Red Dragon!
Tank2 punches Young Red Dragon for 2 hit points!
Tank3 attacks Young Red Dragon!
Tank3 punches Young Red Dragon for 1 hit points!
Merlin attacks Young Red Dragon!
Merlin CAST SPELL ** FIRE BOLT ** on Young Red Dragon
Young Red Dragon is hit for 8 hit points!
Young Red Dragon multi-attacks Tank1!           ← Special multi-attack!
Young Red Dragon pierces Tank1 for 23 hit points!
Young Red Dragon slashes Tank1 for 16 hit points!
Young Red Dragon slashes Tank1 for 13 hit points!
Tank1 is KILLED!
```

---

## Party Formation and Positioning

### ⚠️ IMPORTANT: Positioning for Spellcasting

Characters in positions **0-2** are considered in **melee** (front)
Characters in positions **3+** are considered at **range** (back)

**Wizards and other spellcasters MUST be in positions 3+ to cast spells!**

### ✅ Correct Formation

```python
# Correct formation - The wizard casts spells
fighter1 = simple_character_generator(level=5, class_name='fighter')
fighter2 = simple_character_generator(level=5, class_name='fighter')
fighter3 = simple_character_generator(level=5, class_name='fighter')
wizard = simple_character_generator(level=5, class_name='wizard')

party = [fighter1, fighter2, fighter3, wizard]
#        Position:  0         1         2         3 (back)

print("Party formation:")
for i, char in enumerate(party):
    position = "Front (Melee)" if i < 3 else "Back (Ranged/Spells)"
    print(f"  [{i}] {char.name}: {position}")

# Output:
# [0] Fighter1: Front (Melee)
# [1] Fighter2: Front (Melee)
# [2] Fighter3: Front (Melee)
# [3] Wizard: Back (Ranged/Spells) ← Casts spells!
```

### ❌ Incorrect Formation

```python
# Incorrect formation - The wizard is NOT in back position
wizard = simple_character_generator(level=5, class_name='wizard')
party = [wizard]
#        Position: 0 (melee)

# Result: The wizard will attack in melee instead of casting spells!
# Output: "Wizard punches Ogre for 1 hit points!" ← No spells!
```

### Recommended Party Formation

```python
# Balanced party of 4-6 characters
def create_balanced_party():
    # Front row (tanks/melee)
    tank1 = simple_character_generator(level=5, class_name='fighter', name='Tank1')
    tank2 = simple_character_generator(level=5, class_name='fighter', name='Tank2')
    tank3 = simple_character_generator(level=5, class_name='cleric', name='Healer')
    
    # Back row (range/spells)
    wizard = simple_character_generator(level=5, class_name='wizard', name='Mage')
    ranger = simple_character_generator(level=5, class_name='ranger', name='Archer')
    
    party = [tank1, tank2, tank3, wizard, ranger]
    
    print("⚔️ Party Formation:")
    print(f"   Front Row: {tank1.name}, {tank2.name}, {tank3.name}")
    print(f"   Back Row: {wizard.name}, {ranger.name}")
    
    return party

party = create_balanced_party()
```

---

## Combat System Features

### The `CombatSystem` automatically handles:

1. **🔮 Character Spellcasting**
   - Automatic spell selection
   - Spell slot consumption
   - Cantrips and slotted spells

2. **👹 Monster Spellcasting**
   - Spellcaster monsters (Mage, Lich, etc.) use their spells
   - Automatically calculated saving throws

3. **⚔️ Weapon Attacks**
   - Uses equipped weapons
   - Calculates damage according to dice
   - Multi-attacks handled

4. **🎯 Special Attacks**
   - Dragon breath
   - Multi-attacks
   - Monster abilities

5. **🩹 Automatic Healing**
   - Characters heal wounded allies
   - Potion usage when HP is low
   - Prioritized healing spells

6. **📊 Tactical Intelligence**
   - Priority: Healing → Potions → Spells → Special Attacks → Weapons
   - Intelligent target selection
   - Condition management (restraint, etc.)

---

## Summary

✅ **Use `simple_character_generator()`** to create characters quickly
✅ **Position spellcasters in position 3+** in the party
✅ **Equip weapons and armor** for better combat
✅ **The `CombatSystem` handles everything** - spells, special attacks, healing
✅ **verbose=True** to see all combat details

For more examples, check out the [DnD5e-Test](https://github.com/codingame-team/DND5e-Test) project.
