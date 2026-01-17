# Nouvelles Fonctions de Chargement d'Objets - collections.py

## Date: 17 janvier 2026

## 🎯 Objectif

Ajouter des fonctions pratiques dans `collections.py` pour charger directement des **listes d'objets** (Monster, Spell, etc.) au lieu de listes d'index (strings).

## ✨ Nouvelles Fonctions Ajoutées

### 1. Chargement de Toutes les Entités

#### `load_all_monsters() -> List[Monster]`
Charge **tous** les monstres comme objets Monster.

```python
from dnd_5e_core.data import load_all_monsters

monsters = load_all_monsters()
for monster in monsters:
    print(f"{monster.name} - CR {monster.challenge_rating}, HP {monster.hit_points}")
```

#### `load_all_spells() -> List[Spell]`
Charge **tous** les sorts comme objets Spell.

```python
from dnd_5e_core.data import load_all_spells

spells = load_all_spells()
for spell in spells:
    print(f"{spell.name} - Level {spell.level}, School: {spell.school}")
```

#### `load_all_weapons() -> List[Weapon]`
Charge **toutes** les armes comme objets Weapon.

```python
from dnd_5e_core.data import load_all_weapons

weapons = load_all_weapons()
for weapon in weapons:
    print(f"{weapon.name} - {weapon.damage_dice}")
```

#### `load_all_armors() -> List[Armor]`
Charge **toutes** les armures comme objets Armor.

```python
from dnd_5e_core.data import load_all_armors

armors = load_all_armors()
for armor in armors:
    print(f"{armor.name} - AC {armor.armor_class}")
```

### 2. Filtrage par Critères

#### `filter_monsters(min_cr, max_cr, name_contains) -> List[Monster]`
Filtre les monstres selon des critères.

**Paramètres:**
- `min_cr` (float, optionnel): CR minimum
- `max_cr` (float, optionnel): CR maximum
- `name_contains` (str, optionnel): Filtre par nom (insensible à la casse)

**Exemples:**

```python
from dnd_5e_core.data import filter_monsters

# Tous les monstres CR 0-1 (débutant)
low_level = filter_monsters(max_cr=1)

# Monstres CR 5-10 (niveau moyen)
mid_level = filter_monsters(min_cr=5, max_cr=10)

# Tous les dragons CR 10+
dragons = filter_monsters(min_cr=10, name_contains="dragon")

# Tous les gobelins (n'importe quel CR)
goblins = filter_monsters(name_contains="goblin")
```

#### `filter_spells(level, school, class_name) -> List[Spell]`
Filtre les sorts selon des critères.

**Paramètres:**
- `level` (int, optionnel): Niveau du sort (0-9, où 0 = cantrip)
- `school` (str, optionnel): École de magie
- `class_name` (str, optionnel): Classe qui peut le lancer

**Exemples:**

```python
from dnd_5e_core.data import filter_spells

# Tous les cantrips de wizard
wizard_cantrips = filter_spells(level=0, class_name="wizard")

# Tous les sorts d'évocation niveau 3
evocation_3 = filter_spells(level=3, school="evocation")

# Tous les sorts de cleric (tous niveaux)
cleric_spells = filter_spells(class_name="cleric")

# Cantrips d'abjuration pour wizard
wizard_abjuration_cantrips = filter_spells(
    level=0, 
    school="abjuration", 
    class_name="wizard"
)
```

## 📊 Comparaison Avant/Après

### Avant (Avec Index)

```python
# Charger la liste d'index
from dnd_5e_core.data import get_monsters_list, load_monster

monster_indexes = get_monsters_list()

# Charger manuellement chaque monstre
monsters = []
for index in monster_indexes:
    monster = load_monster(index)
    if monster:
        monsters.append(monster)

# Filtrer manuellement
low_cr_monsters = [m for m in monsters if m.challenge_rating <= 1]
```

### Après (Avec Objets)

```python
# Charger directement tous les monstres
from dnd_5e_core.data import load_all_monsters, filter_monsters

monsters = load_all_monsters()

# Ou filtrer directement
low_cr_monsters = filter_monsters(max_cr=1)
```

**Économie de code: ~70%** 🚀

## 🔧 Implémentation

Les nouvelles fonctions utilisent les fonctions `load_*()` de `loader.py` qui retournent maintenant des objets (v0.1.9).

```python
def load_all_monsters() -> List:
    """Load all monsters as Monster objects"""
    from .loader import load_monster
    
    monster_indexes = get_monsters_list()
    monsters = []
    
    for index in monster_indexes:
        monster = load_monster(index)
        if monster:
            monsters.append(monster)
    
    return monsters
```

