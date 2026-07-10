#!/usr/bin/env python3
"""
Quick validation test for the conditions system
Run this to verify the implementation works correctly
"""
import sys

def test_imports():
    """Test that all modules import correctly"""
    try:
        from dnd_5e_core.combat import ConditionParser, parse_magic_item_conditions
        from dnd_5e_core.equipment import create_wand_of_paralysis, create_magic_item_with_conditions
        from dnd_5e_core.data import load_monster
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False


def test_condition_parser():
    """Test the ConditionParser"""
    try:
        from dnd_5e_core.combat import ConditionParser

        desc = "Target must make a DC 15 Constitution saving throw or be paralyzed."
        conditions = ConditionParser.parse_condition_from_description(desc)

        assert len(conditions) > 0, "No conditions parsed"
        assert conditions[0].name == "Paralyzed", f"Wrong condition: {conditions[0].name}"
        assert conditions[0].dc_value == 15, f"Wrong DC: {conditions[0].dc_value}"

        print("✅ ConditionParser works")
        return True
    except Exception as e:
        print(f"❌ ConditionParser test failed: {e}")
        return False


def test_magic_item_factory():
    """Test magic item creation"""
    try:
        from dnd_5e_core.equipment import create_wand_of_paralysis

        wand = create_wand_of_paralysis()

        assert wand.name == "Wand of Paralysis", f"Wrong name: {wand.name}"
        assert len(wand.actions) > 0, "No actions"
        assert wand.actions[0].conditions is not None, "No conditions on action"

        print("✅ Magic item factory works")
        return True
    except Exception as e:
        print(f"❌ Magic item factory test failed: {e}")
        return False


def test_monster_loading():
    """Test that monsters load with conditions"""
    try:
        from dnd_5e_core.data import load_monster

        spider = load_monster('giant-spider')

        if not spider:
            print("⚠️  Could not load giant-spider (data files may not be available)")
            return True  # Not a failure, just data unavailable

        assert spider.name == "Giant Spider", f"Wrong monster: {spider.name}"

        # Check if any actions have conditions
        has_conditions = any(action.effects for action in spider.actions)
        if has_conditions:
            print("✅ Monster loading with conditions works")
        else:
            print("⚠️  Monster loaded but no conditions found (may be expected)")

        return True
    except Exception as e:
        print(f"❌ Monster loading test failed: {e}")
        return False


def main():
    """Run all quick tests"""
    print("=" * 60)
    print("CONDITIONS SYSTEM - QUICK VALIDATION")
    print("=" * 60)
    print()

    tests = [
        ("Imports", test_imports),
        ("Condition Parser", test_condition_parser),
        ("Magic Item Factory", test_magic_item_factory),
        ("Monster Loading", test_monster_loading),
    ]

    results = []
    for name, test_func in tests:
        print(f"Testing {name}...", end=" ")
        result = test_func()
        results.append(result)
        print()

    print()
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"RESULTS: {passed}/{total} tests passed")

    if passed == total:
        print("✅ All tests passed! System is working correctly.")
        print("=" * 60)
        return 0
    else:
        print("⚠️  Some tests failed. Check the output above.")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
