# Module: combat

## Vue d'ensemble

Le module `combat` fournit un système de combat complet pour D&D 5e, incluant la gestion des actions, des dégâts, des conditions, et de l'initiative.

## Classes principales

### CombatSystem

Système centralisé pour gérer les combats.

**Importation:**
```python
from dnd_5e_core.combat import CombatSystem
```

**Création:**

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Créer le groupe et les monstres
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
]

monsters = [
    load_monster("goblin"),
    load_monster("goblin"),
]

# Initialiser le combat
combat = CombatSystem(verbose=True)

# Ou avec callback pour UI personnalisée
def message_handler(msg):
    print(f"[COMBAT] {msg}")

combat = CombatSystem(verbose=False, message_callback=message_handler)
```

**Méthodes principales:**

#### Tour de joueur
```python
# Attaque au corps à corps
combat.player_turn(
    character=party[0],
    target=monsters[0],
    action_type="melee"
)

# Attaque à distance
combat.player_turn(
    character=party[1],
    target=monsters[0],
    action_type="ranged"
)

# Lancer un sort
combat.player_turn(
    character=party[1],
    target=monsters[0],
    action_type="spell",
    spell=fireball,
    spell_slot_level=3
)

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
combat.player_turn(
    character=party[0],
    action_type="potion",
    potion=potion
)
```

#### Tour de monstre
```python
# Le système gère automatiquement l'IA du monstre
combat.monster_turn(
    monster=monsters[0],
    alive_monsters=monsters,
    alive_chars=party,
    party=party,
    round_num=1
)
```

#### Fonctions utilitaires
```python
# Vérifier si le combat est terminé
if combat.is_combat_over(party, monsters):
    print("Combat terminé!")

# Calculer l'initiative
initiative_order = combat.roll_initiative(party, monsters)

# Distribuer l'XP et l'or
total_xp, gold = combat.distribute_rewards(party, defeated_monsters)
```

---

### Action

Représente une action de combat (attaque, sort, capacité spéciale).

**Importation:**
```python
from dnd_5e_core.combat import Action, ActionType
```

**Types d'actions:**
```python
class ActionType(Enum):
    MELEE = "melee"
    RANGED = "ranged"
    SPELL = "spell"
    SPECIAL = "special"
```

**Propriétés:**
- `name: str` - Nom de l'action
- `action_type: ActionType` - Type d'action
- `attack_bonus: int` - Bonus d'attaque
- `damage: Damage` - Dégâts infligés
- `range_type: RangeType` - Portée (mêlée/distance)
- `normal_range: int` - Portée normale
- `long_range: int` - Portée longue
- `dc_type: str` - Type de jet de sauvegarde (optionnel)
- `dc_value: int` - DC du jet de sauvegarde (optionnel)
- `dc_success: str` - Effet en cas de réussite (optionnel)

**Exemple:**
```python
from dnd_5e_core.combat import Action, ActionType, Damage
from dnd_5e_core.mechanics import DamageDice

action = Action(
    name="Longsword",
    action_type=ActionType.MELEE,
    attack_bonus=5,
    damage=Damage(
        damage_dice=DamageDice("1d8+3"),
        damage_type="slashing"
    ),
    range_type=RangeType.MELEE,
    normal_range=5
)
```

---

### Damage

Représente des dégâts avec type et dés.

**Importation:**
```python
from dnd_5e_core.combat import Damage
```

**Propriétés:**
- `damage_dice: DamageDice` - Dés de dégâts
- `damage_type: str` - Type de dégâts (slashing, piercing, fire, etc.)

**Utilisation:**
```python
from dnd_5e_core.combat import Damage
from dnd_5e_core.mechanics import DamageDice

# Dégâts de mêlée
melee_damage = Damage(
    damage_dice=DamageDice("1d8+3"),
    damage_type="slashing"
)

# Dégâts magiques
fire_damage = Damage(
    damage_dice=DamageDice("8d6"),
    damage_type="fire"
)

# Lancer les dégâts
result = melee_damage.damage_dice.roll()
print(f"Dégâts: {result}")
```

---

### Condition

États et conditions affectant les personnages et monstres.

**Importation:**
```python
from dnd_5e_core.combat import Condition
```

**Conditions standard D&D 5e:**
- `BLINDED` - Aveuglé
- `CHARMED` - Charmé
- `DEAFENED` - Assourdi
- `FRIGHTENED` - Effrayé
- `GRAPPLED` - Agrippé
- `INCAPACITATED` - Neutralisé
- `INVISIBLE` - Invisible
- `PARALYZED` - Paralysé
- `PETRIFIED` - Pétrifié
- `POISONED` - Empoisonné
- `PRONE` - À terre
- `RESTRAINED` - Entravé
- `STUNNED` - Étourdi
- `UNCONSCIOUS` - Inconscient
- `EXHAUSTION` - Épuisement

**Utilisation:**
```python
from dnd_5e_core.combat import Condition

# Appliquer une condition
character.add_condition(Condition.POISONED)

# Vérifier une condition
if character.has_condition(Condition.PARALYZED):
    print("Le personnage est paralysé!")

# Retirer une condition
character.remove_condition(Condition.POISONED)
```

---

### SpecialAbility

Capacités spéciales des monstres.

**Importation:**
```python
from dnd_5e_core.combat import SpecialAbility
```

**Propriétés:**
- `name: str` - Nom de la capacité
- `desc: str` - Description
- `damage: Optional[Damage]` - Dégâts (si applicable)
- `dc_type: str` - Type de jet de sauvegarde
- `dc_value: int` - DC du jet de sauvegarde
- `usage: Optional[dict]` - Limitations d'usage

**Exemple:**
```python
# Les capacités spéciales sont généralement chargées avec le monstre
dragon = load_monster("ancient-red-dragon")

