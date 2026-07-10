# Module: equipment

## Overview

The `equipment` module manages all equipment: weapons, armors, potions, and general items.

## Core Classes

### Weapon

Weapons with combat statistics.

**Import:**
```python
from dnd_5e_core.equipment import Weapon
from dnd_5e_core.data import load_weapon
```

**Load a Weapon:**
```python
from dnd_5e_core.data import load_weapon

# Load from data
longsword = load_weapon("longsword")
longbow = load_weapon("longbow")
dagger = load_weapon("dagger")

print(f"{longsword.name}")
print(f"  Damage: {longsword.damage}")
print(f"  Type: {longsword.damage_type}")
print(f"  Range: {longsword.range_type}")
```

**Properties:**
- `name: str` - Weapon name
- `equipment_category: str` - Category ("Weapon")
- `weapon_category: str` - Type ("Martial", "Simple")
- `weapon_range: str` - Range ("Melee", "Ranged")
- `damage: DamageDice` - Damage dice
- `damage_type: str` - Damage type (slashing, piercing, bludgeoning)
- `range_type: RangeType` - MELEE or RANGED
- `normal_range: int` - Normal range (in feet)
- `long_range: int` - Long range (in feet)
- `cost: Cost` - Cost in gold pieces

**Usage:**
```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_weapon

hero = Character.generate_random_character(level=5, class_name="fighter")
longsword = load_weapon("longsword")

# Equip the weapon
hero.equip_weapon(longsword)

# Attack with it
damage = hero.melee_attack(monster)
```

---

### Armor

Armors with AC bonuses.

**Import:**
```python
from dnd_5e_core.equipment import Armor
from dnd_5e_core.data import load_armor
```

**Load an Armor:**
```python
from dnd_5e_core.data import load_armor

# Light armors
leather = load_armor("leather-armor")
studded = load_armor("studded-leather-armor")

# Medium armors
chain_shirt = load_armor("chain-shirt")
scale_mail = load_armor("scale-mail")

# Heavy armors
chain_mail = load_armor("chain-mail")
plate = load_armor("plate-armor")

print(f"{plate.name}")
print(f"  Base AC: {plate.armor_class}")
print(f"  Category: {plate.armor_category}")
print(f"  Cost: {plate.cost.quantity} {plate.cost.unit}")
```

**Properties:**
- `name: str` - Armor name
- `armor_category: str` - Category ("Light", "Medium", "Heavy")
- `armor_class: int` - Base AC bonus
- `str_minimum: int` - Minimum strength required
- `stealth_disadvantage: bool` - Stealth disadvantage
- `cost: Cost` - Cost

**Categories:**
- **Light Armor** - Adds full DEX modifier
- **Medium Armor** - Adds DEX modifier (max +2)
- **Heavy Armor** - No DEX modifier

---

### HealingPotion

Healing potions.

**Import:**
```python
from dnd_5e_core.equipment import HealingPotion, PotionRarity
```

**Creation:**
```python
from dnd_5e_core.equipment import HealingPotion, PotionRarity

# Common potion (2d4+2)
potion_common = HealingPotion(
    id=1,
    name="Potion of Healing",
    rarity=PotionRarity.COMMON,
    hit_dice="2d4",
    bonus=2,
    min_cost=50,
    max_cost=50
)

# Greater potion (4d4+4)
potion_greater = HealingPotion(
    id=2,
    name="Potion of Greater Healing",
    rarity=PotionRarity.UNCOMMON,
    hit_dice="4d4",
    bonus=4,
    min_cost=150,
    max_cost=150
)

# Supreme potion (10d4+20)
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

**Usage:**
```python
from dnd_5e_core.entities import Character

hero = Character.generate_random_character(level=5, class_name="fighter")

# Injure the hero
hero.hit_points = 10

print(f"HP before: {hero.hit_points}/{hero.max_hit_points}")

# Drink the potion
hp_restored = hero.drink_potion(potion_common)

print(f"Healed for: {hp_restored} HP")
print(f"HP after: {hero.hit_points}/{hero.max_hit_points}")
```

**Available Rarities:**
```python
class PotionRarity(Enum):
    COMMON = "common"           # 2d4+2
    UNCOMMON = "uncommon"       # 4d4+4
    RARE = "rare"               # 8d4+8
    VERY_RARE = "very_rare"     # 10d4+20
```

---

### SpeedPotion

Speed potions.

**Import:**
```python
from dnd_5e_core.equipment import SpeedPotion, PotionRarity
```

**Creation:**
```python
potion = SpeedPotion(
    id=4,
    name="Potion of Speed",
    rarity=PotionRarity.RARE,
    speed_bonus=10,  # +10 feet of speed
    duration_rounds=10,
    min_cost=400,
    max_cost=400
)
```

---

### StrengthPotion

Strength potions.

**Import:**
```python
from dnd_5e_core.equipment import StrengthPotion, PotionRarity
```

**Creation:**
```python
potion = StrengthPotion(
    id=5,
    name="Potion of Giant Strength",
    rarity=PotionRarity.RARE,
    strength_value=21,  # Strength becomes 21
    duration_rounds=60,
    min_cost=500,
    max_cost=500
)
```

---

### Inventory

Inventory management.

**Import:**
```python
from dnd_5e_core.equipment import Inventory
```

**Usage:**
```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_weapon, load_armor

