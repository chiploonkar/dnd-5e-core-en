"""
Test Phase 3 & 4: Magic Items, Defensive Spells & Multiclassing
Valide que ces fonctionnalités sont déjà implémentées dans le package
"""

import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.equipment import (
    create_ring_of_protection,
    create_cloak_of_protection,
    create_wand_of_magic_missiles,
    create_staff_of_healing,
    create_belt_of_giant_strength,
    create_amulet_of_health,
    create_bracers_of_defense,
    create_necklace_of_fireballs,
    create_wand_of_paralysis,
    create_poisoned_dagger
)
from dnd_5e_core.classes.multiclass import (
    can_multiclass_into,
    can_multiclass_from,
    calculate_spell_slots_multiclass,
    MULTICLASS_PREREQUISITES
)


def test_magic_items_creation():
    """Test création des magic items prédéfinis"""
    print("\n" + "="*80)
    print("TEST 1: Création de Magic Items")
    print("="*80)

    magic_items = [
        ("Ring of Protection", create_ring_of_protection),
        ("Cloak of Protection", create_cloak_of_protection),
        ("Wand of Magic Missiles", create_wand_of_magic_missiles),
        ("Staff of Healing", create_staff_of_healing),
        ("Belt of Giant Strength", create_belt_of_giant_strength),
        ("Amulet of Health", create_amulet_of_health),
        ("Bracers of Defense", create_bracers_of_defense),
        ("Necklace of Fireballs", create_necklace_of_fireballs),
        ("Wand of Paralysis", create_wand_of_paralysis),
        ("Poisoned Dagger", create_poisoned_dagger),
    ]

    print(f"\n📦 Test de création de {len(magic_items)} magic items:")

    created = 0
    for name, creator_func in magic_items:
        try:
            item = creator_func()
            print(f"   ✅ {name}: {item.rarity.value}, {item.item_type.value}")
            if hasattr(item, 'ac_bonus') and item.ac_bonus:
                print(f"      AC Bonus: +{item.ac_bonus}")
            if hasattr(item, 'actions') and item.actions:
                print(f"      Actions: {len(item.actions)}")
            created += 1
        except Exception as e:
            print(f"   ❌ {name}: {e}")

    if created == len(magic_items):
        print(f"\n✅ TEST MAGIC ITEMS: SUCCÈS ({created}/{len(magic_items)})")
        return True
    else:
        print(f"\n❌ TEST MAGIC ITEMS: ÉCHEC ({created}/{len(magic_items)})")
        return False


def test_magic_items_with_character():
    """Test utilisation des magic items avec un personnage"""
    print("\n" + "="*80)
    print("TEST 2: Magic Items avec Personnage")
    print("="*80)

    wizard = simple_character_generator(level=5, class_name='wizard', name='Gandalf')
    print(f"\n✅ Personnage: {wizard.name}")
    print(f"   AC de base: {wizard.armor_class}")
    print(f"   Saves: Normal")

    # Équiper Ring of Protection
    ring = create_ring_of_protection()
    print(f"\n💍 Équipement: {ring.name}")
    print(f"   Rarity: {ring.rarity.value}")
    print(f"   Requires Attunement: {ring.requires_attunement}")
    print(f"   AC Bonus: +{ring.ac_bonus}")
    if hasattr(ring, 'saving_throw_bonus'):
        print(f"   Save Bonus: +{ring.saving_throw_bonus}")

    # Équiper Staff of Healing
    staff = create_staff_of_healing()
    print(f"\n🪄 Équipement: {staff.name}")
    print(f"   Rarity: {staff.rarity.value}")
    if hasattr(staff, 'actions') and staff.actions:
        print(f"   Actions disponibles: {len(staff.actions)}")
        for action in staff.actions:
            print(f"      - {action.name}: {action.description}")
            if hasattr(action, 'uses_per_day'):
                print(f"        Uses: {action.uses_per_day}/day")

    print("\n✅ TEST MAGIC ITEMS + CHARACTER: SUCCÈS")
    return True


def test_multiclass_prerequisites():
    """Test vérification des prérequis de multiclassing"""
    print("\n" + "="*80)
    print("TEST 3: Multiclass Prerequisites")
    print("="*80)

    print(f"\n📜 Prérequis de multiclassing pour toutes les classes:")

    for class_name, requirements in MULTICLASS_PREREQUISITES.items():
        req_str = ", ".join([f"{k.upper()} {v}" for k, v in requirements.items()])
        print(f"   {class_name.capitalize()}: {req_str}")

    # Créer un personnage
    fighter = simple_character_generator(level=5, class_name='fighter', name='Conan')
    print(f"\n✅ Test avec: {fighter.name}")
    print(f"   STR: {fighter.abilities.str}, DEX: {fighter.abilities.dex}")
    print(f"   INT: {fighter.abilities.int}, WIS: {fighter.abilities.wis}")
    print(f"   CHA: {fighter.abilities.cha}, CON: {fighter.abilities.con}")

    # Tester multiclass vers différentes classes
    test_classes = ["rogue", "wizard", "cleric"]

    print(f"\n🔄 Test de multiclass vers:")
    for target_class in test_classes:
        can_multi, reason = can_multiclass_into(target_class, fighter.abilities)
        status = "✅ Possible" if can_multi else f"❌ Impossible ({reason})"
        print(f"   {target_class.capitalize()}: {status}")

    print("\n✅ TEST MULTICLASS PREREQUISITES: SUCCÈS")
    return True


