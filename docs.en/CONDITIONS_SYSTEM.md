# Conditions System - Documentation

## Overview

The `dnd-5e-core` package now implements a complete system for parsing and applying conditions for:
- **Monsters**: Conditions are automatically extracted from action descriptions
- **Magic Items**: Items can apply conditions to targets
- **Characters**: Conditions affect combat abilities

## Architecture

### 1. Automatic Parsing of Conditions

#### ConditionParser

The `ConditionParser` class analyzes textual descriptions to extract standard D&D 5e conditions.

```python
from dnd_5e_core.combat import ConditionParser

# Parse from a description
desc = "Target must make a DC 15 Constitution saving throw or be paralyzed for 1 minute."
conditions = ConditionParser.parse_condition_from_description(desc)

# Result: [Condition(name="Paralyzed", dc_type=AbilityType.CON, dc_value=15)]
```

**Recognized conditions**:
- Restrained
- Grappled
- Poisoned
- Paralyzed
- Stunned
- Frightened
- Prone
- Blinded
- Charmed

**Recognized patterns**:
- `"DC XX <ability> saving throw"` → Extracts DC and saving throw type
- `"<ability> save DC XX"` → Alternative format
- Condition keywords in the text → Identifies conditions

### 2. Application to Monsters

Monster actions are automatically parsed when loading from JSON.

```python
from dnd_5e_core.data import load_monster

# Load a monster
spider = load_monster('giant-spider')

# Actions now include conditions
for action in spider.actions:
    if action.effects:  # List of Condition objects
        print(f"{action.name} applies:")
        for condition in action.effects:
            print(f"  - {condition.name} (DC {condition.dc_value} {condition.dc_type.value})")

# In combat
fighter = create_character(...)
messages, damage = spider.attack(fighter, verbose=True)

# Conditions are automatically applied
if fighter.conditions:
    for c in fighter.conditions:
        print(f"Fighter is {c.name}")
```

**Processing flow**:
1. `load_monster()` reads the JSON
2. `ConditionParser.extract_conditions_from_action()` parses the descriptions
3. The `Condition` objects are added to `Action.effects`
4. `Monster.attack()` applies conditions automatically

### 3. Magic Items with Conditions

#### Create a Magic Item

```python
from dnd_5e_core.equipment import create_magic_item_with_conditions, MagicItemRarity, MagicItemType

# Manual creation
wand = create_magic_item_with_conditions(
    name="Wand of Confusion",
    description="This wand confuses enemies",
    rarity=MagicItemRarity.RARE,
    item_type=MagicItemType.WAND,
    action_name="Confuse",
    action_description="Target must make a DC 14 Wisdom saving throw or be stunned for 1 minute.",
    save_dc=14,
    save_ability="wis",
    uses_per_day=3,
    recharge="dawn",
    requires_attunement=True
)

# Conditions are parsed automatically from action_description
```

#### Predefined Items

```python
from dnd_5e_core.equipment import (
    create_wand_of_paralysis,      # Paralyzes (DC 15 CON)
    create_staff_of_entanglement,  # Restrains (DC 13 STR)
    create_ring_of_blinding,       # Blinds (DC 14 CON)
    create_cloak_of_fear,          # Frightens (DC 15 WIS)
    create_poisoned_dagger         # Poisons (DC 13 CON)
)

wand = create_wand_of_paralysis()
print(f"Charges: {wand.actions[0].uses_per_day}")
```

#### Use in Combat

```python
# Equip and attune
wand = create_wand_of_paralysis()
wizard.inventory.append(wand)
wand.equipped = True
wand.attune(wizard)

# Use the action
action = wand.actions[0]  # "Paralyze"

if action.can_use():
    messages, damage, healing = wand.perform_action(
        action=action,
        target=goblin,
        user=wizard,
        verbose=True
    )
    
    # Check applied conditions
    if goblin.conditions:
        for c in goblin.conditions:
            print(f"Goblin is {c.name}")
```

### 4. Condition Management

#### Application

```python
from dnd_5e_core.combat import create_paralyzed_condition

# Create a condition
paralyzed = create_paralyzed_condition(dc_type=AbilityType.CON, dc_value=15)

# Apply to a character
paralyzed.apply_to_character(fighter)

# Apply to a monster
paralyzed.apply_to_monster(goblin)
```

#### Saving Throws

```python
# Attempt to resist/escape
if paralyzed.attempt_save(fighter):
    print("Fighter escapes paralysis!")
    # The condition is automatically removed
else:
    print("Fighter remains paralyzed")
```

#### Manual Removal

```python
# Remove a condition
paralyzed.remove_from_character(fighter)
paralyzed.remove_from_monster(goblin)
```

## Complete Examples

### Example 1: Combat with Giant Spider

```python
from dnd_5e_core.data import load_monster
from dnd_5e_core.data.loaders import simple_character_generator

# Create character and monster
fighter = simple_character_generator(level=5, class_name='fighter', name='Conan')
spider = load_monster('giant-spider')

# Combat
print(f"🕷️ {spider.name} attacks!")

# The spider uses its web attack
web_action = [a for a in spider.actions if 'web' in a.name.lower()][0]
messages, damage = spider.attack(fighter, actions=[web_action])

print(messages)
# Output:
# Giant Spider uses Web on Conan!
# Conan is hit for 0 hit points!
# Conan is now Restrained!

# Check conditions
if fighter.conditions:
    for condition in fighter.conditions:
        print(f"✅ {condition.name} applied")
        print(f"   DC {condition.dc_value} {condition.dc_type.value} to escape")
        
        # Attempt to escape
        if condition.attempt_save(fighter):
            print(f"   Conan escapes!")
```

