# Module: mechanics

## Vue d'ensemble

Le module `mechanics` contient les règles de jeu fondamentales de D&D 5e : lancer de dés, expérience, facteur de puissance, rencontres, et montée de niveau.

## Classes et fonctions principales

### DamageDice

Système de lancer de dés pour dégâts, soins et autres calculs aléatoires.

**Importation:**
```python
from dnd_5e_core.mechanics import DamageDice
```

**Création:**

```python
# Notation standard D&D
damage = DamageDice("2d6+3")  # 2 dés à 6 faces + 3
heal = DamageDice("1d8")      # 1 dé à 8 faces
fireball = DamageDice("8d6")  # 8 dés à 6 faces

# Avec bonus séparé
damage = DamageDice("2d6", bonus=3)

# Avec malus
damage = DamageDice("1d6-2")
```

**Méthodes:**

```python
# Lancer les dés
result = damage.roll()
print(f"Résultat: {result}")

# Valeur maximum possible
max_dmg = damage.max_score
print(f"Maximum: {max_dmg}")

# Valeur moyenne attendue
avg_dmg = damage.avg
print(f"Moyenne: {avg_dmg}")

# Score avec modificateur de réussite
# "none" = dégâts complets, "half" = demi-dégâts
score = damage.score(success_type="half")
```

**Comparaison:**
```python
d6 = DamageDice("1d6")
d8 = DamageDice("1d8")

if d8 > d6:
    print("Le d8 fait plus de dégâts")
```

---

### Expérience

Gestion de l'XP et des niveaux.

**Importation:**
```python
from dnd_5e_core.mechanics import (
    xp_by_cr,
    xp_thresholds_by_level,
    calculate_level_from_xp
)
```

**XP par CR:**
```python
from dnd_5e_core.mechanics import xp_by_cr

# Dictionnaire de XP par CR
xp = xp_by_cr[0.5]  # CR 1/2 donne 100 XP
xp = xp_by_cr[5]    # CR 5 donne 1800 XP
xp = xp_by_cr[20]   # CR 20 donne 25000 XP
```

**Calculer le niveau:**
```python
from dnd_5e_core.mechanics import calculate_level_from_xp

level = calculate_level_from_xp(5000)  # Retourne le niveau correspondant
print(f"Niveau: {level}")
```

**Seuils d'XP par niveau:**
```python
from dnd_5e_core.mechanics import xp_thresholds_by_level

# Seuils pour rencontres (facile, moyenne, difficile, mortelle)
thresholds = xp_thresholds_by_level[5]
print(f"Niveau 5:")
print(f"  Facile: {thresholds['easy']}")
print(f"  Moyenne: {thresholds['medium']}")
print(f"  Difficile: {thresholds['hard']}")
print(f"  Mortelle: {thresholds['deadly']}")
```

---

### Challenge Rating (CR)

Calcul du facteur de puissance et génération de rencontres.

**Importation:**
```python
from dnd_5e_core.mechanics import (
    generate_encounter_cr,
    calculate_party_strength
)
```

**Générer CR de rencontre:**
```python
from dnd_5e_core.mechanics import generate_encounter_cr

# Groupe de 4 personnages niveau 5
party_levels = [5, 5, 5, 5]

# Rencontre moyenne
min_cr, max_cr = generate_encounter_cr(
    party_levels,
    difficulty="medium"
)
print(f"CR recommandé: {min_cr} - {max_cr}")

# Autres difficultés disponibles
min_cr, max_cr = generate_encounter_cr(party_levels, difficulty="easy")
min_cr, max_cr = generate_encounter_cr(party_levels, difficulty="hard")
min_cr, max_cr = generate_encounter_cr(party_levels, difficulty="deadly")
```

**Calculer la force du groupe:**
```python
from dnd_5e_core.mechanics import calculate_party_strength

party_levels = [5, 5, 4, 6]
strength = calculate_party_strength(party_levels)
print(f"Force du groupe: {strength}")
```

---

### Encounter Builder

Construction de rencontres équilibrées.

**Importation:**
```python
from dnd_5e_core.mechanics import build_encounter
```

