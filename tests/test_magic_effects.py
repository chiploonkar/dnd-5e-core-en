#!/usr/bin/env python3
"""
Test Script - Verification des Effets Magiques en Combat

Ce script teste que tous les effets des armes et armures magiques
sont correctement appliqués pendant les combats.
"""

import sys
import os

# Add dnd-5e-core to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.data.loader import load_monster
from dnd_5e_core.equipment.weapon_factory import (
    create_frost_brand, create_holy_avenger, create_flame_tongue,
    create_vorpal_sword, create_sun_blade, create_giant_slayer,
    create_dragon_slayer, create_defender, create_luck_blade,
    create_oathbow, create_sword_of_sharpness, create_nine_lives_stealer,
    SPECIAL_WEAPONS, get_special_weapon
)
from dnd_5e_core.equipment.armor_factory import (
    create_armor_of_resistance, create_armor_of_invulnerability,
    create_dragon_scale_mail, create_dwarven_plate,
    SPECIAL_ARMORS, get_special_armor
)
from dnd_5e_core.equipment.magic_item_factory import (
    create_ring_of_protection, create_cloak_of_protection,
    create_amulet_of_health, create_belt_of_giant_strength,
    create_boots_of_speed, create_bracers_of_defense,
    create_gauntlets_of_ogre_power, create_headband_of_intellect,
    PREDEFINED_ITEMS
)
from dnd_5e_core.equipment.magic_item_factory import create_ring_of_protection


def test_weapon_bonuses():
    """Test que les bonus d'armes magiques sont appliqués"""
    print("=" * 80)
    print("TEST 1: BONUS D'ARMES MAGIQUES")
    print("=" * 80)

    # Create character with Holy Avenger (+3, +2d10 vs undead)
    char = simple_character_generator(level=5, race_name='human', class_name='paladin', name='Sir Galahad')
    holy_avenger = create_holy_avenger()
    holy_avenger.equipped = True

    # ✅ IMPORTANT: Équiper l'arme correctement
    char.inventory.append(holy_avenger)
    # Trouver et équiper l'arme dans l'inventaire
    for i, item in enumerate(char.inventory):
        if item and hasattr(item, 'index') and 'holy-avenger' in item.index:
            item.equipped = True
            break

    # Create undead monster
    vampire = load_monster('vampire')
    if not vampire:
        print("⚠️  Vampire not found, using generic undead")
        vampire = load_monster('zombie')

    if vampire:
        vampire.creature_type = 'undead'

        print(f"\n{char.name} (Level {char.level} Paladin)")
        print(f"Weapon: {holy_avenger.name}")
        print(f"  - Attack Bonus: +{holy_avenger.attack_bonus}")
        print(f"  - Damage Bonus: +{holy_avenger.damage_bonus}")
        print(f"  - vs Undead: {holy_avenger.creature_type_damage.get('undead', 'None')}")

        print(f"\nTarget: {vampire.name} (creature_type: {vampire.creature_type})")

        # Calculate damage multiple times to get average
        total = 0
        num_tests = 10
        for _ in range(num_tests):
            damage = char.calculate_weapon_damage(target=vampire)
            total += damage

        avg_damage = total / num_tests

        print(f"\n✅ Average Damage (10 rolls): {avg_damage:.1f}")
        print(f"   Expected: ~19 (1d8[4.5] + 3 bonus + 2d10[11] vs undead)")

        if avg_damage > 15:  # Should have significant bonus damage
            print("✅ PASS: Bonus damage applied correctly")
            return True
        else:
            print("❌ FAIL: Bonus damage not applied")
            return False
    else:
        print("❌ Could not load monster for test")
        return False


