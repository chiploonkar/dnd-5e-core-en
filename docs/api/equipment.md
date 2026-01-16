# Module: equipment

## Vue d'ensemble

Le module `equipment` gère tout l'équipement : armes, armures, potions et objets généraux.

## Classes principales

### Weapon

Armes avec caractéristiques de combat.

**Importation:**
```python
from dnd_5e_core.equipment import Weapon
from dnd_5e_core.data import load_weapon
```

**Charger une arme:**
```python
from dnd_5e_core.data import load_weapon

# Charger depuis les données
longsword = load_weapon("longsword")
longbow = load_weapon("longbow")
dagger = load_weapon("dagger")

print(f"{longsword.name}")
print(f"  Dégâts: {longsword.damage}")
print(f"  Type: {longsword.damage_type}")
print(f"  Portée: {longsword.range_type}")
```

**Propriétés:**
- `name: str` - Nom de l'arme
- `equipment_category: str` - Catégorie ("Weapon")
- `weapon_category: str` - Type ("Martial", "Simple")
- `weapon_range: str` - Portée ("Melee", "Ranged")
- `damage: DamageDice` - Dés de dégâts
- `damage_type: str` - Type de dégâts (slashing, piercing, bludgeoning)
- `range_type: RangeType` - MELEE ou RANGED
- `normal_range: int` - Portée normale (en pieds)
- `long_range: int` - Portée longue (en pieds)
- `cost: Cost` - Coût en pièces d'or

**Utilisation:**
```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_weapon

hero = Character.generate_random_character(level=5, class_name="fighter")
longsword = load_weapon("longsword")

# Équiper l'arme
hero.equip_weapon(longsword)

# Attaquer avec
damage = hero.melee_attack(monster)
```

---

### Armor

Armures avec bonus de CA.

**Importation:**
```python
from dnd_5e_core.equipment import Armor
from dnd_5e_core.data import load_armor
```

**Charger une armure:**
```python
from dnd_5e_core.data import load_armor

# Armures légères
leather = load_armor("leather-armor")
studded = load_armor("studded-leather-armor")

# Armures moyennes
chain_shirt = load_armor("chain-shirt")
scale_mail = load_armor("scale-mail")

# Armures lourdes
chain_mail = load_armor("chain-mail")
plate = load_armor("plate-armor")

print(f"{plate.name}")
print(f"  CA de base: {plate.armor_class}")
print(f"  Catégorie: {plate.armor_category}")
print(f"  Coût: {plate.cost.quantity} {plate.cost.unit}")
```

**Propriétés:**
- `name: str` - Nom de l'armure
- `armor_category: str` - Catégorie ("Light", "Medium", "Heavy")
- `armor_class: int` - Bonus de CA de base
- `str_minimum: int` - Force minimum requise
- `stealth_disadvantage: bool` - Désavantage en discrétion
- `cost: Cost` - Coût

**Catégories:**
- **Light Armor** - Ajoute bonus DEX complet
- **Medium Armor** - Ajoute bonus DEX (max +2)
- **Heavy Armor** - Pas de bonus DEX

---

### HealingPotion

Potions de soin.

**Importation:**
```python
from dnd_5e_core.equipment import HealingPotion, PotionRarity
```

**Création:**
```python
from dnd_5e_core.equipment import HealingPotion, PotionRarity

# Potion commune (2d4+2)
potion_common = HealingPotion(
    id=1,
    name="Potion of Healing",
    rarity=PotionRarity.COMMON,
    hit_dice="2d4",
    bonus=2,
    min_cost=50,
    max_cost=50
)

# Potion supérieure (4d4+4)
potion_greater = HealingPotion(
    id=2,
    name="Potion of Greater Healing",
    rarity=PotionRarity.UNCOMMON,
    hit_dice="4d4",
    bonus=4,
    min_cost=150,
    max_cost=150
)

# Potion suprême (10d4+20)
potion_supreme = HealingPotion(
    id=3,
    name="Potion of Supreme Healing",
    rarity=PotionRarity.VERY_RARE,
    hit_dice="10d4",
    bonus=20,
    min_cost=1350,
    max_cost=1350
)
```

**Utilisation:**
```python
from dnd_5e_core.entities import Character

hero = Character.generate_random_character(level=5, class_name="fighter")

# Blesser le héros
hero.hit_points = 10

print(f"PV avant: {hero.hit_points}/{hero.max_hit_points}")

# Boire la potion
hp_restored = hero.drink_potion(potion_common)

print(f"Soigné de: {hp_restored} PV")
print(f"PV après: {hero.hit_points}/{hero.max_hit_points}")
```

**Raretés disponibles:**
```python
class PotionRarity(Enum):
    COMMON = "common"           # 2d4+2
    UNCOMMON = "uncommon"       # 4d4+4
    RARE = "rare"               # 8d4+8
    VERY_RARE = "very_rare"     # 10d4+20
```

---

### SpeedPotion

Potions de vitesse.

**Importation:**
```python
from dnd_5e_core.equipment import SpeedPotion, PotionRarity
```

**Création:**
```python
potion = SpeedPotion(
    id=4,
    name="Potion of Speed",
    rarity=PotionRarity.RARE,
    speed_bonus=10,  # +10 pieds de vitesse
    duration_rounds=10,
    min_cost=400,
    max_cost=400
)
```

---

### StrengthPotion

Potions de force.

**Importation:**
```python
from dnd_5e_core.equipment import StrengthPotion, PotionRarity
```

**Création:**
```python
potion = StrengthPotion(
    id=5,
    name="Potion of Giant Strength",
    rarity=PotionRarity.RARE,
    strength_value=21,  # Force devient 21
    duration_rounds=60,
    min_cost=500,
    max_cost=500
)
```

---

