# Module: data

## Vue d'ensemble

Le module `data` fournit les fonctions de chargement et de sérialisation pour toutes les données du jeu : monstres, sorts, armes, armures, races, classes.

**Important:** Toutes les fonctions `load_*()` retournent maintenant des objets de classe (Monster, Spell, Weapon, Armor) au lieu de dictionnaires JSON. Cela permet d'utiliser directement les méthodes et propriétés de ces objets.

## Fonctions de chargement

### load_monster()

Charge un monstre depuis les données JSON et retourne un objet `Monster`.

**Importation:**
```python
from dnd_5e_core.data import load_monster
```

**Signature:**
```python
def load_monster(index: str) -> Optional[Monster]
```

**Utilisation:**
```python
# Charger un monstre de base
goblin = load_monster("goblin")
print(f"{goblin.name} - CR {goblin.challenge_rating}")
print(f"HP: {goblin.hit_points}/{goblin.max_hit_points}")
print(f"AC: {goblin.armor_class}")

# Utiliser les méthodes de l'objet Monster
goblin.hp_roll()  # Relancer les HP pour variation
if goblin.is_spell_caster:
    print(f"DC: {goblin.dc_value}")

# Monstres puissants
dragon = load_monster("ancient-red-dragon")
lich = load_monster("lich")
```

**Retour:**
- Un objet `Monster` avec toutes ses propriétés et méthodes
- `None` si le monstre n'est pas trouvé

**Monstres disponibles:**
- Créatures de bas niveau: goblin, kobold, orc, skeleton, zombie
- Créatures moyennes: ogre, troll, owlbear, wyvern
- Créatures puissantes: giant, dragon, beholder, lich

---

### load_spell()

Charge un sort depuis les données JSON et retourne un objet `Spell`.

**Importation:**
```python
from dnd_5e_core.data import load_spell
```

**Signature:**
```python
def load_spell(index: str) -> Optional[Spell]
```

**Utilisation:**
```python
# Sorts de combat
fireball = load_spell("fireball")
print(f"{fireball.name} - Niveau {fireball.level}")
print(f"École: {fireball.school}")
print(f"Portée: {fireball.range} ft")

# Vérifier les propriétés
if fireball.is_damaging:
    print("Ce sort inflige des dégâts")
if fireball.requires_save:
    print(f"Jet de sauvegarde: {fireball.dc_type}")

# Autres sorts
magic_missile = load_spell("magic-missile")
cure_wounds = load_spell("cure-wounds")
shield = load_spell("shield")
```

**Retour:**
- Un objet `Spell` avec toutes ses propriétés et méthodes
- `None` si le sort n'est pas trouvé

---

### load_weapon()

Charge une arme depuis les données JSON et retourne un objet `Weapon`.

**Importation:**
```python
from dnd_5e_core.data import load_weapon
```

**Signature:**
```python
def load_weapon(index: str) -> Optional[Weapon]
```

**Utilisation:**
```python
# Armes de mêlée
longsword = load_weapon("longsword")
print(f"{longsword.name} - {longsword.damage_dice}")
print(f"Type: {longsword.damage_type}")

# Vérifier les propriétés
if longsword.is_melee:
    print("Arme de mêlée")
if longsword.is_martial:
    print("Arme martiale")

# Armes à distance
longbow = load_weapon("longbow")
if longbow.weapon_range:
    print(f"Portée: {longbow.weapon_range}")
```

**Retour:**
- Un objet `Weapon` avec toutes ses propriétés et méthodes
- `None` si l'arme n'est pas trouvée

---

### load_armor()

Charge une armure depuis les données JSON et retourne un objet `Armor`.

**Importation:**
```python
from dnd_5e_core.data import load_armor
```

**Signature:**
```python
def load_armor(index: str) -> Optional[Armor]
```

**Utilisation:**
```python
# Armures légères
leather = load_armor("leather-armor")
studded = load_armor("studded-leather-armor")

# Armures moyennes
chain_shirt = load_armor("chain-shirt")
scale_mail = load_armor("scale-mail")

# Armures lourdes
chain_mail = load_armor("chain-mail")
plate = load_armor("plate-armor")
```

---

## Chargement par collections

### Collections de monstres

**Importation:**
```python
from dnd_5e_core.entities import ExtendedMonsterLoader
```

**Utilisation:**
```python
loader = ExtendedMonsterLoader()

# Charger tous les monstres implémentés
all_monsters = loader.load_implemented_monsters()
print(f"Monstres disponibles: {len(all_monsters)}")

# Rechercher des monstres
goblins = loader.search_monsters(
    name_contains="goblin",
    min_cr=0,
    max_cr=2
)

dragons = loader.search_monsters(
    name_contains="dragon",
    min_cr=10,
    max_cr=30
)

# Charger un monstre spécifique
boss = loader.load_monster_by_index("ancient-red-dragon")

# Obtenir des statistiques
stats = loader.get_monster_stats()
print(f"Total de monstres: {stats['total']}")
print(f"Implémentés: {stats['implemented']}")
```

---

## Sérialisation

### Sauvegarder et charger des personnages

**Importation:**
```python
from dnd_5e_core.entities import Character
import json
```

