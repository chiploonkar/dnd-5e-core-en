# 📚 dnd-5e-core - Documentation Complète

## Vue d'Ensemble

`dnd-5e-core` est un package Python complet implémentant les règles de Donjons & Dragons 5ème édition, incluant :

- ✅ Système de combat complet avec conditions
- ✅ Gestion des personnages et monstres
- ✅ Système de sorts et spellcasting
- ✅ Équipement et objets magiques
- ✅ **Progression des classes par niveau (1-20)** ✨ NOUVEAU
- ✅ Système d'initiative
- ✅ Calcul automatique des rencontres

---

## 🚀 Installation

```bash
pip install dnd-5e-core
```

Ou depuis les sources :

```bash
cd dnd-5e-core
pip install -e .
```

---

## 📖 Guide de Démarrage Rapide

### 1. Créer un Personnage

```python
from dnd_5e_core.data.loaders import simple_character_generator

# Créer un wizard niveau 5
gandalf = simple_character_generator(
    level=5,
    race_name='elf',
    class_name='wizard',
    name='Gandalf'
)

print(f"{gandalf.name}: Niveau {gandalf.level} {gandalf.class_type.name}")
print(f"HP: {gandalf.hit_points}/{gandalf.max_hit_points}")
print(f"AC: {gandalf.armor_class}")

# Les spell slots sont automatiquement configurés !
if gandalf.sc:
    print(f"Spell slots: {gandalf.sc.spell_slots[1:6]}")
    # Affiche: [4, 3, 2, 0, 0] pour un wizard niveau 5
```

### 2. Faire Monter un Personnage de Niveau

```python
from dnd_5e_core.data.loaders import level_up_character

# Faire passer au niveau 6
gandalf = level_up_character(gandalf, 6, verbose=True)

# Affichera:
# 🎉 Gandalf passe du niveau 5 au niveau 6!
#    ❤️  HP: +5 (38 total)
#    🔮 Spell slots mis à jour
#    ✨ Nouvelles features:
#       - [features du niveau 6]
```

### 3. Charger un Monstre

```python
from dnd_5e_core import load_monster

# Charger un monstre avec ses capacités
dragon = load_monster('adult-red-dragon')

print(f"{dragon.name}: CR {dragon.challenge_rating}")
print(f"HP: {dragon.hit_points}, AC: {dragon.armor_class}")

# Afficher les actions avec conditions
for action in dragon.actions:
    if hasattr(action, 'effects') and action.effects:
        print(f"  {action.name}: {[e.name for e in action.effects]}")
```

### 4. Combat Complet

```python
from dnd_5e_core.combat import CombatSystem

# Créer le système de combat
combat = CombatSystem(verbose=True)

# Groupe et monstres
party = [gandalf, conan, gimli, bilbo]
monsters = [dragon, goblin1, goblin2]

# Initiative (comme dans main.py)
from random import randint

initiative_order = []
for char in party:
    dex_mod = char.abilities.get_modifier('dex')
    roll = randint(1, 20) + dex_mod
    initiative_order.append((char, roll))

for monster in monsters:
    dex_mod = monster.abilities.get_modifier('dex')
    roll = randint(1, 20) + dex_mod
    initiative_order.append((monster, roll))

initiative_order.sort(key=lambda x: x[1], reverse=True)
combatants = [c for c, _ in initiative_order]

# Combat round par round
for combatant in combatants:
    if combatant in party:
        combat.character_turn(combatant, party, monsters, party)
    else:
        combat.monster_turn(combatant, monsters, party, party, round_num=1)
```

---

## 🎓 Fonctionnalités Avancées

### Système de Progression par Niveau

Le package inclut maintenant un système complet de progression utilisant les données officielles de l'API D&D 5e.

#### Charger la Progression d'une Classe

```python
from dnd_5e_core.data.progression_loader import load_class_progression

wizard_prog = load_class_progression('wizard')

# Obtenir les infos pour le niveau 5
level_5 = wizard_prog.get_level(5)

print(f"Bonus de maîtrise: +{level_5.prof_bonus}")
print(f"Features: {[f.name for f in level_5.features]}")
print(f"Spell slots: {level_5.spellcasting.spell_slots}")
```

#### Récupérer les Spell Slots