### Inventory

Gestion d'inventaire.

**Importation:**
```python
from dnd_5e_core.equipment import Inventory
```

**Utilisation:**
```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_weapon, load_armor

hero = Character.generate_random_character(level=5, class_name="fighter")

# L'inventaire est créé automatiquement
inv = hero.inventory

# Ajouter des objets
longsword = load_weapon("longsword")
inv.add_weapon(longsword)

plate = load_armor("plate-armor")
inv.add_armor(plate)

potion = HealingPotion(
    id=1,
    name="Potion of Healing",
    rarity=PotionRarity.COMMON,
    hit_dice="2d4",
    bonus=2,
    min_cost=50,
    max_cost=50
)
inv.add_potion(potion)

# Lister l'inventaire
print(f"Armes: {len(inv.weapons)}")
print(f"Armures: {len(inv.armors)}")
print(f"Potions: {len(inv.potions)}")
```

---

### Equipment

Équipement général.

**Importation:**
```python
from dnd_5e_core.equipment import Equipment, Cost
```

**Création:**
```python
rope = Equipment(
    index="rope",
    name="Rope (50 feet)",
    equipment_category="Adventuring Gear",
    cost=Cost(quantity=1, unit="gp")
)

torch = Equipment(
    index="torch",
    name="Torch",
    equipment_category="Adventuring Gear",
    cost=Cost(quantity=1, unit="cp")
)
```

---

## Exemples complets

### Équiper un personnage

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_weapon, load_armor
from dnd_5e_core.equipment import HealingPotion, PotionRarity

# Créer le personnage
fighter = Character.generate_random_character(level=5, class_name="fighter")

# Équiper armes
longsword = load_weapon("longsword")
fighter.equip_weapon(longsword)

longbow = load_weapon("longbow")
fighter.inventory.add_weapon(longbow)

# Équiper armure
plate = load_armor("plate-armor")
fighter.equip_armor(plate)

# Ajouter potions
for i in range(5):
    potion = HealingPotion(
        id=i,
        name="Potion of Healing",
        rarity=PotionRarity.COMMON,
        hit_dice="2d4",
        bonus=2,
        min_cost=50,
        max_cost=50
    )
    fighter.inventory.add_potion(potion)

print(f"{fighter.name} - {fighter.classe.name} niveau {fighter.level}")
print(f"CA: {fighter.armor_class}")
print(f"Arme: {fighter.weapon.name if fighter.weapon else 'Aucune'}")
print(f"Armure: {fighter.armor.name if fighter.armor else 'Aucune'}")
print(f"Potions: {len(fighter.inventory.potions)}")
```

### Armes par catégorie

```python
from dnd_5e_core.data import load_weapon

# Armes simples de mêlée
simple_melee = [
    "club",
    "dagger",
    "quarterstaff",
    "spear",
]

# Armes de guerre de mêlée
martial_melee = [
    "longsword",
    "greatsword",
    "battleaxe",
    "warhammer",
]

# Armes à distance
ranged = [
    "shortbow",
    "longbow",
    "light-crossbow",
    "heavy-crossbow",
]

print("Armes simples de mêlée:")
for weapon_name in simple_melee:
    weapon = load_weapon(weapon_name)
    print(f"  {weapon.name}: {weapon.damage} {weapon.damage_type}")

print("\nArmes de guerre de mêlée:")
for weapon_name in martial_melee:
    weapon = load_weapon(weapon_name)
    print(f"  {weapon.name}: {weapon.damage} {weapon.damage_type}")

print("\nArmes à distance:")
for weapon_name in ranged:
    weapon = load_weapon(weapon_name)
    print(f"  {weapon.name}: {weapon.damage} {weapon.damage_type} ({weapon.normal_range}ft)")
```

### Armures par catégorie

```python
from dnd_5e_core.data import load_armor

# Armures légères
light_armor = ["padded", "leather-armor", "studded-leather-armor"]

# Armures moyennes
medium_armor = ["hide-armor", "chain-shirt", "scale-mail", "breastplate"]

# Armures lourdes
heavy_armor = ["ring-mail", "chain-mail", "splint-armor", "plate-armor"]

print("Armures légères:")
for armor_name in light_armor:
    armor = load_armor(armor_name)
    print(f"  {armor.name}: CA {armor.armor_class}")

print("\nArmures moyennes:")
for armor_name in medium_armor:
    armor = load_armor(armor_name)
    print(f"  {armor.name}: CA {armor.armor_class}")

print("\nArmures lourdes:")
for armor_name in heavy_armor:
    armor = load_armor(armor_name)
    print(f"  {armor.name}: CA {armor.armor_class} (Force min: {armor.str_minimum})")
```

### Système de potions

```python
from dnd_5e_core.equipment import HealingPotion, PotionRarity

# Toutes les raretés de potions de soin
potions = [
    HealingPotion(1, "Potion of Healing", PotionRarity.COMMON, "2d4", 2, 50, 50),
    HealingPotion(2, "Potion of Greater Healing", PotionRarity.UNCOMMON, "4d4", 4, 150, 150),
    HealingPotion(3, "Potion of Superior Healing", PotionRarity.RARE, "8d4", 8, 450, 450),
    HealingPotion(4, "Potion of Supreme Healing", PotionRarity.VERY_RARE, "10d4", 20, 1350, 1350),
]

print("Potions de soin:")
for potion in potions:
    print(f"{potion.name} ({potion.rarity.value})")
    print(f"  Soigne: {potion.hit_dice}+{potion.bonus}")
    print(f"  Coût: {potion.min_cost} po")
    print()
```

---

## Voir aussi

- [entities](./entities.md) - Personnages et monstres
- [combat](./combat.md) - Système de combat
- [data](./data.md) - Chargement de données

