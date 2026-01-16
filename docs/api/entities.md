# Module: entities

## Vue d'ensemble

Le module `entities` contient les classes principales pour représenter les personnages joueurs et les monstres dans D&D 5e.

## Classes principales

### Sprite

Classe de base pour tous les êtres vivants (personnages et monstres).

**Importation:**
```python
from dnd_5e_core.entities import Sprite
```

**Propriétés:**
- `id: int` - Identifiant unique
- `name: str` - Nom de l'entité
- `position: tuple[int, int]` - Position (x, y) pour UI
- `hit_points: int` - Points de vie actuels
- `max_hit_points: int` - Points de vie maximum
- `armor_class: int` - Classe d'armure
- `speed: int` - Vitesse de déplacement

**Méthodes:**
- `is_alive() -> bool` - Vérifie si l'entité est vivante
- `take_damage(amount: int)` - Inflige des dégâts
- `heal(amount: int)` - Soigne l'entité

---

### Character

Représente un personnage joueur avec toutes ses caractéristiques D&D 5e.

**Importation:**
```python
from dnd_5e_core.entities import Character
```

**Création:**

```python
# Méthode 1: Génération aléatoire
hero = Character.generate_random_character(
    level=5,
    class_name="wizard"
)

# Méthode 2: Création manuelle
from dnd_5e_core.abilities import Abilities
from dnd_5e_core.races import Race
from dnd_5e_core.classes import ClassType

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

**Propriétés principales:**
- `name: str` - Nom du personnage
- `level: int` - Niveau du personnage
- `race: Race` - Race du personnage
- `classe: ClassType` - Classe du personnage
- `abilities: Abilities` - Les 6 caractéristiques (STR, DEX, CON, INT, WIS, CHA)
- `hit_points: int` - Points de vie actuels
- `max_hit_points: int` - Points de vie maximum
- `armor_class: int` - Classe d'armure
- `proficiency_bonus: int` - Bonus de maîtrise
- `experience_points: int` - Points d'expérience
- `inventory: Inventory` - Inventaire d'équipement

**Méthodes principales:**

#### Création et gestion
```python
# Générer un personnage aléatoire
char = Character.generate_random_character(level=3, class_name="fighter")

# Monter de niveau
char.level_up()

# Gagner de l'XP
char.gain_xp(300)
```

#### Combat
```python
# Attaquer
char.melee_attack(monster)
char.ranged_attack(monster)

# Lancer un sort
char.cast_spell(spell, target)

# Jets de sauvegarde
success = char.saving_throw(dc_type="dex", dc_value=15)
```

#### Équipement
```python
# Équiper une arme
from dnd_5e_core.data import load_weapon
weapon = load_weapon("longsword")
char.equip_weapon(weapon)

# Équiper une armure
from dnd_5e_core.data import load_armor
armor = load_armor("chain-mail")
char.equip_armor(armor)

# Utiliser une potion
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
hp_gained = char.drink_potion(potion)
```

#### Sorts (pour lanceurs de sorts)
```python
# Préparer des sorts
char.prepare_spells([spell1, spell2, spell3])

# Lancer un sort
char.cast_spell(spell, target, slot_level=1)

# Vérifier les emplacements de sorts disponibles
slots = char.spell_slots
```

#### Repos
```python
# Repos court
char.short_rest()

# Repos long
char.long_rest()
```

#### Sérialisation
```python
# Sauvegarder
char_data = char.to_dict()
with open("character.json", "w") as f:
    json.dump(char_data, f)

# Charger
with open("character.json", "r") as f:
    char_data = json.load(f)
char = Character.from_dict(char_data)
```

---

### Monster

Représente une créature ou un monstre.

**Importation:**
```python
from dnd_5e_core.entities import Monster
from dnd_5e_core.data import load_monster
```

**Création:**

```python
# Charger depuis les données
goblin = load_monster("goblin")
dragon = load_monster("ancient-red-dragon")