```python
from dnd_5e_core.data.progression_loader import get_spell_slots_for_level

# Pour un Cleric niveau 7
slots = get_spell_slots_for_level('cleric', 7)
# Retourne: [0, 4, 3, 3, 1, 0, 0, 0, 0, 0]
#              ^  L1 L2 L3 L4
```

#### Features Spécifiques aux Classes

```python
from dnd_5e_core.data.progression_loader import get_class_specific_value

# Barbarian - Nombre de rages au niveau 5
rage_count = get_class_specific_value('barbarian', 5, 'rage_count')
# Retourne: 3

# Monk - Ki points au niveau 8
ki_points = get_class_specific_value('monk', 8, 'ki_points')
# Retourne: 8

# Rogue - Dés d'attaque sournoise au niveau 7
sneak_attack = get_class_specific_value('rogue', 7, 'sneak_attack')
# Retourne: {'dice_count': 4, 'dice_value': 6} (4d6)
```

### Sorts de Défense et d'Attaque

```python
# Shield (+5 AC temporaire)
from dnd_5e_core.combat import cast_shield
cast_shield(wizard)

# Hold Person (paralyser un humanoïde)
from dnd_5e_core.combat import cast_hold_person, create_paralyzed_condition
cast_hold_person(wizard, ghoul)  # Paralyse le ghoul si JS raté
```

### Objets Magiques

```python
from dnd_5e_core.equipment import (
    create_ring_of_protection,
    create_wand_of_paralysis,
    HealingPotion,
    PotionRarity
)

# Anneau de protection (+1 AC, +1 saves)
ring = create_ring_of_protection()
ring.attune(gandalf)
ring.apply_to_character(gandalf)

# Baguette de paralysie
wand = create_wand_of_paralysis()
# 3 charges par jour

# Potion de soin
potion = HealingPotion("Potion of Healing", PotionRarity.COMMON, "2d4", 2, 50, 50)
# Soigne 2d4+2 HP
```

### Système de Conditions

```python
from dnd_5e_core.combat import (
    create_paralyzed_condition,
    create_restrained_condition,
    create_poisoned_condition
)

# Appliquer une condition à un personnage
poisoned = create_poisoned_condition(dc_value=13, dc_type=AbilityType.CON)
poisoned.apply_to_character(conan)

# Appliquer une condition à un monstre
paralyzed = create_paralyzed_condition(dc_value=15, dc_type=AbilityType.WIS)
paralyzed.apply_to_monster(goblin)

# Tenter de se libérer
if poisoned.attempt_save(conan):
    print(f"{conan.name} se libère de la condition!")
```

### Génération de Rencontres

```python
from dnd_5e_core.mechanics.encounter_builder import select_monsters_by_encounter_table
from dnd_5e_core.data.collections import load_all_monsters

# Charger tous les monstres
all_monsters = load_all_monsters()

# Générer une rencontre pour un groupe niveau 5
monsters, encounter_type = select_monsters_by_encounter_table(
    encounter_level=5,
    available_monsters=all_monsters,
    allow_pairs=True
)

print(f"Type: {encounter_type}")
print(f"Monstres: {[m.name for m in monsters]}")
```

---

## 📊 Classes Supportées

Toutes les 12 classes officielles D&D 5e sont supportées avec progression complète :

| Classe | Hit Die | Spellcaster | Features Spéciales |
|--------|---------|-------------|-------------------|
| **Barbarian** | d12 | Non | Rage, Brutal Critical |
| **Bard** | d8 | Full | Bardic Inspiration |
| **Cleric** | d8 | Full | Channel Divinity |
| **Druid** | d8 | Full | Wild Shape |
| **Fighter** | d10 | Non | Action Surge, Extra Attack |
| **Monk** | d8 | Non | Ki Points, Martial Arts |
| **Paladin** | d10 | Half | Lay on Hands, Smite |
| **Ranger** | d10 | Half | Favored Enemy, Hunter's Mark |
| **Rogue** | d8 | Non | Sneak Attack, Cunning Action |
| **Sorcerer** | d6 | Full | Sorcery Points, Metamagic |
| **Warlock** | d8 | Pact | Eldritch Invocations |
| **Wizard** | d6 | Full | Arcane Recovery, Spellbook |

---

## 🎮 Exemples Complets

### Exemple 1: Création et Progression d'un Personnage

