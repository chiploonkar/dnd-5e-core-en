# Module: mechanics

## Overview

The `mechanics` module contains the core game rules of D&D 5e: dice rolling, experience, challenge rating, encounters, and level progression.

## Core Classes and Functions

### DamageDice

Dice rolling system for damage, healing, and other random calculations.

**Import:**
```python
from dnd_5e_core.mechanics import DamageDice
```

**Creation:**

=== "Standard Notation"

    ```python
    from dnd_5e_core.mechanics import DamageDice

    damage = DamageDice("2d6+3")  # 2 six-sided dice + 3
    heal = DamageDice("1d8")      # 1 eight-sided die
    fireball = DamageDice("8d6")  # 8 six-sided dice
    ```

=== "With Separate Bonus"

    ```python
    from dnd_5e_core.mechanics import DamageDice

    damage = DamageDice("2d6", bonus=3)
    ```

=== "With Penalty"

    ```python
    from dnd_5e_core.mechanics import DamageDice

    damage = DamageDice("1d6-2")
    ```

**Methods:**

```python
# Roll the dice
result = damage.roll()
print(f"Result: {result}")

# Maximum possible value
max_dmg = damage.max_score
print(f"Maximum: {max_dmg}")

# Average expected value
avg_dmg = damage.avg
print(f"Average: {avg_dmg}")

# Score with success modifier
# "none" = full damage, "half" = half damage
score = damage.score(success_type="half")
```

**Comparison:**
```python
d6 = DamageDice("1d6")
d8 = DamageDice("1d8")

if d8 > d6:
    print("The d8 deals more damage")
```

---

### Experience

XP and level management.

**Import:**
```python
from dnd_5e_core.mechanics import (
    xp_by_cr,
    xp_thresholds_by_level,
    calculate_level_from_xp
)
```

**XP by CR:**
```python
from dnd_5e_core.mechanics import xp_by_cr

# XP by CR dictionary
xp = xp_by_cr[0.5]  # CR 1/2 awards 100 XP
xp = xp_by_cr[5]    # CR 5 awards 1800 XP
xp = xp_by_cr[20]   # CR 20 awards 25000 XP
```

**Calculate Level:**
```python
from dnd_5e_core.mechanics import calculate_level_from_xp

level = calculate_level_from_xp(5000)  # Returns the corresponding level
print(f"Level: {level}")
```

**XP Thresholds by Level:**
```python
from dnd_5e_core.mechanics import xp_thresholds_by_level

# Thresholds for encounters (easy, medium, hard, deadly)
thresholds = xp_thresholds_by_level[5]
print(f"Level 5:")
print(f"  Easy: {thresholds['easy']}")
print(f"  Medium: {thresholds['medium']}")
print(f"  Hard: {thresholds['hard']}")
print(f"  Deadly: {thresholds['deadly']}")
```

---

### Challenge Rating (CR)

Challenge rating calculation and encounter generation.

**Import:**
```python
from dnd_5e_core.mechanics import (
    generate_encounter_cr,
    calculate_party_strength
)
```

**Generate Encounter CR:**
```python
from dnd_5e_core.mechanics import generate_encounter_cr

# Party of 4 level 5 characters
party_levels = [5, 5, 5, 5]

# Medium encounter
min_cr, max_cr = generate_encounter_cr(
    party_levels,
    difficulty="medium"
)
print(f"Recommended CR: {min_cr} - {max_cr}")

# Other available difficulties
min_cr, max_cr = generate_encounter_cr(party_levels, difficulty="easy")
min_cr, max_cr = generate_encounter_cr(party_levels, difficulty="hard")
min_cr, max_cr = generate_encounter_cr(party_levels, difficulty="deadly")
```

**Calculate Party Strength:**
```python
from dnd_5e_core.mechanics import calculate_party_strength

party_levels = [5, 5, 4, 6]
strength = calculate_party_strength(party_levels)
print(f"Party strength: {strength}")
```

---

### Encounter Builder

Building balanced encounters.