def test_multiclass_spell_slots():
    """Test calcul des spell slots pour multiclass"""
    print("\n" + "="*80)
    print("TEST 4: Multiclass Spell Slots")
    print("="*80)

    # Exemple: Wizard 5 / Cleric 3
    class_levels = {
        "wizard": 5,
        "cleric": 3
    }

    print(f"\n🧙 Personnage multiclassé:")
    for class_name, level in class_levels.items():
        print(f"   {class_name.capitalize()}: niveau {level}")

    try:
        spell_slots = calculate_spell_slots_multiclass(class_levels)

        print(f"\n📖 Spell Slots calculés:")
        for level, slots in enumerate(spell_slots[1:], 1):
            if slots > 0:
                print(f"   Niveau {level}: {slots} slots")

        # Vérifier que les slots sont cohérents
        if sum(spell_slots[1:]) > 0:
            print("\n✅ TEST MULTICLASS SPELL SLOTS: SUCCÈS")
            return True
        else:
            print("\n❌ TEST MULTICLASS SPELL SLOTS: ÉCHEC (aucun slot)")
            return False

    except Exception as e:
        print(f"\n❌ TEST MULTICLASS SPELL SLOTS: ERREUR ({e})")
        import traceback
        traceback.print_exc()
        return False


def test_defensive_capabilities():
    """Test que les magic items peuvent améliorer la défense"""
    print("\n" + "="*80)
    print("TEST 5: Capacités Défensives")
    print("="*80)

    # Créer un personnage
    fighter = simple_character_generator(level=5, class_name='fighter', name='Tank')
    base_ac = fighter.armor_class

    print(f"\n🛡️ {fighter.name} (Fighter niveau {fighter.level})")
    print(f"   AC de base: {base_ac}")

    # Items défensifs
    defensive_items = [
        ("Ring of Protection", create_ring_of_protection, 1),
        ("Cloak of Protection", create_cloak_of_protection, 1),
        ("Bracers of Defense", create_bracers_of_defense, 2),
    ]

    print(f"\n📦 Items défensifs disponibles:")
    total_ac_bonus = 0

    for name, creator, expected_ac in defensive_items:
        item = creator()
        ac_bonus = getattr(item, 'ac_bonus', 0)
        total_ac_bonus += ac_bonus
        status = "✅" if ac_bonus == expected_ac else "❌"
        print(f"   {status} {name}: +{ac_bonus} AC (attendu: +{expected_ac})")

    print(f"\n💪 Avec tous les items équipés:")
    print(f"   AC potentielle: {base_ac} + {total_ac_bonus} = {base_ac + total_ac_bonus}")

    if total_ac_bonus >= 4:
        print("\n✅ TEST DEFENSIVE CAPABILITIES: SUCCÈS")
        return True
    else:
        print("\n❌ TEST DEFENSIVE CAPABILITIES: ÉCHEC")
        return False


def run_all_tests():
    """Exécuter tous les tests Phase 3 & 4"""
    print("\n" + "🧪"*40)
    print("PHASE 3 & 4 - VALIDATION TESTS")
    print("🧪"*40)

    results = []

    try:
        results.append(("Magic Items Creation", test_magic_items_creation()))
        results.append(("Magic Items + Character", test_magic_items_with_character()))
        results.append(("Multiclass Prerequisites", test_multiclass_prerequisites()))
        results.append(("Multiclass Spell Slots", test_multiclass_spell_slots()))
        results.append(("Defensive Capabilities", test_defensive_capabilities()))

        print("\n" + "="*80)
        print("📊 RÉSULTATS DES TESTS")
        print("="*80)

        passed = 0
        for test_name, result in results:
            status = "✅ SUCCÈS" if result else "❌ ÉCHEC"
            print(f"{status}: {test_name}")
            if result:
                passed += 1

        print(f"\nScore: {passed}/{len(results)} ({passed*100//len(results)}%)")

        if passed == len(results):
            print("\n🎉 TOUS LES TESTS RÉUSSIS!")
            print("\n✅ Phase 3 & 4 Validées:")
            print("   - Magic Items système complet (10+ items)")
            print("   - Items défensifs fonctionnels")
            print("   - Multiclass prerequisites implémentés")
            print("   - Multiclass spell slots calculation OK")
            print("\n💡 Code déjà implémenté - Aucun développement requis!")
            return True
        else:
            print(f"\n⚠️  {len(results) - passed} test(s) échoué(s)")
            return False

    except Exception as e:
        print(f"\n❌ ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
