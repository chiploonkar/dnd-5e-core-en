# Documentation API - dnd-5e-core

Bienvenue dans la documentation complète du package `dnd-5e-core`.

## 📚 Table des matières

### Documentation principale
- **[INDEX](./INDEX.md)** - Vue d'ensemble complète du package

### Modules du package

#### Modules principaux
1. **[entities](./entities.md)** - Personnages et monstres
   - `Sprite` - Classe de base
   - `Character` - Personnages joueurs
   - `Monster` - Créatures et monstres
   - `ExtendedMonsterLoader` - Chargeur de bestiaire étendu

2. **[combat](./combat.md)** - Système de combat
   - `CombatSystem` - Gestionnaire de combat
   - `Action` - Actions de combat
   - `Damage` - Calcul des dégâts
   - `Condition` - États et conditions
   - `SpecialAbility` - Capacités spéciales

3. **[mechanics](./mechanics.md)** - Règles de jeu
   - `DamageDice` - Système de dés
   - `experience` - Gestion de l'XP
   - `challenge_rating` - Calcul du CR
   - `encounter_builder` - Construction de rencontres
   - `level_up` - Montée de niveau
   - `gold_rewards` - Récompenses en or

4. **[equipment](./equipment.md)** - Équipement
   - `Weapon` - Armes
   - `Armor` - Armures
   - `HealingPotion` - Potions de soin
   - `SpeedPotion` - Potions de vitesse
   - `StrengthPotion` - Potions de force
   - `Inventory` - Gestion d'inventaire

5. **[spells](./spells.md)** - Magie
   - `Spell` - Sorts
   - `SpellCaster` - Lanceurs de sorts
   - `spell_slots` - Emplacements de sorts
   - `cantrips` - Sorts mineurs

6. **[data](./data.md)** - Chargement de données
   - `load_monster()` - Charger un monstre
   - `load_spell()` - Charger un sort
   - `load_weapon()` - Charger une arme
   - `load_armor()` - Charger une armure
   - `api_client` - Client API
   - `serialization` - Sauvegarde/chargement

#### Modules de personnalisation
7. **[races-classes-abilities](./races-classes-abilities.md)** - Personnages
   - **races** - Races et sous-races
   - **classes** - Classes de personnages
   - **abilities** - Caractéristiques et compétences

#### Modules utilitaires
8. **[ui-utils](./ui-utils.md)** - Interface et utilitaires
   - **ui** - Couleurs et affichage
   - **utils** - Fonctions utilitaires

## 🚀 Quick Start

### Installation
```bash
pip install dnd-5e-core
```

### Exemple basique
```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster
from dnd_5e_core.combat import CombatSystem

# Créer un héros
hero = Character.generate_random_character(level=5, class_name="fighter")

# Charger un monstre
goblin = load_monster("goblin")

# Initialiser le combat
combat = CombatSystem(verbose=True)

# Attaquer
combat.player_turn(hero, goblin, action_type="melee")
```

## 📖 Guide de lecture

### Pour débuter
1. Commencez par l'[INDEX](./INDEX.md) pour une vue d'ensemble
2. Lisez [entities](./entities.md) pour comprendre personnages et monstres
3. Consultez [data](./data.md) pour charger des données
4. Explorez [combat](./combat.md) pour les mécaniques de combat

### Pour approfondir
- [mechanics](./mechanics.md) - Comprendre les règles D&D 5e
- [spells](./spells.md) - Système de magie complet
- [equipment](./equipment.md) - Armes, armures et objets

### Pour personnaliser
- [races-classes-abilities](./races-classes-abilities.md) - Créer des personnages uniques
- [ui-utils](./ui-utils.md) - Personnaliser l'affichage

## 🎯 Cas d'usage

### Créer un scénario
```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster
from dnd_5e_core.mechanics import generate_encounter_cr

# Créer le groupe
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=5, class_name="cleric"),
]

# Générer une rencontre appropriée
party_levels = [c.level for c in party]
min_cr, max_cr = generate_encounter_cr(party_levels, difficulty="medium")

# Charger des monstres
monsters = [
    load_monster("orc"),
    load_monster("orc"),
    load_monster("ogre"),
]
```

### Sauvegarder une partie
```python
import json
from dnd_5e_core.entities import Character

# Créer et sauvegarder
hero = Character.generate_random_character(level=5, class_name="wizard")
with open("hero.json", "w") as f:
    json.dump(hero.to_dict(), f, indent=2)

# Charger
with open("hero.json", "r") as f:
    data = json.load(f)
loaded_hero = Character.from_dict(data)
```

### Interface graphique
```python
from dnd_5e_core.combat import CombatSystem

# Callback pour interface personnalisée
def display_message(msg):
    # Votre logique d'affichage (pygame, tkinter, etc.)
    print(msg)

combat = CombatSystem(verbose=False, message_callback=display_message)
```

## 🔗 Liens utiles

### Projets d'exemple
- **DnD5e-Scenarios** - Scénarios narratifs complets
  - https://github.com/codingame-team/DnD5e-Scenarios
  
- **DnD-5th-Edition-API** - Frontends graphiques (PyQt, Pygame, ncurses)
  - https://github.com/codingame-team/DnD-5th-Edition-API

### Ressources D&D 5e
- API officielle: https://www.dnd5eapi.co
- Règles SRD: https://dnd.wizards.com/resources/systems-reference-document

## 📝 Notes

- Toutes les classes sont documentées avec des exemples
- Les exemples sont testés et fonctionnels
- Le package est indépendant de toute UI
- Compatible Python 3.8+

## 🤝 Contribution

Pour contribuer à la documentation:
1. Créez une issue pour discuter des changements
2. Forkez le repository
3. Créez une pull request

Voir [CONTRIBUTING.md](../../CONTRIBUTING.md) pour plus de détails.

## 📄 Licence

MIT License - voir [LICENSE](../../LICENSE)