**Import:**
```python
from dnd_5e_core.mechanics import build_encounter
```

**Build an Encounter:**
```python
from dnd_5e_core.mechanics import build_encounter
from dnd_5e_core.data import load_monster

# Party
party_levels = [5, 5, 5, 5]

# Available monster pool
available_monsters = [
    load_monster("goblin"),
    load_monster("hobgoblin"),
    load_monster("bugbear"),
    load_monster("orc"),
]

# Build a balanced encounter
encounter = build_encounter(
    party_levels=party_levels,
    available_monsters=available_monsters,
    difficulty="medium"
)

print(f"Encounter created with {len(encounter)} monsters:")
for monster in encounter:
    print(f"  - {monster.name} (CR {monster.challenge_rating})")
```

---

### Level Up

Level up management.

**Import:**
```python
from dnd_5e_core.mechanics import level_up_character
```

**Level Up:**
```python
from dnd_5e_core.mechanics import level_up_character
from dnd_5e_core.entities import Character

hero = Character.generate_random_character(level=5, class_name="fighter")

# Gain XP
hero.experience_points += 3000

# Check for level up
from dnd_5e_core.mechanics import calculate_level_from_xp
new_level = calculate_level_from_xp(hero.experience_points)

if new_level > hero.level:
    print(f"Level up! {hero.level} -> {new_level}")
    level_up_character(hero)
```

---

### Gold Rewards

Gold reward calculations.

**Import:**
```python
from dnd_5e_core.mechanics import (
    calculate_gold_reward,
    distribute_gold
)
```

**Calculate Gold:**
```python
from dnd_5e_core.mechanics import calculate_gold_reward

# Gold based on CR
gold = calculate_gold_reward(challenge_rating=5)
print(f"Gold earned: {gold} gp")
```

**Distribute Gold:**
```python
from dnd_5e_core.mechanics import distribute_gold

total_gold = 1000
party_size = 4

gold_per_member = distribute_gold(total_gold, party_size)
print(f"Each member receives: {gold_per_member} gp")
```

---

## Complete Examples

### Complete Dice System

```python
from dnd_5e_core.mechanics import DamageDice

# Weapon damage
longsword = DamageDice("1d8+3")
greataxe = DamageDice("1d12+5")

print(f"Longsword: {longsword.roll()}")
print(f"Greataxe: {greataxe.roll()}")

# Fireball spell (level 3)
fireball_lv3 = DamageDice("8d6")
print(f"Fireball: {fireball_lv3.roll()}")

# Upcasted Fireball spell (level 5)
fireball_lv5 = DamageDice("10d6")  # +1d6 per level above 3
print(f"Level 5 Fireball: {fireball_lv5.roll()}")

# Healing
cure_wounds = DamageDice("1d8+4")
hp_restored = cure_wounds.roll()
print(f"Healing: {hp_restored} HP")

# Compare damage
if greataxe > longsword:
    print("The greataxe deals more damage (on average)")
```

### XP and Level Management

```python
from dnd_5e_core.mechanics import (
    xp_by_cr,
    calculate_level_from_xp
)
from dnd_5e_core.entities import Character

# Create a level 1 hero
hero = Character.generate_random_character(level=1, class_name="fighter")
print(f"{hero.name} - Level {hero.level} - XP: {hero.experience_points}")

# Fight monsters
defeated_monsters = [
    ("goblin", 0.25),      # CR 1/4 = 50 XP
    ("goblin", 0.25),
    ("hobgoblin", 0.5),    # CR 1/2 = 100 XP
]

for monster_name, cr in defeated_monsters:
    xp_gained = xp_by_cr[cr]
    hero.experience_points += xp_gained
    print(f"Defeated {monster_name}! +{xp_gained} XP")
    
    # Check for level up
    new_level = calculate_level_from_xp(hero.experience_points)
    if new_level > hero.level:
        old_level = hero.level
        hero.level_up()
        print(f"LEVEL UP! {old_level} -> {hero.level}")
        print(f"   New max HP: {hero.max_hit_points}")
        print(f"   New proficiency bonus: {hero.proficiency_bonus}")

print(f"\nFinal: {hero.name} - Level {hero.level} - XP: {hero.experience_points}")
```

