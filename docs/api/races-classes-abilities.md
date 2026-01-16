# Modules: races, classes, abilities

## Module: races

### Vue d'ensemble
Gestion des races et sous-races de personnages D&D 5e.

### Race

**Importation:**
```python
from dnd_5e_core.races import Race
```

**Races disponibles:**
- Dwarf (Nain)
- Elf (Elfe)
- Halfling
- Human (Humain)
- Dragonborn
- Gnome
- Half-Elf (Demi-elfe)
- Half-Orc (Demi-orc)
- Tiefling

**Utilisation:**
```python
from dnd_5e_core.races import Race

# Charger une race
elf_race = Race.load_from_json("elf")
dwarf_race = Race.load_from_json("dwarf")

print(f"{elf_race.name}")
print(f"  Bonus: +{elf_race.ability_bonuses}")
print(f"  Vitesse: {elf_race.speed} pieds")
print(f"  Langues: {elf_race.languages}")
```

### SubRace

**Sous-races:**
- High Elf / Wood Elf
- Mountain Dwarf / Hill Dwarf
- Lightfoot Halfling / Stout Halfling

### Trait

Traits raciaux spéciaux.

**Exemple:**
```python
# Les traits sont chargés automatiquement avec la race
elf = Race.load_from_json("elf")
for trait in elf.traits:
    print(f"- {trait.name}: {trait.desc}")
```

### Language

Langages connus.

**Langages standards:**
- Common (Commun)
- Elvish (Elfe)
- Dwarvish (Nain)
- Draconic (Draconique)
- etc.

---

## Module: classes

### Vue d'ensemble
Classes de personnages avec progression de niveau.

### ClassType

**Importation:**
```python
from dnd_5e_core.classes import ClassType
```

**Classes disponibles:**
- Barbarian (Barbare)
- Bard (Barde)
- Cleric (Clerc)
- Druid (Druide)
- Fighter (Guerrier)
- Monk (Moine)
- Paladin
- Ranger (Rôdeur)
- Rogue (Roublard)
- Sorcerer (Ensorceleur)
- Warlock (Sorcier)
- Wizard (Magicien)

**Utilisation:**
```python
from dnd_5e_core.classes import ClassType

# Charger une classe
fighter = ClassType.load_from_json("fighter")
wizard = ClassType.load_from_json("wizard")

print(f"{fighter.name}")
print(f"  Dé de vie: {fighter.hit_die}")
print(f"  Maîtrises: {fighter.proficiencies}")
```

### Proficiency

Maîtrises et compétences.

**Types:**
```python
from dnd_5e_core.classes import ProfType

ProfType.ARMOR     # Armures
ProfType.WEAPON    # Armes
ProfType.TOOL      # Outils
ProfType.SKILL     # Compétences
ProfType.SAVING_THROW  # Jets de sauvegarde
```

**Exemple:**
```python
fighter = ClassType.load_from_json("fighter")

# Maîtrises d'armures
armor_profs = [p for p in fighter.proficiencies if p.type == ProfType.ARMOR]
print("Maîtrises d'armures:")
for prof in armor_profs:
    print(f"  - {prof.name}")
```

### Multiclass

Gestion du multiclassage.

**Exemple:**
```python
from dnd_5e_core.entities import Character

# Créer un personnage multiclassé
hero = Character.generate_random_character(level=3, class_name="fighter")

# Ajouter un niveau dans une autre classe
# (À implémenter selon vos besoins spécifiques)
```

---

## Module: abilities

### Vue d'ensemble
Les six caractéristiques de base et leurs modificateurs.

### Abilities

**Importation:**
```python
from dnd_5e_core.abilities import Abilities, AbilityType
```

**Création:**
```python
# Méthode 1: Valeurs spécifiques
abilities = Abilities(
    str=16,  # Force
    dex=14,  # Dextérité
    con=13,  # Constitution
    int=12,  # Intelligence
    wis=10,  # Sagesse
    cha=8    # Charisme
)

# Méthode 2: Lancer aléatoire
abilities = Abilities.roll_abilities()

# Accès aux valeurs
print(f"Force: {abilities.str}")
print(f"Modificateur de Force: {abilities.str_mod}")

# Tous les modificateurs
print(f"STR: {abilities.str} ({abilities.str_mod:+d})")
print(f"DEX: {abilities.dex} ({abilities.dex_mod:+d})")
print(f"CON: {abilities.con} ({abilities.con_mod:+d})")
print(f"INT: {abilities.int} ({abilities.int_mod:+d})")
print(f"WIS: {abilities.wis} ({abilities.wis_mod:+d})")
print(f"CHA: {abilities.cha} ({abilities.cha_mod:+d})")
```

