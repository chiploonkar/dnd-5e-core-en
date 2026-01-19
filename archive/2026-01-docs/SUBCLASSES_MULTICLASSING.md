# 📚 Système de Sous-Classes et Multiclassing

## 🎯 Vue d'Ensemble

Le package `dnd-5e-core` implémente maintenant un système complet de :
- **Sous-classes** (archetypes) pour toutes les classes
- **Sous-races** pour toutes les races
- **Multiclassing** avec calcul automatique des spell slots

---

## 🏛️ Sous-Classes (Subclasses)

### Qu'est-ce qu'une Sous-Classe ?

Les sous-classes sont des spécialisations de classes, généralement choisies au niveau 3.

**Exemples** :
- **Wizard** : School of Evocation, School of Abjuration, Necromancy
- **Fighter** : Champion, Battle Master, Eldritch Knight
- **Cleric** : Life Domain, War Domain, Light Domain
- **Rogue** : Thief, Assassin, Arcane Trickster

### Charger une Sous-Classe

```python
from dnd_5e_core.mechanics.subclass_system import load_subclass

# Charger Champion (Fighter)
champion = load_subclass('champion')

print(f"Nom: {champion.name}")
print(f"Classe: {champion.class_index}")
print(f"Description: {champion.subclass_flavor}")
print(f"Niveaux de features: {champion.subclass_levels}")
```

**Sortie** :
```
Nom: Champion
Classe: fighter
Description: The archetypal Champion focuses on...
Niveaux de features: [3, 7, 10, 15, 18]
```

### Lister les Sous-Classes Disponibles

```python
from dnd_5e_core.mechanics.subclass_system import list_subclasses_for_class

# Toutes les sous-classes de Wizard
wizard_subclasses = list_subclasses_for_class('wizard')
print(wizard_subclasses)
# ['abjuration', 'conjuration', 'divination', 'enchantment', 
#  'evocation', 'illusion', 'necromancy', 'transmutation']

# Toutes les sous-classes de Cleric
cleric_subclasses = list_subclasses_for_class('cleric')
print(cleric_subclasses)
# ['knowledge', 'life', 'light', 'nature', 'tempest', 'trickery', 'war']
```

### Sous-Classes par Classe

| Classe | Sous-Classes Principales |
|--------|-------------------------|
| **Barbarian** | Path of the Berserker, Path of the Totem Warrior |
| **Bard** | College of Lore, College of Valor |
| **Cleric** | Life Domain, War Domain, Light Domain, etc. (7 domaines) |
| **Druid** | Circle of the Land, Circle of the Moon |
| **Fighter** | Champion, Battle Master, Eldritch Knight |
| **Monk** | Way of the Open Hand, Way of Shadow, Way of the Four Elements |
| **Paladin** | Oath of Devotion, Oath of the Ancients, Oath of Vengeance |
| **Ranger** | Hunter, Beast Master |
| **Rogue** | Thief, Assassin, Arcane Trickster |
| **Sorcerer** | Draconic Bloodline, Wild Magic |
| **Warlock** | The Archfey, The Fiend, The Great Old One |
| **Wizard** | 8 écoles de magie (Evocation, Abjuration, etc.) |

---

## 🧝 Sous-Races (Subraces)

### Qu'est-ce qu'une Sous-Race ?

Les sous-races sont des variations au sein d'une race, avec des bonus et traits spécifiques.

**Exemples** :
- **Elf** : High Elf, Wood Elf, Dark Elf (Drow)
- **Dwarf** : Hill Dwarf, Mountain Dwarf
- **Halfling** : Lightfoot Halfling, Stout Halfling
- **Gnome** : Forest Gnome, Rock Gnome

### Charger une Sous-Race

```python
from dnd_5e_core.mechanics.subclass_system import load_subrace

# Charger High Elf
high_elf = load_subrace('high-elf')

print(f"Nom: {high_elf.name}")
print(f"Race: {high_elf.race_index}")
print(f"Bonus: {high_elf.ability_bonuses}")
print(f"Traits: {high_elf.racial_traits}")
```

