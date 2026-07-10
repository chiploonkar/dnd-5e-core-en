# Integration Guide for populate_functions.py

This document explains how to integrate the new extended monster modules into the `populate_functions.py` file of DnD-5th-Edition-API.

## Step 1: Add Imports

At the beginning of `populate_functions.py`, add:

```python
# Imports for 5e.tools extended monsters
from dnd_5e_core.entities import get_extended_monster_loader, get_special_actions_builder

# Initialize global instances
_extended_monster_loader = get_extended_monster_loader()
_special_actions_builder = get_special_actions_builder()
```

## Step 2: Create a Helper Function

Add this helper function to retrieve monster JSON data:

```python
def get_extended_monster_data(name: str) -> Optional[Dict[str, Any]]:
    """
    Retrieves the JSON data of an extended monster from 5e.tools
    
    :param name: Name of the monster
    :return: Dictionary with monster data or None
    """
    return _extended_monster_loader.get_monster_by_name(name)
```

## Step 3: Verify Actions Implementation

Modify the `get_special_monster_actions()` function to first check if the monster is implemented:

```python
def get_special_monster_actions(name: str) -> tuple[List[Action], List[SpecialAbility], SpellCaster]:
    """
    Retrieves actions and special abilities for a 5e.tools monster
    
    Note: This function is now integrated with dnd-5e-core
    """
    actions: List[Action] = []
    special_abilities: List[SpecialAbility] = []
    spell_caster: SpellCaster = None
    
    # Check if the monster is implemented
    if not _special_actions_builder.is_implemented(name):
        print(f"[WARNING] Monster '{name}' does not have special actions implemented")
        return actions, special_abilities, spell_caster
    
    # Rest of the existing code...
    if name == "Orc Eye of Gruumsh":
        # Existing code...
    elif name == "Ogre Bolt Launcher":
        # Existing code...
    # ... etc.
    
    return actions, special_abilities, spell_caster
```

## Step 4: Use JSON Data (Optional)

If you want to use JSON data instead of hardcoding, you can do:

```python
def create_monster_from_5etools(name: str) -> Optional[Monster]:
    """
    Creates a monster from 5e.tools data
    
    :param name: Name of the monster
    :return: Monster instance or None
    """
    # Retrieve JSON data
    data = get_extended_monster_data(name)
    if not data:
        return None
    
    # Retrieve special actions
    actions, special_abilities, spell_caster = get_special_monster_actions(name)
    
    # Extract base data
    cr = data.get('cr', 0)
    if isinstance(cr, dict):
        cr = cr.get('cr', 0)
    if isinstance(cr, str) and '/' in cr:
        num, den = cr.split('/')
        cr = float(num) / float(den)
    else:
        cr = float(cr)
    
    # Build the monster
    # Note: Adapt according to your data structure
    monster = Monster(
        index=data.get('name', '').lower().replace(' ', '-'),
        name=data['name'],
        abilities=create_abilities_from_data(data),  # To be implemented
        proficiencies=[],  # To be extracted from data
        armor_class=extract_ac(data),  # To be implemented
        hit_points=data.get('hp', {}).get('average', 0),
        hit_dice=data.get('hp', {}).get('formula', '1d8'),
        xp=calculate_xp_from_cr(cr),  # To be implemented
        speed=extract_speed(data),  # To be implemented
        challenge_rating=cr,
        actions=actions,
        sc=spell_caster,
        sa=special_abilities
    )
    
    return monster
```

## Step 5: Utility Functions

Add these functions to extract data:

```python
def extract_ac(data: Dict[str, Any]) -> int:
    """Extracts AC from 5e.tools data"""
    ac_data = data.get('ac', [])
    if isinstance(ac_data, list) and len(ac_data) > 0:
        ac_entry = ac_data[0]
        if isinstance(ac_entry, dict):
            return ac_entry.get('ac', 10)
        return ac_entry
    return 10

def extract_speed(data: Dict[str, Any]) -> int:
    """Extracts speed from 5e.tools data"""
    speed_data = data.get('speed', {})
    if isinstance(speed_data, dict):
        walk = speed_data.get('walk', 30)
        if isinstance(walk, dict):
            return walk.get('number', 30)
        return walk
    return 30

def create_abilities_from_data(data: Dict[str, Any]) -> Abilities:
    """Creates an Abilities object from 5e.tools data"""
    return Abilities(
        strength=data.get('str', 10),
        dexterity=data.get('dex', 10),
        constitution=data.get('con', 10),
        intelligence=data.get('int', 10),
        wisdom=data.get('wis', 10),
        charisma=data.get('cha', 10)
    )

def calculate_xp_from_cr(cr: float) -> int:
    """Calculates XP from CR"""
    xp_by_cr = {
        0: 10, 0.125: 25, 0.25: 50, 0.5: 100,
        1: 200, 2: 450, 3: 700, 4: 1100, 5: 1800,
        6: 2300, 7: 2900, 8: 3900, 9: 5000, 10: 5900,
        # ... complete according to D&D 5e table
    }
    return xp_by_cr.get(cr, int(cr * 1000))
```

## Step 6: Full Usage Example

```python
# In your main code
from populate_functions import create_monster_from_5etools

# Create an extended monster
orc_eye = create_monster_from_5etools("Orc Eye of Gruumsh")
if orc_eye:
    print(f"Created {orc_eye.name} with {len(orc_eye.actions)} actions")
    
# List all implemented monsters
from dnd_5e_core.entities import get_special_actions_builder

builder = get_special_actions_builder()
implemented = builder.get_implemented_monsters()
print(f"Total monsters with actions: {len(implemented)}")
```

## Step 7: Download Tokens

Add a function to download tokens for the monsters used:

```python
from dnd_5e_core.utils import download_monster_token

def download_monster_tokens(monster_names: List[str], output_folder: str = "./images/monsters/tokens"):
    """
    Downloads tokens for a list of monsters
    
    :param monster_names: List of monster names
    :param output_folder: Destination folder
    """
    from dnd_5e_core.entities import get_extended_monster_loader
    
    loader = get_extended_monster_loader()
    monster_list = []
    
    for name in monster_names:
        data = loader.get_monster_by_name(name)
        if data:
            source = data.get('source', 'MM')
            monster_list.append((name, source))
    
    if monster_list:
        from dnd_5e_core.utils import download_tokens_batch
        results = download_tokens_batch(monster_list, output_folder)
        return results
    
    return {}
```

## Important Notes

1. **Dependencies**: Make sure `dnd-5e-core` is installed:
   ```bash
   pip install -e /path/to/dnd-5e-core
   ```

2. **Compatibility**: Existing code continues to work, we are just adding features

3. **Performance**: The loader caches JSON data after the first load

4. **Testing**: Test each monster after migration to verify that actions are correct

## Migration Checklist

- [ ] Add imports at the top of `populate_functions.py`
- [ ] Create helper functions
- [ ] Test with a monster (e.g. "Orc Eye of Gruumsh")
- [ ] Gradually migrate other monsters
- [ ] Download necessary tokens
- [ ] Clean up old JSON files
- [ ] Update project documentation
- [ ] Run tests

## Support

For any questions:
- Consult `docs/EXTENDED_MONSTERS_MIGRATION.md`
- See examples in `test_extended_monsters.py`
- Check `dnd_5e_core/entities/extended_monsters.py` code