```python
from dnd_5e_core.data.loaders import simple_character_generator, level_up_character

# Créer un Fighter niveau 1
fighter = simple_character_generator(1, 'human', 'fighter', 'Conan')
print(f"{fighter.name}: {fighter.hit_points} HP, AC {fighter.armor_class}")

# Faire monter de niveau
for level in range(2, 6):
    fighter = level_up_character(fighter, level, verbose=True)

# Fighter niveau 5 avec Extra Attack
print(f"Final: {fighter.name} niveau {fighter.level}")
```

### Exemple 2: Combat avec Conditions

```python
# Voir: test_complete_combat_v4.py
# Script complet démontrant:
# - Initiative
# - Sorts de défense (Shield, Mage Armor)
# - Sorts d'attaque (Hold Person, Entangle)
# - Conditions bidirectionnelles (personnages ↔ monstres)
# - Objets magiques
# - Potions de soin
```

### Exemple 3: Progression Automatique

```python
# Voir: demo_progression_integration.py
# Démonstration de:
# - Création avec spell slots automatiques
# - Level up avec features
# - Test de toutes les classes
```

---

## 📚 Documentation de l'API

### Modules Principaux

- `dnd_5e_core.entities` - Character, Monster, Sprite
- `dnd_5e_core.combat` - CombatSystem, Conditions
- `dnd_5e_core.equipment` - Weapons, Armor, Magic Items, Potions
- `dnd_5e_core.spells` - Spell, SpellCaster
- `dnd_5e_core.mechanics` - Dice, Encounter Builder, Class Progression
- `dnd_5e_core.data` - Loaders pour les données

### Documentation Détaillée

- **CLASS_PROGRESSION_SYSTEM.md** - Système de progression des classes
- **COMBAT_V4_GUIDE.md** - Guide du système de combat v4.0
- **ENCOUNTER_BUILDER_IMPROVEMENTS.md** - Système de rencontres
- **CONDITIONS_SYSTEM.md** - Système de conditions

---

## 🛠️ Scripts Utiles

### Télécharger les Données de Progression

```bash
cd dnd-5e-core
python download_class_progression.py
```

### Tester le Système de Progression

```bash
python test_class_progression.py
```

### Démo d'Intégration

```bash
python demo_progression_integration.py
```

### Test de Combat Complet

```bash
cd ../DnD5e-Scenarios
python test_complete_combat_v4.py
```

---

## 📝 Changelog

### v0.2.5 (Janvier 2026) - Système de Progression ✨

**Nouvelles Fonctionnalités** :
- ✨ Système complet de progression des classes (niveaux 1-20)
- ✨ Spell slots basés sur les données officielles de l'API
- ✨ Features de classe par niveau
- ✨ Fonction `level_up_character()` automatique
- ✨ Support des class-specific features (rage, ki, sneak attack, etc.)
- ✨ Intégration dans `simple_character_generator()`

**Améliorations** :
- 📈 Spell slots calculés dynamiquement depuis l'API
- 📈 Bonus de maîtrise corrects par niveau
- 📈 HP gains basés sur le hit die de la classe

### v0.2.4 (Janvier 2026) - Combat Avancé

**Fonctionnalités** :
- ⚔️ Système d'initiative (1d20 + DEX)
- ⚔️ Armes magiques avec bonus
- 🛡️ Sorts de défense (Shield, Mage Armor)
- ⚡ Sorts affectant les monstres (Hold Person, Entangle)
- 🔴 Conditions bidirectionnelles (personnages ↔ monstres)
- 💊 Objets magiques et potions de soin

---

## 🤝 Contribution

Pour contribuer au projet :

1. Fork le repository
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

## 🙏 Remerciements

- **D&D 5e API** : https://www.dnd5eapi.co
- **Wizards of the Coast** : Pour D&D 5e SRD
- **Contributeurs** : Merci à tous ceux qui ont contribué !

---

## 📧 Contact

Pour toute question ou suggestion :
- GitHub Issues : https://github.com/votre-repo/dnd-5e-core/issues
- Documentation : https://github.com/votre-repo/dnd-5e-core/wiki

---

**Version** : 0.2.5  
**Date** : 18 Janvier 2026  
**Status** : ✅ Production Ready

🎲 Bon jeu ! ⚔️🐉✨