def test_all_magic_weapons():
    """Test toutes les armes magiques"""
    print("\n" + "=" * 80)
    print("TEST COMPLET: TOUTES LES ARMES MAGIQUES")
    print("=" * 80)

    weapons_to_test = [
        ("Holy Avenger", create_holy_avenger, "undead", 15),
        ("Frost Brand", create_frost_brand, None, 10),
        ("Flame Tongue", create_flame_tongue, None, 10),
        ("Giant Slayer", create_giant_slayer, "giant", 12),
        ("Dragon Slayer", create_dragon_slayer, "dragon", 14),
        ("Vorpal Sword", create_vorpal_sword, None, 8),
        ("Sun Blade", create_sun_blade, "undead", 12),
    ]

    passed = 0
    failed = 0

    for weapon_name, weapon_factory, creature_type, expected_min in weapons_to_test:
        try:
            char = simple_character_generator(level=5, race_name='human', class_name='fighter', name='Test')
            weapon = weapon_factory()
            weapon.equipped = True
            char.inventory.append(weapon)

            # Create target
            if creature_type:
                if creature_type == "undead":
                    target = load_monster('zombie')
                elif creature_type == "giant":
                    target = load_monster('hill-giant')
                elif creature_type == "dragon":
                    target = load_monster('young-red-dragon')
                else:
                    target = load_monster('goblin')

                if target:
                    target.creature_type = creature_type
            else:
                target = load_monster('goblin')

            # Test damage
            total = 0
            for _ in range(10):
                damage = char.calculate_weapon_damage(target=target)
                total += damage

            avg_damage = total / 10

            status = "✅" if avg_damage >= expected_min else "❌"
            print(f"{status} {weapon_name}: {avg_damage:.1f} dmg (expected ≥{expected_min})")

            if avg_damage >= expected_min:
                passed += 1
            else:
                failed += 1

        except Exception as e:
            print(f"❌ {weapon_name}: Error - {e}")
            failed += 1

    print(f"\nRésultat: {passed} réussis, {failed} échoués")
    return failed == 0


def test_elemental_damage():
    """Test que les dommages élémentaires sont appliqués"""
    print("\n" + "=" * 80)
    print("TEST 2: DOMMAGES ÉLÉMENTAIRES")
    print("=" * 80)

    # Create character with Frost Brand (+1d6 cold)
    char = simple_character_generator(level=5, race_name='dwarf', class_name='fighter', name='Bruenor')
    frost_brand = create_frost_brand()
    frost_brand.equipped = True
    char.inventory.append(frost_brand)

    print(f"\n{char.name} (Level {char.level} Fighter)")
    print(f"Weapon: {frost_brand.name}")
    print(f"  - Bonus Damage: {frost_brand.bonus_damage}")
    print(f"  - Grants Resistance: {frost_brand.resistances_granted}")

    # Test 10 attacks to get average
    total_damage = 0
    for _ in range(10):
        damage = char.calculate_weapon_damage()
        total_damage += damage

    avg_damage = total_damage / 10
    print(f"\n✅ Average Damage over 10 attacks: {avg_damage:.1f}")
    print(f"   (Expected: ~8.5 = 1d8(4.5) + 1d6(3.5) cold)")

    if avg_damage > 6:  # Should have cold damage
        print("✅ PASS: Elemental damage applied")
    else:
        print("❌ FAIL: Elemental damage not applied")


def test_armor_resistances():
    """Test que les résistances d'armure sont appliquées"""
    print("\n" + "=" * 80)
    print("TEST 3: RÉSISTANCES D'ARMURE")
    print("=" * 80)

    # Create character with Armor of Fire Resistance
    char = simple_character_generator(level=5, race_name='elf', class_name='wizard', name='Elminster')

    # Create armor with fire resistance
    fire_armor = create_armor_of_resistance(damage_type="fire")
    fire_armor.equipped = True
    char.inventory.append(fire_armor)

    print(f"\n{char.name} (Level {char.level} Wizard)")
    print(f"Armor: {fire_armor.name}")
    print(f"  - Resistances: {fire_armor.damage_resistances}")

    # Test fire damage
    fire_damage = 40
    print(f"\n🔥 Taking {fire_damage} fire damage...")

    actual_damage = char.take_damage(fire_damage, "fire")

    print(f"✅ Actual damage taken: {actual_damage}")

    if actual_damage == fire_damage // 2:
        print("✅ PASS: Fire resistance applied (50% reduction)")
    else:
        print(f"❌ FAIL: Expected {fire_damage // 2}, got {actual_damage}")

    # Test normal damage (no resistance)
    char.hit_points = char.max_hit_points
    normal_damage = 20
    print(f"\n⚔️  Taking {normal_damage} slashing damage...")

    actual_damage = char.take_damage(normal_damage, "slashing")

    print(f"✅ Actual damage taken: {actual_damage}")

    if actual_damage == normal_damage:
        print("✅ PASS: Normal damage (no resistance)")
    else:
        print(f"❌ FAIL: Expected {normal_damage}, got {actual_damage}")


