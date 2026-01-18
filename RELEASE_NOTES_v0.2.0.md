# 🎉 dnd-5e-core v0.2.0 - Magic Items & Defensive Spells

## 📅 Date de publication : 18 janvier 2026

## 🌟 Nouveautés majeures

### 1. 🪄 Système de Magic Items complet

Le package inclut désormais un système complet de **magic items** (objets magiques) utilisables en combat :

#### Fonctionnalités
- ✅ **Passive bonuses** : AC, saving throws, ability scores
- ✅ **Active abilities** : Combat actions (attacks, healing, defense)
- ✅ **Attunement system** : Max 3 items attuned per character
- ✅ **Charges/Uses tracking** : Limited uses per day with recharge
- ✅ **Rarity system** : Common, Uncommon, Rare, Very Rare, Legendary, Artifact

#### Classes principales
```python
from dnd_5e_core.equipment import MagicItem, MagicItemAction, MagicItemRarity

# Création d'un magic item
ring = MagicItem(
    index="ring-of-protection",
    name="Ring of Protection",
    rarity=MagicItemRarity.RARE,
    ac_bonus=1,
    saving_throw_bonus=1,
    requires_attunement=True
)
```

#### 8 Magic Items prédéfinis

```python
from dnd_5e_core.equipment import (
    create_ring_of_protection,      # +1 AC, +1 saves
    create_cloak_of_protection,     # +1 AC, +1 saves
    create_wand_of_magic_missiles,  # 7 charges/day
    create_staff_of_healing,        # 10 charges/day
    create_belt_of_giant_strength,  # STR 21
    create_amulet_of_health,        # CON 19
    create_bracers_of_defense,      # +2 AC
    create_necklace_of_fireballs    # 6 beads
)

# Utilisation
ring = create_ring_of_protection()
ring.attune(character)
ring.equipped = True
ring.apply_to_character(character)
```

#### Loader de magic items

```python
from dnd_5e_core.data import load_magic_item

# Charger depuis JSON
ring = load_magic_item("ring-of-protection")
staff = load_magic_item("staff-of-healing")
```

### 2. 🛡️ Sorts de défense et buffs

Les sorts peuvent maintenant fournir des **bonus défensifs** et des **buffs** :

#### Nouvelles propriétés de Spell
```python
@dataclass
class Spell:
    # ... propriétés existantes ...
    
    # 🆕 Nouvelles propriétés
    duration: Optional[str]              # "1 round", "8 hours", etc.
    concentration: bool                  # Requires concentration
    ac_bonus: Optional[int]             # AC bonus
    saving_throw_bonus: Optional[int]   # Saving throw bonus
    ability_bonuses: Optional[Dict]     # Ability score bonuses
    damage_resistance: Optional[List]    # Damage types resisted
    damage_immunity: Optional[List]      # Damage types immune
    conditions_immunity: Optional[List]  # Conditions prevented
```

#### Nouvelles méthodes
```python
# Vérifier le type de sort
shield = load_spell("shield")
print(shield.is_defensive)  # True
print(shield.is_damaging)   # False
print(shield.is_healing)    # False
print(shield.is_buff)       # False

# Propriétés
print(shield.ac_bonus)      # 5
print(shield.duration)      # "1 round"
print(shield.concentration) # False
```

#### Sorts de défense parsés

Les sorts suivants sont automatiquement parsés depuis les JSON :

| Sort | Niveau | AC Bonus | Durée | Concentration |
|------|--------|----------|-------|---------------|
| **Shield** | 1 | +5 | 1 round | Non |
| **Mage Armor** | 1 | +3 | 8 hours | Non |
| **Shield of Faith** | 1 | +2 | 10 minutes | Oui |
| **Protection from Energy** | 3 | - | 1 hour | Oui |

```python
from dnd_5e_core.data import load_spell

# Shield (+5 AC, 1 round)
shield = load_spell("shield")
print(f"{shield.name}: +{shield.ac_bonus} AC for {shield.duration}")

# Mage Armor (AC 13 + DEX)
mage_armor = load_spell("mage-armor")
print(f"{mage_armor.name}: +{mage_armor.ac_bonus} AC for {mage_armor.duration}")

# Shield of Faith (+2 AC, concentration)
shield_of_faith = load_spell("shield-of-faith")
print(f"{shield_of_faith.name}: +{shield_of_faith.ac_bonus} AC")
print(f"Concentration: {shield_of_faith.concentration}")
```

