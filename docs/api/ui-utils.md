# Modules: ui & utils

## Module: ui

### Vue d'ensemble
Utilitaires pour l'interface utilisateur : couleurs et affichage formaté.

### Color

Couleurs ANSI pour terminal.

**Importation:**
```python
from dnd_5e_core.ui import Color, color, cprint
```

**Couleurs disponibles:**
```python
Color.BLACK
Color.RED
Color.GREEN
Color.YELLOW
Color.BLUE
Color.MAGENTA
Color.CYAN
Color.WHITE

# Couleurs vives
Color.BRIGHT_BLACK
Color.BRIGHT_RED
Color.BRIGHT_GREEN
Color.BRIGHT_YELLOW
Color.BRIGHT_BLUE
Color.BRIGHT_MAGENTA
Color.BRIGHT_CYAN
Color.BRIGHT_WHITE

# Couleurs de fond
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

Colorise du texte.

**Utilisation:**
```python
from dnd_5e_core.ui import color, Color

# Texte coloré
red_text = color("DANGER!", Color.RED)
green_text = color("SUCCESS!", Color.GREEN)

print(red_text)
print(green_text)

# Avec style
bold_red = color("IMPORTANT", Color.RED, Color.BOLD)
print(bold_red)

# Plusieurs couleurs
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

Affiche du texte coloré directement.

**Utilisation:**
```python
from dnd_5e_core.ui import cprint, Color

# Affichage simple
cprint("Erreur!", Color.RED)
cprint("Succès!", Color.GREEN)
cprint("Info", Color.CYAN)

# Avec plusieurs couleurs
cprint("Attention!", Color.YELLOW, Color.BOLD)
```

---

## Exemples UI

### Affichage de combat coloré

```python
from dnd_5e_core.ui import color, Color
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

hero = Character.generate_random_character(level=5, class_name="fighter")
goblin = load_monster("goblin")

print(color("⚔️  COMBAT!", Color.BOLD, Color.YELLOW))
print()

# Afficher les combattants
print(color(f"🦸 {hero.name}", Color.GREEN, Color.BOLD))
print(f"  HP: {color(str(hero.hit_points), Color.GREEN)}/{hero.max_hit_points}")
print(f"  CA: {hero.armor_class}")
print()

print(color(f"👹 {goblin.name}", Color.RED, Color.BOLD))
print(f"  HP: {color(str(goblin.hit_points), Color.RED)}/{goblin.max_hit_points}")
print(f"  CA: {goblin.armor_class}")
print()

# Afficher une attaque
damage = 8
print(color(f"⚔️  {hero.name} attaque!", Color.CYAN))
print(color(f"💥 {damage} dégâts!", Color.YELLOW, Color.BOLD))
```

### Barre de vie colorée

```python
from dnd_5e_core.ui import color, Color

def hp_bar(current, maximum, width=20):
    """Affiche une barre de vie colorée"""
    percentage = current / maximum
    filled = int(width * percentage)
    bar = "█" * filled + "░" * (width - filled)
    
    # Choisir la couleur selon le pourcentage
    if percentage > 0.6:
        col = Color.GREEN
    elif percentage > 0.3:
        col = Color.YELLOW
    else:
        col = Color.RED
    
    return f"{color(bar, col)} {current}/{maximum} HP"

# Utilisation
print(hp_bar(50, 50))   # Plein (vert)
print(hp_bar(25, 50))   # Moyen (jaune)
print(hp_bar(10, 50))   # Faible (rouge)
```

### Fiche de personnage formatée

```python
from dnd_5e_core.ui import color, Color
from dnd_5e_core.entities import Character

def display_character_sheet(character):
    """Affiche une fiche de personnage formatée"""
    print("=" * 60)
    print(color(f"  {character.name.upper()}", Color.CYAN, Color.BOLD))
    print("=" * 60)
    
    # Informations de base
    print(f"{color('Race:', Color.YELLOW)} {character.race.name}")
    print(f"{color('Classe:', Color.YELLOW)} {character.classe.name} niveau {character.level}")
    print(f"{color('XP:', Color.YELLOW)} {character.experience_points}")
    print()
    
    # Caractéristiques
    print(color("CARACTÉRISTIQUES:", Color.GREEN, Color.BOLD))
    abilities = [
        ("FOR", character.abilities.str, character.abilities.str_mod),
        ("DEX", character.abilities.dex, character.abilities.dex_mod),
        ("CON", character.abilities.con, character.abilities.con_mod),
        ("INT", character.abilities.int, character.abilities.int_mod),
        ("SAG", character.abilities.wis, character.abilities.wis_mod),
        ("CHA", character.abilities.cha, character.abilities.cha_mod),
    ]
    
    for name, value, mod in abilities:
        mod_str = f"{mod:+d}"
        print(f"  {name}: {value:2d} ({color(mod_str, Color.CYAN)})")
    print()
    
    # Combat
    print(color("COMBAT:", Color.RED, Color.BOLD))
    print(f"  PV: {color(str(character.hit_points), Color.GREEN)}/{character.max_hit_points}")
    print(f"  CA: {character.armor_class}")
    print(f"  Bonus de maîtrise: +{character.proficiency_bonus}")
    print("=" * 60)

# Utilisation
hero = Character.generate_random_character(level=5, class_name="wizard")
display_character_sheet(hero)
```