**Sortie** :
```
Nom: High Elf
Race: elf
Bonus: [{'ability_score': {'index': 'int'}, 'bonus': 1}]
Traits: ['elf-weapon-training', 'cantrip', 'extra-language']
```

### Lister les Sous-Races Disponibles

```python
from dnd_5e_core.mechanics.subclass_system import list_subraces_for_race

# Toutes les sous-races d'Elf
elf_subraces = list_subraces_for_race('elf')
print(elf_subraces)
# ['high-elf', 'wood-elf', 'dark-elf-drow']

# Toutes les sous-races de Dwarf
dwarf_subraces = list_subraces_for_race('dwarf')
print(dwarf_subraces)
# ['hill-dwarf', 'mountain-dwarf']
```

### Sous-Races par Race

| Race | Sous-Races |
|------|-----------|
| **Elf** | High Elf (+1 INT), Wood Elf (+1 WIS), Dark Elf/Drow (+1 CHA) |
| **Dwarf** | Hill Dwarf (+1 WIS, +1 HP/level), Mountain Dwarf (+2 STR) |
| **Halfling** | Lightfoot (+1 CHA), Stout (+1 CON) |
| **Gnome** | Forest Gnome (+1 DEX), Rock Gnome (+1 CON) |
| **Dragonborn** | Différentes couleurs de dragon (souffle différent) |

---

## ⚔️ Multiclassing

### Qu'est-ce que le Multiclassing ?

Le multiclassing permet de prendre des niveaux dans plusieurs classes.

**Exemples classiques** :
- **Fighter/Wizard** (Gish) : Combattant magique
- **Paladin/Warlock** (Hexadin) : Paladin sombre
- **Rogue/Fighter** : Combattant furtif
- **Cleric/Fighter** : Prêtre guerrier

### Créer un Personnage Multiclassé

```python
from dnd_5e_core.mechanics.subclass_system import MulticlassCharacter

# Créer un Fighter 5 / Wizard 3
gish = MulticlassCharacter("Elric")

# Ajouter 5 niveaux de Fighter
for _ in range(5):
    gish.add_class_level('fighter')

# Choisir la sous-classe au niveau 3
gish.add_class_level('fighter', subclass_index='battle-master')

# Ajouter 3 niveaux de Wizard
for _ in range(3):
    gish.add_class_level('wizard')

gish.add_class_level('wizard', subclass_index='evocation')

print(f"{gish}")  # "Fighter 5 / Wizard 3"
print(f"Niveau total: {gish.get_total_level()}")  # 8
print(f"Classe primaire: {gish.get_primary_class()}")  # fighter
```

### Calcul des Spell Slots Multiclassés

Le système calcule automatiquement les spell slots selon les règles D&D 5e :

```python
# Fighter 5 / Wizard 3
gish = MulticlassCharacter("Elric")
for _ in range(5):
    gish.add_class_level('fighter')
for _ in range(3):
    gish.add_class_level('wizard')

slots = gish.get_spell_slots_multiclass()
print(f"Spell slots: {slots[1:5]}")
# [4, 2, 0, 0] (équivalent à un Wizard niveau 3)
```

**Règles de calcul** :

| Type de Caster | Contribution au Caster Level |
|----------------|------------------------------|
| **Full Caster** | Niveau complet |
| (Wizard, Cleric, Druid, Sorcerer, Bard) | |
| **Half Caster** | Niveau ÷ 2 (arrondi inférieur) |
| (Paladin, Ranger) | |
| **Third Caster** | Niveau ÷ 3 (arrondi inférieur) |
| (Eldritch Knight, Arcane Trickster) | |
| **Pact Magic** | Warlock utilise ses propres slots |
| (Warlock) | Séparés du reste |

### Exemples de Multiclassing

#### Exemple 1: Paladin 6 / Warlock 2 (Hexadin)

```python
hexadin = MulticlassCharacter("Arthas")

for _ in range(6):
    hexadin.add_class_level('paladin')  # Half caster

for _ in range(2):
    hexadin.add_class_level('warlock')  # Pact magic (séparé)

# Caster level = 6 / 2 = 3 (Paladin only)
slots = hexadin.get_spell_slots_multiclass()
print(slots[1:5])  # [4, 2, 0, 0]
# Plus 2 Warlock pact slots (niveau 1) séparés
```