if dragon.sa:
    for ability in dragon.sa:
        print(f"- {ability.name}: {ability.desc}")
```

---

## Exemples complets

### Combat tour par tour

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Préparation
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="cleric"),
]

monsters = [
    load_monster("goblin"),
    load_monster("goblin"),
    load_monster("hobgoblin"),
]

combat = CombatSystem(verbose=True)

# Lancer l'initiative
print("🎲 Lancer d'initiative...")
# (L'initiative est généralement gérée par votre UI)

# Boucle de combat
round_num = 1
while True:
    alive_party = [c for c in party if c.is_alive]
    alive_monsters = [m for m in monsters if m.is_alive]
    
    if not alive_party:
        print("💀 Défaite! Tous les héros sont tombés.")
        break
    
    if not alive_monsters:
        print("🎉 Victoire! Tous les monstres sont vaincus.")
        # Distribuer les récompenses
        xp, gold = combat.distribute_rewards(party, monsters)
        print(f"XP gagné: {xp}, Or: {gold}")
        break
    
    print(f"\n=== Round {round_num} ===")
    
    # Tours des joueurs
    for char in alive_party:
        target = alive_monsters[0]  # Cibler le premier monstre vivant
        combat.player_turn(char, target, action_type="melee")
    
    # Tours des monstres
    for monster in alive_monsters:
        combat.monster_turn(
            monster,
            alive_monsters,
            alive_party,
            party,
            round_num
        )
    
    round_num += 1
```

### Combat avec sorts

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster, load_spell

# Créer un groupe avec un lanceur de sorts
wizard = Character.generate_random_character(level=5, class_name="wizard")
fighter = Character.generate_random_character(level=5, class_name="fighter")
party = [wizard, fighter]

monsters = [load_monster("ogre")]

combat = CombatSystem(verbose=True)

# Le sorcier lance un sort
fireball = load_spell("fireball")
if wizard.spell_slots[2] > 0:  # Vérifier l'emplacement de niveau 3
    combat.player_turn(
        character=wizard,
        target=monsters[0],
        action_type="spell",
        spell=fireball,
        spell_slot_level=3
    )
```

### Combat avec positionnement (front/back)

```python
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Créer un groupe
party = [
    # Front (peuvent attaquer au corps à corps)
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="paladin"),
    Character.generate_random_character(level=5, class_name="barbarian"),
    # Back (attaques à distance uniquement)
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=5, class_name="ranger"),
    Character.generate_random_character(level=5, class_name="cleric"),
]

monsters = [
    load_monster("orc"),
    load_monster("orc"),
    load_monster("orc"),
]

combat = CombatSystem(verbose=True)

# Front row attaque au corps à corps
for i in range(3):
    if party[i].is_alive and monsters:
        combat.player_turn(
            party[i],
            monsters[0],
            action_type="melee"
        )

# Back row attaque à distance
for i in range(3, 6):
    if party[i].is_alive and monsters:
        combat.player_turn(
            party[i],
            monsters[0],
            action_type="ranged"
        )

# Les monstres ne peuvent attaquer que le front
alive_front = [c for c in party[:3] if c.is_alive]
alive_monsters = [m for m in monsters if m.is_alive]

for monster in alive_monsters:
    if alive_front:
        combat.monster_turn(
            monster,
            alive_monsters,
            alive_front,
            party,
            round_num=1
        )
```

### Gestion des conditions

```python
from dnd_5e_core.combat import Condition
from dnd_5e_core.entities import Character

hero = Character.generate_random_character(level=5, class_name="fighter")

# Appliquer empoisonnement
hero.add_condition(Condition.POISONED)
print(f"Conditions: {hero.conditions}")

# Vérifier avant d'attaquer
if hero.has_condition(Condition.PARALYZED):
    print("Ne peut pas attaquer - paralysé!")
elif hero.has_condition(Condition.POISONED):
    print("Désavantage aux jets d'attaque et de caractéristique")
    # Implémenter la logique de désavantage
    
# Retirer après un repos
hero.long_rest()
hero.remove_condition(Condition.POISONED)
```

---

## Règles implémentées

Le système de combat implémente les règles suivantes de D&D 5e:

### Attaque
- ✅ Jets d'attaque avec bonus d'attaque
- ✅ Comparaison avec la classe d'armure (CA)
- ✅ Coup critique (20 naturel)
- ✅ Échec critique (1 naturel)
- ✅ Attaques de mêlée et à distance
- ✅ Portée normale et longue

### Dégâts
- ✅ Lancer de dés de dégâts
- ✅ Types de dégâts (physiques et magiques)
- ✅ Bonus de caractéristique
- ✅ Dégâts doublés sur critique

### Sorts
- ✅ Emplacements de sorts par niveau
- ✅ Jets de sauvegarde contre sorts
- ✅ Dégâts de sort par niveau
- ✅ Sorts de zone (AOE)
- ✅ Sorts de soin

### IA des monstres
- ✅ Choix intelligent de cible
- ✅ Utilisation de sorts de soin sur alliés blessés
- ✅ Utilisation d'attaques spéciales
- ✅ Gestion des emplacements de sorts

### Récompenses
- ✅ Distribution d'XP selon CR
- ✅ Distribution d'or aléatoire
- ✅ Montée de niveau automatique

---

## Voir aussi

- [entities](./entities.md) - Personnages et monstres
- [mechanics](./mechanics.md) - Règles de jeu
- [spells](./spells.md) - Système de magie
- [equipment](./equipment.md) - Armes et armures

