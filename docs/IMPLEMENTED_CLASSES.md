# Classes Implémentées dans dnd-5e-core

Ce document liste toutes les classes et fonctions implémentées dans le package `dnd-5e-core` qui ont été migrées depuis `dao_classes.py`.

## Résumé de la Migration

Toutes les classes métier de `dao_classes.py` ont été migrées vers `dnd-5e-core` en séparant la logique métier de la présentation (UI).

### Classes Principales Déjà Migrées

#### Entités (entities/)
- ✅ `Sprite` - Classe de base pour les entités avec position
- ✅ `Monster` - Classe représentant les monstres
- ✅ `Character` - Classe représentant les personnages joueurs

#### Équipement (equipment/)
- ✅ `Cost` - Coût d'un objet
- ✅ `Equipment` - Classe de base pour l'équipement
- ✅ `EquipmentCategory` - Catégorie d'équipement
- ✅ `Weapon` / `WeaponData` - Armes
- ✅ `Armor` / `ArmorData` - Armures
- ✅ `Potion` - Classe de base pour les potions
- ✅ `HealingPotion` - Potion de soin
- ✅ `SpeedPotion` - Potion de vitesse
- ✅ `StrengthPotion` - Potion de force
- ✅ `PotionRarity` - Rareté des potions
- ✅ `Inventory` - **NOUVELLEMENT IMPLÉMENTÉ**

#### Races (races/)
- ✅ `Language` - Langues
- ✅ `Trait` - Traits raciaux
- ✅ `SubRace` - Sous-races
- ✅ `Race` - Races

#### Classes (classes/)
- ✅ `ProfType` - Types de maîtrise
- ✅ `Proficiency` - Maîtrises
- ✅ `ClassType` - Classes de personnages
- ✅ `Feature` - Capacités de classe
- ✅ `Level` - Niveau de classe
- ✅ `BackGround` - Historiques
- ✅ **Multiclassing** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `MulticlassRequirements`
  - `MULTICLASS_PREREQUISITES`
  - `can_multiclass_into()`
  - `can_multiclass_from()`
  - `calculate_spell_slots_multiclass()`
  - `get_multiclass_proficiencies()`
  - `calculate_hit_points_multiclass()`

#### Capacités (abilities/)
- ✅ `AbilityType` - Types de caractéristiques
- ✅ `Abilities` - Les 6 caractéristiques
- ✅ **Skills** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `SkillType` - Types de compétences
  - `Skill` - Compétences
  - `get_all_skills()`
- ✅ **Saving Throws** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `SavingThrowType` - Types de jets de sauvegarde
  - `SavingThrow` - Jets de sauvegarde
  - `make_saving_throw()`

#### Sorts (spells/)
- ✅ `Spell` - Sorts
- ✅ `SpellCaster` - Lanceur de sorts
- ✅ `AreaOfEffect` - Zone d'effet
- ✅ **Spell Slots** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `SpellSlots` - Gestion des emplacements de sorts
  - `get_spell_slots_by_level()`
- ✅ **Cantrips** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `is_cantrip()`
  - `get_cantrip_damage_scaling()`
  - `get_cantrip_damage()`
  - `filter_cantrips()`
  - `get_cantrips_known_by_level()`
  - `DAMAGE_CANTRIPS`
  - `UTILITY_CANTRIPS`

#### Combat (combat/)
- ✅ `Damage` - Dégâts
- ✅ `DamageType` - Types de dégâts
- ✅ `Condition` - Conditions/états
- ✅ `ActionType` - Types d'actions
- ✅ `Action` - Actions
- ✅ `SpecialAbility` - Capacités spéciales
- ✅ `RangeType` - Types de portée
- ✅ `CategoryType` - Types de catégories

#### Mécanique de Jeu (mechanics/)
- ✅ `DamageDice` - Dés de dégâts
- ✅ **Experience System** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `XP_LEVELS` - Seuils d'XP par niveau
  - `get_level_from_xp()`
  - `get_xp_for_level()`
  - `get_xp_to_next_level()`
  - `should_level_up()`
  - `calculate_proficiency_bonus()`
  - `get_cr_xp()`
- ✅ **Level Up System** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `LevelUpResult` - Résultat de montée de niveau
  - `calculate_hp_gain()`
  - `can_level_up()`
  - `get_ability_score_improvement_levels()`
  - `is_ability_score_improvement_level()`
  - `perform_level_up()`
- ✅ **Challenge Rating** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `ChallengeRating` - Facteur de puissance
  - `EncounterDifficulty` - Difficulté de rencontre
  - `get_xp_thresholds_for_level()`
  - `calculate_encounter_difficulty()`
  - `get_appropriate_cr_range()`

#### Utilitaires (utils/)
- ✅ `token_downloader` - Téléchargement de tokens
- ✅ **Helpers** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `roll_dice()`
  - `roll_with_advantage()`
  - `roll_with_disadvantage()`
  - `calculate_modifier()`
  - `calculate_ac()`
  - `calculate_attack_bonus()`
  - `calculate_save_dc()`
  - `is_critical_hit()`
  - `is_critical_fail()`
  - `apply_resistance()`
  - `apply_vulnerability()`
  - `calculate_spell_attack_bonus()`
  - `get_random_ability_scores()`
  - `get_standard_array()`
  - `calculate_carrying_capacity()`
  - `calculate_jump_distance()`
  - `format_modifier()`
  - `format_dice()`