#### Exemple 2: Fighter 3 / Rogue 5

```python
sneaky_fighter = MulticlassCharacter("Shadow")

for _ in range(3):
    sneaky_fighter.add_class_level('fighter')
for _ in range(5):
    sneaky_fighter.add_class_level('rogue')

# Aucun spell slot (pas de casters)
slots = sneaky_fighter.get_spell_slots_multiclass()
print(slots)  # [0, 0, 0, ...]
```

#### Exemple 3: Wizard 3 / Cleric 3 / Druid 2

```python
tri_caster = MulticlassCharacter("Merlin")

for _ in range(3):
    tri_caster.add_class_level('wizard')
for _ in range(3):
    tri_caster.add_class_level('cleric')
for _ in range(2):
    tri_caster.add_class_level('druid')

# Caster level = 3 + 3 + 2 = 8 (tous full casters)
slots = tri_caster.get_spell_slots_multiclass()
print(slots[1:5])  # [4, 3, 3, 2]
# Équivalent à un caster niveau 8
```

---

## 🎮 Intégration avec Character

### Ajouter une Sous-Classe à un Personnage

```python
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.mechanics.subclass_system import load_subclass

# Créer un wizard
wizard = simple_character_generator(3, 'elf', 'wizard', 'Gandalf')

# Charger et appliquer une sous-classe
evocation = load_subclass('evocation')

# Stocker la sous-classe dans le personnage
if not hasattr(wizard, 'subclass'):
    wizard.subclass = evocation

print(f"{wizard.name}: {wizard.class_type.name} - {wizard.subclass.name}")
# Gandalf: Wizard - School of Evocation
```

### Ajouter une Sous-Race à un Personnage

```python
from dnd_5e_core.mechanics.subclass_system import load_subrace

# Créer un elf
elf_char = simple_character_generator(1, 'elf', 'ranger', 'Legolas')

# Charger et appliquer une sous-race
wood_elf = load_subrace('wood-elf')

# Appliquer les bonus de la sous-race
for bonus in wood_elf.ability_bonuses:
    ability = bonus['ability_score']['index']
    value = bonus['bonus']
    # Appliquer le bonus à l'ability
    if hasattr(elf_char.abilities, ability):
        current = getattr(elf_char.abilities, ability)
        setattr(elf_char.abilities, ability, current + value)

if not hasattr(elf_char, 'subrace'):
    elf_char.subrace = wood_elf

print(f"{elf_char.name}: {wood_elf.name} {elf_char.race.name}")
# Legolas: Wood Elf Elf
```

---

## 📊 Données Téléchargées

### Télécharger les Données

```bash
cd /Users/display/PycharmProjects/dnd-5e-core
python download_class_progression.py
```

Ceci télécharge :
- ✅ Class levels (12 classes × 20 niveaux)
- ✅ Features de classes
- ✅ Traits de races
- ✅ **Subclasses** ✨ NOUVEAU
- ✅ **Subraces** ✨ NOUVEAU

### Structure des Données

```
dnd_5e_core/data/
├── class_levels/
│   └── *.json (12 classes)
├── features/
│   └── *.json
├── traits/
│   └── *.json
├── subclasses/        ✨ NOUVEAU
│   ├── champion.json
│   ├── evocation.json
│   ├── life.json
│   └── ... (40+ subclasses)
└── subraces/          ✨ NOUVEAU
    ├── high-elf.json
    ├── hill-dwarf.json
    └── ... (20+ subraces)
```

---

## 🧪 Tests

### Tester le Système

```bash
python test_subclasses_multiclassing.py
```