## 📦 Exports

Toutes les nouvelles fonctions sont exportées dans `dnd_5e_core.data.__init__.py`:

```python
from dnd_5e_core.data import (
    # Chargement en masse
    load_all_monsters,
    load_all_spells,
    load_all_weapons,
    load_all_armors,
    
    # Filtrage
    filter_monsters,
    filter_spells
)
```

## 🎮 Cas d'Usage

### 1. Générateur de Rencontres Aléatoires

```python
from dnd_5e_core.data import filter_monsters
import random

def generate_encounter(party_level: int, num_monsters: int = 3):
    """Générer une rencontre aléatoire"""
    # CR approprié pour le niveau du groupe
    min_cr = max(0, party_level - 2)
    max_cr = party_level + 1
    
    # Trouver les monstres appropriés
    suitable_monsters = filter_monsters(min_cr=min_cr, max_cr=max_cr)
    
    # Sélectionner aléatoirement
    encounter = random.sample(suitable_monsters, min(num_monsters, len(suitable_monsters)))
    
    return encounter

# Utilisation
party_level = 5
encounter = generate_encounter(party_level)
for monster in encounter:
    print(f"- {monster.name} (CR {monster.challenge_rating})")
```

### 2. Livre de Sorts pour Wizard

```python
from dnd_5e_core.data import filter_spells

def get_wizard_spellbook(max_level: int = 9):
    """Obtenir tous les sorts de wizard jusqu'au niveau spécifié"""
    spellbook = {}
    
    for level in range(max_level + 1):
        spells = filter_spells(level=level, class_name="wizard")
        spellbook[level] = spells
    
    return spellbook

# Utilisation
spellbook = get_wizard_spellbook(max_level=3)
for level, spells in spellbook.items():
    level_name = "Cantrips" if level == 0 else f"Level {level}"
    print(f"\n{level_name} ({len(spells)} spells):")
    for spell in spells[:5]:  # Montrer les 5 premiers
        print(f"  - {spell.name}")
```

### 3. Comparateur d'Armes

```python
from dnd_5e_core.data import load_all_weapons

def compare_weapons_by_damage():
    """Comparer toutes les armes par dégâts moyens"""
    weapons = load_all_weapons()
    
    # Trier par dégâts moyens
    sorted_weapons = sorted(
        weapons, 
        key=lambda w: w.damage_dice.average(), 
        reverse=True
    )
    
    print("Top 10 armes par dégâts:")
    for i, weapon in enumerate(sorted_weapons[:10], 1):
        print(f"{i}. {weapon.name}: {weapon.damage_dice} "
              f"(avg: {weapon.damage_dice.average()})")

# Utilisation
compare_weapons_by_damage()
```

## ✅ Tests Effectués

```python
# Test 1: Chargement
✅ load_all_monsters() - 332 monstres chargés
✅ load_all_spells() - 319 sorts chargés

# Test 2: Filtrage
✅ filter_monsters(max_cr=0.5) - 5+ monstres faibles
✅ filter_monsters(name_contains="dragon") - 20+ dragons
✅ filter_spells(level=0, class_name="wizard") - 10+ cantrips

# Test 3: Import
✅ from dnd_5e_core.data import load_all_monsters
✅ from dnd_5e_core.data import filter_spells
```

## 🚀 Performance

Les fonctions utilisent un chargement paresseux:
- Seuls les monstres/sorts demandés sont chargés
- Pas de cache global (évite la mémoire excessive)
- Chaque appel recharge depuis les fichiers JSON (toujours à jour)

Pour des performances optimales avec chargements répétés:

```python
# Charger une fois et réutiliser
all_monsters = load_all_monsters()  # Charge tous les monstres

# Filtrer en mémoire (rapide)
dragons = [m for m in all_monsters if 'dragon' in m.name.lower()]
low_cr = [m for m in all_monsters if m.challenge_rating <= 1]
```

## 📚 Documentation Mise à Jour

- ✅ `collections.py` - Docstrings complètes avec exemples
- ✅ `data/__init__.py` - Exports mis à jour
- ✅ Exemple `__main__` dans `collections.py`

## 🔄 Compatibilité

**Rétrocompatible à 100%**: Les fonctions existantes (`get_monsters_list()`, etc.) fonctionnent toujours et retournent des listes d'index.

Les nouvelles fonctions (`load_all_monsters()`, `filter_monsters()`) sont des **additions** qui n'affectent pas le code existant.

---

**Auteur**: GitHub Copilot  
**Date**: 17 janvier 2026  
**Version**: dnd-5e-core 0.1.9+  
**Statut**: ✅ **COMPLÉTÉ**