**Construire une rencontre:**
```python
from dnd_5e_core.mechanics import build_encounter
from dnd_5e_core.data import load_monster

# Groupe
party_levels = [5, 5, 5, 5]

# Pool de monstres disponibles
available_monsters = [
    load_monster("goblin"),
    load_monster("hobgoblin"),
    load_monster("bugbear"),
    load_monster("orc"),
]

# Construire une rencontre équilibrée
encounter = build_encounter(
    party_levels=party_levels,
    available_monsters=available_monsters,
    difficulty="medium"
)

print(f"Rencontre créée avec {len(encounter)} monstres:")
for monster in encounter:
    print(f"  - {monster.name} (CR {monster.challenge_rating})")
```

---

### Level Up

Gestion de la montée de niveau.

**Importation:**
```python
from dnd_5e_core.mechanics import level_up_character
```

**Monter de niveau:**
```python
from dnd_5e_core.mechanics import level_up_character
from dnd_5e_core.entities import Character

hero = Character.generate_random_character(level=5, class_name="fighter")

# Gagner de l'XP
hero.experience_points += 3000

# Vérifier si montée de niveau
from dnd_5e_core.mechanics import calculate_level_from_xp
new_level = calculate_level_from_xp(hero.experience_points)

if new_level > hero.level:
    print(f"Montée de niveau! {hero.level} -> {new_level}")
    level_up_character(hero)
```

---

### Gold Rewards

Calcul des récompenses en or.

**Importation:**
```python
from dnd_5e_core.mechanics import (
    calculate_gold_reward,
    distribute_gold
)
```

**Calculer l'or:**
```python
from dnd_5e_core.mechanics import calculate_gold_reward

# Or basé sur le CR
gold = calculate_gold_reward(challenge_rating=5)
print(f"Or gagné: {gold} po")
```

**Distribuer l'or:**
```python
from dnd_5e_core.mechanics import distribute_gold

total_gold = 1000
party_size = 4

gold_per_member = distribute_gold(total_gold, party_size)
print(f"Chaque membre reçoit: {gold_per_member} po")
```

---

## Exemples complets

### Système de dés complet

```python
from dnd_5e_core.mechanics import DamageDice

# Dégâts d'arme
longsword = DamageDice("1d8+3")
greataxe = DamageDice("1d12+5")

print(f"Épée longue: {longsword.roll()}")
print(f"Hache d'armes: {greataxe.roll()}")

# Sort de boule de feu (niveau 3)
fireball_lv3 = DamageDice("8d6")
print(f"Boule de feu: {fireball_lv3.roll()}")

# Sort de boule de feu amélioré (niveau 5)
fireball_lv5 = DamageDice("10d6")  # +1d6 par niveau au-dessus de 3
print(f"Boule de feu niveau 5: {fireball_lv5.roll()}")

# Soin
cure_wounds = DamageDice("1d8+4")
hp_restored = cure_wounds.roll()
print(f"Soins: {hp_restored} PV")

# Comparer les dégâts
if greataxe > longsword:
    print("La hache fait plus de dégâts (en moyenne)")
```

### Gestion d'XP et niveaux

```python
from dnd_5e_core.mechanics import (
    xp_by_cr,
    calculate_level_from_xp
)
from dnd_5e_core.entities import Character

# Créer un héros niveau 1
hero = Character.generate_random_character(level=1, class_name="fighter")
print(f"{hero.name} - Niveau {hero.level} - XP: {hero.experience_points}")

# Combattre des monstres
defeated_monsters = [
    ("goblin", 0.25),      # CR 1/4 = 50 XP
    ("goblin", 0.25),
    ("hobgoblin", 0.5),    # CR 1/2 = 100 XP
]

for monster_name, cr in defeated_monsters:
    xp_gained = xp_by_cr[cr]
    hero.experience_points += xp_gained
    print(f"Vaincu {monster_name}! +{xp_gained} XP")
    
    # Vérifier montée de niveau
    new_level = calculate_level_from_xp(hero.experience_points)
    if new_level > hero.level:
        old_level = hero.level
        hero.level_up()
        print(f"🎉 MONTÉE DE NIVEAU! {old_level} -> {hero.level}")
        print(f"   Nouveaux PV max: {hero.max_hit_points}")
        print(f"   Nouveau bonus de maîtrise: {hero.proficiency_bonus}")

print(f"\nFinal: {hero.name} - Niveau {hero.level} - XP: {hero.experience_points}")
```