hero = Character.generate_random_character(level=5, class_name="fighter")

# The inventory is automatically created
inv = hero.inventory

# Add items
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

# List the inventory
print(f"Weapons: {len(inv.weapons)}")
print(f"Armors: {len(inv.armors)}")
print(f"Potions: {len(inv.potions)}")
```

---

### Equipment

General equipment.

**Import:**
```python
from dnd_5e_core.equipment import Equipment, Cost
```

**Creation:**
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

## Complete Examples

### Equip a Character

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_weapon, load_armor
from dnd_5e_core.equipment import HealingPotion, PotionRarity

# Create the character
fighter = Character.generate_random_character(level=5, class_name="fighter")

# Equip weapons
longsword = load_weapon("longsword")
fighter.equip_weapon(longsword)

longbow = load_weapon("longbow")
fighter.inventory.add_weapon(longbow)

# Equip armor
plate = load_armor("plate-armor")
fighter.equip_armor(plate)

# Add potions
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

print(f"{fighter.name} - {fighter.classe.name} level {fighter.level}")
print(f"AC: {fighter.armor_class}")
print(f"Weapon: {fighter.weapon.name if fighter.weapon else 'None'}")
print(f"Armor: {fighter.armor.name if fighter.armor else 'None'}")
print(f"Potions: {len(fighter.inventory.potions)}")
```

### Weapons by Category

```python
from dnd_5e_core.data import load_weapon

# Simple melee weapons
simple_melee = [
    "club",
    "dagger",
    "quarterstaff",
    "spear",
]

# Martial melee weapons
martial_melee = [
    "longsword",
    "greatsword",
    "battleaxe",
    "warhammer",
]

# Ranged weapons
ranged = [
    "shortbow",
    "longbow",
    "light-crossbow",
    "heavy-crossbow",
]

print("Simple melee weapons:")
for weapon_name in simple_melee:
    weapon = load_weapon(weapon_name)
    print(f"  {weapon.name}: {weapon.damage} {weapon.damage_type}")

print("\nMartial melee weapons:")
for weapon_name in martial_melee:
    weapon = load_weapon(weapon_name)
    print(f"  {weapon.name}: {weapon.damage} {weapon.damage_type}")

print("\nRanged weapons:")
for weapon_name in ranged:
    weapon = load_weapon(weapon_name)
    print(f"  {weapon.name}: {weapon.damage} {weapon.damage_type} ({weapon.normal_range}ft)")
```

### Armors by Category

```python
from dnd_5e_core.data import load_armor

# Light armors
light_armor = ["padded", "leather-armor", "studded-leather-armor"]

# Medium armors
medium_armor = ["hide-armor", "chain-shirt", "scale-mail", "breastplate"]

# Heavy armors
heavy_armor = ["ring-mail", "chain-mail", "splint-armor", "plate-armor"]

print("Light armors:")
for armor_name in light_armor:
    armor = load_armor(armor_name)
    print(f"  {armor.name}: AC {armor.armor_class}")

print("\nMedium armors:")
for armor_name in medium_armor:
    armor = load_armor(armor_name)
    print(f"  {armor.name}: AC {armor.armor_class}")

print("\nHeavy armors:")
for armor_name in heavy_armor:
    armor = load_armor(armor_name)
    print(f"  {armor.name}: AC {armor.armor_class} (Min Strength: {armor.str_minimum})")
```

### Potion System

```python
from dnd_5e_core.equipment import HealingPotion, PotionRarity

# All rarities of healing potions
potions = [
    HealingPotion(1, "Potion of Healing", PotionRarity.COMMON, "2d4", 2, 50, 50),
    HealingPotion(2, "Potion of Greater Healing", PotionRarity.UNCOMMON, "4d4", 4, 150, 150),
    HealingPotion(3, "Potion of Superior Healing", PotionRarity.RARE, "8d4", 8, 450, 450),
    HealingPotion(4, "Potion of Supreme Healing", PotionRarity.VERY_RARE, "10d4", 20, 1350, 1350),
]

print("Healing potions:")
for potion in potions:
    print(f"{potion.name} ({potion.rarity.value})")
    print(f"  Heals: {potion.hit_dice}+{potion.bonus}")
    print(f"  Cost: {potion.min_cost} gp")
    print()
```

---

## See Also

- [entities](entities.md) - Characters and monsters
- [combat](combat.md) - Combat system
- [data](data-loading.md) - Data loading