### Example 2: Wand of Paralysis

```python
from dnd_5e_core.equipment import create_wand_of_paralysis
from dnd_5e_core.data import load_monster

# Create wizard and goblin
wizard = simple_character_generator(level=7, class_name='wizard', name='Gandalf')
goblin = load_monster('goblin')

# Create and equip the wand
wand = create_wand_of_paralysis()
wizard.inventory.append(wand)
wand.equipped = True
wand.attuned = True

# Use the wand
action = wand.actions[0]
print(f"⚡ {wizard.name} uses {wand.name}!")
print(f"   Remaining charges: {action.remaining_uses}/{action.uses_per_day}")

messages, dmg, heal = wand.perform_action(action, goblin, wizard, verbose=True)

# The goblin is paralyzed
if goblin.conditions:
    print(f"🔴 {goblin.name} is paralyzed!")
    
# Recharge after rest
wand.recharge_actions(recharge_type="dawn")
print(f"   Charges after rest: {action.remaining_uses}/{action.uses_per_day}")
```

### Example 3: Parse Custom Descriptions

```python
from dnd_5e_core.combat import ConditionParser

# Description of a custom feature
custom_desc = """
The creature must make a DC 16 Strength saving throw or be grappled.
Additionally, it must make a DC 14 Constitution saving throw or be poisoned
for 1 hour. A grappled creature can use its action to escape with a DC 16
Strength check.
"""

# Parse the conditions
conditions = ConditionParser.parse_condition_from_description(custom_desc)

for condition in conditions:
    print(f"Condition: {condition.name}")
    print(f"  DC: {condition.dc_value} {condition.dc_type.value}")
    print(f"  Description: {condition.desc}")
```

## Integration in the Loader

The system is integrated automatically when loading monsters:

```python
# In dnd_5e_core/data/loader.py
from ..combat.condition_parser import ConditionParser

def _create_monster_from_data(index: str, data: dict):
    # ... existing code ...
    
    for action in data['actions']:
        # Parse conditions automatically
        conditions = ConditionParser.extract_conditions_from_action(action)
        
        # Add to action effects
        action_obj = Action(
            name=action['name'],
            effects=conditions,  # ← Conditions parsed automatically
            # ... other fields ...
        )
```

## Advanced Use Cases

### Multiple Conditions

```python
# A monster can apply multiple conditions
desc = "Target is grappled and poisoned. DC 13 STR to escape grapple, DC 12 CON or remain poisoned."
conditions = ConditionParser.parse_condition_from_description(desc)

# Result: [Grappled(DC 13 STR), Poisoned(DC 12 CON)]
```

### Conditions Linked to the Source

```python
# For frightened, grappled, charmed, restrained
frightened = create_frightened_condition(
    creature=dragon,  # Source of the fear
    dc_type=AbilityType.WIS,
    dc_value=18
)

# The condition references the dragon
frightened.apply_to_character(fighter)
# fighter.conditions[0].creature == dragon
```

### Duration Management

```python
# Conditions can have durations
from dnd_5e_core.combat import Condition, ConditionType, AbilityType

poisoned = Condition(
    index="poisoned",
    name="Poisoned",
    desc="Disadvantage on attack rolls and ability checks",
    type=ConditionType.DEBUFF,
    dc_type=AbilityType.CON,
    dc_value=14,
    duration_rounds=10  # Lasts 10 rounds
)

# In your combat system
for condition in character.conditions:
    if hasattr(condition, 'duration_rounds') and condition.duration_rounds:
        condition.duration_rounds -= 1
        if condition.duration_rounds <= 0:
            condition.remove_from_character(character)
```

## Tests

Execute the complete test suite:

```bash
python tests/test_conditions_system.py
```

Tests included:
1. ✅ Automatic parsing of monsters
2. ✅ Magic items with conditions
3. ✅ Combat with condition application
4. ✅ Using magic items in combat
5. ✅ Direct condition parser

## Performance Notes

- Condition parsing is performed **only once** when loading data
- Conditions are lightweight objects (dataclasses)
- Applying conditions uses references, not deep copies
- Saving throws are O(1)

## Compatibility

✅ Compatible with:
- All monsters from the D&D 5e API
- Existing combat system
- Custom magic items
- DnD5e-Scenarios

## Future Improvements

- [ ] Support for temporary conditions with automatic duration
- [ ] Multiple condition effects (advantage/disadvantage)
- [ ] Condition immunities by race/class
- [ ] Environmental conditions (difficult terrain, darkness)
- [ ] Parse conditions from spells

## API Reference

See the inline documentation in:
- `dnd_5e_core/combat/condition_parser.py`
- `dnd_5e_core/equipment/magic_item.py`
- `dnd_5e_core/equipment/magic_item_factory.py`
