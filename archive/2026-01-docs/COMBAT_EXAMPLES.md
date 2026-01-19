# Combat Examples - dnd-5e-core

Ce document contient des exemples complets de combat utilisant le package `dnd-5e-core`.

## Table des Matières

1. [Combat Simple avec Spellcasting](#combat-simple-avec-spellcasting)
2. [Combat avec Équipement](#combat-avec-équipement)
3. [Combat Spellcaster vs Spellcaster](#combat-spellcaster-vs-spellcaster)
4. [Combat avec Attaques Spéciales de Monstre](#combat-avec-attaques-spéciales)
5. [Formation de Groupe et Positionnement](#formation-de-groupe)

---

## Combat Simple avec Spellcasting

### Code Complet

```python
from dnd_5e_core import load_monster
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.combat import CombatSystem

# Créer un wizard
wizard = simple_character_generator(level=5, race_name='elf', class_name='wizard', name='Gandalf')

# Créer des guerriers pour le front
fighter1 = simple_character_generator(level=5, class_name='fighter', name='Conan')
fighter2 = simple_character_generator(level=5, class_name='fighter', name='Aragorn')
fighter3 = simple_character_generator(level=5, class_name='fighter', name='Beorn')

# Charger un monstre
ogre = load_monster('ogre')

# Formation: guerriers devant (0-2), wizard derrière (3) pour lancer des sorts
party = [fighter1, fighter2, fighter3, wizard]

print(f"📖 {wizard.name}'s Spells:")
if hasattr(wizard, 'sc') and wizard.sc:
    print(f"   Spells Known: {len(wizard.sc.learned_spells)}")
    print(f"   Spell Slots: {wizard.sc.spell_slots[1:6]}")
    for spell in wizard.sc.learned_spells[:5]:
        spell_type = "Cantrip" if spell.level == 0 else f"Level {spell.level}"
        print(f"      - {spell.name} ({spell_type})")

# Démarrer le combat
combat = CombatSystem(verbose=True)
alive_chars = [c for c in party if c.hit_points > 0]
alive_monsters = [ogre]

round_num = 1
max_rounds = 10

print(f"\n⚔️ Starting combat!")

while alive_chars and alive_monsters and round_num <= max_rounds:
    print(f"\n=== Round {round_num} ===")
    
    # Tours des personnages
    for char in alive_chars[:]:
        if not alive_monsters:
            break
        if char.hit_points <= 0:
            if char in alive_chars:
                alive_chars.remove(char)
            continue
        
        combat.character_turn(
            character=char,
            alive_chars=alive_chars,
            alive_monsters=alive_monsters,
            party=party
        )
    
    # Tours des monstres
    for monster in alive_monsters[:]:
        if not alive_chars:
            break
        if monster.hit_points <= 0:
            if monster in alive_monsters:
                alive_monsters.remove(monster)
            continue
        
        combat.monster_turn(
            monster=monster,
            alive_monsters=alive_monsters,
            alive_chars=alive_chars,
            party=party,
            round_num=round_num
        )
    
    round_num += 1

# Résultats
if alive_chars:
    print(f"\n✅ VICTORY!")
    if hasattr(wizard, 'sc') and wizard.sc:
        print(f"\n{wizard.name}'s Spell Usage:")
        print(f"   Spell Slots After:  {wizard.sc.spell_slots[1:6]}")
```

### Sortie Attendue

```
📖 Gandalf's Spells:
   Spells Known: 10
   Spell Slots: [4, 3, 2, 0, 0]
      - Fire Bolt (Cantrip)
      - Shocking Grasp (Cantrip)
      - Ice Storm (Level 4)
      - Black Tentacles (Level 4)
      - Scorching Ray (Level 2)

⚔️ Starting combat!

=== Round 1 ===
Conan attacks Ogre!
Conan punches Ogre for 2 hit points!
Aragorn attacks Ogre!
Aragorn punches Ogre for 1 hit points!
Beorn attacks Ogre!
Beorn punches Ogre for 1 hit points!
Gandalf attacks Ogre!
Gandalf CAST SPELL ** ICE STORM ** on Ogre
Ogre is hit for 18 hit points!
Ogre bludgeones Conan for 12 hit points!

=== Round 2 ===
...

✅ VICTORY!
Gandalf's Spell Usage:
   Spell Slots After: [4, 0, 0, 0, 0]
```

---

## Combat avec Équipement

### Code Complet

```python
from dnd_5e_core import load_monster
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.data import load_weapon, load_armor
from dnd_5e_core.combat import CombatSystem

# Créer des personnages
fighter1 = simple_character_generator(level=5, class_name='fighter', name='Conan')
fighter2 = simple_character_generator(level=5, class_name='fighter', name='Aragorn')
fighter3 = simple_character_generator(level=5, class_name='fighter', name='Beorn')
wizard = simple_character_generator(level=5, class_name='wizard', name='Gandalf')

# Charger les équipements
longsword = load_weapon("longsword")
battleaxe = load_weapon("battleaxe")
greatsword = load_weapon("greatsword")

chain_mail = load_armor("chain-mail")
scale_mail = load_armor("scale-mail")
ring_mail = load_armor("ring-mail")

# Équiper Fighter1 avec longsword et chain mail
if fighter1.inventory and longsword:
    for i, item in enumerate(fighter1.inventory):
        if item is None:
            fighter1.inventory[i] = longsword
            break
    fighter1.equip(longsword)
    
if fighter1.inventory and chain_mail:
    for i, item in enumerate(fighter1.inventory):
        if item is None:
            fighter1.inventory[i] = chain_mail
            break
    fighter1.equip(chain_mail)
    print(f"✅ {fighter1.name}: {longsword.name} + {chain_mail.name} (AC {chain_mail.armor_class['base']})")

# Équiper Fighter2
if fighter2.inventory and battleaxe:
    for i, item in enumerate(fighter2.inventory):
        if item is None:
            fighter2.inventory[i] = battleaxe
            break
    fighter2.equip(battleaxe)

if fighter2.inventory and scale_mail:
    for i, item in enumerate(fighter2.inventory):
        if item is None:
            fighter2.inventory[i] = scale_mail
            break
    fighter2.equip(scale_mail)
    print(f"✅ {fighter2.name}: {battleaxe.name} + {scale_mail.name} (AC {scale_mail.armor_class['base']})")

# Équiper Fighter3
if fighter3.inventory and greatsword:
    for i, item in enumerate(fighter3.inventory):
        if item is None:
            fighter3.inventory[i] = greatsword
            break
    fighter3.equip(greatsword)

if fighter3.inventory and ring_mail:
    for i, item in enumerate(fighter3.inventory):
        if item is None:
            fighter3.inventory[i] = ring_mail
            break
    fighter3.equip(ring_mail)
    print(f"✅ {fighter3.name}: {greatsword.name} + {ring_mail.name} (AC {ring_mail.armor_class['base']})")

# Charger monstre
ogre = load_monster('ogre')

# Formation de groupe
party = [fighter1, fighter2, fighter3, wizard]

# Combat (même code que précédemment)
# ...
```

### Sortie Attendue

```
✅ Conan: Longsword + Chain Mail (AC 16)
✅ Aragorn: Battleaxe + Scale Mail (AC 14)
✅ Beorn: Greatsword + Ring Mail (AC 14)

=== Round 1 ===
Conan attacks Ogre!
Conan slashes Ogre for 5 hit points!     ← Utilise l'épée longue!
Aragorn attacks Ogre!
Aragorn slashes Ogre for 6 hit points!   ← Utilise la hache!
Beorn attacks Ogre!
Beorn slashes Ogre for 10 hit points!    ← Utilise la grande épée!
Gandalf CAST SPELL ** ICE STORM ** on Ogre
Ogre is hit for 18 hit points!
Ogre bludgeones Conan for 7 hit points!  ← Dégâts réduits grâce à l'armure AC 16
```

**Différence Notable:**
- Sans équipement: "punches" pour 1-2 dégâts
- Avec équipement: "slashes" pour 5-10 dégâts
- AC amélioré: 10 → 14-16

---

## Combat Spellcaster vs Spellcaster

### Code Complet

```python
from dnd_5e_core import load_monster
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.combat import CombatSystem

# Créer deux wizards
wizard = simple_character_generator(level=5, class_name='wizard', name='Gandalf')

# Charger un monstre lanceur de sorts
mage = load_monster('mage')

print(f"✨ {wizard.name} (Player)")
if hasattr(wizard, 'sc') and wizard.sc:
    print(f"   Spells: {len(wizard.sc.learned_spells)}")

print(f"\n✨ {mage.name} (Monster)")
if hasattr(mage, 'is_spell_caster') and mage.is_spell_caster:
    print(f"   Spellcaster: Yes")
    if hasattr(mage, 'sc'):
        print(f"   Spells: {len(mage.sc.learned_spells)}")

# Ajouter des gardes pour mettre les wizards en position arrière
guard1 = simple_character_generator(level=5, class_name='fighter', name='Guard1')
guard2 = simple_character_generator(level=5, class_name='fighter', name='Guard2')
guard3 = simple_character_generator(level=5, class_name='fighter', name='Guard3')

party = [guard1, guard2, guard3, wizard]
monsters = [mage]

# Combat
combat = CombatSystem(verbose=True)
alive_chars = [c for c in party if c.hit_points > 0]
alive_monsters = monsters.copy()

round_num = 1
while alive_chars and alive_monsters and round_num <= 10:
    print(f"\n=== Round {round_num} ===")
    
    for char in alive_chars[:]:
        if not alive_monsters:
            break
        combat.character_turn(char, alive_chars, alive_monsters, party)
    
    for monster in alive_monsters[:]:
        if not alive_chars:
            break
        combat.monster_turn(monster, alive_monsters, alive_chars, party, round_num)
    
    round_num += 1
```

### Sortie Attendue

```
✨ Gandalf (Player)
   Spells: 10

✨ Mage (Monster)
   Spellcaster: Yes
   Spells: 16

=== Round 1 ===
Guard1 attacks Mage!
Guard1 punches Mage for 2 hit points!
Guard2 attacks Mage!
Guard2 punches Mage for 1 hit points!
Guard3 attacks Mage!
Guard3 punches Mage for 1 hit points!
Gandalf attacks Mage!
Gandalf CAST SPELL ** BLACK TENTACLES ** on Mage
Mage is hit for 12 hit points!
Mage casts CONE OF COLD on Gandalf!      ← Le Mage riposte avec un sort!
Gandalf is hit for 27 hit points!
```

---

## Combat avec Attaques Spéciales

### Code Complet

```python
from dnd_5e_core import load_monster
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.combat import CombatSystem

# Créer un groupe
party = [
    simple_character_generator(level=5, class_name='fighter', name='Tank1'),
    simple_character_generator(level=5, class_name='fighter', name='Tank2'),
    simple_character_generator(level=5, class_name='fighter', name='Tank3'),
    simple_character_generator(level=5, class_name='wizard', name='Merlin')
]

# Charger un monstre avec attaques spéciales
try:
    dragon = load_monster('young-red-dragon')
    print(f"✨ Loaded: {dragon.name}")
    
    if hasattr(dragon, 'sa') and dragon.sa:
        print(f"   Special Attacks: {[sa.name for sa in dragon.sa]}")
        # Sortie: Multi-attack, Breath Weapon
except:
    dragon = load_monster('ogre')

# Combat
combat = CombatSystem(verbose=True)
alive_chars = [c for c in party if c.hit_points > 0]
alive_monsters = [dragon]

round_num = 1
while alive_chars and alive_monsters and round_num <= 5:
    print(f"\n=== Round {round_num} ===")
    
    for char in alive_chars[:]:
        if not alive_monsters:
            break
        combat.character_turn(char, alive_chars, alive_monsters, party)
    
    for monster in alive_monsters[:]:
        if not alive_chars:
            break
        combat.monster_turn(monster, alive_monsters, alive_chars, party, round_num)
    
    round_num += 1
```

### Sortie Attendue

```
✨ Loaded: Young Red Dragon
   Special Attacks: ['Multi-attack', 'Breath Weapon']

=== Round 1 ===
Tank1 attacks Young Red Dragon!
Tank1 punches Young Red Dragon for 1 hit points!
Tank2 attacks Young Red Dragon!
Tank2 punches Young Red Dragon for 2 hit points!
Tank3 attacks Young Red Dragon!
Tank3 punches Young Red Dragon for 1 hit points!
Merlin attacks Young Red Dragon!
Merlin CAST SPELL ** FIRE BOLT ** on Young Red Dragon
Young Red Dragon is hit for 8 hit points!
Young Red Dragon multi-attacks Tank1!           ← Multi-attaque spéciale!
Young Red Dragon pierces Tank1 for 23 hit points!
Young Red Dragon slashes Tank1 for 16 hit points!
Young Red Dragon slashes Tank1 for 13 hit points!
Tank1 is KILLED!
```

---

## Formation de Groupe et Positionnement

### ⚠️ IMPORTANT: Positionnement pour Spellcasting

Les personnages en positions **0-2** sont considérés en **mêlée** (front)
Les personnages en positions **3+** sont considérés en **distance** (arrière)

**Les wizards et autres lanceurs de sorts DOIVENT être en positions 3+ pour lancer des sorts!**

### ✅ Formation Correcte

```python
# Formation correcte - Le wizard lance des sorts
fighter1 = simple_character_generator(level=5, class_name='fighter')
fighter2 = simple_character_generator(level=5, class_name='fighter')
fighter3 = simple_character_generator(level=5, class_name='fighter')
wizard = simple_character_generator(level=5, class_name='wizard')

party = [fighter1, fighter2, fighter3, wizard]
#        Position:  0         1         2         3 (arrière)

print("Party formation:")
for i, char in enumerate(party):
    position = "Front (Melee)" if i < 3 else "Back (Ranged/Spells)"
    print(f"  [{i}] {char.name}: {position}")

# Sortie:
# [0] Fighter1: Front (Melee)
# [1] Fighter2: Front (Melee)
# [2] Fighter3: Front (Melee)
# [3] Wizard: Back (Ranged/Spells) ← Lance des sorts!
```

### ❌ Formation Incorrecte

```python
# Formation incorrecte - Le wizard n'est PAS en position arrière
wizard = simple_character_generator(level=5, class_name='wizard')
party = [wizard]
#        Position: 0 (mêlée)

# Résultat: Le wizard attaquera au corps-à-corps au lieu de lancer des sorts!
# Sortie: "Wizard punches Ogre for 1 hit points!" ← Pas de sorts!
```

### Formation de Groupe Recommandée

```python
# Groupe équilibré de 4-6 personnages
def create_balanced_party():
    # Front row (tanks/mêlée)
    tank1 = simple_character_generator(level=5, class_name='fighter', name='Tank1')
    tank2 = simple_character_generator(level=5, class_name='fighter', name='Tank2')
    tank3 = simple_character_generator(level=5, class_name='cleric', name='Healer')
    
    # Back row (distance/sorts)
    wizard = simple_character_generator(level=5, class_name='wizard', name='Mage')
    ranger = simple_character_generator(level=5, class_name='ranger', name='Archer')
    
    party = [tank1, tank2, tank3, wizard, ranger]
    
    print("⚔️ Party Formation:")
    print(f"   Front Row: {tank1.name}, {tank2.name}, {tank3.name}")
    print(f"   Back Row: {wizard.name}, {ranger.name}")
    
    return party

party = create_balanced_party()
```

---

## Fonctionnalités du Système de Combat

### Le `CombatSystem` gère automatiquement:

1. **🔮 Spellcasting des Personnages**
   - Sélection automatique des sorts
   - Consommation des emplacements de sorts
   - Cantrips et sorts à emplacements

2. **👹 Spellcasting des Monstres**
   - Les monstres lanceurs (Mage, Lich, etc.) utilisent leurs sorts
   - Jets de sauvegarde calculés automatiquement

3. **⚔️ Attaques d'Armes**
   - Utilise les armes équipées
   - Calcule les dégâts selon les dés
   - Multi-attaques gérées

4. **🎯 Attaques Spéciales**
   - Souffle de dragon
   - Multi-attaques
   - Capacités de monstre

5. **🩹 Soins Automatiques**
   - Les personnages soignent les alliés blessés
   - Utilisation de potions quand HP bas
   - Sorts de soin priorisés

6. **📊 Intelligence Tactique**
   - Priorité: Soins → Potions → Sorts → Attaques Spéciales → Armes
   - Sélection de cible intelligente
   - Gestion des conditions (restraint, etc.)

---

## Résumé

✅ **Utilisez `simple_character_generator()`** pour créer des personnages rapidement
✅ **Positionnez les lanceurs de sorts en position 3+** dans le groupe
✅ **Équipez armes et armures** pour de meilleurs combats
✅ **Le `CombatSystem` gère tout** - sorts, attaques spéciales, soins
✅ **verbose=True** pour voir tous les détails du combat

Pour plus d'exemples, consultez le projet [DnD5e-Test](https://github.com/codingame-team/DND5e-Test).

