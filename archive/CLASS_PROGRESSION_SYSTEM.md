# 📚 Système de Progression des Classes D&D 5e

## 🎯 Vue d'Ensemble

Ce système implémente la progression complète des classes D&D 5e, incluant :
- Progression par niveau (1-20)
- Spell slots pour les lanceurs de sorts
- Features de classe par niveau
- Bonus spécifiques aux classes
- Traits de races
- Amélioration de caractéristiques

## 📥 Données Téléchargées depuis l'API

### Source
API D&D 5e officielle : https://www.dnd5eapi.co

### Endpoints utilisés

#### 1. Class Levels
```
GET /api/classes/{index}/levels
```
**Exemple** : `/api/classes/wizard/levels`

**Données récupérées** :
- Bonus de maîtrise par niveau
- Features obtenues à chaque niveau
- Spell slots pour les lanceurs de sorts
- Données spécifiques aux classes (rage, ki points, etc.)

#### 2. Features
```
GET /api/features/{index}
```
**Exemples** :
- `/api/features/spellcasting-wizard`
- `/api/features/rage`
- `/api/features/extra-attack`

#### 3. Traits
```
GET /api/traits/{index}
```
**Exemples** :
- `/api/traits/darkvision`
- `/api/traits/fey-ancestry`
- `/api/traits/dwarven-resilience`

## 🏗️ Architecture

### 1. Classes Principales

#### `ClassLevelProgression`
Représente la progression à un niveau spécifique.

```python
@dataclass
class ClassLevelProgression:
    level: int
    class_index: str
    ability_score_bonuses: int
    prof_bonus: int
    features: List[ClassFeature]
    spellcasting: Optional[SpellcastingInfo]
    class_specific: Dict[str, Any]
```

**Exemple pour Wizard niveau 1** :
```python
{
    "level": 1,
    "prof_bonus": 2,
    "features": ["Spellcasting", "Arcane Recovery"],
    "spellcasting": {
        "cantrips_known": 3,
        "spell_slots_level_1": 2
    }
}
```

#### `SpellcastingInfo`
Informations sur les sorts à un niveau donné.

```python
@dataclass
class SpellcastingInfo:
    level: int
    cantrips_known: int
    spells_known: int
    spell_slots_level_1: int
    spell_slots_level_2: int
    # ... jusqu'au niveau 9
```

**Propriété `spell_slots`** :
```python
>>> wizard_lvl5 = progression.get_spellcasting(5)
>>> wizard_lvl5.spell_slots
[0, 4, 3, 2, 0, 0, 0, 0, 0, 0]
#    L1 L2 L3 L4 L5 L6 L7 L8 L9
```

#### `ClassProgression`
Progression complète sur 20 niveaux.

```python
@dataclass
class ClassProgression:
    class_index: str
    class_name: str
    hit_die: int
    levels: Dict[int, ClassLevelProgression]
    saving_throws: List[str]
    skills: List[str]
```

### 2. Fichiers de Données

#### Structure des Répertoires
```
dnd_5e_core/data/
├── class_levels/
│   ├── barbarian_levels.json
│   ├── bard_levels.json
│   ├── cleric_levels.json
│   ├── druid_levels.json
│   ├── fighter_levels.json
│   ├── monk_levels.json
│   ├── paladin_levels.json
│   ├── ranger_levels.json
│   ├── rogue_levels.json
│   ├── sorcerer_levels.json
│   ├── warlock_levels.json
│   └── wizard_levels.json
├── features/
│   ├── spellcasting-wizard.json
│   ├── rage.json
│   ├── extra-attack.json
│   └── ...
└── traits/
    ├── darkvision.json
    ├── fey-ancestry.json
    └── ...
```

## 🔧 Utilisation

### 1. Charger la Progression d'une Classe

```python
from dnd_5e_core.data.progression_loader import load_class_progression

wizard_progression = load_class_progression('wizard')

# Obtenir les infos pour un niveau
level_5_data = wizard_progression.get_level(5)
print(f"Prof bonus: +{level_5_data.prof_bonus}")
print(f"Features: {[f.name for f in level_5_data.features]}")
```

### 2. Récupérer les Spell Slots

```python
from dnd_5e_core.data.progression_loader import get_spell_slots_for_level

# Pour un Wizard niveau 5
spell_slots = get_spell_slots_for_level('wizard', 5)
# Retourne: [0, 4, 3, 2, 0, 0, 0, 0, 0, 0]
#            ^  ^  ^  ^
#            |  |  |  Level 3: 2 slots
#            |  |  Level 2: 3 slots
#            |  Level 1: 4 slots
#            Niveau 0 (non utilisé)
```

### 3. Appliquer un Level Up

```python
from dnd_5e_core.data.progression_loader import apply_level_up_benefits

# Quand un personnage monte de niveau
character.level = 5
apply_level_up_benefits(character, 5)

# Affichera:
#    ❤️  HP: +6 (38 total)
#    🔮 Spell slots mis à jour
#    ✨ Nouvelles features:
#       - Extra Attack
```

### 4. Bonus Spécifiques aux Classes

