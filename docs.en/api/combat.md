# Module: combat

## Overview

The `combat` module provides a complete combat system for D&D 5e, including action management, damage calculation, conditions, and initiative.

## Core Classes

### CombatSystem

Centralized system to manage combat.

**Import:**
```python
from dnd_5e_core.combat import CombatSystem
```

**Creation:**

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Create the party and monsters
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
]

monsters = [
    load_monster("goblin"),
    load_monster("goblin"),
]

# Initialize combat
combat = CombatSystem(verbose=True)

# Or with callback for custom UI
def message_handler(msg):
    print(f"[COMBAT] {msg}")

combat = CombatSystem(verbose=False, message_callback=message_handler)
```

**Core Methods:**

#### Player Turn
```python
# Melee attack
combat.player_turn(
    character=party[0],
    target=monsters[0],
    action_type="melee"
)

# Ranged attack
combat.player_turn(
    character=party[1],
    target=monsters[0],
    action_type="ranged"
)

# Cast a spell
combat.player_turn(
    character=party[1],
    target=monsters[0],
    action_type="spell",
    spell=fireball,
    spell_slot_level=3
)

# Use a potion
from dnd_5e_core.equipment import HealingPotion, PotionRarity
potion = HealingPotion(
    id=1,
    name="Potion of Healing",
    rarity=PotionRarity.COMMON,
    hit_dice="2d4",
    bonus=2,
    min_cost=50,
    max_cost=50
)
combat.player_turn(
    character=party[0],
    action_type="potion",
    potion=potion
)
```

#### Monster Turn
```python
# The system automatically handles monster AI
combat.monster_turn(
    monster=monsters[0],
    alive_monsters=monsters,
    alive_chars=party,
    party=party,
    round_num=1
)
```

#### Utility Functions
```python
# Check if combat is over
if combat.is_combat_over(party, monsters):
    print("Combat over!")

# Roll initiative
initiative_order = combat.roll_initiative(party, monsters)

# Distribute XP and gold
total_xp, gold = combat.distribute_rewards(party, defeated_monsters)
```

---

### Action

Represents a combat action (attack, spell, special ability).

**Import:**
```python
from dnd_5e_core.combat import Action, ActionType
```

**Action Types:**
```python
class ActionType(Enum):
    MELEE = "melee"
    RANGED = "ranged"
    SPELL = "spell"
    SPECIAL = "special"
```

**Properties:**
- `name: str` - Action name
- `action_type: ActionType` - Action type
- `attack_bonus: int` - Attack bonus
- `damage: Damage` - Damage dealt
- `range_type: RangeType` - Range type (melee/ranged)
- `normal_range: int` - Normal range
- `long_range: int` - Long range
- `dc_type: str` - Saving throw type (optional)
- `dc_value: int` - Saving throw DC (optional)
- `dc_success: str` - Effect on success (optional)

**Example:**
```python
from dnd_5e_core.combat import Action, ActionType, Damage
from dnd_5e_core.mechanics import DamageDice

action = Action(
    name="Longsword",
    action_type=ActionType.MELEE,
    attack_bonus=5,
    damage=Damage(
        damage_dice=DamageDice("1d8+3"),
        damage_type="slashing"
    ),
    range_type=RangeType.MELEE,
    normal_range=5
)
```

---

### Damage

Represents damage with a type and dice.

**Import:**
```python
from dnd_5e_core.combat import Damage
```

**Properties:**
- `damage_dice: DamageDice` - Damage dice
- `damage_type: str` - Damage type (slashing, piercing, fire, etc.)

**Usage:**
```python
from dnd_5e_core.combat import Damage
from dnd_5e_core.mechanics import DamageDice

# Melee damage
melee_damage = Damage(
    damage_dice=DamageDice("1d8+3"),
    damage_type="slashing"
)

# Magic damage
fire_damage = Damage(
    damage_dice=DamageDice("8d6"),
    damage_type="fire"
)

# Roll damage
result = melee_damage.damage_dice.roll()
print(f"Damage: {result}")
```

---

### Condition

States and conditions affecting characters and monsters.

**Import:**
```python
from dnd_5e_core.combat import Condition
```

**Standard D&D 5e Conditions:**
- `BLINDED` - Blinded
- `CHARMED` - Charmed
- `DEAFENED` - Deafened
- `FRIGHTENED` - Frightened
- `GRAPPLED` - Grappled
- `INCAPACITATED` - Incapacitated
- `INVISIBLE` - Invisible
- `PARALYZED` - Paralyzed
- `PETRIFIED` - Petrified
- `POISONED` - Poisoned
- `PRONE` - Prone
- `RESTRAINED` - Restrained
- `STUNNED` - Stunned
- `UNCONSCIOUS` - Unconscious
- `EXHAUSTION` - Exhaustion

**Usage:**
```python
from dnd_5e_core.combat import Condition

# Apply a condition
character.add_condition(Condition.POISONED)

# Check a condition
if character.has_condition(Condition.PARALYZED):
    print("The character is paralyzed!")