# Créer une copie
goblin2 = copy(goblin)
goblin2.hp_roll()  # Relancer les HP
```

**Propriétés principales:**
- `index: str` - Identifiant API (ex: "goblin")
- `name: str` - Nom affiché
- `abilities: Abilities` - Les 6 caractéristiques
- `armor_class: int` - CA
- `hit_points: int` - PV actuels
- `max_hit_points: int` - PV maximum
- `hit_dice: str` - Dés de vie (ex: "2d8+2")
- `challenge_rating: float` - Facteur de puissance
- `xp: int` - XP donné à la défaite
- `speed: int` - Vitesse
- `actions: List[Action]` - Actions de combat
- `sc: SpellCaster` - Lanceur de sorts (optionnel)
- `sa: List[SpecialAbility]` - Capacités spéciales (optionnel)

**Méthodes principales:**

```python
# Vérifier l'état
if monster.is_alive:
    print(f"{monster.name} est vivant")

# Relancer les HP
monster.hp_roll()

# Jets de sauvegarde
success = monster.saving_throw(dc_type="con", dc_value=14)

# Lancer un sort de soin (si lanceur de sorts)
if monster.is_spell_caster:
    hp_gained = monster.cast_heal(spell, slot_level=1, targets=[ally])

# Lancer un sort d'attaque
if monster.is_spell_caster:
    messages, damage = monster.cast_attack(target, spell)
```

**Propriétés calculées:**

```python
# Niveau effectif
effective_level = monster.level

# DC des sorts
if monster.is_spell_caster:
    dc = monster.dc_value
```

---

## Classes utilitaires

### ExtendedMonsterLoader

Chargeur pour monstres étendus (bestiary complète).

**Importation:**
```python
from dnd_5e_core.entities import ExtendedMonsterLoader
```

**Utilisation:**

```python
loader = ExtendedMonsterLoader()

# Charger tous les monstres implémentés
monsters = loader.load_implemented_monsters()

# Rechercher des monstres
goblins = loader.search_monsters(
    name_contains="goblin",
    min_cr=0,
    max_cr=2
)

# Charger un monstre spécifique
goblin_boss = loader.load_monster_by_index("goblin-boss")

# Obtenir les stats
stats = loader.get_monster_stats()
print(f"Total: {stats['total']}")
print(f"Implémentés: {stats['implemented']}")
```

---

## Exemples complets

### Créer un groupe d'aventuriers

```python
from dnd_5e_core.entities import Character

party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=5, class_name="cleric"),
    Character.generate_random_character(level=5, class_name="rogue"),
]

# Afficher le groupe
for hero in party:
    print(f"{hero.name} - {hero.classe.name} niveau {hero.level}")
    print(f"  HP: {hero.hit_points}/{hero.max_hit_points}")
    print(f"  CA: {hero.armor_class}")
```

### Combat simple

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Créer les combattants
hero = Character.generate_random_character(level=3, class_name="fighter")
goblin = load_monster("goblin")

# Combat
while hero.is_alive and goblin.is_alive:
    # Tour du héros
    damage = hero.melee_attack(goblin)
    print(f"{hero.name} inflige {damage} dégâts à {goblin.name}")
    
    if not goblin.is_alive:
        print(f"{goblin.name} est vaincu!")
        break
    
    # Tour du monstre (simplifié)
    from random import randint
    action = goblin.actions[0]
    attack_roll = randint(1, 20) + action.attack_bonus
    
    if attack_roll >= hero.armor_class:
        damage = action.damage.roll()
        hero.hit_points -= damage
        print(f"{goblin.name} inflige {damage} dégâts à {hero.name}")
    
    if not hero.is_alive:
        print(f"{hero.name} est vaincu!")
```

### Sauvegarder et charger

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

print(f"Héros chargé: {loaded_hero.name}")
```

---

## Voir aussi

- [combat](./combat.md) - Système de combat
- [mechanics](./mechanics.md) - Règles de jeu
- [equipment](./equipment.md) - Équipement
- [spells](./spells.md) - Sorts
- [data](./data.md) - Chargement de données

