# Module: spells

## Overview

The `spells` module manages the D&D 5e magic system: spells, spellcasters, spell slots, and cantrips.

## Core Classes

### Spell

Represents a spell with all its parameters.

**Import:**
```python
from dnd_5e_core.spells import Spell
from dnd_5e_core.data import load_spell
```

**Load a Spell:**
```python
from dnd_5e_core.data import load_spell

# Combat spells
fireball = load_spell("fireball")
magic_missile = load_spell("magic-missile")
lightning_bolt = load_spell("lightning-bolt")

# Healing spells
cure_wounds = load_spell("cure-wounds")
healing_word = load_spell("healing-word")

# Utility spells
shield = load_spell("shield")
detect_magic = load_spell("detect-magic")

print(f"{fireball.name}")
print(f"  Level: {fireball.level}")
print(f"  School: {fireball.school}")
print(f"  Range: {fireball.range}")
print(f"  Casting Time: {fireball.casting_time}")
```

**Properties:**
- `index: str` - Unique identifier
- `name: str` - Spell name
- `level: int` - Level (0-9)
- `school: str` - School of magic
- `casting_time: str` - Casting time
- `range: str` - Range
- `components: List[str]` - Components (V, S, M)
- `duration: str` - Duration
- `concentration: bool` - Requires concentration
- `ritual: bool` - Can be cast as a ritual
- `damage: Optional[Damage]` - Damage (if applicable)
- `dc: Optional[dict]` - Saving throw
- `heal_at_slot_level: Optional[dict]` - Healing by level

**Methods:**
```python
# Get damage at a spell slot level
damage_dice = fireball.get_damage_effect(slot_level=3)
result = damage_dice.roll()

# Get healing at a spell slot level
heal_dice = cure_wounds.get_heal_effect(slot_level=1, ability_modifier=3)
hp_restored = heal_dice.roll()
```

---

### SpellCaster

Management of spellcasting abilities.

**Import:**
```python
from dnd_5e_core.spells import SpellCaster
```

**Properties:**
- `ability: str` - Spellcasting ability ("int", "wis", "cha")
- `ability_modifier: int` - Ability score modifier
- `dc_value: int` - Spell save DC
- `spell_attack_bonus: int` - Spell attack bonus
- `spell_slots: List[int]` - Spell slots by level
- `learned_spells: List[Spell]` - Known spells
- `prepared_spells: List[Spell]` - Prepared spells

**Usage:**
```python
from dnd_5e_core.entities import Character

# Create a spellcaster
wizard = Character.generate_random_character(level=5, class_name="wizard")

# Check spell slots
print(f"Spell slots:")
for level, slots in enumerate(wizard.spell_slots, 1):
    if slots > 0:
        print(f"  Level {level}: {slots}")

# Prepare spells
from dnd_5e_core.data import load_spell
spells_to_prepare = [
    load_spell("magic-missile"),
    load_spell("shield"),
    load_spell("misty-step"),
    load_spell("fireball"),
]
wizard.prepare_spells(spells_to_prepare)

# Cast a spell
fireball = load_spell("fireball")
wizard.cast_spell(fireball, target=monster, slot_level=3)
```

---

### Cantrips

Minor spells (level 0).

**Import:**
```python
from dnd_5e_core.data import load_spell
```

**Combat Cantrips:**
```python
# Cantrips that deal damage
fire_bolt = load_spell("fire-bolt")        # 1d10 fire
ray_of_frost = load_spell("ray-of-frost")  # 1d8 cold
eldritch_blast = load_spell("eldritch-blast")  # 1d10 force

# Usage
damage = fire_bolt.get_damage_effect(character_level=5)
result = damage.roll()
```

**Utility Cantrips:**
```python
mage_hand = load_spell("mage-hand")
prestidigitation = load_spell("prestidigitation")
light = load_spell("light")
```

---

### Spell Slots

Spell slot management.

**Spell slots by class level:**
```python
# Level 1: [2, 0, 0, 0, 0, 0, 0, 0, 0]  # 2 level 1 slots
# Level 5: [4, 3, 2, 0, 0, 0, 0, 0, 0]  # 4/3/2 slots
# Level 20: [4, 3, 3, 3, 3, 2, 2, 1, 1] # All levels

from dnd_5e_core.entities import Character

wizard = Character.generate_random_character(level=5, class_name="wizard")

# Use a slot
slot_level = 3
if wizard.spell_slots[slot_level - 1] > 0:
    wizard.spell_slots[slot_level - 1] -= 1
    print(f"Level {slot_level} slot used")

# Long rest restores all slots
wizard.long_rest()
```

---

## Complete Examples

### Complete Spellcaster

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_spell

# Create a wizard
wizard = Character.generate_random_character(level=5, class_name="wizard")

print(f"{wizard.name} - Wizard level {wizard.level}")
print(f"Intelligence: {wizard.abilities.int}")
print(f"Spell Save DC: {wizard.sc.dc_value}")
print(f"Spell Attack Bonus: {wizard.sc.spell_attack_bonus}")

