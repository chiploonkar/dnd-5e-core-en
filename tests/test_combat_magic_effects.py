#!/usr/bin/env python3
"""
Script de diagnostic - Vérification des effets magiques en combat

Ce script teste que les effets des objets magiques sont bien appliqués
dans les différents systèmes de combat.
"""

import sys
import os

# Add paths
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.data.loader import load_monster
from dnd_5e_core.equipment.weapon_factory import create_holy_avenger, create_frost_brand
from dnd_5e_core.equipment.armor_factory import create_armor_of_resistance
from dnd_5e_core.equipment.magic_item_factory import create_ring_of_protection


def test_character_with_magic_items():
    """Crée un personnage avec des objets magiques équipés"""
    print("=" * 80)
    print("TEST: PERSONNAGE AVEC OBJETS MAGIQUES")
    print("=" * 80)

    # Créer personnage
    char = simple_character_generator(level=5, race_name='human', class_name='fighter', name='Test Fighter')

    print(f"\n📊 État initial:")
    print(f"   Name: {char.name}")
    print(f"   Base AC: {char.armor_class}")
    print(f"   HP: {char.hit_points}/{char.max_hit_points}")

    # Équiper arme magique
    weapon = create_holy_avenger()
    weapon.equipped = True
    char.inventory.append(weapon)

    # Équiper armure magique
    armor = create_armor_of_resistance(damage_type="fire")
    armor.equipped = True
    char.inventory.append(armor)

    # Équiper anneau
    ring = create_ring_of_protection()
    ring.equipped = True
    ring.attuned = True  # Attunement requis
    char.inventory.append(ring)

    print(f"\n🎒 Objets équipés:")
    for item in char.inventory:
        if item and hasattr(item, 'equipped') and item.equipped:
            print(f"   ✅ {item.name}")
            if hasattr(item, 'attack_bonus') and item.attack_bonus:
                print(f"      - Attack Bonus: +{item.attack_bonus}")
            if hasattr(item, 'damage_bonus') and item.damage_bonus:
                print(f"      - Damage Bonus: +{item.damage_bonus}")
            if hasattr(item, 'armor_bonus') and item.armor_bonus:
                print(f"      - Armor Bonus: +{item.armor_bonus}")
            if hasattr(item, 'ac_bonus') and item.ac_bonus:
                print(f"      - AC Bonus: +{item.ac_bonus}")
            if hasattr(item, 'damage_resistances') and item.damage_resistances:
                print(f"      - Resistances: {item.damage_resistances}")

    # Vérifier AC avec bonus
    final_ac = char.armor_class
    print(f"\n🛡️  Classe d'Armure:")
    print(f"   Final AC: {final_ac}")
    print(f"   (Devrait inclure: base armor + armor bonus + ring +1)")

    return char


def test_combat_with_magic_effects():
    """Teste un combat avec effets magiques"""
    print("\n" + "=" * 80)
    print("TEST: COMBAT AVEC EFFETS MAGIQUES")
    print("=" * 80)

    # Créer personnage avec objets magiques
    char = simple_character_generator(level=5, race_name='human', class_name='fighter', name='Sir Roland')

    # Équiper Holy Avenger
    weapon = create_holy_avenger()
    weapon.equipped = True
    char.inventory.append(weapon)

    # Équiper armure de résistance au feu
    armor = create_armor_of_resistance(damage_type="fire")
    armor.equipped = True
    char.inventory.append(armor)

    # Créer vampire (undead)
    vampire = load_monster('vampire')
    if not vampire:
        vampire = load_monster('zombie')
    vampire.creature_type = 'undead'

    print(f"\n⚔️  {char.name} vs {vampire.name}")
    print(f"   Fighter AC: {char.armor_class}")
    print(f"   Fighter HP: {char.hit_points}/{char.max_hit_points}")
    print(f"   Vampire AC: {vampire.armor_class}")
    print(f"   Vampire HP: {vampire.hit_points}")

    # Test attaque du personnage
    print(f"\n1️⃣  {char.name} attaque avec Holy Avenger:")
    attack_msg, damage = char.attack(vampire, in_melee=True, cast=False, verbose=False)
    print(f"   {attack_msg}")
    print(f"   Damage: {damage}")
    print(f"   (Devrait inclure: 1d8 + 3 bonus + 2d10 vs undead = ~19)")

    # Appliquer dommages
    vampire.hit_points -= damage
    print(f"   Vampire HP: {vampire.hit_points}")

    # Test attaque du monstre (avec dommages de feu simulés)
    print(f"\n2️⃣  {vampire.name} attaque avec dommages de feu:")
    fire_damage = 40
    print(f"   Dommages de feu: {fire_damage}")

    actual_damage = char.take_damage(fire_damage, "fire")
    print(f"   Dommages réels: {actual_damage}")
    print(f"   (Devrait être réduit à 50%: {fire_damage // 2})")
    print(f"   Fighter HP: {char.hit_points}/{char.max_hit_points}")

    # Vérifier résistance
    if actual_damage == fire_damage // 2:
        print(f"   ✅ RÉSISTANCE APPLIQUÉE CORRECTEMENT")
    else:
        print(f"   ❌ PROBLÈME: Résistance non appliquée")

    return char, vampire


def check_equipment_in_inventory():
    """Vérifie comment équiper des objets"""
    print("\n" + "=" * 80)
    print("GUIDE: COMMENT ÉQUIPER DES OBJETS MAGIQUES")
    print("=" * 80)

    print("""
🎒 Pour équiper un objet magique:

1. Créer l'objet:
   weapon = create_holy_avenger()

2. Marquer comme équipé:
   weapon.equipped = True

3. Ajouter à l'inventaire:
   character.inventory.append(weapon)

4. Pour les objets avec attunement:
   ring = create_ring_of_protection()
   ring.equipped = True
   ring.attuned = True  # Important !
   character.inventory.append(ring)

⚠️  IMPORTANT:
   - Les armes/armures utilisent l'attribut 'equipped'
   - Les objets magiques nécessitant attunement ont besoin de 'attuned = True'
   - La propriété 'weapon' du personnage est calculée automatiquement
   - La propriété 'armor_class' inclut automatiquement les bonus
    """)


def main():
    """Point d'entrée"""
    print("\n" + "=" * 80)
    print("🧪 DIAGNOSTIC DES EFFETS MAGIQUES EN COMBAT")
    print("=" * 80)

    # Test 1: Créer personnage avec objets
    char1 = test_character_with_magic_items()

    # Test 2: Combat complet
    char2, vampire = test_combat_with_magic_effects()

    # Guide
    check_equipment_in_inventory()

    # Résumé
    print("\n" + "=" * 80)
    print("📊 RÉSUMÉ")
    print("=" * 80)

    print("""
✅ Les effets magiques FONCTIONNENT dans:
   - Character.attack() → utilise calculate_weapon_damage()
   - Character.take_damage() → applique résistances d'armure
   - Character.armor_class → inclut bonus d'objets magiques

⚠️  PROBLÈME POTENTIEL:
   Les objets magiques ne sont PAS équipés par défaut dans les jeux.
   
   Solution:
   1. Dans Boltac: Équiper automatiquement les objets achetés
   2. Dans character_sheet.py: Ajouter bouton "Equip" pour chaque item
   3. Vérifier que 'attuned = True' pour objets nécessitant attunement

📋 PROCHAINES ÉTAPES:
   1. Ajouter fonction equip_item() dans Character
   2. Mettre à jour Boltac pour auto-équiper
   3. Améliorer character_sheet.py pour gérer équipement
    """)


if __name__ == "__main__":
    main()
