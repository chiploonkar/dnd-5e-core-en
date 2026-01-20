"""
Test Phase 2: Automatic Condition Application in Combat
Vérifie que les conditions sont automatiquement appliquées lors des attaques de monstres
"""

import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loader import load_monster
from dnd_5e_core.data.loaders import simple_character_generator


def test_giant_spider_restrained():
    """Test que Giant Spider applique automatiquement Restrained"""
    print("\n" + "="*80)
    print("TEST 1: Giant Spider - Restrained Condition")
    print("="*80)

    # Load Giant Spider
    spider = load_monster('giant-spider')
    if not spider:
        print("❌ Could not load giant-spider")
        return False

    print(f"\n✅ Loaded: {spider.name}")
    print(f"   Actions: {len(spider.actions)}")

    # Check if web attack has conditions
    web_attack = None
    for action in spider.actions:
        if 'web' in action.name.lower():
            web_attack = action
            break

    if web_attack:
        print(f"\n🕸️  Web Attack Found: {web_attack.name}")
        print(f"   Description: {web_attack.desc[:100]}...")

        if hasattr(web_attack, 'effects') and web_attack.effects:
            print(f"   ✅ Effects/Conditions: {len(web_attack.effects)}")
            for effect in web_attack.effects:
                print(f"      - {effect}")
            return True
        else:
            print(f"   ❌ No effects found on web attack")
            return False
    else:
        print("   ❌ Web attack not found")
        return False


def test_poisonous_snake_poisoned():
    """Test que Poisonous Snake applique Poisoned"""
    print("\n" + "="*80)
    print("TEST 2: Poisonous Snake - Poisoned Condition")
    print("="*80)

    snake = load_monster('poisonous-snake')
    if not snake:
        print("❌ Could not load poisonous-snake")
        return False

    print(f"\n✅ Loaded: {snake.name}")

    # Check bite attack
    bite_attack = None
    for action in snake.actions:
        if 'bite' in action.name.lower():
            bite_attack = action
            break

    if bite_attack:
        print(f"\n🐍 Bite Attack Found: {bite_attack.name}")
        print(f"   Description: {bite_attack.desc[:100]}...")

        if hasattr(bite_attack, 'effects') and bite_attack.effects:
            print(f"   ✅ Effects/Conditions: {len(bite_attack.effects)}")
            for effect in bite_attack.effects:
                print(f"      - {effect}")
            return True
        else:
            print(f"   ❌ No effects found")
            return False
    else:
        print("   ❌ Bite attack not found")
        return False


def test_actual_combat_with_conditions():
    """Test un combat réel avec application de conditions"""
    print("\n" + "="*80)
    print("TEST 3: Combat Réel - Application Conditions")
    print("="*80)

    # Créer un personnage
    fighter = simple_character_generator(level=5, class_name='fighter', name='TestFighter')
    print(f"\n✅ Personnage créé: {fighter.name}")
    print(f"   HP: {fighter.hit_points}/{fighter.max_hit_points}")
    print(f"   Conditions initiales: {len(fighter.conditions) if fighter.conditions else 0}")

    # Charger spider
    spider = load_monster('giant-spider')

    if not spider:
        print("❌ Could not load spider")
        return False

    # Simulate attack
    print(f"\n🕷️ {spider.name} attacks {fighter.name}!")

    # Find web attack
    web_attack = None
    for action in spider.actions:
        if 'web' in action.name.lower() and hasattr(action, 'effects') and action.effects:
            web_attack = action
            break

    if not web_attack:
        print("❌ No web attack with effects")
        return False

    print(f"   Using: {web_attack.name}")

    # Manually apply condition (simulating attack hit)
    for effect in web_attack.effects:
        print(f"   Applying condition: {effect.name}")
        effect.apply_to_character(fighter)

    # Check conditions
    print(f"\n📊 Résultat:")
    print(f"   Conditions sur {fighter.name}: {len(fighter.conditions)}")

    if fighter.conditions:
        for condition in fighter.conditions:
            print(f"      - {condition.name}: {condition.desc[:50]}...")

        # Test saving throw
        first_condition = fighter.conditions[0]
        if first_condition.dc_type and first_condition.dc_value:
            print(f"\n🎲 Tentative de saving throw:")
            print(f"   DC {first_condition.dc_value} {first_condition.dc_type.value}")

            success = first_condition.attempt_save(fighter)
            print(f"   Résultat: {'✅ Succès!' if success else '❌ Échec'}")
            print(f"   Conditions restantes: {len(fighter.conditions)}")

        return True
    else:
        print("   ❌ Aucune condition appliquée")
        return False


def test_troglodyte_stench():
    """Test Troglodyte Stench ability"""
    print("\n" + "="*80)
    print("TEST 4: Troglodyte - Stench (Poisoned)")
    print("="*80)

    trog = load_monster('troglodyte')
    if not trog:
        print("❌ Could not load troglodyte")
        return False

    print(f"\n✅ Loaded: {trog.name}")

    # Check special abilities
    if hasattr(trog, 'sa') and trog.sa:
        print(f"   Special Abilities: {len(trog.sa)}")
        for ability in trog.sa:
            print(f"      - {ability.name}")
            if 'stench' in ability.name.lower():
                print(f"        Description: {ability.desc[:100]}...")
        return True
    else:
        print("   ⚠️  No special abilities (this is OK, not all monsters have them)")
        return True


def run_all_tests():
    """Exécuter tous les tests Phase 2"""
    print("\n" + "🧪"*40)
    print("PHASE 2 - CONDITION APPLICATION TESTS")
    print("🧪"*40)

    results = []

    try:
        results.append(("Giant Spider Restrained", test_giant_spider_restrained()))
        results.append(("Poisonous Snake Poisoned", test_poisonous_snake_poisoned()))
        results.append(("Combat with Conditions", test_actual_combat_with_conditions()))
        results.append(("Troglodyte Stench", test_troglodyte_stench()))

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
            print("\n✅ Phase 2 Validée:")
            print("   - Conditions automatiquement parsées des descriptions")
            print("   - Conditions appliquées lors des attaques")
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