## 📚 Exemples d'utilisation

### Combat avec Magic Items

```python
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.equipment import create_ring_of_protection, create_wand_of_magic_missiles
from dnd_5e_core.combat import CombatSystem

# Créer un wizard
wizard = simple_character_generator(level=5, class_name='wizard', name='Gandalf')

# Équiper Ring of Protection
ring = create_ring_of_protection()
ring.attune(wizard)
ring.equipped = True
ring.apply_to_character(wizard)

print(f"AC: {wizard.armor_class}")  # +1 from ring

# Équiper Wand of Magic Missiles
wand = create_wand_of_magic_missiles()
wand.equipped = True

# Utiliser l'action du wand en combat
magic_missile_action = wand.actions[0]
if wand.can_perform_action(magic_missile_action):
    wand.use_action(magic_missile_action)
    print(f"Used Magic Missile! Remaining charges: {magic_missile_action.remaining_uses}")
```

### Utilisation de sorts de défense

```python
from dnd_5e_core.data import load_spell

# Charger les sorts de défense
shield = load_spell("shield")
mage_armor = load_spell("mage-armor")

# Appliquer en combat (conceptuel)
if under_attack and wizard.can_cast_spell(shield.level):
    # Cast Shield as reaction
    wizard.cast_spell(shield.level)
    temporary_ac_bonus = shield.ac_bonus  # +5
    print(f"Shield cast! AC temporarily increased by {temporary_ac_bonus}")
```

## 🔧 Intégration avec le système de combat

Les magic items et sorts de défense s'intègrent parfaitement avec le `CombatSystem` existant :

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.data import load_monster

combat = CombatSystem(verbose=True)

# Le wizard avec Ring of Protection aura +1 AC automatiquement
# Le système de combat tiendra compte de l'AC modifié
goblin = load_monster('goblin')

combat.character_turn(
    character=wizard,
    alive_chars=[wizard],
    alive_monsters=[goblin],
    party=[wizard]
)
```

## 📖 Documentation

### Modules ajoutés

- `dnd_5e_core.equipment.magic_item` - Système de magic items
- `dnd_5e_core.equipment.predefined_magic_items` - 8 magic items prêts à l'emploi

### Fonctions ajoutées

- `load_magic_item(index)` - Charger un magic item depuis JSON
- `get_magic_item(index)` - Obtenir un magic item prédéfini
- `create_*()` - 8 fonctions pour créer des magic items spécifiques

### Tests

Un script de test complet est disponible :

```bash
python tests/test_magic_items_and_defense.py
```

## 🚀 Migration depuis v0.1.9

Aucun changement breaking ! Toutes les fonctionnalités existantes restent compatibles.

### Nouvelles fonctionnalités disponibles

```python
# Avant v0.2.0
from dnd_5e_core.data import load_spell
shield = load_spell("shield")
# shield.ac_bonus n'existait pas

# v0.2.0+
from dnd_5e_core.data import load_spell
shield = load_spell("shield")
print(shield.ac_bonus)      # 5
print(shield.is_defensive)  # True
print(shield.duration)      # "1 round"
```

## 📦 Installation

```bash
pip install dnd-5e-core==0.2.0
```

ou

```bash
pip install --upgrade dnd-5e-core
```

## 🔗 Liens utiles

- **PyPI** : https://pypi.org/project/dnd-5e-core/0.2.0/
- **GitHub** : https://github.com/codingame-team/dnd-5e-core
- **Documentation** : https://github.com/codingame-team/dnd-5e-core/tree/main/docs
- **CHANGELOG** : https://github.com/codingame-team/dnd-5e-core/blob/main/CHANGELOG.md

## 🎮 Exemples de projets

Voir comment utiliser ces fonctionnalités dans de vrais projets :

- **DnD5e-Scenarios** : https://github.com/codingame-team/DnD5e-Scenarios
- **DnD-5th-Edition-API** : https://github.com/codingame-team/DnD-5th-Edition-API

## 🙏 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

- Ouvrir une issue pour signaler un bug
- Proposer de nouveaux magic items
- Améliorer la documentation
- Ajouter des tests

## 📝 Changelog complet

Voir [CHANGELOG.md](https://github.com/codingame-team/dnd-5e-core/blob/main/CHANGELOG.md) pour tous les détails.