---

## Module: utils

### Vue d'ensemble
Fonctions utilitaires diverses.

### constants

Constantes du jeu.

**Importation:**
```python
from dnd_5e_core.utils import constants
```

**Constantes disponibles:**
```python
# Tailles de créatures
SIZE_TINY = "Tiny"
SIZE_SMALL = "Small"
SIZE_MEDIUM = "Medium"
SIZE_LARGE = "Large"
SIZE_HUGE = "Huge"
SIZE_GARGANTUAN = "Gargantuan"

# Types de créatures
TYPE_HUMANOID = "humanoid"
TYPE_BEAST = "beast"
TYPE_DRAGON = "dragon"
TYPE_UNDEAD = "undead"
# etc.

# Alignements
ALIGNMENT_LAWFUL_GOOD = "lawful-good"
ALIGNMENT_NEUTRAL_GOOD = "neutral-good"
ALIGNMENT_CHAOTIC_GOOD = "chaotic-good"
# etc.
```

### helpers

Fonctions utilitaires.

**Importation:**
```python
from dnd_5e_core.utils import helpers
```

**Fonctions:**
```python
# Calculer modificateur d'une caractéristique
mod = helpers.ability_modifier(16)  # Retourne +3

# Formater un nombre avec signe
text = helpers.format_modifier(3)   # Retourne "+3"
text = helpers.format_modifier(-2)  # Retourne "-2"

# Valider un lancer de dé
is_valid = helpers.is_valid_dice("2d6+3")  # True
is_valid = helpers.is_valid_dice("abc")     # False
```

### token_downloader

Téléchargement de tokens de créatures (pour UI graphique).

**Importation:**
```python
from dnd_5e_core.utils import token_downloader
```

**Utilisation:**
```python
# Télécharger un token de monstre
token_path = token_downloader.download_token("goblin")

# Télécharger tous les tokens
token_downloader.download_all_tokens()
```

---

## Exemples utils

### Calculs de base

```python
from dnd_5e_core.utils import helpers

# Calculer tous les modificateurs
abilities = [8, 10, 12, 14, 16, 18, 20]

print("Valeur → Modificateur")
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

### Validation de dés

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

## Interface complète

### Système de menu coloré

```python
from dnd_5e_core.ui import color, Color, cprint

def display_menu(title, options):
    """Affiche un menu coloré"""
    print()
    print("=" * 60)
    cprint(f"  {title}", Color.CYAN, Color.BOLD)
    print("=" * 60)
    
    for i, option in enumerate(options, 1):
        print(f"  {color(str(i), Color.YELLOW)}. {option}")
    
    print("=" * 60)
    choice = input(color("Votre choix: ", Color.GREEN))
    return choice

# Utilisation
options = [
    "Créer un personnage",
    "Charger un personnage",
    "Commencer un combat",
    "Quitter"
]

choice = display_menu("MENU PRINCIPAL", options)
```

### Logger de combat

```python
from dnd_5e_core.ui import color, Color

class CombatLogger:
    """Logger coloré pour les combats"""
    
    @staticmethod
    def attack(attacker, target, damage):
        print(color(f"⚔️  {attacker} attaque {target}!", Color.CYAN))
        if damage > 0:
            print(color(f"   💥 {damage} dégâts!", Color.YELLOW))
        else:
            print(color("   ✗ Raté!", Color.RED))
    
    @staticmethod
    def heal(healer, target, hp):
        print(color(f"✨ {healer} soigne {target}", Color.GREEN))
        print(color(f"   💚 +{hp} PV", Color.GREEN, Color.BOLD))
    
    @staticmethod
    def spell(caster, spell_name):
        print(color(f"🔮 {caster} lance {spell_name}!", Color.MAGENTA, Color.BOLD))
    
    @staticmethod
    def death(name):
        print(color(f"💀 {name} est vaincu!", Color.RED, Color.BOLD))
    
    @staticmethod
    def victory():
        print()
        print(color("=" * 60, Color.GREEN))
        print(color("  🎉 VICTOIRE!", Color.GREEN, Color.BOLD))
        print(color("=" * 60, Color.GREEN))

# Utilisation
logger = CombatLogger()
logger.attack("Gandalf", "Balrog", 25)
logger.spell("Gandalf", "Fireball")
logger.heal("Cleric", "Fighter", 12)
logger.death("Balrog")
logger.victory()
```

---

## Voir aussi

- [entities](./entities.md) - Personnages et monstres
- [combat](./combat.md) - Système de combat
- [mechanics](./mechanics.md) - Règles de jeu

