# Système de Conditions - Documentation

## Vue d'ensemble

Le package `dnd-5e-core` implémente maintenant un système complet de parsing et d'application des conditions pour :
- **Monstres** : Les conditions sont automatiquement extraites des descriptions d'actions
- **Objets magiques** : Les objets peuvent appliquer des conditions aux cibles
- **Personnages** : Les conditions affectent les capacités en combat

## Architecture

### 1. Parsing Automatique des Conditions

#### ConditionParser

La classe `ConditionParser` analyse les descriptions textuelles pour extraire les conditions D&D 5e standard.

```python
from dnd_5e_core.combat import ConditionParser

# Parse depuis une description
desc = "Target must make a DC 15 Constitution saving throw or be paralyzed for 1 minute."
conditions = ConditionParser.parse_condition_from_description(desc)

# Résultat: [Condition(name="Paralyzed", dc_type=AbilityType.CON, dc_value=15)]
```

**Conditions reconnues** :
- Restrained (Entravé)
- Grappled (Agrippé)
- Poisoned (Empoisonné)
- Paralyzed (Paralysé)
- Stunned (Étourdi)
- Frightened (Effrayé)
- Prone (À terre)
- Blinded (Aveuglé)
- Charmed (Charmé)

**Patterns reconnus** :
- `"DC XX <ability> saving throw"` → Extrait DC et type de sauvegarde
- `"<ability> save DC XX"` → Format alternatif
- Mots-clés de condition dans le texte → Identifie les conditions

### 2. Application aux Monstres

Les actions de monstres sont automatiquement parsées lors du chargement depuis JSON.

```python
from dnd_5e_core.data import load_monster

# Charger un monstre
spider = load_monster('giant-spider')

# Les actions incluent maintenant les conditions
for action in spider.actions:
    if action.effects:  # Liste de Condition objects
        print(f"{action.name} applique:")
        for condition in action.effects:
            print(f"  - {condition.name} (DC {condition.dc_value} {condition.dc_type.value})")

# En combat
fighter = create_character(...)
messages, damage = spider.attack(fighter, verbose=True)

# Les conditions sont automatiquement appliquées
if fighter.conditions:
    for c in fighter.conditions:
        print(f"Fighter est {c.name}")
```

**Flux de traitement** :
1. `load_monster()` lit le JSON
2. `ConditionParser.extract_conditions_from_action()` parse les descriptions
3. Les `Condition` sont ajoutées à `Action.effects`
4. `Monster.attack()` applique les conditions automatiquement

### 3. Objets Magiques avec Conditions

#### Créer un objet magique

```python
from dnd_5e_core.equipment import create_magic_item_with_conditions, MagicItemRarity, MagicItemType

# Création manuelle
wand = create_magic_item_with_conditions(
    name="Wand of Confusion",
    description="This wand confuses enemies",
    rarity=MagicItemRarity.RARE,
    item_type=MagicItemType.WAND,
    action_name="Confuse",
    action_description="Target must make a DC 14 Wisdom saving throw or be stunned for 1 minute.",
    save_dc=14,
    save_ability="wis",
    uses_per_day=3,
    recharge="dawn",
    requires_attunement=True
)

# Les conditions sont parsées automatiquement depuis action_description
```

#### Objets prédéfinis

```python
from dnd_5e_core.equipment import (
    create_wand_of_paralysis,      # Paralyse (DC 15 CON)
    create_staff_of_entanglement,  # Entrave (DC 13 STR)
    create_ring_of_blinding,       # Aveugle (DC 14 CON)
    create_cloak_of_fear,          # Effraie (DC 15 WIS)
    create_poisoned_dagger         # Empoisonne (DC 13 CON)
)

wand = create_wand_of_paralysis()
print(f"Charges: {wand.actions[0].uses_per_day}")
```

#### Utiliser en combat

```python
# Équiper et harmoniser
wand = create_wand_of_paralysis()
wizard.inventory.append(wand)
wand.equipped = True
wand.attune(wizard)

# Utiliser l'action
action = wand.actions[0]  # "Paralyze"

if action.can_use():
    messages, damage, healing = wand.perform_action(
        action=action,
        target=goblin,
        user=wizard,
        verbose=True
    )
    
    # Vérifier les conditions appliquées
    if goblin.conditions:
        for c in goblin.conditions:
            print(f"Goblin is {c.name}")
```

### 4. Gestion des Conditions

#### Application

```python
from dnd_5e_core.combat import create_paralyzed_condition

# Créer une condition
paralyzed = create_paralyzed_condition(dc_type=AbilityType.CON, dc_value=15)

# Appliquer à un personnage
paralyzed.apply_to_character(fighter)

# Appliquer à un monstre
paralyzed.apply_to_monster(goblin)
```

#### Jets de sauvegarde

```python
# Tenter de résister/échapper
if paralyzed.attempt_save(fighter):
    print("Fighter échappe à la paralysie!")
    # La condition est automatiquement retirée
else:
    print("Fighter reste paralysé")
```

#### Retrait manuel

```python
# Retirer une condition
paralyzed.remove_from_character(fighter)
paralyzed.remove_from_monster(goblin)
```

## Exemples Complets

### Exemple 1 : Combat avec Araignée Géante

