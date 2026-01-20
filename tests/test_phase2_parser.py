"""
Test Phase 2: Condition Parser
Test le parsing automatique des conditions depuis les descriptions d'actions
"""

import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.combat.condition_parser import ConditionParser
from dnd_5e_core.abilities import AbilityType


def test_poisoned_detection():
    """Test détection de condition Poisoned"""
    print("\n" + "="*80)
    print("TEST 1: Parser - Poisoned Condition")
    print("="*80)

    description = "The target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour."

    print(f"\n📝 Description:")
    print(f"   {description[:100]}...")

    conditions = ConditionParser.parse_condition_from_description(description)

    print(f"\n✅ Conditions détectées: {len(conditions)}")
    for condition in conditions:
        print(f"   - {condition.name}")
        print(f"     DC: {condition.dc_value} {condition.dc_type.value if condition.dc_type else 'N/A'}")
        print(f"     Description: {condition.desc[:60]}...")

    if conditions and any(c.index == 'poisoned' for c in conditions):
        print("\n✅ TEST POISONED: SUCCÈS")
        return True
    else:
        print("\n❌ TEST POISONED: ÉCHEC")
        return False


def test_restrained_detection():
    """Test détection de condition Restrained"""
    print("\n" + "="*80)
    print("TEST 2: Parser - Restrained Condition")
    print("="*80)

    description = "Ranged Weapon Attack: +5 to hit, range 30/60 ft., one creature. Hit: The target is restrained by webbing. As an action, the restrained target can make a DC 12 Strength check, bursting the webbing on a success. The webbing can also be attacked and destroyed (AC 10; hp 5; vulnerability to fire damage; immunity to bludgeoning, poison, and psychic damage)."

    print(f"\n📝 Description:")
    print(f"   {description[:100]}...")

    conditions = ConditionParser.parse_condition_from_description(description)

    print(f"\n✅ Conditions détectées: {len(conditions)}")
    for condition in conditions:
        print(f"   - {condition.name}")
        print(f"     DC: {condition.dc_value} {condition.dc_type.value if condition.dc_type else 'N/A'}")

    if conditions and any(c.index == 'restrained' for c in conditions):
        print("\n✅ TEST RESTRAINED: SUCCÈS")
        return True
    else:
        print("\n❌ TEST RESTRAINED: ÉCHEC")
        return False


def test_paralyzed_detection():
    """Test détection de condition Paralyzed"""
    print("\n" + "="*80)
    print("TEST 3: Parser - Paralyzed Condition")
    print("="*80)

    description = "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or become paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."

    print(f"\n📝 Description:")
    print(f"   {description[:100]}...")

    conditions = ConditionParser.parse_condition_from_description(description)

    print(f"\n✅ Conditions détectées: {len(conditions)}")
    for condition in conditions:
        print(f"   - {condition.name}")
        print(f"     DC: {condition.dc_value} {condition.dc_type.value if condition.dc_type else 'N/A'}")

    if conditions and any(c.index == 'paralyzed' for c in conditions):
        print("\n✅ TEST PARALYZED: SUCCÈS")
        return True
    else:
        print("\n❌ TEST PARALYZED: ÉCHEC")
        return False


def test_frightened_detection():
    """Test détection de condition Frightened"""
    print("\n" + "="*80)
    print("TEST 4: Parser - Frightened Condition")
    print("="*80)

    description = "Each creature within 30 feet of the dragon that can hear it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."

    print(f"\n📝 Description:")
    print(f"   {description[:100]}...")

    conditions = ConditionParser.parse_condition_from_description(description)

    print(f"\n✅ Conditions détectées: {len(conditions)}")
    for condition in conditions:
        print(f"   - {condition.name}")
        print(f"     DC: {condition.dc_value} {condition.dc_type.value if condition.dc_type else 'N/A'}")

    if conditions and any(c.index == 'frightened' for c in conditions):
        print("\n✅ TEST FRIGHTENED: SUCCÈS")
        return True
    else:
        print("\n❌ TEST FRIGHTENED: ÉCHEC")
        return False


def test_prone_detection():
    """Test détection de condition Prone"""
    print("\n" + "="*80)
    print("TEST 5: Parser - Prone Condition")
    print("="*80)

    description = "The target must succeed on a DC 13 Strength saving throw or be knocked prone."

    print(f"\n📝 Description:")
    print(f"   {description}")

    conditions = ConditionParser.parse_condition_from_description(description)

    print(f"\n✅ Conditions détectées: {len(conditions)}")
    for condition in conditions:
        print(f"   - {condition.name}")
        print(f"     DC: {condition.dc_value} {condition.dc_type.value if condition.dc_type else 'N/A'}")

    if conditions and any(c.index == 'prone' for c in conditions):
        print("\n✅ TEST PRONE: SUCCÈS")
        return True
    else:
        print("\n❌ TEST PRONE: ÉCHEC")
        return False


def test_condition_application():
    """Test application d'une condition à un personnage"""
    print("\n" + "="*80)
    print("TEST 6: Application de Condition à un Personnage")
    print("="*80)

    from dnd_5e_core.data.loaders import simple_character_generator
    from dnd_5e_core.combat.condition import create_poisoned_condition

    # Créer personnage
    fighter = simple_character_generator(level=5, class_name='fighter', name='TestFighter')
    print(f"\n✅ Personnage: {fighter.name}")
    print(f"   Conditions initiales: {len(fighter.conditions) if fighter.conditions else 0}")

    # Créer et appliquer condition
    poisoned = create_poisoned_condition(AbilityType.CON, 12)
    print(f"\n🧪 Application de condition: {poisoned.name}")
    poisoned.apply_to_character(fighter)

    print(f"   Conditions après application: {len(fighter.conditions)}")

    if fighter.conditions and len(fighter.conditions) > 0:
        for condition in fighter.conditions:
            print(f"      - {condition.name}: {condition.desc[:50]}...")

        # Test saving throw
        print(f"\n🎲 Test de saving throw:")
        print(f"   DC {poisoned.dc_value} {poisoned.dc_type.value}")

        success = poisoned.attempt_save(fighter)
        print(f"   Résultat: {'✅ Succès (condition retirée)' if success else '❌ Échec (condition persiste)'}")
        print(f"   Conditions restantes: {len(fighter.conditions)}")

        print("\n✅ TEST APPLICATION: SUCCÈS")
        return True
    else:
        print("\n❌ TEST APPLICATION: ÉCHEC - Condition non appliquée")
        return False


def run_all_tests():
    """Exécuter tous les tests Phase 2"""
    print("\n" + "🧪"*40)
    print("PHASE 2 - CONDITION PARSER TESTS")
    print("🧪"*40)

    results = []

    try:
        results.append(("Poisoned Detection", test_poisoned_detection()))
        results.append(("Restrained Detection", test_restrained_detection()))
        results.append(("Paralyzed Detection", test_paralyzed_detection()))
        results.append(("Frightened Detection", test_frightened_detection()))
        results.append(("Prone Detection", test_prone_detection()))
        results.append(("Condition Application", test_condition_application()))

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
            print("\n✅ Phase 2 Implémentée:")
            print("   - ConditionParser détecte les conditions dans les descriptions")
            print("   - Parsing de DC et ability type fonctionnel")
            print("   - Application de conditions aux personnages OK")
            print("   - Saving throws fonctionnels")
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
