# Modules: ui & utils

## Module: ui

### Overview
Utilities for the user interface: colors and formatted display.

### Color

ANSI colors for terminal.

**Import:**
```python
from dnd_5e_core.ui import Color, color, cprint
```

**Available Colors:**
```python
Color.BLACK
Color.RED
Color.GREEN
Color.YELLOW
Color.BLUE
Color.MAGENTA
Color.CYAN
Color.WHITE

# Bright colors
Color.BRIGHT_BLACK
Color.BRIGHT_RED
Color.BRIGHT_GREEN
Color.BRIGHT_YELLOW
Color.BRIGHT_BLUE
Color.BRIGHT_MAGENTA
Color.BRIGHT_CYAN
Color.BRIGHT_WHITE

# Background colors
Color.BG_BLACK
Color.BG_RED
Color.BG_GREEN
# ... etc

# Styles
Color.BOLD
Color.UNDERLINE
Color.RESET
```

### color()

Colorizes text.

**Usage:**
```python
from dnd_5e_core.ui import color, Color

# Colored text
red_text = color("DANGER!", Color.RED)
green_text = color("SUCCESS!", Color.GREEN)

print(red_text)
print(green_text)

# With style
bold_red = color("IMPORTANT", Color.RED, Color.BOLD)
print(bold_red)

# Multiple colors
rainbow = (
    color("R", Color.RED) +
    color("A", Color.YELLOW) +
    color("I", Color.GREEN) +
    color("N", Color.CYAN) +
    color("B", Color.BLUE) +
    color("O", Color.MAGENTA) +
    color("W", Color.RED)
)
print(rainbow)
```

### cprint()

Prints colored text directly.

**Usage:**
```python
from dnd_5e_core.ui import cprint, Color

# Simple display
cprint("Error!", Color.RED)
cprint("Success!", Color.GREEN)
cprint("Info", Color.CYAN)

# With multiple colors
cprint("Warning!", Color.YELLOW, Color.BOLD)
```

---

## UI Examples

### Colored Combat Display

```python
from dnd_5e_core.ui import color, Color
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

hero = Character.generate_random_character(level=5, class_name="fighter")
goblin = load_monster("goblin")

print(color("⚔️  COMBAT!", Color.BOLD, Color.YELLOW))
print()

# Display the combatants
print(color(f"🦸 {hero.name}", Color.GREEN, Color.BOLD))
print(f"  HP: {color(str(hero.hit_points), Color.GREEN)}/{hero.max_hit_points}")
print(f"  AC: {hero.armor_class}")
print()

print(color(f"👹 {goblin.name}", Color.RED, Color.BOLD))
print(f"  HP: {color(str(goblin.hit_points), Color.RED)}/{goblin.max_hit_points}")
print(f"  AC: {goblin.armor_class}")
print()

# Display an attack
damage = 8
print(color(f"⚔️  {hero.name} attacks!", Color.CYAN))
print(color(f"💥 {damage} damage!", Color.YELLOW, Color.BOLD))
```

### Colored Hit Point Bar

```python
from dnd_5e_core.ui import color, Color

def hp_bar(current, maximum, width=20):
    """Displays a colored hit point bar"""
    percentage = current / maximum
    filled = int(width * percentage)
    bar = "█" * filled + "░" * (width - filled)
    
    # Choose the color based on the percentage
    if percentage > 0.6:
        col = Color.GREEN
    elif percentage > 0.3:
        col = Color.YELLOW
    else:
        col = Color.RED
    
    return f"{color(bar, col)} {current}/{maximum} HP"

# Usage
print(hp_bar(50, 50))   # Full (green)
print(hp_bar(25, 50))   # Medium (yellow)
print(hp_bar(10, 50))   # Low (red)
```

### Formatted Character Sheet

```python
from dnd_5e_core.ui import color, Color
from dnd_5e_core.entities import Character

def display_character_sheet(character):
    """Displays a formatted character sheet"""
    print("=" * 60)
    print(color(f"  {character.name.upper()}", Color.CYAN, Color.BOLD))
    print("=" * 60)
    
    # Basic Information
    print(f"{color('Race:', Color.YELLOW)} {character.race.name}")
    print(f"{color('Class:', Color.YELLOW)} {character.classe.name} level {character.level}")
    print(f"{color('XP:', Color.YELLOW)} {character.experience_points}")
    print()
    
    # Ability Scores
    print(color("ABILITY SCORES:", Color.GREEN, Color.BOLD))
    abilities = [
        ("STR", character.abilities.str, character.abilities.str_mod),
        ("DEX", character.abilities.dex, character.abilities.dex_mod),
        ("CON", character.abilities.con, character.abilities.con_mod),
        ("INT", character.abilities.int, character.abilities.int_mod),
        ("WIS", character.abilities.wis, character.abilities.wis_mod),
        ("CHA", character.abilities.cha, character.abilities.cha_mod),
    ]
    
    for name, value, mod in abilities:
        mod_str = f"{mod:+d}"
        print(f"  {name}: {value:2d} ({color(mod_str, Color.CYAN)})")
    print()
    
    # Combat
    print(color("COMBAT:", Color.RED, Color.BOLD))
    print(f"  HP: {color(str(character.hit_points), Color.GREEN)}/{character.max_hit_points}")
    print(f"  AC: {character.armor_class}")
    print(f"  Proficiency Bonus: +{character.proficiency_bonus}")
    print("=" * 60)

# Usage
hero = Character.generate_random_character(level=5, class_name="wizard")
display_character_sheet(hero)
```