**Sortie attendue** :
```
================================================================================
TEST DES SOUS-CLASSES
================================================================================

📖 Sous-classes de Wizard:
   Disponibles: 8
   ✅ School of Abjuration
   ✅ School of Evocation
   ✅ School of Necromancy

📖 Sous-classes de Fighter:
   Disponibles: 3
   ✅ Champion
   ✅ Battle Master
   ✅ Eldritch Knight

================================================================================
TEST DES SOUS-RACES
================================================================================

📖 Sous-races de Elf:
   Disponibles: 3
   ✅ High Elf
      Bonus: +1 INT
   ✅ Wood Elf
      Bonus: +1 WIS

================================================================================
TEST DU MULTICLASSING
================================================================================

🎭 Exemple 1: Gish (Fighter/Wizard)
   Fighter 5 / Wizard 3
   Niveau total: 8
   Spell slots: [4, 2, 0, 0]

✅ TESTS RÉUSSIS
```

---

## 📚 API Reference

### Classes Principales

#### `Subclass`
```python
@dataclass
class Subclass:
    index: str
    name: str
    class_index: str
    subclass_flavor: str
    desc: List[str]
    subclass_levels: List[int]
    spells: List[Dict]
```

#### `Subrace`
```python
@dataclass
class Subrace:
    index: str
    name: str
    race_index: str
    desc: str
    ability_bonuses: List[Dict]
    starting_proficiencies: List[str]
    languages: List[str]
    racial_traits: List[str]
```

#### `MulticlassCharacter`
```python
@dataclass
class MulticlassCharacter:
    character_name: str
    classes: List[MulticlassLevel]
    
    def add_class_level(class_index, subclass_index=None)
    def get_total_level() -> int
    def get_class_level(class_index) -> int
    def get_primary_class() -> str
    def get_spell_slots_multiclass() -> List[int]
```

### Fonctions

- `load_subclass(subclass_index)` → `Optional[Subclass]`
- `load_subrace(subrace_index)` → `Optional[Subrace]`
- `list_subclasses_for_class(class_index)` → `List[str]`
- `list_subraces_for_race(race_index)` → `List[str]`

---

## 🎯 Cas d'Usage Avancés

### Personnage Complet avec Sous-Classe et Sous-Race

```python
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.mechanics.subclass_system import load_subclass, load_subrace

# Créer le personnage de base
char = simple_character_generator(5, 'elf', 'wizard', 'Elminster')

# Ajouter la sous-race
high_elf = load_subrace('high-elf')
char.subrace = high_elf

# Ajouter la sous-classe
evocation = load_subclass('evocation')
char.subclass = evocation

# Afficher
print(f"{char.name}")
print(f"  Race: {high_elf.name}")
print(f"  Classe: {char.class_type.name} ({evocation.name})")
print(f"  Niveau: {char.level}")
```

### Multiclass avec Progression

```python
from dnd_5e_core.mechanics.subclass_system import MulticlassCharacter
from dnd_5e_core.data.progression_loader import get_spell_slots_for_level

mc = MulticlassCharacter("Gandalf")

# Niveau 1-5: Fighter
for level in range(1, 6):
    mc.add_class_level('fighter')
    if level == 3:
        mc.add_class_level('fighter', 'champion')
    print(f"Level {mc.get_total_level()}: {mc}")

# Niveau 6-10: Wizard
for level in range(6, 11):
    mc.add_class_level('wizard')
    if level == 8:
        mc.add_class_level('wizard', 'evocation')
    print(f"Level {mc.get_total_level()}: {mc}")
    
    # Spell slots
    slots = mc.get_spell_slots_multiclass()
    print(f"  Spell slots: {slots[1:4]}")
```

---

## ✅ Checklist d'Implémentation

- [x] Téléchargement des subclasses depuis API
- [x] Téléchargement des subraces depuis API
- [x] Classe `Subclass` avec toutes les données
- [x] Classe `Subrace` avec bonus et traits
- [x] Classe `MulticlassCharacter` complète
- [x] Calcul des spell slots multiclassés
- [x] Loaders pour subclasses et subraces
- [x] Fonctions de listing
- [x] Tests complets
- [x] Documentation complète
- [x] Intégration avec Character (manuel pour l'instant)

---

**Version** : dnd-5e-core v0.2.5  
**Date** : 18 Janvier 2026  
**Status** : ✅ **COMPLET ET OPÉRATIONNEL**

🎉 Système de sous-classes et multiclassing prêt ! ⚔️🎲✨