# Remove a condition
character.remove_condition(Condition.POISONED)
```

---

### SpecialAbility

Special abilities of monsters.

**Import:**
```python
from dnd_5e_core.combat import SpecialAbility
```

**Properties:**
- `name: str` - Ability name
- `desc: str` - Description
- `damage: Optional[Damage]` - Damage (if applicable)
- `dc_type: str` - Saving throw type
- `dc_value: int` - Saving throw DC
- `usage: Optional[dict]` - Usage limitations

**Example:**
```python
# Special abilities are generally loaded with the monster
dragon = load_monster("ancient-red-dragon")

if dragon.sa:
    for ability in dragon.sa:
        print(f"- {ability.name}: {ability.desc}")
```

---

## Complete Examples

### Turn-Based Combat

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Preparation
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="cleric"),
]

monsters = [
    load_monster("goblin"),
    load_monster("goblin"),
    load_monster("hobgoblin"),
]

combat = CombatSystem(verbose=True)

# Roll initiative
print("🎲 Rolling initiative...")
# (Initiative is generally handled by your UI)

# Combat loop
round_num = 1
while True:
    alive_party = [c for c in party if c.is_alive]
    alive_monsters = [m for m in monsters if m.is_alive]
    
    if not alive_party:
        print("💀 Defeat! All heroes have fallen.")
        break
    
    if not alive_monsters:
        print("🎉 Victory! All monsters are defeated.")
        # Distribute rewards
        xp, gold = combat.distribute_rewards(party, monsters)
        print(f"XP Gained: {xp}, Gold: {gold}")
        break
    
    print(f"\n=== Round {round_num} ===")
    
    # Player turns
    for char in alive_party:
        target = alive_monsters[0]  # Target the first living monster
        combat.player_turn(char, target, action_type="melee")
    
    # Monster turns
    for monster in alive_monsters:
        combat.monster_turn(
            monster,
            alive_monsters,
            alive_party,
            party,
            round_num
        )
    
    round_num += 1
```

### Combat with Spells

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster, load_spell

# Create a party with a spellcaster
wizard = Character.generate_random_character(level=5, class_name="wizard")
fighter = Character.generate_random_character(level=5, class_name="fighter")
party = [wizard, fighter]

monsters = [load_monster("ogre")]

combat = CombatSystem(verbose=True)

# The wizard casts a spell
fireball = load_spell("fireball")
if wizard.spell_slots[2] > 0:  # Check 3rd level spell slots
    combat.player_turn(
        character=wizard,
        target=monsters[0],
        action_type="spell",
        spell=fireball,
        spell_slot_level=3
    )
```

### Combat with Positioning (front/back)

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Create a party
party = [
    # Front (can attack in melee)
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="paladin"),
    Character.generate_random_character(level=5, class_name="barbarian"),
    # Back (ranged attacks only)
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=5, class_name="ranger"),
    Character.generate_random_character(level=5, class_name="cleric"),
]

monsters = [
    load_monster("orc"),
    load_monster("orc"),
    load_monster("orc"),
]

combat = CombatSystem(verbose=True)

# Front row attacks in melee
for i in range(3):
    if party[i].is_alive and monsters:
        combat.player_turn(
            party[i],
            monsters[0],
            action_type="melee"
        )

# Back row attacks at range
for i in range(3, 6):
    if party[i].is_alive and monsters:
        combat.player_turn(
            party[i],
            monsters[0],
            action_type="ranged"
        )

# Monsters can only attack the front row
alive_front = [c for c in party[:3] if c.is_alive]
alive_monsters = [m for m in monsters if m.is_alive]

for monster in alive_monsters:
    if alive_front:
        combat.monster_turn(
            monster,
            alive_monsters,
            alive_front,
            party,
            round_num=1
        )
```

### Condition Management

```python
from dnd_5e_core.combat import Condition
from dnd_5e_core.entities import Character

hero = Character.generate_random_character(level=5, class_name="fighter")

# Apply poisoned condition
hero.add_condition(Condition.POISONED)
print(f"Conditions: {hero.conditions}")

# Check before attacking
if hero.has_condition(Condition.PARALYZED):
    print("Cannot attack - paralyzed!")
elif hero.has_condition(Condition.POISONED):
    print("Disadvantage on attack rolls and ability checks")
    # Implement disadvantage logic
    
# Remove after a rest
hero.long_rest()
hero.remove_condition(Condition.POISONED)
```

---

## Implemented Rules

The combat system implements the following D&D 5e rules:

### Attack
- ✅ Attack rolls with attack bonuses
- ✅ Comparison with Armor Class (AC)
- ✅ Critical hit (natural 20)
- ✅ Critical miss (natural 1)
- ✅ Melee and ranged attacks
- ✅ Normal and long range

### Damage
- ✅ Damage dice rolling
- ✅ Damage types (physical and magical)
- ✅ Ability score modifier bonus
- ✅ Doubled damage on critical hits

### Spells
- ✅ Spell slots by level
- ✅ Spell saving throws
- ✅ Spell damage by level
- ✅ Area of effect (AOE) spells
- ✅ Healing spells

### Monster AI
- ✅ Smart target selection
- ✅ Use of healing spells on injured allies
- ✅ Use of special attacks
- ✅ Spell slot management

### Rewards
- ✅ XP distribution according to CR
- ✅ Random gold distribution
- ✅ Automatic level up

---

## See Also

- [entities](./entities.md) - Characters and monsters
- [mechanics](./mechanics.md) - Game rules
- [spells](./spells.md) - Magic system
- [equipment](./equipment.md) - Weapons and armors
