# Module: spells

## Vue d'ensemble

Le module `spells` gère le système de magie de D&D 5e : sorts, lanceurs de sorts, emplacements de sorts et cantrips.

## Classes principales

### Spell

Représente un sort avec tous ses paramètres.

**Importation:**
```python
from dnd_5e_core.spells import Spell
from dnd_5e_core.data import load_spell
```

**Charger un sort:**
```python
from dnd_5e_core.data import load_spell

# Sorts de combat
fireball = load_spell("fireball")
magic_missile = load_spell("magic-missile")
lightning_bolt = load_spell("lightning-bolt")

# Sorts de soin
cure_wounds = load_spell("cure-wounds")
healing_word = load_spell("healing-word")

# Sorts utilitaires
shield = load_spell("shield")
detect_magic = load_spell("detect-magic")

print(f"{fireball.name}")
print(f"  Niveau: {fireball.level}")
print(f"  École: {fireball.school}")
print(f"  Portée: {fireball.range}")
print(f"  Temps d'incantation: {fireball.casting_time}")
```

**Propriétés:**
- `index: str` - Identifiant unique
- `name: str` - Nom du sort
- `level: int` - Niveau (0-9)
- `school: str` - École de magie
- `casting_time: str` - Temps d'incantation
- `range: str` - Portée
- `components: List[str]` - Composants (V, S, M)
- `duration: str` - Durée
- `concentration: bool` - Nécessite concentration
- `ritual: bool` - Peut être lancé en rituel
- `damage: Optional[Damage]` - Dégâts (si applicable)
- `dc: Optional[dict]` - Jet de sauvegarde
- `heal_at_slot_level: Optional[dict]` - Soins par niveau

**Méthodes:**
```python
# Obtenir les dégâts à un niveau de sort
damage_dice = fireball.get_damage_effect(slot_level=3)
result = damage_dice.roll()

# Obtenir les soins à un niveau de sort
heal_dice = cure_wounds.get_heal_effect(slot_level=1, ability_modifier=3)
hp_restored = heal_dice.roll()
```

---

### SpellCaster

Gestion des capacités de lancement de sorts.

**Importation:**
```python
from dnd_5e_core.spells import SpellCaster
```

**Propriétés:**
- `ability: str` - Caractéristique d'incantation ("int", "wis", "cha")
- `ability_modifier: int` - Modificateur de caractéristique
- `dc_value: int` - DD des sorts
- `spell_attack_bonus: int` - Bonus d'attaque magique
- `spell_slots: List[int]` - Emplacements par niveau
- `learned_spells: List[Spell]` - Sorts connus
- `prepared_spells: List[Spell]` - Sorts préparés

**Utilisation:**
```python
from dnd_5e_core.entities import Character

# Créer un lanceur de sorts
wizard = Character.generate_random_character(level=5, class_name="wizard")

# Vérifier les emplacements
print(f"Emplacements de sorts:")
for level, slots in enumerate(wizard.spell_slots, 1):
    if slots > 0:
        print(f"  Niveau {level}: {slots}")

# Préparer des sorts
from dnd_5e_core.data import load_spell
spells_to_prepare = [
    load_spell("magic-missile"),
    load_spell("shield"),
    load_spell("misty-step"),
    load_spell("fireball"),
]
wizard.prepare_spells(spells_to_prepare)

# Lancer un sort
fireball = load_spell("fireball")
wizard.cast_spell(fireball, target=monster, slot_level=3)
```

---

### Cantrips

Sorts mineurs (niveau 0).

**Importation:**
```python
from dnd_5e_core.data import load_spell
```

**Cantrips de combat:**
```python
# Cantrips qui infligent des dégâts
fire_bolt = load_spell("fire-bolt")        # 1d10 feu
ray_of_frost = load_spell("ray-of-frost")  # 1d8 froid
eldritch_blast = load_spell("eldritch-blast")  # 1d10 force

# Utilisation
damage = fire_bolt.get_damage_effect(character_level=5)
result = damage.roll()
```

**Cantrips utilitaires:**
```python
mage_hand = load_spell("mage-hand")
prestidigitation = load_spell("prestidigitation")
light = load_spell("light")
```

---

### Spell Slots

Gestion des emplacements de sorts.

**Emplacements par niveau de classe:**
```python
# Niveau 1: [2, 0, 0, 0, 0, 0, 0, 0, 0]  # 2 emplacements niveau 1
# Niveau 5: [4, 3, 2, 0, 0, 0, 0, 0, 0]  # 4/3/2 emplacements
# Niveau 20: [4, 3, 3, 3, 3, 2, 2, 1, 1] # Tous les niveaux

from dnd_5e_core.entities import Character

wizard = Character.generate_random_character(level=5, class_name="wizard")

# Utiliser un emplacement
slot_level = 3
if wizard.spell_slots[slot_level - 1] > 0:
    wizard.spell_slots[slot_level - 1] -= 1
    print(f"Emplacement niveau {slot_level} utilisé")

# Repos long restaure tous les emplacements
wizard.long_rest()
```

---

## Exemples complets

### Lanceur de sorts complet

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_spell

# Créer un sorcier
wizard = Character.generate_random_character(level=5, class_name="wizard")

print(f"{wizard.name} - Sorcier niveau {wizard.level}")
print(f"Intelligence: {wizard.abilities.int}")
print(f"DD des sorts: {wizard.sc.dc_value}")
print(f"Bonus d'attaque magique: {wizard.sc.spell_attack_bonus}")