#### Barbarian
```python
from dnd_5e_core.data.progression_loader import get_class_specific_value

# Rage count au niveau 3
rage_count = get_class_specific_value('barbarian', 3, 'rage_count')
# Retourne: 3

# Rage damage bonus
rage_damage = get_class_specific_value('barbarian', 3, 'rage_damage_bonus')
# Retourne: 2
```

#### Monk
```python
# Ki points au niveau 5
ki_points = get_class_specific_value('monk', 5, 'ki_points')
# Retourne: 5

# Martial arts dice
martial_arts = get_class_specific_value('monk', 5, 'martial_arts', {'dice_count': 1, 'dice_value': 6})
# Retourne: {'dice_count': 1, 'dice_value': 6} (1d6)
```

#### Rogue
```python
# Sneak attack dice au niveau 5
sneak_attack = get_class_specific_value('rogue', 5, 'sneak_attack', {'dice_count': 3, 'dice_value': 6})
# Retourne: {'dice_count': 3, 'dice_value': 6} (3d6)
```

## 📊 Exemples de Données

### Wizard Niveau 1-3

```json
[
  {
    "level": 1,
    "prof_bonus": 2,
    "features": [
      {
        "index": "spellcasting-wizard",
        "name": "Spellcasting"
      },
      {
        "index": "arcane-recovery",
        "name": "Arcane Recovery"
      }
    ],
    "spellcasting": {
      "cantrips_known": 3,
      "spell_slots_level_1": 2
    }
  },
  {
    "level": 2,
    "prof_bonus": 2,
    "features": [
      {
        "index": "arcane-tradition",
        "name": "Arcane Tradition"
      }
    ],
    "spellcasting": {
      "cantrips_known": 3,
      "spell_slots_level_1": 3
    }
  },
  {
    "level": 3,
    "prof_bonus": 2,
    "features": [],
    "spellcasting": {
      "cantrips_known": 3,
      "spell_slots_level_1": 4,
      "spell_slots_level_2": 2
    }
  }
]
```

### Barbarian class_specific

```json
{
  "class_specific": {
    "rage_count": 3,
    "rage_damage_bonus": 2,
    "brutal_critical_dice": 0
  }
}
```

### Fighter class_specific

```json
{
  "class_specific": {
    "action_surge_count": 1,
    "indomitable_uses": 0,
    "extra_attacks": 1
  }
}
```

## 🎮 Intégration avec Character

### Extension de la Classe Character

Les données de progression sont automatiquement utilisées dans :

#### 1. Création de Personnage
```python
from dnd_5e_core.data.loaders import simple_character_generator

wizard = simple_character_generator(5, 'elf', 'wizard', 'Gandalf')
# Les spell slots sont automatiquement configurés pour le niveau 5
```

#### 2. Level Up
```python
wizard.level = 6
apply_level_up_benefits(wizard, 6)
# Applique tous les bénéfices du niveau 6
```

#### 3. Spell Casting
```python
# Les spell slots sont récupérés de la progression
if hasattr(wizard, 'sc') and wizard.sc:
    wizard.sc.spell_slots = get_spell_slots_for_level('wizard', wizard.level)
```

## 🔍 Vérification des Implémentations Existantes

### Traits et Features déjà implémentés

✅ **Race Traits** (déjà dans Character)
- Darkvision
- Ability bonuses
- Proficiencies

✅ **Class Features** (partiellement implémentés)
- Spellcasting (via SpellCaster class)
- Proficiencies (weapons, armor, saves)

⚠️ **À implémenter**
- Specific class features (Rage, Ki, etc.)
- Subclass choices
- Feat selection

### Skills System

✅ **Déjà implémenté**
```python
# Character possède déjà un système de compétences
character.proficiencies  # Liste des proficiencies
character.class_type.index  # Index de la classe
```

## 📝 TODO List

### Court Terme
- [x] Télécharger les données de progression
- [x] Créer les classes de données
- [x] Implémenter le loader
- [ ] Tester avec toutes les classes
- [ ] Intégrer dans simple_character_generator
- [ ] Documenter les exemples

### Moyen Terme
- [ ] Implémenter les subclass
- [ ] Système de choix de features
- [ ] Multiclassing support
- [ ] Feats system

### Long Terme
- [ ] UI pour level up
- [ ] Validation des choix
- [ ] Export/Import de personnages

## 🚀 Scripts Utiles

### 1. Télécharger les Données
```bash
cd /Users/display/PycharmProjects/dnd-5e-core
python download_class_progression.py
```

### 2. Tester le Système
```python
from dnd_5e_core.data.progression_loader import load_class_progression

# Tester pour toutes les classes
classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 
           'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 
           'warlock', 'wizard']

for class_index in classes:
    prog = load_class_progression(class_index)
    if prog:
        print(f"✅ {class_index}: {prog.class_name}")
    else:
        print(f"❌ {class_index}: Failed to load")
```

## 📚 Références

- **API Documentation** : https://5e-bits.github.io/docs/api
- **D&D 5e SRD** : https://dnd.wizards.com/resources/systems-reference-document
- **Class Levels** : https://5e-bits.github.io/docs/api/get-all-level-resources-for-a-class

---

**Version** : 1.0  
**Date** : 18 Janvier 2026  
**Status** : 🚧 En développement  
**Compatibilité** : dnd-5e-core v0.2.4+