---

## Module: utils

### Overview
Miscellaneous utilities.

### constants

Game constants.

**Import:**
```python
from dnd_5e_core.utils import constants
```

**Available Constants:**
```python
# Creature sizes
SIZE_TINY = "Tiny"
SIZE_SMALL = "Small"
SIZE_MEDIUM = "Medium"
SIZE_LARGE = "Large"
SIZE_HUGE = "Huge"
SIZE_GARGANTUAN = "Gargantuan"

# Creature types
TYPE_HUMANOID = "humanoid"
TYPE_BEAST = "beast"
TYPE_DRAGON = "dragon"
TYPE_UNDEAD = "undead"
# etc.

# Alignments
ALIGNMENT_LAWFUL_GOOD = "lawful-good"
ALIGNMENT_NEUTRAL_GOOD = "neutral-good"
ALIGNMENT_CHAOTIC_GOOD = "chaotic-good"
# etc.
```

### helpers

Utility functions.

**Import:**
```python
from dnd_5e_core.utils import helpers
```

**Functions:**
```python
# Calculate ability modifier
mod = helpers.ability_modifier(16)  # Returns +3

# Format modifier with sign
text = helpers.format_modifier(3)   # Returns "+3"
text = helpers.format_modifier(-2)  # Returns "-2"

# Validate a dice roll
is_valid = helpers.is_valid_dice("2d6+3")  # True
is_valid = helpers.is_valid_dice("abc")     # False
```

### token_downloader

Creature token downloader (for graphical UI).

**Import:**
```python
from dnd_5e_core.utils import token_downloader
```

**Usage:**
```python
# Download a monster token
token_path = token_downloader.download_token("goblin")

# Download all tokens
token_downloader.download_all_tokens()
```

---

## Utils Examples

### Basic Calculations

```python
from dnd_5e_core.utils import helpers

# Calculate all modifiers
abilities = [8, 10, 12, 14, 16, 18, 20]

print("Value → Modifier")
for ability in abilities:
    mod = helpers.ability_modifier(ability)
    print(f"{ability:2d} → {helpers.format_modifier(mod)}")

# Output:
#  8 → -1
# 10 → +0
# 12 → +1
# 14 → +2
# 16 → +3
# 18 → +4
# 20 → +5
```

### Dice Validation

```python
from dnd_5e_core.utils import helpers

dice_strings = [
    "1d6",
    "2d8+3",
    "3d10-2",
    "invalid",
    "10d20",
]

for dice in dice_strings:
    valid = helpers.is_valid_dice(dice)
    status = "✅" if valid else "❌"
    print(f"{status} {dice}")
```

---

## Complete Interface

### Colored Menu System

```python
from dnd_5e_core.ui import color, Color, cprint

def display_menu(title, options):
    """Displays a colored menu system"""
    print()
    print("=" * 60)
    cprint(f"  {title}", Color.CYAN, Color.BOLD)
    print("=" * 60)
    
    for i, option in enumerate(options, 1):
        print(f"  {color(str(i), Color.YELLOW)}. {option}")
    
    print("=" * 60)
    choice = input(color("Your choice: ", Color.GREEN))
    return choice

# Usage
options = [
    "Create a character",
    "Load a character",
    "Start a combat",
    "Quit"
]

choice = display_menu("MAIN MENU", options)
```

### Combat Logger

```python
from dnd_5e_core.ui import color, Color

class CombatLogger:
    """Colored logger for combat"""
    
    @staticmethod
    def attack(attacker, target, damage):
        print(color(f"⚔️  {attacker} attacks {target}!", Color.CYAN))
        if damage > 0:
            print(color(f"   💥 {damage} damage!", Color.YELLOW))
        else:
            print(color("   ✗ Missed!", Color.RED))
    
    @staticmethod
    def heal(healer, target, hp):
        print(color(f"✨ {healer} heals {target}", Color.GREEN))
        print(color(f"   💚 +{hp} HP", Color.GREEN, Color.BOLD))
    
    @staticmethod
    def spell(caster, spell_name):
        print(color(f"🔮 {caster} casts {spell_name}!", Color.MAGENTA, Color.BOLD))
    
    @staticmethod
    def death(name):
        print(color(f"💀 {name} is defeated!", Color.RED, Color.BOLD))
    
    @staticmethod
    def victory():
        print()
        print(color("=" * 60, Color.GREEN))
        print(color("  🎉 VICTORY!", Color.GREEN, Color.BOLD))
        print(color("=" * 60, Color.GREEN))

# Usage
logger = CombatLogger()
logger.attack("Gandalf", "Balrog", 25)
logger.spell("Gandalf", "Fireball")
logger.heal("Cleric", "Fighter", 12)
logger.death("Balrog")
logger.victory()
```

---

## See Also

- [entities](entities.md) - Characters and monsters
- [combat](combat.md) - Combat system
- [mechanics](rules-mechanics.md) - Game rules