### AbilityType

Types de caractéristiques.

```python
from dnd_5e_core.abilities import AbilityType

AbilityType.STRENGTH      # Force
AbilityType.DEXTERITY     # Dextérité
AbilityType.CONSTITUTION  # Constitution
AbilityType.INTELLIGENCE  # Intelligence
AbilityType.WISDOM        # Sagesse
AbilityType.CHARISMA      # Charisme
```

### Skill

Compétences basées sur les caractéristiques.

**Compétences par caractéristique:**

**Force:**
- Athletics (Athlétisme)

**Dextérité:**
- Acrobatics (Acrobaties)
- Sleight of Hand (Escamotage)
- Stealth (Discrétion)

**Intelligence:**
- Arcana
- History (Histoire)
- Investigation
- Nature
- Religion

**Sagesse:**
- Animal Handling (Dressage)
- Insight (Intuition)
- Medicine (Médecine)
- Perception
- Survival (Survie)

**Charisme:**
- Deception (Tromperie)
- Intimidation
- Performance (Représentation)
- Persuasion

**Exemple:**
```python
from dnd_5e_core.entities import Character

hero = Character.generate_random_character(level=5, class_name="rogue")

# Test de compétence
perception_bonus = hero.abilities.wis_mod + hero.proficiency_bonus
perception_roll = randint(1, 20) + perception_bonus

if perception_roll >= 15:
    print("Vous repérez l'embuscade!")
```

### Saving Throw

Jets de sauvegarde.

**Exemple:**
```python
from dnd_5e_core.entities import Character

hero = Character.generate_random_character(level=5, class_name="wizard")

# Jet de sauvegarde
dc_value = 15
success = hero.saving_throw(dc_type="dex", dc_value=dc_value)

if success:
    print("Jet de sauvegarde réussi!")
else:
    print("Jet de sauvegarde raté!")
```

---

## Exemples complets

### Créer un personnage complet

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.abilities import Abilities
from dnd_5e_core.races import Race
from dnd_5e_core.classes import ClassType

# Créer les composants
abilities = Abilities(str=16, dex=14, con=15, int=8, wis=10, cha=12)
race = Race.load_from_json("dwarf")
char_class = ClassType.load_from_json("fighter")

# Créer le personnage
hero = Character(
    id=1,
    name="Thorin Oakenshield",
    abilities=abilities,
    race=race,
    classe=char_class,
    level=5
)

print(f"{hero.name}")
print(f"  Race: {hero.race.name}")
print(f"  Classe: {hero.classe.name} niveau {hero.level}")
print(f"  PV: {hero.max_hit_points}")
print(f"  CA: {hero.armor_class}")
```

### Afficher toutes les races

```python
from dnd_5e_core.races import Race

races = ["dwarf", "elf", "halfling", "human", "dragonborn", 
         "gnome", "half-elf", "half-orc", "tiefling"]

print("RACES DISPONIBLES:\n")
for race_name in races:
    race = Race.load_from_json(race_name)
    print(f"{race.name}")
    print(f"  Vitesse: {race.speed} pieds")
    print(f"  Langues: {len(race.languages)}")
    print(f"  Traits: {len(race.traits)}")
    print()
```

### Afficher toutes les classes

```python
from dnd_5e_core.classes import ClassType

classes = ["barbarian", "bard", "cleric", "druid", "fighter",
           "monk", "paladin", "ranger", "rogue", "sorcerer",
           "warlock", "wizard"]

print("CLASSES DISPONIBLES:\n")
for class_name in classes:
    char_class = ClassType.load_from_json(class_name)
    print(f"{char_class.name}")
    print(f"  Dé de vie: d{char_class.hit_die}")
    print(f"  Caractéristique principale: {char_class.primary_ability}")
    print()
```

---

## Voir aussi

- [entities](./entities.md) - Personnages utilisant races et classes
- [mechanics](./mechanics.md) - Calculs de modificateurs
- [combat](./combat.md) - Utilisation des compétences en combat

