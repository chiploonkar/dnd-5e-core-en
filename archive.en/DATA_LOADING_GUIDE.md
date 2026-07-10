# Guide: Loading D&D 5e Data from JSON

## Current Situation

The `dnd-5e-core` package installed via PyPI **does not contain** all JSON data files (races, classes, equipment, etc.) to reduce the package size.

**Only monster data** is included in the PyPI package (`bestiary-sublist-data.json`).

## Options for Loading Data

### Option 1: Manual Creation (Recommended for Examples)

Create your objects manually like in `create_character.py`:

```python
from dnd_5e_core.races import Race
from dnd_5e_core.classes import ClassType

# Create a race manually
elf = Race(
    index="elf",
    name="Elf",
    speed=30,
    ability_bonuses={"dex": 2},
    alignment="Chaotic Good",
    age="Elves can live to be 750 years old",
    size="Medium",
    size_description="Elves range from under 5 to over 6 feet tall",
    starting_proficiencies=[],
    starting_proficiency_options=[],
    languages=[],
    language_desc="You can speak, read, and write Common and Elvish",
    traits=[],
    subraces=[]
)
```

### Option 2: Download JSON Files from GitHub

1. **Download complete data**:
   ```bash
   git clone https://github.com/codingame-team/dnd-5e-core.git
   cd dnd-5e-core
   ```

2. **Copy data folders**:
   ```bash
   cp -r data /your/project/
   ```

3. **Configure the data directory**:
   ```python
   from dnd_5e_core.data import set_data_directory, load_race, load_class
   
   # Point to your local data folder
   set_data_directory("/path/to/data")
   
   # Load data
   elf_data = load_race("elf")
   wizard_data = load_class("wizard")
   
   # Create objects (requires a parser to convert JSON → Python objects)
   # Note: Currently, there is no automatic from_dict() method
   ```

### Option 3: Use the D&D 5e API (Online)

Use the official D&D 5e API: https://www.dnd5eapi.co/

```python
import requests

def load_from_api(category: str, index: str):
    """Load from the D&D 5e API"""
    url = f"https://www.dnd5eapi.co/api/{category}/{index}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Example
elf_data = load_from_api("races", "elf")
wizard_data = load_from_api("classes", "wizard")
```

## JSON Files Available in the PyPI Package

✅ **Included**:
- `dnd_5e_core/data/monsters/bestiary-sublist-data.json` (422 KB)
- `dnd_5e_core/data/monsters/bestiary-sublist-data-all-monsters.json` (8.5 MB)

❌ **Not included** (available on GitHub):
- `data/races/*.json`
- `data/classes/*.json`
- `data/spells/*.json`
- `data/equipment/*.json`
- `data/weapons/*.json`
- `data/armors/*.json`
- `collections/*.json`
- Image tokens (102 MB)

## Why is the data not included?

### PyPI Size Limit
- Default limit: **100 MB**
- Image tokens alone are **102 MB**
- The complete JSON data adds several additional MBs

### Applied Solution
To respect the PyPI limit, we have:
1. ✅ Included monster data (essential for `search_monsters()`)
2. ❌ Excluded image tokens
3. ❌ Excluded other JSON data (races, classes, etc.)

Users can download these files from GitHub according to their needs.

## Complete Example with Manual Data

See the `create_character.py` file for a functional example that:
- Creates an Elf Wizard character
- Defines abilities
- Displays stats

This script works **without needing to download** additional JSON files.

## Available Loading Functions

```python
from dnd_5e_core.data import (
    load_monster,   # ✅ Works (data included)
    load_race,      # ⚠️ Requires local data/races/
    load_class,     # ⚠️ Requires local data/classes/
    load_spell,     # ⚠️ Requires local data/spells/
    load_equipment, # ⚠️ Requires local data/equipment/
    load_weapon,    # ⚠️ Requires local data/weapons/
    load_armor,     # ⚠️ Requires local data/armors/
)
```

## Recommendations

### To test quickly
→ Use manual creation (as in `create_character.py`)

### For a complete project
→ Download data from GitHub and configure `set_data_directory()`

### For a production application
→ Use the online D&D 5e API (https://www.dnd5eapi.co/) with local cache

## Useful Links

- **PyPI Package**: https://pypi.org/project/dnd-5e-core/
- **GitHub Repository**: https://github.com/codingame-team/dnd-5e-core
- **JSON Data**: https://github.com/codingame-team/dnd-5e-core/tree/main/data
- **D&D 5e API**: https://www.dnd5eapi.co/
- **API Documentation**: https://www.dnd5eapi.co/docs/
