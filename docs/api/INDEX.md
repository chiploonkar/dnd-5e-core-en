# Documentation API dnd-5e-core

## Vue d'ensemble

`dnd-5e-core` est un package Python complet implémentant les règles de base de D&D 5ème édition.
Le package est indépendant de toute interface utilisateur et peut être utilisé avec pygame, ncurses, web, ou toute autre interface.

**Version:** 0.1.7  
**Auteur:** D&D Development Team  
**Licence:** MIT

## Installation

```bash
pip install dnd-5e-core
```

## Quick Start

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.mechanics import DamageDice
from dnd_5e_core.data import load_monster

# Charger un monstre
goblin = load_monster("goblin")

# Créer un personnage
hero = Character.generate_random_character(level=5, class_name="fighter")

# Lancer des dés
damage = DamageDice("2d6+3")
result = damage.roll()
```

## Structure du Package

Le package est organisé en modules logiques :

### 📦 [entities](./entities.md)
Classes principales pour les personnages et monstres.
- `Sprite` - Classe de base pour tous les êtres
- `Character` - Personnages joueurs
- `Monster` - Créatures et monstres

### ⚔️ [combat](./combat.md)
Système de combat complet.
- `CombatSystem` - Gestion des combats
- `Action` - Actions de combat
- `Damage` - Calcul des dégâts
- `Condition` - États et conditions

### 🎲 [mechanics](./mechanics.md)
Règles de jeu et mécaniques.
- `DamageDice` - Système de lancer de dés
- `experience` - Gestion de l'XP
- `challenge_rating` - Calcul du CR
- `encounter_builder` - Construction de rencontres
- `level_up` - Montée de niveau

### 🎒 [equipment](./equipment.md)
Équipement et objets.
- `Weapon` - Armes
- `Armor` - Armures
- `Equipment` - Équipement général
- `HealingPotion`, `SpeedPotion`, `StrengthPotion` - Potions

### ✨ [spells](./spells.md)
Magie et sorts.
- `Spell` - Sorts
- `SpellCaster` - Lanceurs de sorts
- `spell_slots` - Emplacements de sorts
- `cantrips` - Sorts mineurs

### 👤 [races](./races.md)
Races et sous-races.
- `Race` - Races de personnages
- `SubRace` - Sous-races
- `Trait` - Traits raciaux
- `Language` - Langages

### 🎓 [classes](./classes.md)
Classes de personnages.
- `ClassType` - Classes de personnages
- `Proficiency` - Maîtrises
- `multiclass` - Multiclassage

### 💪 [abilities](./abilities.md)
Caractéristiques et compétences.
- `Abilities` - Six caractéristiques de base
- `AbilityType` - Types de caractéristiques
- `skill` - Compétences
- `saving_throw` - Jets de sauvegarde

### 📊 [data](./data.md)
Chargement et gestion des données.
- `load_monster()` - Charger un monstre
- `load_spell()` - Charger un sort
- `load_weapon()` - Charger une arme
- `load_armor()` - Charger une armure
- `api_client` - Client API D&D 5e
- `serialization` - Sauvegarde/chargement

### 🎨 [ui](./ui.md)
Utilitaires d'interface.
- `Color` - Couleurs
- `color()` - Colorisation de texte
- `cprint()` - Affichage coloré

### 🔧 [utils](./utils.md)
Utilitaires divers.
- `constants` - Constantes du jeu
- `helpers` - Fonctions utilitaires
- `token_downloader` - Téléchargement de tokens

## Exemples d'Utilisation

### Créer un personnage

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.races import Race
from dnd_5e_core.classes import ClassType
from dnd_5e_core.abilities import Abilities

# Méthode 1: Génération aléatoire
hero = Character.generate_random_character(level=3, class_name="wizard")

# Méthode 2: Création manuelle
abilities = Abilities(str=10, dex=14, con=12, int=16, wis=13, cha=8)
race = Race.load_from_json("elf")
char_class = ClassType.load_from_json("wizard")

wizard = Character(
    id=1,
    name="Gandalf",
    abilities=abilities,
    race=race,
    classe=char_class,
    level=5
)
```

### Charger un monstre

```python
from dnd_5e_core.data import load_monster

# Charger depuis l'API
dragon = load_monster("ancient-red-dragon")

# Afficher les statistiques
print(f"CR: {dragon.challenge_rating}")
print(f"HP: {dragon.hit_points}")
print(f"AC: {dragon.armor_class}")
```

### Gérer un combat

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Créer le groupe
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="cleric"),
]

# Charger les monstres
monsters = [
    load_monster("goblin"),
    load_monster("goblin"),
    load_monster("goblin"),
]

# Initialiser le combat
combat = CombatSystem(party, monsters)

# Tour de joueur
target = monsters[0]
combat.player_turn(party[0], target, action_type="melee")

# Tour de monstre
combat.monster_turn(monsters[0], party)
```

### Lancer des dés

```python
from dnd_5e_core.mechanics import DamageDice

# Dés de dégâts
damage = DamageDice("2d6+3")
result = damage.roll()
print(f"Dégâts: {result}")

# Dés multiples
dice = DamageDice("3d8+2d6+5")
total = dice.roll()
```

### Calculer une rencontre

```python
from dnd_5e_core.mechanics import generate_encounter_cr

# Groupe de 4 personnages niveau 5
party_levels = [5, 5, 5, 5]

# Calculer le CR approprié
min_cr, max_cr = generate_encounter_cr(party_levels, difficulty="medium")
print(f"CR recommandé: {min_cr} - {max_cr}")
```

## Projets d'Exemple

### DnD5e-Scenarios
Exemples de scénarios complets utilisant le package.
- Scénarios narratifs avec combats
- Gestion de groupe multi-personnages
- Sauvegarde/chargement de parties
- https://github.com/codingame-team/DnD5e-Scenarios

### DnD-5th-Edition-API
Frontends graphiques (PyQt, Pygame, ncurses).
- Interface PyQt avec gestionnaire de taverne
- Version Pygame avec donjon
- Version ncurses pour terminal
- https://github.com/codingame-team/DnD-5th-Edition-API

## Contribuer

Les contributions sont les bienvenues! Voir [CONTRIBUTING.md](../../CONTRIBUTING.md) pour plus de détails.

## Licence

MIT License - voir [LICENSE](../../LICENSE) pour plus de détails.

## Support

- Issues: https://github.com/codingame-team/dnd-5e-core/issues
- Documentation: https://github.com/codingame-team/dnd-5e-core/docs