- ✅ **Constants** - **NOUVELLEMENT IMPLÉMENTÉ**
  - Constantes de jeu pour D&D 5e
  - Valeurs par défaut
  - Tables de référence

#### Données (data/)
- ✅ `loader` - Chargement des données
- ✅ `collections` - Collections de données
- ✅ **API Client** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `DndApiClient` - Client pour accéder à l'API D&D 5e
  - `get_default_client()`
  - `set_default_client()`
- ✅ **Serialization** - **NOUVELLEMENT IMPLÉMENTÉ**
  - `DndJSONEncoder` - Encodeur JSON personnalisé
  - `to_json()`
  - `from_json()`
  - `save_to_file()`
  - `load_from_file()`
  - `serialize_character()`
  - `deserialize_character()`
  - `save_character()`
  - `load_character()`
  - `save_party()`
  - `load_party()`
  - `create_backup()`

## Classes UI Séparées

Les classes suivantes ont été retirées du package métier et doivent être gérées par les frontends (pygame, ncurses, etc.):

- `color` - Couleurs de terminal → dans `dnd_5e_core.ui`
- Méthodes `draw()` et `draw_effect()` de `Sprite` → à gérer dans `game_entity.py` du frontend

## Utilisation

### Import des nouvelles classes

```python
# Experience et Level Up
from dnd_5e_core.mechanics import (
    get_level_from_xp,
    should_level_up,
    perform_level_up,
    calculate_proficiency_bonus
)

# Skills et Saving Throws
from dnd_5e_core.abilities import (
    Skill,
    SkillType,
    SavingThrow,
    make_saving_throw
)

# Spell Slots
from dnd_5e_core.spells import (
    SpellSlots,
    get_spell_slots_by_level
)

# Cantrips
from dnd_5e_core.spells import (
    is_cantrip,
    get_cantrip_damage_scaling
)

# Multiclassing
from dnd_5e_core.classes import (
    can_multiclass_into,
    calculate_spell_slots_multiclass
)

# Challenge Rating
from dnd_5e_core.mechanics import (
    ChallengeRating,
    calculate_encounter_difficulty
)

# Helpers
from dnd_5e_core.utils import (
    roll_with_advantage,
    calculate_modifier,
    calculate_ac
)

# Constants
from dnd_5e_core.utils import constants

# Serialization
from dnd_5e_core.data.serialization import (
    save_character,
    load_character,
    save_party
)

# API Client
from dnd_5e_core.data.api_client import (
    DndApiClient,
    get_default_client
)
```

### Exemples d'utilisation

```python
# Vérifier si un personnage peut monter de niveau
from dnd_5e_core.mechanics import should_level_up, perform_level_up

if should_level_up(character.xp, character.level):
    result = perform_level_up(character, available_spells)
    for msg in result.messages:
        print(msg)
    
    character.level = result.new_level
    character.max_hit_points = result.new_max_hp

# Faire un jet de sauvegarde
from dnd_5e_core.abilities import make_saving_throw

total, success = make_saving_throw(
    dc=15,
    ability_type="dex",
    abilities=character.abilities,
    proficiency_bonus=character.proficiency_bonus,
    proficiencies=character.saving_throw_proficiencies,
    advantage=True
)

# Calculer les slots de sorts pour multiclassage
from dnd_5e_core.classes import calculate_spell_slots_multiclass

class_levels = {"wizard": 3, "cleric": 2}
spell_slots = calculate_spell_slots_multiclass(class_levels)

# Utiliser l'API client
from dnd_5e_core.data.api_client import get_default_client

client = get_default_client()
monster_data = client.get_monster("adult-black-dragon")
```

## Notes de Migration

1. **Séparation UI/Métier** : Toutes les fonctions d'affichage (cprint, draw, etc.) ont été retirées des classes métier.

2. **Format des Messages** : Les méthodes retournent maintenant des tuples `(messages: List[str], result)` permettant aux frontends de gérer l'affichage.

3. **GameEntity** : Pour les jeux pygame, utilisez `GameEntity` de `game_entity.py` qui encapsule les classes métier et ajoute les fonctionnalités de positionnement/affichage.

4. **Imports** : Vérifiez que tous les imports utilisent le package `dnd_5e_core` au lieu de `dao_classes`.

## Prochaines Étapes

- ✅ Toutes les classes vides ont été implémentées
- ✅ Les exports des modules ont été mis à jour
- ✅ Documentation créée
- 🔄 Tests à ajouter pour les nouvelles fonctionnalités
- 🔄 Intégration complète dans les frontends (main.py, main_ncurses.py, wizardry.py)

## Date de Migration

Migration complétée le : 5 janvier 2026
Version du package : 0.1.2