```python
from dnd_5e_core.data import load_monster
from dnd_5e_core.data.loaders import simple_character_generator

# Créer personnage et monstre
fighter = simple_character_generator(level=5, class_name='fighter', name='Conan')
spider = load_monster('giant-spider')

# Combat
print(f"🕷️ {spider.name} attaque!")

# L'araignée utilise son attaque de toile
web_action = [a for a in spider.actions if 'web' in a.name.lower()][0]
messages, damage = spider.attack(fighter, actions=[web_action])

print(messages)
# Output:
# Giant Spider uses Web on Conan!
# Conan is hit for 0 hit points!
# Conan is now Restrained!

# Vérifier les conditions
if fighter.conditions:
    for condition in fighter.conditions:
        print(f"✅ {condition.name} appliqué")
        print(f"   DC {condition.dc_value} {condition.dc_type.value} pour échapper")
        
        # Tenter d'échapper
        if condition.attempt_save(fighter):
            print(f"   Conan s'échappe!")
```

### Exemple 2 : Baguette de Paralysie

```python
from dnd_5e_core.equipment import create_wand_of_paralysis
from dnd_5e_core.data import load_monster

# Créer magicien et gobelin
wizard = simple_character_generator(level=7, class_name='wizard', name='Gandalf')
goblin = load_monster('goblin')

# Créer et équiper la baguette
wand = create_wand_of_paralysis()
wizard.inventory.append(wand)
wand.equipped = True
wand.attuned = True

# Utiliser la baguette
action = wand.actions[0]
print(f"⚡ {wizard.name} utilise {wand.name}!")
print(f"   Charges restantes: {action.remaining_uses}/{action.uses_per_day}")

messages, dmg, heal = wand.perform_action(action, goblin, wizard, verbose=True)

# Le gobelin est paralysé
if goblin.conditions:
    print(f"🔴 {goblin.name} est paralysé!")
    
# Recharger après repos
wand.recharge_actions(recharge_type="dawn")
print(f"   Charges après repos: {action.remaining_uses}/{action.uses_per_day}")
```

### Exemple 3 : Parser des Descriptions Personnalisées

```python
from dnd_5e_core.combat import ConditionParser

# Description d'une capacité personnalisée
custom_desc = """
The creature must make a DC 16 Strength saving throw or be grappled.
Additionally, it must make a DC 14 Constitution saving throw or be poisoned
for 1 hour. A grappled creature can use its action to escape with a DC 16
Strength check.
"""

# Parser les conditions
conditions = ConditionParser.parse_condition_from_description(custom_desc)

for condition in conditions:
    print(f"Condition: {condition.name}")
    print(f"  DC: {condition.dc_value} {condition.dc_type.value}")
    print(f"  Description: {condition.desc}")
```

## Intégration dans le Loader

Le système est intégré automatiquement lors du chargement des monstres :

```python
# Dans dnd_5e_core/data/loader.py
from ..combat.condition_parser import ConditionParser

def _create_monster_from_data(index: str, data: dict):
    # ... code existant ...
    
    for action in data['actions']:
        # Parse conditions automatiquement
        conditions = ConditionParser.extract_conditions_from_action(action)
        
        # Ajoute aux effets de l'action
        action_obj = Action(
            name=action['name'],
            effects=conditions,  # ← Conditions parsées automatiquement
            # ... autres champs ...
        )
```

## Cas d'Usage Avancés

### Conditions Multiples

```python
# Un monstre peut appliquer plusieurs conditions
desc = "Target is grappled and poisoned. DC 13 STR to escape grapple, DC 12 CON or remain poisoned."
conditions = ConditionParser.parse_condition_from_description(desc)

# Résultat: [Grappled(DC 13 STR), Poisoned(DC 12 CON)]
```

### Conditions Liées au Lanceur

```python
# Pour frightened, grappled, charmed, restrained
frightened = create_frightened_condition(
    creature=dragon,  # Source de la peur
    dc_type=AbilityType.WIS,
    dc_value=18
)

# La condition référence le dragon
frightened.apply_to_character(fighter)
# fighter.conditions[0].creature == dragon
```

### Gestion des Durées

```python
# Les conditions peuvent avoir des durées
from dnd_5e_core.combat import Condition, ConditionType, AbilityType

poisoned = Condition(
    index="poisoned",
    name="Poisoned",
    desc="Disadvantage on attack rolls and ability checks",
    type=ConditionType.DEBUFF,
    dc_type=AbilityType.CON,
    dc_value=14,
    duration_rounds=10  # Dure 10 rounds
)

# Dans votre système de combat
for condition in character.conditions:
    if hasattr(condition, 'duration_rounds') and condition.duration_rounds:
        condition.duration_rounds -= 1
        if condition.duration_rounds <= 0:
            condition.remove_from_character(character)
```

## Tests

Exécuter la suite de tests complète :

```bash
python tests/test_conditions_system.py
```

Tests inclus :
1. ✅ Parsing automatique des monstres
2. ✅ Objets magiques avec conditions
3. ✅ Combat avec application de conditions
4. ✅ Utilisation d'objets magiques en combat
5. ✅ Parser de conditions direct

## Notes de Performance

- Le parsing des conditions est effectué **une seule fois** au chargement des données
- Les conditions sont des objets légers (dataclass)
- L'application de conditions utilise des références, pas de copies profondes
- Les jets de sauvegarde sont O(1)

## Compatibilité

✅ Compatible avec :
- Tous les monstres de l'API D&D 5e
- Système de combat existant
- Objets magiques personnalisés
- Scénarios DnD5e-Scenarios

## Prochaines Améliorations

- [ ] Support des conditions temporaires avec durée automatique
- [ ] Effets de conditions multiples (avantage/désavantage)
- [ ] Immunités aux conditions par race/classe
- [ ] Conditions environnementales (terrain difficile, obscurité)
- [ ] Parser les conditions depuis les sorts

## API Reference

Voir la documentation inline dans :
- `dnd_5e_core/combat/condition_parser.py`
- `dnd_5e_core/equipment/magic_item.py`
- `dnd_5e_core/equipment/magic_item_factory.py`