### Encounter Construction

```python
from dnd_5e_core.mechanics import generate_encounter_cr, xp_by_cr
from dnd_5e_core.data import load_monster

# Party of 4 level 5 adventurers
party_levels = [5, 5, 5, 5]

# Determine appropriate CR
min_cr, max_cr = generate_encounter_cr(
    party_levels,
    difficulty="medium"
)

print(f"Recommended CR for medium encounter: {min_cr} - {max_cr}")

# Load monsters in this range
possible_monsters = [
    "goblin",           # CR 0.25
    "hobgoblin",        # CR 0.5
    "orc",              # CR 1
    "ogre",             # CR 2
    "owlbear",          # CR 3
    "hill-giant",       # CR 5
]

encounter = []
total_xp = 0
target_xp = 1400  # XP budget for a medium level 5 encounter

for monster_name in possible_monsters:
    monster = load_monster(monster_name)
    if min_cr <= monster.challenge_rating <= max_cr:
        # Add copies until budget is met
        while total_xp + monster.xp <= target_xp:
            encounter.append(load_monster(monster_name))
            total_xp += monster.xp

print(f"\nEncounter generated (Total XP: {total_xp}):")
from collections import Counter
monster_counts = Counter([m.name for m in encounter])
for monster_name, count in monster_counts.items():
    monster = next(m for m in encounter if m.name == monster_name)
    print(f"  {count}x {monster_name} (CR {monster.challenge_rating})")
```

### Complete Reward System

```python
from dnd_5e_core.mechanics import (
    xp_by_cr,
    calculate_gold_reward,
    distribute_gold
)
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Party
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=4, class_name="cleric"),
    Character.generate_random_character(level=5, class_name="rogue"),
]

# Defeated monsters
defeated = [
    load_monster("orc"),
    load_monster("orc"),
    load_monster("ogre"),
]

# Calculate total XP
total_xp = sum([m.xp for m in defeated])
xp_per_member = total_xp // len(party)

print(f"Defeated monsters:")
for monster in defeated:
    print(f"  - {monster.name} (CR {monster.challenge_rating}, {monster.xp} XP)")

print(f"\nTotal XP: {total_xp}")
print(f"   XP per member: {xp_per_member}")

# Distribute XP
for hero in party:
    old_xp = hero.experience_points
    hero.gain_xp(xp_per_member)
    print(f"   {hero.name}: {old_xp} -> {hero.experience_points}")

# Calculate gold
total_gold = sum([calculate_gold_reward(m.challenge_rating) for m in defeated])
gold_per_member = distribute_gold(total_gold, len(party))

print(f"\nTotal gold: {total_gold} gp")
print(f"   Gold per member: {gold_per_member} gp")

for hero in party:
    hero.gold += gold_per_member
    print(f"   {hero.name}: {hero.gold} gp")
```

---

## Useful Constants

### XP by CR
```python
xp_by_cr = {
    0: 10,
    0.125: 25,
    0.25: 50,
    0.5: 100,
    1: 200,
    2: 450,
    3: 700,
    4: 1100,
    5: 1800,
    10: 5900,
    15: 13000,
    20: 25000,
    30: 155000,
}
```

### XP Thresholds by Level
```python
xp_thresholds_by_level = {
    1: {"easy": 25, "medium": 50, "hard": 75, "deadly": 100},
    5: {"easy": 500, "medium": 1100, "hard": 1600, "deadly": 2400},
    10: {"easy": 1200, "medium": 2400, "hard": 3600, "deadly": 5400},
    20: {"easy": 2800, "medium": 5700, "hard": 8500, "deadly": 12700},
}
```

---

## See Also

- [combat](combat.md) - Combat system
- [entities](entities.md) - Characters and monsters
- [spells](magic-spells.md) - Spells and magic
- [equipment](equipment.md) - Equipment