# Prepare spells
spells = [
    load_spell("magic-missile"),     # Level 1
    load_spell("shield"),            # Level 1
    load_spell("detect-magic"),      # Level 1
    load_spell("misty-step"),        # Level 2
    load_spell("fireball"),          # Level 3
    load_spell("counterspell"),      # Level 3
]

wizard.prepare_spells(spells)

print(f"\nPrepared spells: {len(wizard.sc.prepared_spells)}")
for spell in wizard.sc.prepared_spells:
    print(f"  - {spell.name} (level {spell.level})")

# Combat
from dnd_5e_core.data import load_monster
goblin = load_monster("goblin")

# Cast Magic Missile (always hits)
magic_missile = load_spell("magic-missile")
print(f"\n{wizard.name} casts {magic_missile.name}!")
damage_dice = magic_missile.get_damage_effect(slot_level=1)
damage = damage_dice.roll()
goblin.hit_points -= damage
print(f"  {damage} force damage!")
```

### School of Magic

```python
from dnd_5e_core.data import load_spell

# Schools of magic
schools = {
    "Abjuration": ["shield", "counterspell"],
    "Conjuration": ["misty-step", "conjure-animals"],
    "Divination": ["detect-magic", "identify"],
    "Enchantment": ["charm-person", "hold-person"],
    "Evocation": ["magic-missile", "fireball", "lightning-bolt"],
    "Illusion": ["disguise-self", "invisibility"],
    "Necromancy": ["inflict-wounds", "animate-dead"],
    "Transmutation": ["alter-self", "haste"],
}

print("Spells by school:")
for school, spell_names in schools.items():
    print(f"\n{school}:")
    for spell_name in spell_names:
        spell = load_spell(spell_name)
        print(f"  - {spell.name} (level {spell.level})")
```

### Magical Healing System

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_spell

# Create a cleric
cleric = Character.generate_random_character(level=5, class_name="cleric")
fighter = Character.generate_random_character(level=5, class_name="fighter")

# Injure the fighter
fighter.hit_points = 10
print(f"{fighter.name}: {fighter.hit_points}/{fighter.max_hit_points} HP")

# Cast Cure Wounds
cure_wounds = load_spell("cure-wounds")
print(f"\n{cleric.name} casts {cure_wounds.name}!")

# Level 1
heal_dice = cure_wounds.get_heal_effect(slot_level=1, ability_modifier=cleric.abilities.wis_mod)
hp_restored = heal_dice.roll()
fighter.hit_points = min(fighter.hit_points + hp_restored, fighter.max_hit_points)
print(f"  {hp_restored} HP restored")
print(f"{fighter.name}: {fighter.hit_points}/{fighter.max_hit_points} HP")
```

### Area of Effect (AOE) Spells

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_spell, load_monster

wizard = Character.generate_random_character(level=5, class_name="wizard")

# Group of goblins
goblins = [load_monster("goblin") for _ in range(5)]

# Cast Fireball
fireball = load_spell("fireball")
print(f"{wizard.name} casts {fireball.name}!")

damage_dice = fireball.get_damage_effect(slot_level=3)

for goblin in goblins:
    # DEX saving throw
    save_successful = goblin.saving_throw(
        dc_type=fireball.dc['dc_type']['index'],
        dc_value=wizard.sc.dc_value
    )
    
    damage = damage_dice.roll()
    if save_successful:
        damage = damage // 2
        print(f"  {goblin.name} succeeds on saving throw: {damage} damage (reduced)")
    else:
        print(f"  {goblin.name} fails saving throw: {damage} damage")
    
    goblin.hit_points -= damage
    
    if goblin.is_dead:
        print(f"    {goblin.name} is defeated!")
```

---

## Spells by Level

### Level 0 (Cantrips)
- `fire-bolt` - 1d10 fire
- `ray-of-frost` - 1d8 cold
- `sacred-flame` - 1d8 radiant
- `eldritch-blast` - 1d10 force

### Level 1
- `magic-missile` - 3×(1d4+1) force, always hits
- `cure-wounds` - 1d8 + mod healing
- `shield` - +5 AC (reaction)
- `burning-hands` - 3d6 fire (AOE)

### Level 2
- `scorching-ray` - 3×(2d6) fire
- `misty-step` - Teleport 30 feet
- `hold-person` - Paralysis

### Level 3
- `fireball` - 8d6 fire (AOE)
- `lightning-bolt` - 8d6 lightning (line)
- `counterspell` - Negates a spell

### Level 4+
- `wall-of-fire` (4) - 5d8 fire (wall)
- `cone-of-cold` (5) - 8d8 cold (cone)
- `chain-lightning` (6) - 10d8 lightning (multiple)
- Upcasted `fireball` - +1d6 per level above 3

---

## See Also

- [entities](./entities.md) - Spellcasting characters
- [combat](./combat.md) - Spells in combat
- [mechanics](./mechanics.md) - Dice and calculations
- [data](./data.md) - Spell loading