### Construction de rencontres

```python
from dnd_5e_core.mechanics import generate_encounter_cr, xp_by_cr
from dnd_5e_core.data import load_monster

# Groupe de 4 aventuriers niveau 5
party_levels = [5, 5, 5, 5]

# Déterminer le CR approprié
min_cr, max_cr = generate_encounter_cr(
    party_levels,
    difficulty="medium"
)

print(f"CR recommandé pour rencontre moyenne: {min_cr} - {max_cr}")

# Charger des monstres dans cette plage
possible_monsters = [
    "goblin",           # CR 0.25
    "hobgoblin",        # CR 0.5
    "orc",              # CR 1
    "ogre",             # CR 2
    "owlbear",          # CR 3
    "hill-giant",       # CR 5
]

encounter = []
total_xp = 0
target_xp = 1400  # Budget XP pour rencontre moyenne niveau 5

for monster_name in possible_monsters:
    monster = load_monster(monster_name)
    if min_cr <= monster.challenge_rating <= max_cr:
        # Ajouter des copies jusqu'à atteindre le budget
        while total_xp + monster.xp <= target_xp:
            encounter.append(load_monster(monster_name))
            total_xp += monster.xp

print(f"\n🎲 Rencontre générée (XP total: {total_xp}):")
from collections import Counter
monster_counts = Counter([m.name for m in encounter])
for monster_name, count in monster_counts.items():
    monster = next(m for m in encounter if m.name == monster_name)
    print(f"  {count}x {monster_name} (CR {monster.challenge_rating})")
```

### Système de récompenses complet

```python
from dnd_5e_core.mechanics import (
    xp_by_cr,
    calculate_gold_reward,
    distribute_gold
)
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_monster

# Groupe
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=4, class_name="cleric"),
    Character.generate_random_character(level=5, class_name="rogue"),
]

# Monstres vaincus
defeated = [
    load_monster("orc"),
    load_monster("orc"),
    load_monster("ogre"),
]

# Calculer XP total
total_xp = sum([m.xp for m in defeated])
xp_per_member = total_xp // len(party)

print(f"💀 Monstres vaincus:")
for monster in defeated:
    print(f"  - {monster.name} (CR {monster.challenge_rating}, {monster.xp} XP)")

print(f"\n⭐ XP total: {total_xp}")
print(f"   XP par membre: {xp_per_member}")

# Distribuer XP
for hero in party:
    old_xp = hero.experience_points
    hero.gain_xp(xp_per_member)
    print(f"   {hero.name}: {old_xp} -> {hero.experience_points}")

# Calculer or
total_gold = sum([calculate_gold_reward(m.challenge_rating) for m in defeated])
gold_per_member = distribute_gold(total_gold, len(party))

print(f"\n💰 Or total: {total_gold} po")
print(f"   Or par membre: {gold_per_member} po")

for hero in party:
    hero.gold += gold_per_member
    print(f"   {hero.name}: {hero.gold} po")
```

---

## Constantes utiles

### XP par CR
```python
xp_by_cr = {
    0: 10,
    0.125: 25,
    0.25: 50,
    0.5: 100,
    1: 200,
    2: 450,
    3: 700,
    4: 1100,
    5: 1800,
    10: 5900,
    15: 13000,
    20: 25000,
    30: 155000,
}
```

### Seuils XP par niveau
```python
xp_thresholds_by_level = {
    1: {"easy": 25, "medium": 50, "hard": 75, "deadly": 100},
    5: {"easy": 500, "medium": 1100, "hard": 1600, "deadly": 2400},
    10: {"easy": 1200, "medium": 2400, "hard": 3600, "deadly": 5400},
    20: {"easy": 2800, "medium": 5700, "hard": 8500, "deadly": 12700},
}
```

---

## Voir aussi

- [combat](./combat.md) - Système de combat
- [entities](./entities.md) - Personnages et monstres
- [spells](./spells.md) - Sorts et magie
- [equipment](./equipment.md) - Équipement