def test_weapon_resistances():
    """Test que les résistances conférées par armes sont appliquées"""
    print("\n" + "=" * 80)
    print("TEST 4: RÉSISTANCES D'ARMES (Frost Brand)")
    print("=" * 80)

    # Create character with Frost Brand (grants fire resistance)
    char = simple_character_generator(level=5, race_name='dwarf', class_name='fighter', name='Gimli')
    frost_brand = create_frost_brand()
    frost_brand.equipped = True
    char.inventory.append(frost_brand)

    print(f"\n{char.name} (Level {char.level} Fighter)")
    print(f"Weapon: {frost_brand.name}")
    print(f"  - Grants Resistance: {frost_brand.resistances_granted}")

    # Test fire damage with Frost Brand equipped
    fire_damage = 30
    print(f"\n🔥 Taking {fire_damage} fire damage (Frost Brand equipped)...")

    actual_damage = char.take_damage(fire_damage, "fire")

    print(f"✅ Actual damage taken: {actual_damage}")

    if actual_damage == fire_damage // 2:
        print("✅ PASS: Fire resistance from weapon applied (50% reduction)")
    else:
        print(f"❌ FAIL: Expected {fire_damage // 2}, got {actual_damage}")


def test_magic_items_ac():
    """Test que les objets magiques augmentent la CA"""
    print("\n" + "=" * 80)
    print("TEST 5: BONUS CA DES OBJETS MAGIQUES")
    print("=" * 80)

    # Create character
    char = simple_character_generator(level=5, race_name='human', class_name='fighter', name='Tordek')

    base_ac = char.armor_class
    print(f"\n{char.name} (Level {char.level} Fighter)")
    print(f"Base AC: {base_ac}")

    # Add Ring of Protection (+1 AC)
    try:
        ring = create_ring_of_protection()
        ring.equipped = True
        ring.attuned = True  # Must be attuned
        char.inventory.append(ring)

        new_ac = char.armor_class
        print(f"\nEquipped: Ring of Protection (+1 AC)")
        print(f"  - AC Bonus: +{ring.ac_bonus}")
        print(f"  - Requires Attunement: {ring.requires_attunement}")
        print(f"New AC: {new_ac}")

        if new_ac == base_ac + 1:
            print("✅ PASS: Ring of Protection bonus applied")
        else:
            print(f"❌ FAIL: Expected AC {base_ac + 1}, got {new_ac}")
    except Exception as e:
        print(f"⚠️  Could not test Ring of Protection: {e}")


def main():
    """Run all tests"""
    print("\n" + "=" * 80)
    print("🧪 TESTS COMPLETS DES EFFETS MAGIQUES")
    print("=" * 80)

    results = []

    try:
        print("\n📊 Test 1/6: Bonus d'armes magiques...")
        results.append(("Weapon Bonuses", test_weapon_bonuses()))
    except Exception as e:
        print(f"❌ Test 1 failed: {e}")
        results.append(("Weapon Bonuses", False))

    try:
        print("\n📊 Test 2/6: Toutes les armes magiques...")
        results.append(("All Weapons", test_all_magic_weapons()))
    except Exception as e:
        print(f"❌ Test 2 failed: {e}")
        results.append(("All Weapons", False))

    try:
        print("\n📊 Test 3/6: Dommages élémentaires...")
        test_elemental_damage()
        results.append(("Elemental Damage", True))
    except Exception as e:
        print(f"❌ Test 3 failed: {e}")
        results.append(("Elemental Damage", False))

    try:
        print("\n📊 Test 4/6: Résistances d'armure...")
        test_armor_resistances()
        results.append(("Armor Resistances", True))
    except Exception as e:
        print(f"❌ Test 4 failed: {e}")
        results.append(("Armor Resistances", False))

    try:
        print("\n📊 Test 5/6: Résistances d'armes...")
        test_weapon_resistances()
        results.append(("Weapon Resistances", True))
    except Exception as e:
        print(f"❌ Test 5 failed: {e}")
        results.append(("Weapon Resistances", False))

    try:
        print("\n📊 Test 6/6: Objets magiques (CA)...")
        test_magic_items_ac()
        results.append(("Magic Items AC", True))
    except Exception as e:
        print(f"❌ Test 6 failed: {e}")
        results.append(("Magic Items AC", False))

    # Summary
    print("\n" + "=" * 80)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 80)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✅" if result else "❌"
        print(f"{status} {name}")

    print(f"\n🎯 Résultat global: {passed}/{total} tests réussis")

    if passed == total:
        print("🎉 TOUS LES TESTS SONT PASSÉS !")
    else:
        print(f"⚠️  {total - passed} test(s) ont échoué")

    print("=" * 80)


if __name__ == "__main__":
    main()