# Préparer des sorts
spells = [
    load_spell("magic-missile"),     # Niveau 1
    load_spell("shield"),             # Niveau 1
    load_spell("detect-magic"),       # Niveau 1
    load_spell("misty-step"),         # Niveau 2
    load_spell("fireball"),           # Niveau 3
    load_spell("counterspell"),       # Niveau 3
]

wizard.prepare_spells(spells)

print(f"\nSorts préparés: {len(wizard.sc.prepared_spells)}")
for spell in wizard.sc.prepared_spells:
    print(f"  - {spell.name} (niveau {spell.level})")

# Combat
from dnd_5e_core.data import load_monster
goblin = load_monster("goblin")

# Lancer Magic Missile (toujours touche)
magic_missile = load_spell("magic-missile")
print(f"\n{wizard.name} lance {magic_missile.name}!")
damage_dice = magic_missile.get_damage_effect(slot_level=1)
damage = damage_dice.roll()
goblin.hit_points -= damage
print(f"  {damage} dégâts de force!")
```

### École de magie

```python
from dnd_5e_core.data import load_spell

# Écoles de magie
schools = {
    "Abjuration": ["shield", "counterspell"],
    "Conjuration": ["misty-step", "conjure-animals"],
    "Divination": ["detect-magic", "identify"],
    "Enchantment": ["charm-person", "hold-person"],
    "Evocation": ["magic-missile", "fireball", "lightning-bolt"],
    "Illusion": ["disguise-self", "invisibility"],
    "Necromancy": ["inflict-wounds", "animate-dead"],
    "Transmutation": ["alter-self", "haste"],
}

print("Sorts par école:")
for school, spell_names in schools.items():
    print(f"\n{school}:")
    for spell_name in spell_names:
        spell = load_spell(spell_name)
        print(f"  - {spell.name} (niveau {spell.level})")
```

### Système de soin magique

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_spell

# Créer un clerc
cleric = Character.generate_random_character(level=5, class_name="cleric")
fighter = Character.generate_random_character(level=5, class_name="fighter")

# Blesser le guerrier
fighter.hit_points = 10
print(f"{fighter.name}: {fighter.hit_points}/{fighter.max_hit_points} PV")

# Lancer Cure Wounds
cure_wounds = load_spell("cure-wounds")
print(f"\n{cleric.name} lance {cure_wounds.name}!")

# Niveau 1
heal_dice = cure_wounds.get_heal_effect(slot_level=1, ability_modifier=cleric.abilities.wis_mod)
hp_restored = heal_dice.roll()
fighter.hit_points = min(fighter.hit_points + hp_restored, fighter.max_hit_points)
print(f"  {hp_restored} PV restaurés")
print(f"{fighter.name}: {fighter.hit_points}/{fighter.max_hit_points} PV")
```

### Sorts de zone (AOE)

```python
from dnd_5e_core.entities import Character
from dnd_5e_core.data import load_spell, load_monster

wizard = Character.generate_random_character(level=5, class_name="wizard")

# Groupe de gobelins
goblins = [load_monster("goblin") for _ in range(5)]

# Lancer Fireball
fireball = load_spell("fireball")
print(f"{wizard.name} lance {fireball.name}!")

damage_dice = fireball.get_damage_effect(slot_level=3)

for goblin in goblins:
    # Jet de sauvegarde DEX
    save_successful = goblin.saving_throw(
        dc_type=fireball.dc['dc_type']['index'],
        dc_value=wizard.sc.dc_value
    )
    
    damage = damage_dice.roll()
    if save_successful:
        damage = damage // 2
        print(f"  {goblin.name} réussit son JdS: {damage} dégâts (réduits)")
    else:
        print(f"  {goblin.name} rate son JdS: {damage} dégâts")
    
    goblin.hit_points -= damage
    
    if goblin.is_dead:
        print(f"    {goblin.name} est vaincu!")
```

---

## Sorts par niveau

### Niveau 0 (Cantrips)
- `fire-bolt` - 1d10 feu
- `ray-of-frost` - 1d8 froid
- `sacred-flame` - 1d8 radiant
- `eldritch-blast` - 1d10 force

### Niveau 1
- `magic-missile` - 3×(1d4+1) force, toujours touche
- `cure-wounds` - 1d8 + mod soin
- `shield` - +5 CA (réaction)
- `burning-hands` - 3d6 feu (AOE)

### Niveau 2
- `scorching-ray` - 3×(2d6) feu
- `misty-step` - Téléportation 30 pieds
- `hold-person` - Paralysie

### Niveau 3
- `fireball` - 8d6 feu (AOE)
- `lightning-bolt` - 8d6 foudre (ligne)
- `counterspell` - Annule un sort

### Niveau 4+
- `wall-of-fire` (4) - 5d8 feu (mur)
- `cone-of-cold` (5) - 8d8 froid (cône)
- `chain-lightning` (6) - 10d8 foudre (multiple)
- `fireball` amélioré - +1d6 par niveau au-dessus de 3

---

## Voir aussi

- [entities](./entities.md) - Personnages lanceurs de sorts
- [combat](./combat.md) - Sorts en combat
- [mechanics](./mechanics.md) - Dés et calculs
- [data](./data.md) - Chargement de sorts

