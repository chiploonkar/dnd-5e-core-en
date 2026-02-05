# dnd-5e-core - Guide d'Utilisation pour IA Agentique

**Version du package:** 0.4.3  
**Date de création:** 5 février 2026  
**Objectif:** Documentation optimisée pour l'utilisation du package par des IA agentiques

---

## 📋 Table des Matières

1. [Vue d'ensemble](#vue-densemble)
2. [Installation et Setup](#installation-et-setup)
3. [Concepts Fondamentaux](#concepts-fondamentaux)
4. [Patterns d'Utilisation](#patterns-dutilisation)
5. [API Complète par Module](#api-complète-par-module)
6. [Gestion des Erreurs Courantes](#gestion-des-erreurs-courantes)
7. [Cas d'Usage Avancés](#cas-dusage-avancés)
8. [Intégration avec d'Autres Projets](#intégration-avec-dautres-projets)
9. [Dépannage et Debug](#dépannage-et-debug)
10. [Checklist de Validation](#checklist-de-validation)

---

## 🎯 Vue d'ensemble

### Qu'est-ce que dnd-5e-core?

**dnd-5e-core** est un moteur de règles complet pour Dungeons & Dragons 5e édition. Il fournit:

- **24 Capacités de Classes** (Rage, Extra Attack, Sneak Attack, Ki Points, etc.)
- **20 Traits Raciaux** (Darkvision, Lucky, Fey Ancestry, etc.)
- **40+ Sous-classes** (Champion, Évocation, Domaine de la Vie, etc.)
- **Système de Multiclassing** complet
- **Système de Combat Avancé** avec sorts, conditions, attaques spéciales
- **49 Objets Magiques** (anneaux, baguettes, armes, armures)
- **Système de Trésors** conforme au DMG
- **Système de Conditions** (Empoisonné, Paralysé, Effrayé, etc.)

### Données Embarquées (8.7 MB)

- **332 Monstres** avec stats complètes
- **319+ Sorts** avec descriptions et mécaniques
- **65+ Armes** avec dégâts, propriétés, portées
- **30+ Armures** avec calculs de CA
- **237+ Équipements**
- **100% Offline** - Aucun appel API nécessaire

### Architecture

```
dnd-5e-core/
├── dnd_5e_core/           # Package principal
│   ├── __init__.py        # Exports principaux
│   ├── entities/          # Character, Monster, Sprite
│   ├── equipment/         # Weapon, Armor, MagicItem
│   ├── spells/            # Spell, SpellCaster
│   ├── combat/            # CombatSystem, Condition, Action
│   ├── mechanics/         # Règles du jeu (dés, XP, etc.)
│   ├── races/             # Races et sous-races
│   ├── classes/           # Classes et sous-classes
│   ├── abilities/         # Caractéristiques et compétences
│   └── data/              # Loaders et utilitaires
├── data/                  # Données JSON (8.7 MB)
│   ├── monsters/          # 332 monstres
│   ├── spells/            # 319+ sorts
│   ├── equipment/         # Armes, armures, objets
│   └── magic-items/       # 49 objets magiques
├── examples/              # Exemples d'utilisation
├── tests/                 # Tests unitaires
└── docs/                  # Documentation complète
```

---

## 🔧 Installation et Setup

### Installation Simple

```bash
pip install dnd-5e-core
```

### Installation pour Développement

```bash
git clone https://github.com/codingame-team/dnd-5e-core.git
cd dnd-5e-core
pip install -e .[dev]
```

### Vérification de l'Installation

```python
import dnd_5e_core

# Vérifier la version
print(dnd_5e_core.__version__)  # 0.4.3

# Tester un import simple
from dnd_5e_core import Character, Monster, load_monster

# Charger un monstre pour tester
orc = load_monster("orc")
print(f"Loaded: {orc.name}, HP: {orc.hit_points}, AC: {orc.armor_class}")
```

### Imports Essentiels

```python
# Entités de base
from dnd_5e_core import Character, Monster, Sprite

# Équipement
from dnd_5e_core import Weapon, Armor, HealingPotion
from dnd_5e_core.equipment import get_magic_item, get_special_weapon, get_special_armor

# Combat
from dnd_5e_core.combat import CombatSystem, Condition, Action

# Création de personnages
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.mechanics import level_up_character

# Chargement de données
from dnd_5e_core import load_monster, load_spell, load_weapon, load_armor
from dnd_5e_core.data import load_magic_item, list_monsters, list_spells

# Mécaniques de jeu
from dnd_5e_core.mechanics import (
    roll_dice, DamageDice,
    calculate_encounter_difficulty,
    get_encounter_gold,
    calculate_treasure_hoard
)

# Capacités et traits
from dnd_5e_core.mechanics import ClassAbilities, RacialTraits
```

---

## 🧠 Concepts Fondamentaux

### 1. Character (Personnage)

Un personnage est l'entité principale du joueur.

**Attributs Clés:**
- `name`: Nom du personnage
- `race`: Race (humain, elfe, nain, etc.)
- `class_type`: Classe (guerrier, magicien, etc.)
- `level`: Niveau (1-20)
- `hit_points`: Points de vie actuels
- `max_hit_points`: Points de vie maximum
- `armor_class`: Classe d'armure (CA)
- `abilities`: Scores de caractéristiques (FOR, DEX, CON, INT, SAG, CHA)
- `inventory`: Inventaire (10 emplacements)
- `equipped_items`: Objets équipés
- `is_spell_caster`: Peut lancer des sorts

**Méthodes Importantes:**
- `attack(target)`: Attaquer une cible
- `cast_attack(target, spell)`: Lancer un sort d'attaque
- `cast_heal(target, spell)`: Lancer un sort de soin
- `take_damage(amount)`: Recevoir des dégâts
- `heal(amount)`: Recevoir des soins
- `equip(item)`: Équiper un objet
- `unequip(item)`: Déséquiper un objet
- `can_cast(spell)`: Vérifier si peut lancer un sort
- `saving_throw(ability, dc)`: Jet de sauvegarde

### 2. Monster (Monstre)

Un monstre est une créature hostile.

**Attributs Clés:**
- `name`: Nom du monstre
- `hit_points`: Points de vie
- `armor_class`: Classe d'armure
- `challenge_rating`: Indice de dangerosité (CR)
- `actions`: Actions disponibles
- `special_abilities`: Capacités spéciales
- `xp_value`: Valeur en XP

**Méthodes Importantes:**
- `attack(target)`: Attaquer une cible
- `take_damage(amount)`: Recevoir des dégâts
- `use_special_ability(ability, targets)`: Utiliser une capacité spéciale
- `cast_spell(spell, targets)`: Lancer un sort

### 3. Equipment (Équipement)

**Types d'Équipement:**
- `Weapon`: Armes (épées, arcs, etc.)
- `Armor`: Armures (cotte de mailles, cuir, etc.)
- `HealingPotion`: Potions de soins
- `MagicItem`: Objets magiques (anneaux, baguettes, etc.)

**Slots d'Équipement:**
- `weapon`: Arme principale
- `armor`: Armure
- `shield`: Bouclier
- `ring`: Anneau (2 slots)
- `amulet`: Amulette
- `belt`: Ceinture
- `cloak`: Cape
- `gloves`: Gants
- `boots`: Bottes
- `helmet`: Casque
- `wand`: Baguette

### 4. Spells (Sorts)

**Niveaux de Sorts:** 0-9 (cantrips = niveau 0)

**Types de Sorts:**
- **Attack**: Sorts d'attaque (Magic Missile, Fireball, etc.)
- **Heal**: Sorts de soins (Cure Wounds, Healing Word, etc.)
- **Buff**: Sorts d'amélioration (Bless, Shield, etc.)
- **Debuff**: Sorts d'affaiblissement (Bane, Hold Person, etc.)
- **Utility**: Sorts utilitaires (Detect Magic, Light, etc.)

**Spell Slots (Emplacements de Sorts):**
- Un personnage lanceur de sorts a un nombre limité d'emplacements par niveau
- Les emplacements se rechargent après un repos long

### 5. Combat System (Système de Combat)

Le système de combat gère automatiquement:
- Initiative (ordre de combat)
- Attaques (jets d'attaque, jets de dégâts)
- Sorts (jets d'attaque, jets de sauvegarde)
- Conditions (empoisonné, paralysé, etc.)
- Tactiques (lanceurs de sorts en arrière, combattants au front)

### 6. Conditions (États)

**Conditions Standard D&D 5e:**
- `Blinded`: Aveuglé
- `Charmed`: Charmé
- `Deafened`: Assourdi
- `Frightened`: Effrayé
- `Grappled`: Agrippé
- `Incapacitated`: Neutralisé
- `Invisible`: Invisible
- `Paralyzed`: Paralysé
- `Petrified`: Pétrifié
- `Poisoned`: Empoisonné
- `Prone`: À terre
- `Restrained`: Entravé
- `Stunned`: Étourdi
- `Unconscious`: Inconscient

---

## 🔨 Patterns d'Utilisation

### Pattern 1: Création de Personnage Simple

```python
from dnd_5e_core.data.loaders import simple_character_generator

# Créer un personnage avec capacités automatiques
fighter = simple_character_generator(
    level=5,
    race_name="human",
    class_name="fighter",
    name="Conan"
)

# Le personnage reçoit automatiquement:
# - Extra Attack (2 attaques par tour)
# - Second Wind (soins d'urgence)
# - Action Surge (action supplémentaire)
# - Scores de caractéristiques optimisés pour la classe
# - Équipement de départ

print(f"Name: {fighter.name}")
print(f"Level: {fighter.level}")
print(f"HP: {fighter.hit_points}/{fighter.max_hit_points}")
print(f"AC: {fighter.armor_class}")
print(f"Attacks per turn: {fighter.multi_attacks}")
```

**⚠️ IMPORTANT - Gestion des Prérequis de Classe:**

Le générateur vérifie automatiquement les prérequis minimaux de chaque classe. Si les caractéristiques générées ne correspondent pas, une `ValueError` est levée.

```python
# ❌ ERREUR POSSIBLE:
try:
    paladin = simple_character_generator(5, "human", "paladin", "Arthur")
except ValueError as e:
    print(f"Error: {e}")
    # "Abilities do not meet minimum requirements for class 'paladin': Requires STR 13"
```

**✅ SOLUTION - Forcer les Caractéristiques:**

```python
from dnd_5e_core.abilities import Abilities

# Créer des caractéristiques qui respectent les prérequis
abilities = Abilities(
    strength=15,      # Paladin nécessite FOR 13+
    dexterity=10,
    constitution=14,
    intelligence=8,
    wisdom=12,
    charisma=14       # Paladin nécessite CHA 13+ (pour sorts)
)

# Créer le personnage avec ces caractéristiques
from dnd_5e_core.data.loaders import character_generator
from dnd_5e_core import Race, ClassType

paladin = character_generator(
    level=5,
    race=Race.HUMAN,
    class_type=ClassType.PALADIN,
    abilities=abilities,
    name="Arthur"
)
```

**Prérequis Minimaux par Classe:**

| Classe | Prérequis Minimaux |
|--------|-------------------|
| Barbarian | FOR 13 |
| Bard | CHA 13 |
| Cleric | SAG 13 |
| Druid | SAG 13 |
| Fighter | FOR 13 ou DEX 13 |
| Monk | DEX 13, SAG 13 |
| Paladin | FOR 13, CHA 13 |
| Ranger | DEX 13, SAG 13 |
| Rogue | DEX 13 |
| Sorcerer | CHA 13 |
| Warlock | CHA 13 |
| Wizard | INT 13 |

### Pattern 2: Chargement de Données

```python
from dnd_5e_core import load_monster, load_spell, load_weapon, load_armor
from dnd_5e_core.data import list_monsters, list_spells

# Charger un monstre spécifique
orc = load_monster("orc")
dragon = load_monster("ancient-red-dragon")

# Charger un sort
fireball = load_spell("fireball")
cure_wounds = load_spell("cure-wounds")

# Charger une arme
longsword = load_weapon("longsword")
longbow = load_weapon("longbow")

# Charger une armure
chain_mail = load_armor("chain-mail")
leather = load_armor("leather")

# Lister toutes les ressources disponibles
all_monsters = list_monsters()
all_spells = list_spells()

print(f"Available monsters: {len(all_monsters)}")
print(f"Available spells: {len(all_spells)}")
```

### Pattern 3: Équipement d'Objets

```python
from dnd_5e_core import load_weapon, load_armor

# Créer un personnage
fighter = simple_character_generator(5, "human", "fighter", "Conan")

# Charger des objets
longsword = load_weapon("longsword")
chain_mail = load_armor("chain-mail")

# Trouver un emplacement libre dans l'inventaire
free_slot = None
for i, item in enumerate(fighter.inventory):
    if item is None:
        free_slot = i
        break

# Ajouter à l'inventaire
if free_slot is not None:
    fighter.inventory[free_slot] = longsword
    
    # Équiper l'objet
    success = fighter.equip(longsword)
    print(f"Équipement réussi: {success}")

# Pour l'armure
free_slot = None
for i, item in enumerate(fighter.inventory):
    if item is None:
        free_slot = i
        break

if free_slot is not None:
    fighter.inventory[free_slot] = chain_mail
    success = fighter.equip(chain_mail)
    print(f"Armure équipée: {success}")
    print(f"Nouvelle CA: {fighter.armor_class}")
```

### Pattern 4: Objets Magiques

```python
from dnd_5e_core.equipment import get_magic_item, get_special_weapon

# Charger un objet magique
ring = get_magic_item("ring-of-protection")  # +1 CA, +1 aux jets de sauvegarde
wand = get_magic_item("wand-of-magic-missiles")  # 7 charges

# Charger une arme magique
flame_tongue = get_special_weapon("flame-tongue")  # +1, +2d6 feu
defender = get_special_weapon("defender")  # +3 CA ou +3 attaque

# Équiper un objet magique (nécessite attunement)
for i, item in enumerate(fighter.inventory):
    if item is None:
        fighter.inventory[i] = ring
        messages, success = fighter.equip_magic_item(ring)
        print(messages)
        if success:
            print(f"Nouvelle CA: {fighter.armor_class}")
        break
```

**⚠️ PROBLÈMES COURANTS avec les Objets Magiques:**

```python
# ❌ ERREUR: Équiper un objet déjà équipé
necklace = get_magic_item("necklace-of-fireballs")
fighter.inventory[0] = necklace
messages1, success1 = fighter.equip_magic_item(necklace)  # Succès
messages2, success2 = fighter.equip_magic_item(necklace)  # Échec
print(messages2)  # "Hero cannot equip Necklace of Fireballs - already wearing..."

# ❌ ERREUR: Équiper une arme quand une autre est déjà équipée
defender = get_special_weapon("defender")
fighter.inventory[1] = defender
messages, success = fighter.equip_magic_item(defender)
print(messages)  # "Hero cannot equip Defender - Please un-equip Greatsword first!"

# ✅ SOLUTION: Déséquiper d'abord
if fighter.equipped_items.get('weapon'):
    fighter.unequip(fighter.equipped_items['weapon'])
    
messages, success = fighter.equip_magic_item(defender)
print(messages)  # "⚔️  Hero equipped Defender"
```

### Pattern 5: Combat Automatique

```python
from dnd_5e_core.combat import CombatSystem

# Créer un groupe
party = [
    simple_character_generator(5, "human", "fighter", "Conan"),
    simple_character_generator(5, "elf", "wizard", "Gandalf"),
    simple_character_generator(5, "dwarf", "cleric", "Gimli"),
]

# Charger des monstres
monsters = [
    load_monster("orc"),
    load_monster("orc"),
]

# Initialiser le système de combat
combat = CombatSystem(verbose=True)

# Boucle de combat
round_num = 1
alive_chars = party[:]
alive_monsters = monsters[:]

while alive_chars and alive_monsters and round_num <= 10:
    print(f"=== Round {round_num} ===")
    
    # Tours des personnages
    for char in alive_chars[:]:
        if not alive_monsters:
            break
        if char.hit_points <= 0:
            alive_chars.remove(char)
            continue
            
        combat.character_turn(
            character=char,
            alive_chars=alive_chars,
            alive_monsters=alive_monsters,
            party=party
        )
    
    # Tours des monstres
    for monster in alive_monsters[:]:
        if not alive_chars:
            break
        if monster.hit_points <= 0:
            alive_monsters.remove(monster)
            continue
            
        combat.monster_turn(
            monster=monster,
            alive_monsters=alive_monsters,
            alive_chars=alive_chars,
            party=party,
            round_num=round_num
        )
    
    round_num += 1

# Résultats
if alive_chars:
    print(f"✅ VICTOIRE! Survivants: {len(alive_chars)}")
else:
    print(f"💀 DÉFAITE! Tous les personnages sont tombés.")
```

### Pattern 6: Combat Manuel

```python
# Combat simple 1v1
fighter = simple_character_generator(5, "human", "fighter", "Hero")
orc = load_monster("orc")

round_num = 1
while fighter.hit_points > 0 and orc.hit_points > 0 and round_num <= 10:
    print(f"--- Round {round_num} ---")
    
    # Le combattant attaque
    damage = fighter.attack(orc)
    print(f"{fighter.name} inflige {damage} dégâts!")
    print(f"  {orc.name} HP: {orc.hit_points}")
    
    if orc.hit_points <= 0:
        print(f"  {orc.name} est vaincu!")
        break
    
    # L'orc contre-attaque
    damage = orc.attack(fighter)
    print(f"{orc.name} inflige {damage} dégâts!")
    print(f"  {fighter.name} HP: {fighter.hit_points}")
    
    round_num += 1

if fighter.hit_points > 0:
    print(f"✅ {fighter.name} gagne!")
else:
    print(f"💀 {fighter.name} est vaincu!")
```

### Pattern 7: Lancer de Sorts

```python
from dnd_5e_core import load_spell

# Créer un lanceur de sorts
wizard = simple_character_generator(5, "elf", "wizard", "Merlin")
cleric = simple_character_generator(5, "human", "cleric", "Healer")

# Charger des sorts
fireball = load_spell("fireball")
cure_wounds = load_spell("cure-wounds")

# Vérifier si peut lancer
if wizard.can_cast(fireball):
    print(f"Emplacements de niveau 3: {wizard.sc.spell_slots[3]}")
    
    # Lancer un sort d'attaque
    orc = load_monster("orc")
    damage = wizard.cast_attack(orc, fireball)
    print(f"Fireball inflige {damage} dégâts!")
    print(f"Emplacements restants: {wizard.sc.spell_slots[3]}")

# Sort de soin
if cleric.can_cast(cure_wounds):
    # Soigner le combattant blessé
    fighter.hit_points = 20  # Blessé
    healing = cleric.cast_heal(fighter, cure_wounds)
    print(f"Cure Wounds soigne {healing} HP!")
    print(f"HP de {fighter.name}: {fighter.hit_points}")
```

### Pattern 8: Multiclassing

```python
from dnd_5e_core.mechanics.subclass_system import MulticlassCharacter

# Créer un personnage multiclassé
gish = MulticlassCharacter("Elric")

# Ajouter 5 niveaux de Fighter
for _ in range(5):
    gish.add_class_level('fighter')

# Ajouter 3 niveaux de Wizard
for _ in range(3):
    gish.add_class_level('wizard')

# Vérifier les emplacements de sorts (multiclassé)
spell_slots = gish.get_spell_slots_multiclass()
print(f"Niveau total: {gish.total_level}")
print(f"Classes: {gish.get_class_levels()}")
print(f"Emplacements de sorts: {spell_slots}")
```

### Pattern 9: Génération de Trésors

```python
from dnd_5e_core.mechanics import calculate_treasure_hoard

# Générer un trésor après un combat
treasure = calculate_treasure_hoard(
    encounter_level=5,
    difficulty="hard",
    cr=5,
    include_items=True
)

print(f"Or: {treasure['gold']} po")
print(f"Objets: {[item.name for item in treasure['items']]}")
print(f"Valeur totale: {treasure['total_value']} po")

# Distribution aux personnages
gold_per_char = treasure['gold'] // len(party)
for char in party:
    char.gold += gold_per_char
    print(f"{char.name} reçoit {gold_per_char} po")
```

### Pattern 10: Construction de Rencontres

```python
from dnd_5e_core.mechanics import (
    calculate_encounter_difficulty,
    select_monsters_by_encounter_table
)

# Calculer la difficulté appropriée
party_level = 5
party_size = 4

# Sélectionner des monstres appropriés
monsters, difficulty = select_monsters_by_encounter_table(
    encounter_level=party_level,
    available_monsters=list_monsters(),
    allow_pairs=True
)

print(f"Difficulté: {difficulty}")
print(f"Monstres: {[m.name for m in monsters]}")
print(f"CR total: {sum(m.challenge_rating for m in monsters)}")
```

---

## 📖 API Complète par Module

### Module: `dnd_5e_core` (Exports Principaux)

```python
from dnd_5e_core import (
    # Entités
    Character,
    Monster,
    Sprite,
    
    # Équipement
    Weapon,
    Armor,
    HealingPotion,
    
    # Énumérations
    Race,
    ClassType,
    AbilityType,
    
    # Loaders
    load_monster,
    load_spell,
    load_weapon,
    load_armor,
)
```

### Module: `dnd_5e_core.data.loaders`

**Fonction Principale: `simple_character_generator`**

```python
def simple_character_generator(
    level: int,
    race_name: str,
    class_name: str,
    name: str
) -> Character:
    """
    Génère un personnage avec capacités automatiques.
    
    Args:
        level: Niveau (1-20)
        race_name: "human", "elf", "dwarf", "halfling", "dragonborn", etc.
        class_name: "fighter", "wizard", "cleric", "rogue", "barbarian", etc.
        name: Nom du personnage
        
    Returns:
        Character avec:
        - Scores de caractéristiques optimisés
        - Capacités de classe automatiques
        - Traits raciaux automatiques
        - Équipement de départ
        - Sorts préparés (si lanceur de sorts)
        
    Raises:
        ValueError: Si les caractéristiques ne respectent pas les prérequis minimaux
        
    Examples:
        >>> fighter = simple_character_generator(5, "human", "fighter", "Conan")
        >>> wizard = simple_character_generator(5, "elf", "wizard", "Gandalf")
    """
```

**Fonction Avancée: `character_generator`**

```python
def character_generator(
    level: int,
    race: Race,
    class_type: ClassType,
    abilities: Abilities,
    name: str
) -> Character:
    """
    Génère un personnage avec caractéristiques personnalisées.
    
    Args:
        level: Niveau (1-20)
        race: Énumération Race
        class_type: Énumération ClassType
        abilities: Objet Abilities avec scores
        name: Nom du personnage
        
    Returns:
        Character personnalisé
        
    Examples:
        >>> from dnd_5e_core.abilities import Abilities
        >>> abilities = Abilities(15, 14, 13, 12, 10, 8)
        >>> char = character_generator(
        ...     level=5,
        ...     race=Race.HUMAN,
        ...     class_type=ClassType.FIGHTER,
        ...     abilities=abilities,
        ...     name="Hero"
        ... )
    """
```

**Autres Fonctions:**

```python
def list_monsters() -> List[str]:
    """Liste tous les monstres disponibles."""

def list_spells() -> List[str]:
    """Liste tous les sorts disponibles."""

def list_weapons() -> List[str]:
    """Liste toutes les armes disponibles."""

def list_armors() -> List[str]:
    """Liste toutes les armures disponibles."""

def load_magic_item(name: str) -> MagicItem:
    """Charge un objet magique."""
```

### Module: `dnd_5e_core.combat`

**Classe: `CombatSystem`**

```python
class CombatSystem:
    def __init__(self, verbose: bool = False):
        """
        Initialise le système de combat.
        
        Args:
            verbose: Afficher les détails du combat
        """
    
    def character_turn(
        self,
        character: Character,
        alive_chars: List[Character],
        alive_monsters: List[Monster],
        party: List[Character]
    ):
        """
        Exécute le tour d'un personnage.
        
        Logique automatique:
        - Lanceurs de sorts utilisent des sorts depuis l'arrière
        - Combattants utilisent armes et attaques spéciales
        - Sorts de soin sur alliés blessés
        - Conditions appliquées automatiquement
        
        Args:
            character: Personnage qui joue
            alive_chars: Personnages vivants
            alive_monsters: Monstres vivants
            party: Groupe complet
        """
    
    def monster_turn(
        self,
        monster: Monster,
        alive_monsters: List[Monster],
        alive_chars: List[Character],
        party: List[Character],
        round_num: int
    ):
        """
        Exécute le tour d'un monstre.
        
        Args:
            monster: Monstre qui joue
            alive_monsters: Monstres vivants
            alive_chars: Personnages vivants
            party: Groupe complet
            round_num: Numéro du round
        """
    
    def apply_condition(
        self,
        target: Union[Character, Monster],
        condition: Condition,
        duration: int = 1
    ):
        """
        Applique une condition à une cible.
        
        Args:
            target: Cible de la condition
            condition: Type de condition (Poisoned, Paralyzed, etc.)
            duration: Durée en rounds
        """
```

**Énumération: `Condition`**

```python
class Condition(Enum):
    BLINDED = "blinded"
    CHARMED = "charmed"
    DEAFENED = "deafened"
    FRIGHTENED = "frightened"
    GRAPPLED = "grappled"
    INCAPACITATED = "incapacitated"
    INVISIBLE = "invisible"
    PARALYZED = "paralyzed"
    PETRIFIED = "petrified"
    POISONED = "poisoned"
    PRONE = "prone"
    RESTRAINED = "restrained"
    STUNNED = "stunned"
    UNCONSCIOUS = "unconscious"
```

### Module: `dnd_5e_core.mechanics`

**Fonctions de Dés:**

```python
def roll_dice(dice_notation: str) -> int:
    """
    Lance des dés selon la notation D&D.
    
    Args:
        dice_notation: Format "NdM+B" (ex: "2d6+3", "1d20", "4d8-2")
        
    Returns:
        Résultat du lancé
        
    Examples:
        >>> roll_dice("1d20")  # 1-20
        >>> roll_dice("2d6+3")  # 5-15
        >>> roll_dice("4d8-2")  # 2-30
    """

class DamageDice:
    """Représente des dégâts avec dés."""
    
    def __init__(self, dice_notation: str, damage_type: str = "slashing"):
        """
        Args:
            dice_notation: Format "NdM+B"
            damage_type: Type de dégâts (slashing, piercing, bludgeoning, etc.)
        """
    
    def roll(self) -> int:
        """Lance les dés de dégâts."""
```

**Fonctions de Rencontres:**

```python
def calculate_encounter_difficulty(
    party_level: int,
    party_size: int,
    total_monster_xp: int
) -> str:
    """
    Calcule la difficulté d'une rencontre.
    
    Returns:
        "easy", "medium", "hard", "deadly"
    """

def get_encounter_gold(
    monsters: List[Monster],
    difficulty: str = "medium"
) -> int:
    """
    Calcule l'or récompensé pour une rencontre.
    
    Args:
        monsters: Liste des monstres vaincus
        difficulty: Difficulté de la rencontre
        
    Returns:
        Quantité d'or en pièces d'or (po)
    """

def calculate_treasure_hoard(
    encounter_level: int,
    difficulty: str = "medium",
    cr: float = 1.0,
    include_items: bool = True
) -> Dict[str, Any]:
    """
    Génère un trésor conforme au DMG.
    
    Returns:
        {
            'gold': int,
            'items': List[MagicItem],
            'total_value': int
        }
    """
```

**Fonctions de Niveau:**

```python
def level_up_character(character: Character) -> Character:
    """
    Fait monter un personnage de niveau.
    
    - Augmente HP
    - Augmente proficiency bonus
    - Ajoute nouvelles capacités de classe
    - Ajoute nouveaux emplacements de sorts
    
    Returns:
        Character mis à jour
    """
```

**Capacités de Classes:**

```python
class ClassAbilities:
    """Gère les capacités de classes."""
    
    @staticmethod
    def apply_rage(character: Character) -> None:
        """Applique Rage (Barbarian)."""
    
    @staticmethod
    def apply_extra_attack(character: Character, count: int = 2) -> None:
        """Applique Extra Attack (Fighter, etc.)."""
    
    @staticmethod
    def apply_sneak_attack(character: Character, dice: str) -> None:
        """Applique Sneak Attack (Rogue)."""
    
    @staticmethod
    def apply_ki_points(character: Character, points: int) -> None:
        """Applique Ki Points (Monk)."""
```

**Traits Raciaux:**

```python
class RacialTraits:
    """Gère les traits raciaux."""
    
    @staticmethod
    def apply_darkvision(character: Character, range_ft: int = 60) -> None:
        """Applique Darkvision."""
    
    @staticmethod
    def apply_lucky(character: Character) -> None:
        """Applique Lucky (Halfling)."""
    
    @staticmethod
    def apply_fey_ancestry(character: Character) -> None:
        """Applique Fey Ancestry (Elf)."""
    
    @staticmethod
    def apply_relentless_endurance(character: Character) -> None:
        """Applique Relentless Endurance (Half-Orc)."""
```

### Module: `dnd_5e_core.equipment`

**Fonctions Principales:**

```python
def get_magic_item(name: str) -> MagicItem:
    """
    Charge un objet magique.
    
    Args:
        name: Nom de l'objet (en minuscules, avec tirets)
        
    Returns:
        MagicItem
        
    Examples:
        >>> ring = get_magic_item("ring-of-protection")
        >>> wand = get_magic_item("wand-of-magic-missiles")
        >>> belt = get_magic_item("belt-of-storm-giant-strength")
    """

def get_special_weapon(name: str) -> Weapon:
    """
    Charge une arme magique.
    
    Args:
        name: Nom de l'arme
        
    Returns:
        Weapon avec propriétés magiques
        
    Examples:
        >>> flame_tongue = get_special_weapon("flame-tongue")
        >>> vorpal_sword = get_special_weapon("vorpal-sword")
        >>> defender = get_special_weapon("defender")
    """

def get_special_armor(name: str) -> Armor:
    """
    Charge une armure magique.
    
    Args:
        name: Nom de l'armure
        
    Returns:
        Armor avec propriétés magiques
        
    Examples:
        >>> mithral = get_special_armor("mithral-armor")
        >>> adamantine = get_special_armor("adamantine-armor")
    """
```

**Classe: `MagicItem`**

```python
class MagicItem:
    """Représente un objet magique."""
    
    def __init__(
        self,
        name: str,
        rarity: str,
        requires_attunement: bool = False,
        slot: str = None,
        bonus_ac: int = 0,
        bonus_saves: int = 0,
        charges: int = 0,
        effects: List[str] = None
    ):
        """
        Args:
            name: Nom de l'objet
            rarity: "common", "uncommon", "rare", "very rare", "legendary"
            requires_attunement: Nécessite harmonisation
            slot: Emplacement d'équipement
            bonus_ac: Bonus de CA
            bonus_saves: Bonus aux jets de sauvegarde
            charges: Nombre de charges
            effects: Liste d'effets spéciaux
        """
    
    def use_charge(self) -> bool:
        """Utilise une charge. Returns True si succès."""
    
    def recharge(self, amount: int = None) -> None:
        """Recharge (repos long ou manuel)."""
```

### Module: `dnd_5e_core.entities`

**Classe: `Character` (Détaillée)**

```python
class Character:
    """Personnage joueur."""
    
    # Attributs principaux
    name: str
    race: Race
    class_type: ClassType
    level: int
    hit_points: int
    max_hit_points: int
    armor_class: int
    abilities: Abilities
    proficiency_bonus: int
    
    # Équipement
    inventory: List[Optional[Equipment]]  # 10 emplacements
    equipped_items: Dict[str, Equipment]
    gold: int
    
    # Combat
    multi_attacks: int
    conditions: List[Condition]
    
    # Sorts (si lanceur de sorts)
    is_spell_caster: bool
    sc: Optional[SpellCaster]
    
    # Méthodes de combat
    def attack(self, target: Monster) -> int:
        """
        Attaque avec l'arme équipée.
        
        - Jet d'attaque (1d20 + modificateur)
        - Si touche: jet de dégâts
        - Applique multi_attacks
        
        Returns:
            Dégâts totaux infligés
        """
    
    def cast_attack(self, target: Monster, spell: Spell) -> int:
        """
        Lance un sort d'attaque.
        
        - Vérifie emplacements de sorts
        - Jet d'attaque de sort ou jet de sauvegarde
        - Applique dégâts
        - Consomme emplacement
        
        Returns:
            Dégâts infligés
        """
    
    def cast_heal(self, target: 'Character', spell: Spell) -> int:
        """
        Lance un sort de soin.
        
        Returns:
            HP soignés
        """
    
    def take_damage(self, damage: int) -> None:
        """Reçoit des dégâts."""
    
    def heal(self, amount: int) -> None:
        """Reçoit des soins."""
    
    # Méthodes d'équipement
    def equip(self, item: Equipment) -> bool:
        """
        Équipe un objet normal.
        
        Returns:
            True si succès
        """
    
    def equip_magic_item(self, item: MagicItem) -> Tuple[str, bool]:
        """
        Équipe un objet magique.
        
        - Gère l'harmonisation (attunement)
        - Vérifie les slots
        - Applique les bonus
        
        Returns:
            (message, succès)
        """
    
    def unequip(self, item: Equipment) -> bool:
        """Déséquipe un objet."""
    
    def drink_potion(self, potion: HealingPotion) -> int:
        """
        Boit une potion de soin.
        
        Returns:
            HP soignés
        """
    
    # Méthodes de sorts
    def can_cast(self, spell: Spell) -> bool:
        """Vérifie si peut lancer le sort."""
    
    def get_spell_dc(self) -> int:
        """Calcule le DD des jets de sauvegarde contre les sorts."""
    
    def get_spell_attack_bonus(self) -> int:
        """Calcule le bonus d'attaque de sort."""
    
    # Jets de sauvegarde
    def saving_throw(self, ability: AbilityType, dc: int) -> bool:
        """
        Effectue un jet de sauvegarde.
        
        Args:
            ability: Caractéristique utilisée
            dc: Difficulté (Difficulty Class)
            
        Returns:
            True si réussite
        """
    
    # Repos
    def short_rest(self) -> None:
        """Repos court (1 heure): récupère certaines capacités."""
    
    def long_rest(self) -> None:
        """Repos long (8 heures): récupère HP et sorts."""
```

**Classe: `Monster` (Détaillée)**

```python
class Monster:
    """Créature hostile."""
    
    # Attributs principaux
    name: str
    hit_points: int
    max_hit_points: int
    armor_class: int
    challenge_rating: float
    xp_value: int
    
    # Caractéristiques
    abilities: Abilities
    
    # Combat
    actions: List[Action]
    special_abilities: List[SpecialAbility]
    legendary_actions: int
    
    # Sorts (si lanceur de sorts)
    spells: List[Spell]
    spell_slots: Dict[int, int]
    
    # Immunités/Résistances
    damage_resistances: List[str]
    damage_immunities: List[str]
    condition_immunities: List[Condition]
    
    # Propriétés
    @property
    def is_alive(self) -> bool:
        """Monster a > 0 HP."""
    
    @property
    def is_spellcaster(self) -> bool:
        """Peut lancer des sorts."""
    
    # Méthodes de combat
    def attack(self, target: Character) -> int:
        """Attaque de base."""
    
    def use_special_ability(
        self,
        ability: SpecialAbility,
        targets: List[Character]
    ) -> List[int]:
        """
        Utilise une capacité spéciale.
        
        Returns:
            Liste de dégâts pour chaque cible
        """
    
    def cast_spell(self, spell: Spell, targets: List[Character]) -> List[int]:
        """Lance un sort."""
    
    def take_damage(self, damage: int) -> None:
        """Reçoit des dégâts."""
    
    def heal(self, amount: int) -> None:
        """Reçoit des soins."""
```

### Module: `dnd_5e_core.spells`

**Classe: `Spell`**

```python
class Spell:
    """Représente un sort D&D 5e."""
    
    name: str
    level: int  # 0-9 (0 = cantrip)
    school: str  # "evocation", "abjuration", etc.
    casting_time: str  # "1 action", "1 bonus action", etc.
    range: str  # "60 feet", "self", etc.
    components: List[str]  # ["V", "S", "M"]
    duration: str  # "Instantaneous", "Concentration, up to 1 minute", etc.
    description: str
    
    # Mécanique
    damage: Optional[str]  # "8d6" pour Fireball
    damage_type: Optional[str]  # "fire", "cold", etc.
    healing: Optional[str]  # "1d8+mod" pour Cure Wounds
    save_type: Optional[str]  # "dexterity", "constitution", etc.
    attack_type: Optional[str]  # "ranged", "melee", None
    
    def get_damage_dice(self, caster_level: int = None) -> str:
        """Obtient les dés de dégâts (scaling pour cantrips)."""
    
    def get_healing_dice(self, caster_level: int = None) -> str:
        """Obtient les dés de soin (scaling)."""
```

**Classe: `SpellCaster`**

```python
class SpellCaster:
    """Gère les capacités de lancement de sorts."""
    
    character: Character
    spell_slots: Dict[int, int]  # {niveau: emplacements restants}
    max_spell_slots: Dict[int, int]  # {niveau: emplacements maximum}
    prepared_spells: List[Spell]
    known_spells: List[Spell]
    spellcasting_ability: AbilityType  # INT, WIS, ou CHA
    
    def can_cast(self, spell: Spell) -> bool:
        """Vérifie si peut lancer le sort."""
    
    def cast_spell(self, spell: Spell) -> bool:
        """Consomme un emplacement de sort."""
    
    def get_spell_dc(self) -> int:
        """DD de sauvegarde = 8 + proficiency + modificateur."""
    
    def get_spell_attack_bonus(self) -> int:
        """Bonus d'attaque = proficiency + modificateur."""
    
    def short_rest(self) -> None:
        """Repos court (certaines classes récupèrent des sorts)."""
    
    def long_rest(self) -> None:
        """Repos long (récupère tous les emplacements)."""
```

---

## ⚠️ Gestion des Erreurs Courantes

### Erreur 1: Prérequis de Classe Non Respectés

**Symptôme:**
```python
ValueError: Abilities do not meet minimum requirements for class 'paladin': Requires STR 13
```

**Cause:**
Les caractéristiques générées aléatoirement ne respectent pas les minimums requis.

**Solution:**
```python
from dnd_5e_core.abilities import Abilities
from dnd_5e_core.data.loaders import character_generator
from dnd_5e_core import Race, ClassType

# Définir des caractéristiques valides
abilities = Abilities(
    strength=15,      # Paladin nécessite FOR 13+
    dexterity=10,
    constitution=14,
    intelligence=8,
    wisdom=12,
    charisma=14       # Paladin nécessite CHA 13+
)

# Créer avec ces caractéristiques
paladin = character_generator(
    level=5,
    race=Race.HUMAN,
    class_type=ClassType.PALADIN,
    abilities=abilities,
    name="Arthur"
)
```

### Erreur 2: Objet Magique Déjà Équipé

**Symptôme:**
```
Hero cannot equip Necklace of Fireballs - already wearing Necklace of Fireballs in slot amulet!
```

**Cause:**
Tentative d'équiper un objet déjà équipé ou occupant le même slot.

**Solution:**
```python
# Vérifier avant d'équiper
if magic_item.slot in character.equipped_items:
    current_item = character.equipped_items[magic_item.slot]
    character.unequip(current_item)

# Maintenant équiper
messages, success = character.equip_magic_item(magic_item)
```

### Erreur 3: Arme Déjà Équipée

**Symptôme:**
```
Hero cannot equip Defender - Please un-equip Greatsword first!
```

**Cause:**
Une arme est déjà équipée.

**Solution:**
```python
# Déséquiper l'arme actuelle
if 'weapon' in character.equipped_items:
    character.unequip(character.equipped_items['weapon'])

# Équiper la nouvelle arme
messages, success = character.equip_magic_item(new_weapon)
```

### Erreur 4: Inventaire Plein

**Symptôme:**
Impossible d'ajouter un objet à l'inventaire.

**Cause:**
Les 10 emplacements sont occupés.

**Solution:**
```python
# Trouver un emplacement libre
free_slot = None
for i, item in enumerate(character.inventory):
    if item is None:
        free_slot = i
        break

if free_slot is None:
    # Inventaire plein, libérer un emplacement
    character.inventory[0] = None  # ou vendre/détruire un objet
    free_slot = 0

character.inventory[free_slot] = new_item
```

### Erreur 5: Manque d'Emplacements de Sorts

**Symptôme:**
```python
character.can_cast(spell)  # Returns False
```

**Cause:**
Tous les emplacements de ce niveau sont utilisés.

**Solution:**
```python
# Vérifier les emplacements disponibles
if character.sc and character.sc.spell_slots[spell.level] > 0:
    character.cast_attack(target, spell)
else:
    print(f"No spell slots of level {spell.level} available")
    # Utiliser un sort de niveau inférieur ou une arme
    character.attack(target)
```

### Erreur 6: Monstre Introuvable

**Symptôme:**
```python
load_monster("dragon")  # Returns None
```

**Cause:**
Le nom exact du monstre est différent.

**Solution:**
```python
# Lister tous les monstres disponibles
available = list_monsters()
print([m for m in available if "dragon" in m.lower()])

# Utiliser le nom exact
dragon = load_monster("ancient-red-dragon")
```

### Erreur 7: Condition Non Appliquée

**Symptôme:**
La condition ne s'applique pas correctement.

**Cause:**
Le monstre a une immunité à cette condition.

**Solution:**
```python
from dnd_5e_core.combat import Condition

# Vérifier les immunités
if Condition.POISONED not in monster.condition_immunities:
    combat.apply_condition(monster, Condition.POISONED, duration=3)
else:
    print(f"{monster.name} is immune to poison!")
```

---

## 🎯 Cas d'Usage Avancés

### Cas 1: Système de Combat Complet avec UI

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core import load_monster

class GameEngine:
    """Moteur de jeu complet."""
    
    def __init__(self):
        self.combat = CombatSystem(verbose=True)
        self.party = []
        self.current_encounter = []
        self.round_num = 0
        
    def create_party(self, party_specs):
        """
        Crée un groupe de personnages.
        
        Args:
            party_specs: List[Tuple[level, race, class, name]]
        """
        self.party = []
        for level, race, cls, name in party_specs:
            char = simple_character_generator(level, race, cls, name)
            self.party.append(char)
            
    def start_encounter(self, monster_names):
        """
        Démarre une rencontre.
        
        Args:
            monster_names: List[str] des noms de monstres
        """
        self.current_encounter = []
        for name in monster_names:
            monster = load_monster(name)
            if monster:
                self.current_encounter.append(monster)
        
        self.round_num = 0
        
    def run_round(self):
        """Exécute un round de combat."""
        self.round_num += 1
        
        # Tours des personnages vivants
        alive_chars = [c for c in self.party if c.hit_points > 0]
        alive_monsters = [m for m in self.current_encounter if m.hit_points > 0]
        
        for char in alive_chars:
            if not alive_monsters:
                break
            self.combat.character_turn(
                char, alive_chars, alive_monsters, self.party
            )
            
        # Tours des monstres vivants
        alive_monsters = [m for m in self.current_encounter if m.hit_points > 0]
        for monster in alive_monsters:
            if not alive_chars:
                break
            self.combat.monster_turn(
                monster, alive_monsters, alive_chars, self.party, self.round_num
            )
            
    def is_combat_over(self):
        """Vérifie si le combat est terminé."""
        alive_chars = any(c.hit_points > 0 for c in self.party)
        alive_monsters = any(m.hit_points > 0 for m in self.current_encounter)
        
        return not alive_chars or not alive_monsters
        
    def get_combat_result(self):
        """Retourne le résultat du combat."""
        alive_chars = [c for c in self.party if c.hit_points > 0]
        
        if alive_chars:
            total_xp = sum(m.xp_value for m in self.current_encounter)
            return {
                'victory': True,
                'survivors': len(alive_chars),
                'total_xp': total_xp,
                'xp_per_char': total_xp // len(self.party)
            }
        else:
            return {
                'victory': False,
                'survivors': 0,
                'total_xp': 0,
                'xp_per_char': 0
            }

# Utilisation
engine = GameEngine()
engine.create_party([
    (5, "human", "fighter", "Conan"),
    (5, "elf", "wizard", "Gandalf"),
    (5, "dwarf", "cleric", "Gimli"),
])

engine.start_encounter(["orc", "orc", "goblin"])

while not engine.is_combat_over():
    engine.run_round()
    
result = engine.get_combat_result()
if result['victory']:
    print(f"Victoire! XP par personnage: {result['xp_per_char']}")
else:
    print("Défaite!")
```

### Cas 2: Générateur de Donjon Procédural

```python
from dnd_5e_core.mechanics import (
    select_monsters_by_encounter_table,
    calculate_treasure_hoard
)
from dnd_5e_core.data import list_monsters
import random

class DungeonGenerator:
    """Génère des donjons procéduraux."""
    
    def __init__(self, party_level, party_size):
        self.party_level = party_level
        self.party_size = party_size
        self.all_monsters = list_monsters()
        
    def generate_room(self, difficulty="medium"):
        """Génère une salle de donjon."""
        # Sélectionner des monstres appropriés
        monsters, actual_difficulty = select_monsters_by_encounter_table(
            encounter_level=self.party_level,
            available_monsters=self.all_monsters,
            allow_pairs=True
        )
        
        # Générer du trésor
        avg_cr = sum(m.challenge_rating for m in monsters) / len(monsters)
        treasure = calculate_treasure_hoard(
            encounter_level=self.party_level,
            difficulty=actual_difficulty,
            cr=avg_cr,
            include_items=True
        )
        
        return {
            'monsters': monsters,
            'difficulty': actual_difficulty,
            'treasure': treasure,
            'description': self._generate_description(monsters, treasure)
        }
    
    def _generate_description(self, monsters, treasure):
        """Génère une description narrative."""
        monster_names = [m.name for m in monsters]
        
        if len(monster_names) == 1:
            desc = f"Dans cette salle, un {monster_names[0]} vous attend."
        else:
            desc = f"Dans cette salle, vous trouvez {', '.join(monster_names)}."
            
        if treasure['gold'] > 0:
            desc += f" Un coffre contient {treasure['gold']} po"
            if treasure['items']:
                item_names = [i.name for i in treasure['items']]
                desc += f" et {', '.join(item_names)}"
            desc += "."
            
        return desc
    
    def generate_dungeon(self, num_rooms=5):
        """Génère un donjon complet."""
        dungeon = []
        
        for i in range(num_rooms):
            # Varier la difficulté
            if i == 0:
                difficulty = "easy"  # Première salle facile
            elif i == num_rooms - 1:
                difficulty = "deadly"  # Boss final
            else:
                difficulty = random.choice(["medium", "hard"])
                
            room = self.generate_room(difficulty)
            room['number'] = i + 1
            dungeon.append(room)
            
        return dungeon

# Utilisation
generator = DungeonGenerator(party_level=5, party_size=4)
dungeon = generator.generate_dungeon(num_rooms=5)

for room in dungeon:
    print(f"\n=== Salle {room['number']} - {room['difficulty']} ===")
    print(room['description'])
```

### Cas 3: Système de Progression de Campagne

```python
from dnd_5e_core.mechanics import level_up_character

class CampaignManager:
    """Gère une campagne D&D complète."""
    
    def __init__(self, party):
        self.party = party
        self.encounters_won = 0
        self.total_xp = 0
        self.total_gold = 0
        self.sessions = []
        
    def award_xp(self, xp_amount):
        """Distribue XP et gère les montées de niveau."""
        xp_per_char = xp_amount // len(self.party)
        self.total_xp += xp_amount
        
        for char in self.party:
            char.xp += xp_per_char
            
            # Vérifier montée de niveau
            if char.xp >= self.xp_for_level(char.level + 1):
                print(f"{char.name} monte au niveau {char.level + 1}!")
                char = level_up_character(char)
                
    def xp_for_level(self, level):
        """XP nécessaire pour un niveau."""
        xp_table = {
            1: 0, 2: 300, 3: 900, 4: 2700, 5: 6500,
            6: 14000, 7: 23000, 8: 34000, 9: 48000, 10: 64000,
            11: 85000, 12: 100000, 13: 120000, 14: 140000, 15: 165000,
            16: 195000, 17: 225000, 18: 265000, 19: 305000, 20: 355000
        }
        return xp_table.get(level, 355000)
        
    def award_treasure(self, treasure):
        """Distribue trésor."""
        gold_per_char = treasure['gold'] // len(self.party)
        self.total_gold += treasure['gold']
        
        for char in self.party:
            char.gold += gold_per_char
            
        # Distribuer les objets
        for item in treasure['items']:
            # Distribution aléatoire ou selon logique
            recipient = random.choice(self.party)
            
            # Trouver emplacement libre
            for i, inv_item in enumerate(recipient.inventory):
                if inv_item is None:
                    recipient.inventory[i] = item
                    print(f"{recipient.name} reçoit {item.name}!")
                    break
                    
    def long_rest(self):
        """Repos long pour tout le groupe."""
        for char in self.party:
            char.long_rest()
            
    def session_summary(self):
        """Résumé de la session."""
        summary = {
            'party_level': sum(c.level for c in self.party) // len(self.party),
            'total_xp': self.total_xp,
            'total_gold': self.total_gold,
            'encounters_won': self.encounters_won,
            'party_status': [
                {
                    'name': c.name,
                    'level': c.level,
                    'hp': f"{c.hit_points}/{c.max_hit_points}",
                    'gold': c.gold
                }
                for c in self.party
            ]
        }
        return summary

# Utilisation
campaign = CampaignManager(party)
campaign.award_xp(2000)
campaign.award_treasure(treasure)
campaign.long_rest()
print(campaign.session_summary())
```

---

## 🔌 Intégration avec d'Autres Projets

### Intégration avec PyQt/PySide

```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core import load_monster

class CombatWindow(QMainWindow):
    """Fenêtre de combat avec dnd-5e-core."""
    
    def __init__(self):
        super().__init__()
        self.combat = CombatSystem(verbose=False)
        self.setup_ui()
        
    def setup_ui(self):
        self.text_area = QTextEdit()
        self.setCentralWidget(self.text_area)
        
    def run_combat(self, party, monsters):
        """Exécute un combat et affiche dans l'UI."""
        round_num = 1
        alive_chars = party[:]
        alive_monsters = monsters[:]
        
        while alive_chars and alive_monsters and round_num <= 20:
            self.text_area.append(f"\n=== Round {round_num} ===")
            
            # Tours des personnages
            for char in alive_chars[:]:
                if not alive_monsters:
                    break
                    
                # Capture la sortie
                result = self.combat.character_turn(
                    char, alive_chars, alive_monsters, party
                )
                self.text_area.append(f"{char.name}: {result}")
                
            # Tours des monstres
            for monster in alive_monsters[:]:
                if not alive_chars:
                    break
                    
                result = self.combat.monster_turn(
                    monster, alive_monsters, alive_chars, party, round_num
                )
                self.text_area.append(f"{monster.name}: {result}")
                
            round_num += 1
```

### Intégration avec Pygame

```python
import pygame
from dnd_5e_core.combat import CombatSystem

class PygameGame:
    """Jeu Pygame avec dnd-5e-core."""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.combat = CombatSystem(verbose=False)
        self.font = pygame.font.Font(None, 24)
        
    def draw_character(self, char, x, y):
        """Affiche un personnage."""
        # Nom
        name_surf = self.font.render(char.name, True, (255, 255, 255))
        self.screen.blit(name_surf, (x, y))
        
        # HP
        hp_text = f"HP: {char.hit_points}/{char.max_hit_points}"
        hp_surf = self.font.render(hp_text, True, (0, 255, 0))
        self.screen.blit(hp_surf, (x, y + 25))
        
        # Barre de HP
        hp_percent = char.hit_points / char.max_hit_points
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            (x, y + 50, 100, 10)
        )
        pygame.draw.rect(
            self.screen,
            (0, 255, 0),
            (x, y + 50, int(100 * hp_percent), 10)
        )
        
    def run(self, party, monsters):
        """Boucle principale."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            self.screen.fill((0, 0, 0))
            
            # Afficher le groupe
            for i, char in enumerate(party):
                self.draw_character(char, 50, 50 + i * 100)
                
            # Afficher les monstres
            for i, monster in enumerate(monsters):
                self.draw_character(monster, 500, 50 + i * 100)
                
            pygame.display.flip()
```

### Intégration avec Flask (Web)

```python
from flask import Flask, jsonify, request
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core import load_monster
from dnd_5e_core.combat import CombatSystem

app = Flask(__name__)
combat_system = CombatSystem(verbose=False)

@app.route('/api/character/create', methods=['POST'])
def create_character():
    """API pour créer un personnage."""
    data = request.json
    
    char = simple_character_generator(
        level=data['level'],
        race_name=data['race'],
        class_name=data['class'],
        name=data['name']
    )
    
    return jsonify({
        'name': char.name,
        'level': char.level,
        'hp': char.hit_points,
        'ac': char.armor_class,
        'class': char.class_type.name,
        'race': char.race.name
    })

@app.route('/api/combat/attack', methods=['POST'])
def combat_attack():
    """API pour une attaque."""
    data = request.json
    
    # Charger attaquant et cible
    attacker = simple_character_generator(
        data['attacker']['level'],
        data['attacker']['race'],
        data['attacker']['class'],
        data['attacker']['name']
    )
    
    target = load_monster(data['target'])
    
    # Effectuer l'attaque
    damage = attacker.attack(target)
    
    return jsonify({
        'damage': damage,
        'target_hp': target.hit_points,
        'target_alive': target.hit_points > 0
    })

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🐛 Dépannage et Debug

### Activer le Mode Verbose

```python
from dnd_5e_core.combat import CombatSystem

# Mode verbose pour voir tous les détails
combat = CombatSystem(verbose=True)

# Maintenant tous les calculs sont affichés
combat.character_turn(char, alive_chars, alive_monsters, party)
```

### Inspecter un Personnage

```python
def debug_character(char):
    """Affiche toutes les infos d'un personnage."""
    print(f"=== {char.name} ===")
    print(f"Level: {char.level}")
    print(f"Class: {char.class_type.name}")
    print(f"Race: {char.race.name}")
    print(f"HP: {char.hit_points}/{char.max_hit_points}")
    print(f"AC: {char.armor_class}")
    print(f"Multi-attacks: {char.multi_attacks}")
    
    print("\nAbilities:")
    print(f"  STR: {char.abilities.strength} ({char.abilities.strength_modifier:+d})")
    print(f"  DEX: {char.abilities.dexterity} ({char.abilities.dexterity_modifier:+d})")
    print(f"  CON: {char.abilities.constitution} ({char.abilities.constitution_modifier:+d})")
    print(f"  INT: {char.abilities.intelligence} ({char.abilities.intelligence_modifier:+d})")
    print(f"  WIS: {char.abilities.wisdom} ({char.abilities.wisdom_modifier:+d})")
    print(f"  CHA: {char.abilities.charisma} ({char.abilities.charisma_modifier:+d})")
    
    print("\nEquipped Items:")
    for slot, item in char.equipped_items.items():
        print(f"  {slot}: {item.name if item else 'None'}")
        
    if char.is_spell_caster and char.sc:
        print("\nSpell Slots:")
        for level, slots in char.sc.spell_slots.items():
            if slots > 0:
                print(f"  Level {level}: {slots}")
                
    print(f"\nGold: {char.gold} gp")
```

### Vérifier les Données Chargées

```python
from dnd_5e_core.data import list_monsters, list_spells

# Vérifier que les données sont chargées
monsters = list_monsters()
spells = list_spells()

print(f"Monsters loaded: {len(monsters)}")
print(f"Spells loaded: {len(spells)}")

# Exemples
print("\nSample monsters:", monsters[:5])
print("\nSample spells:", spells[:5])
```

### Tester le Chargement

```python
def test_loaders():
    """Teste tous les loaders."""
    from dnd_5e_core import load_monster, load_spell, load_weapon, load_armor
    
    # Test monster
    orc = load_monster("orc")
    assert orc is not None, "Failed to load orc"
    assert orc.hit_points > 0, "Orc has no HP"
    
    # Test spell
    fireball = load_spell("fireball")
    assert fireball is not None, "Failed to load fireball"
    assert fireball.level == 3, "Fireball should be level 3"
    
    # Test weapon
    sword = load_weapon("longsword")
    assert sword is not None, "Failed to load longsword"
    
    # Test armor
    armor = load_armor("chain-mail")
    assert armor is not None, "Failed to load chain-mail"
    
    print("✅ All loaders working!")

test_loaders()
```

---

## ✅ Checklist de Validation

### Avant de Déployer

- [ ] **Installation testée**
  ```bash
  pip install dnd-5e-core
  python -c "import dnd_5e_core; print(dnd_5e_core.__version__)"
  ```

- [ ] **Imports fonctionnent**
  ```python
  from dnd_5e_core import Character, Monster, load_monster
  ```

- [ ] **Création de personnage fonctionne**
  ```python
  char = simple_character_generator(5, "human", "fighter", "Test")
  assert char.hit_points > 0
  ```

- [ ] **Combat fonctionne**
  ```python
  combat = CombatSystem(verbose=False)
  orc = load_monster("orc")
  damage = char.attack(orc)
  assert damage >= 0
  ```

- [ ] **Objets magiques fonctionnent**
  ```python
  ring = get_magic_item("ring-of-protection")
  assert ring is not None
  ```

- [ ] **Sorts fonctionnent**
  ```python
  wizard = simple_character_generator(5, "elf", "wizard", "Test")
  assert wizard.is_spell_caster
  assert wizard.sc.spell_slots[1] > 0
  ```

### Tests d'Intégration

```python
def integration_test():
    """Test d'intégration complet."""
    
    # 1. Créer un groupe
    party = [
        simple_character_generator(5, "human", "fighter", "Fighter"),
        simple_character_generator(5, "elf", "wizard", "Wizard"),
    ]
    
    # 2. Créer des monstres
    monsters = [load_monster("orc"), load_monster("goblin")]
    
    # 3. Combat
    combat = CombatSystem(verbose=False)
    round_num = 1
    
    while all(c.hit_points > 0 for c in party) and \
          any(m.hit_points > 0 for m in monsters) and \
          round_num <= 5:
        
        for char in party:
            alive_monsters = [m for m in monsters if m.hit_points > 0]
            if alive_monsters:
                combat.character_turn(char, party, alive_monsters, party)
                
        for monster in monsters:
            if monster.hit_points > 0 and any(c.hit_points > 0 for c in party):
                combat.monster_turn(monster, monsters, party, party, round_num)
                
        round_num += 1
    
    # 4. Vérifier résultat
    assert round_num > 1, "Combat should last at least 1 round"
    print("✅ Integration test passed!")

integration_test()
```

---

## 📚 Ressources Supplémentaires

### Documentation Officielle

- **README Principal**: `/Users/display/PycharmProjects/dnd-5e-core/README.md`
- **API Reference**: `/Users/display/PycharmProjects/dnd-5e-core/docs/API_REFERENCE.md`
- **Changelog**: `/Users/display/PycharmProjects/dnd-5e-core/CHANGELOG.md`
- **Guide de Contribution**: `/Users/display/PycharmProjects/dnd-5e-core/CONTRIBUTING.md`

### Exemples

- **Combat System**: `/Users/display/PycharmProjects/dnd-5e-core/examples/combat_system.py`
- **Character Creation**: `/Users/display/PycharmProjects/dnd-5e-core/examples/character_creation.py`
- **Equipment**: `/Users/display/PycharmProjects/dnd-5e-core/examples/equipment_demo.py`

### Projets d'Exemple

- **DND5e-Test**: https://github.com/codingame-team/DND5e-Test
- **DnD-5th-Edition-API**: https://github.com/codingame-team/DnD-5th-Edition-API
- **DnD5e-Scenarios**: https://github.com/codingame-team/DnD5e-Scenarios

### Ressources D&D 5e

- **API Officielle**: https://www.dnd5eapi.co
- **SRD**: https://dnd.wizards.com/resources/systems-reference-document

---

## 🤖 Recommandations pour IA Agentique

### Ordre d'Apprentissage Recommandé

1. **Débutant**:
   - Créer des personnages avec `simple_character_generator`
   - Charger des monstres avec `load_monster`
   - Combat simple avec `attack()`

2. **Intermédiaire**:
   - Utiliser `CombatSystem` pour combat automatique
   - Gérer équipement avec `equip()` et `unequip()`
   - Lancer des sorts avec `cast_attack()` et `cast_heal()`

3. **Avancé**:
   - Multiclassing avec `MulticlassCharacter`
   - Génération de rencontres avec `select_monsters_by_encounter_table`
   - Système de trésors avec `calculate_treasure_hoard`
   - Intégration UI personnalisée

### Patterns à Privilégier

✅ **BON**:
```python
# Utiliser les générateurs
char = simple_character_generator(5, "human", "fighter", "Hero")

# Vérifier avant d'utiliser
if char.can_cast(spell):
    char.cast_attack(target, spell)
    
# Gérer les erreurs
try:
    char = simple_character_generator(5, "human", "paladin", "Hero")
except ValueError as e:
    print(f"Error: {e}")
    # Utiliser des caractéristiques personnalisées
```

❌ **MAUVAIS**:
```python
# Créer manuellement sans vérifications
char = Character(...)  # Trop complexe

# Ne pas vérifier
char.cast_attack(target, spell)  # Peut échouer si pas d'emplacements

# Ignorer les erreurs
char = simple_character_generator(...)  # Peut crash si prérequis non respectés
```

### Debug Efficace

1. **Activer verbose**: `CombatSystem(verbose=True)`
2. **Utiliser debug_character()** (fonction ci-dessus)
3. **Vérifier les données**: `list_monsters()`, `list_spells()`
4. **Tester progressivement**: Créer → Équiper → Combattre

---

## 📝 Notes de Version

**Version 0.4.3** (Actuelle)
- Correction: Vérification des prérequis de classe dans `simple_character_generator`
- Amélioration: Messages d'erreur plus clairs pour équipement magique
- Fix: Gestion des slots d'équipement occupés

**Prochaines Versions**
- 0.4.4: Amélioration du système de conditions
- 0.5.0: Support complet des actions légendaires
- 1.0.0: API stable, support Python 3.13+

---

## 🎯 Conclusion

Ce guide fournit toutes les informations nécessaires pour qu'une IA agentique puisse:

1. **Installer et configurer** le package
2. **Comprendre les concepts** fondamentaux
3. **Utiliser les patterns** courants
4. **Gérer les erreurs** efficacement
5. **Intégrer** avec d'autres projets
6. **Débugger** et valider

Pour toute question ou problème:
- Issues GitHub: https://github.com/codingame-team/dnd-5e-core/issues
- Documentation: https://github.com/codingame-team/dnd-5e-core/docs

---

**Document créé le:** 5 février 2026  
**Auteur:** D&D Development Team  
**Licence:** MIT