**Sauvegarder:**
```python
# Créer un personnage
hero = Character.generate_random_character(level=5, class_name="wizard")

# Convertir en dictionnaire
char_data = hero.to_dict()

# Sauvegarder dans un fichier JSON
with open("hero.json", "w") as f:
    json.dump(char_data, f, indent=2)

print("Personnage sauvegardé!")
```

**Charger:**
```python
# Charger depuis un fichier JSON
with open("hero.json", "r") as f:
    char_data = json.load(f)

# Créer le personnage depuis les données
hero = Character.from_dict(char_data)

print(f"Personnage chargé: {hero.name} - {hero.classe.name} niveau {hero.level}")
```

---

### Sauvegarder un groupe

```python
import json
from dnd_5e_core.entities import Character

# Créer un groupe
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=5, class_name="cleric"),
    Character.generate_random_character(level=5, class_name="rogue"),
]

# Sauvegarder
party_data = {
    "party": [char.to_dict() for char in party]
}

with open("party.json", "w") as f:
    json.dump(party_data, f, indent=2)

# Charger
with open("party.json", "r") as f:
    party_data = json.load(f)

loaded_party = [Character.from_dict(char_data) for char_data in party_data["party"]]

print(f"Groupe chargé: {len(loaded_party)} membres")
for hero in loaded_party:
    print(f"  - {hero.name} ({hero.classe.name} {hero.level})")
```

---

## API Client

Accès direct à l'API D&D 5e.

**Importation:**
```python
from dnd_5e_core.data import api_client
```

**Utilisation:**
```python
# Requête directe à l'API
monster_data = api_client.get_monster("goblin")
spell_data = api_client.get_spell("fireball")

# Note: Les fonctions load_* sont recommandées car elles incluent
# des données locales enrichies et gèrent le cache
```

---

## Exemples complets

### Charger toutes les données pour un scénario

```python
from dnd_5e_core.data import load_monster, load_spell, load_weapon, load_armor
from dnd_5e_core.entities import Character

# Créer le groupe
party = [
    Character.generate_random_character(level=5, class_name="fighter"),
    Character.generate_random_character(level=5, class_name="wizard"),
    Character.generate_random_character(level=5, class_name="cleric"),
]

# Équiper le groupe
longsword = load_weapon("longsword")
party[0].equip_weapon(longsword)

plate = load_armor("plate-armor")
party[0].equip_armor(plate)

# Préparer les sorts
fireball = load_spell("fireball")
party[1].prepare_spells([fireball])

cure_wounds = load_spell("cure-wounds")
party[2].prepare_spells([cure_wounds])

# Charger les monstres
encounter = [
    load_monster("orc"),
    load_monster("orc"),
    load_monster("ogre"),
]

print("Groupe prêt pour l'aventure!")
print(f"  {len(party)} héros")
print(f"  {len(encounter)} monstres")
```

### Construire un bestiaire

```python
from dnd_5e_core.entities import ExtendedMonsterLoader

loader = ExtendedMonsterLoader()

# Charger par catégorie
categories = {
    "Faible (CR 0-1)": loader.search_monsters(min_cr=0, max_cr=1),
    "Moyen (CR 2-5)": loader.search_monsters(min_cr=2, max_cr=5),
    "Fort (CR 6-10)": loader.search_monsters(min_cr=6, max_cr=10),
    "Très fort (CR 11+)": loader.search_monsters(min_cr=11, max_cr=30),
}

print("📚 BESTIAIRE D&D 5e")
for category, monsters in categories.items():
    print(f"\n{category}:")
    for monster in sorted(monsters, key=lambda m: m.challenge_rating):
        print(f"  - {monster.name} (CR {monster.challenge_rating}, {monster.xp} XP)")
```

### Système de cache

```python
from dnd_5e_core.data import load_monster
import time

# Premier chargement (depuis fichier/API)
start = time.time()
dragon1 = load_monster("ancient-red-dragon")
first_load = time.time() - start

# Deuxième chargement (depuis cache)
start = time.time()
dragon2 = load_monster("ancient-red-dragon")
cached_load = time.time() - start

print(f"Premier chargement: {first_load:.4f}s")
print(f"Chargement depuis cache: {cached_load:.4f}s")
print(f"Accélération: {first_load / cached_load:.1f}x")
```

---

## Sources de données

Le package utilise plusieurs sources :

### 1. API D&D 5e officielle
- URL: https://www.dnd5eapi.co
- Données de base pour monstres, sorts, équipement
- Cache local pour performance

### 2. Données locales enrichies
- Monstres étendus (bestiaire complet)
- Statistiques personnalisées
- Fichiers JSON dans `data/`

### 3. Collections
- Listes de monstres par catégorie
- Templates de personnages
- Équipement pré-configuré

---

## Fichiers de données

Structure du répertoire `data/`:

```
data/
├── monsters/
│   ├── monsters.json           # Monstres de base
│   └── bestiary-sublist-data.json  # Monstres étendus
├── spells/
│   └── spells.json
├── equipment/
│   ├── weapons.json
│   └── armor.json
├── races/
│   └── races.json
└── classes/
    └── classes.json
```

---

## Voir aussi

- [entities](./entities.md) - Personnages et monstres
- [equipment](./equipment.md) - Armes et armures
- [spells](./spells.md) - Sorts
- [combat](./combat.md) - Système de combat

