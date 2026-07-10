"""
Test of the special_monster_actions module with JSON extraction
"""
import sys
from pathlib import Path

# Add the package path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dnd_5e_core.entities import get_special_monster_actions


def test_manual_definitions():
    """Test of monsters with manual definitions"""
    print("=" * 80)
    print("TEST 1: Monsters with Manual Definitions")
    print("=" * 80)

    # These monsters have manual definitions in populate_functions.py
    manual_monsters = [
        "Orc Eye of Gruumsh",
        "Goblin Boss",
        "Hobgoblin Captain"
    ]

    for monster_name in manual_monsters:
        print(f"\n{monster_name}:")
        try:
            actions, abilities, spellcaster = get_special_monster_actions(monster_name)
            print(f"  ✅ Actions: {len(actions)}")
            for action in actions:
                print(f"     - {action.name} ({action.type.value if hasattr(action.type, 'value') else action.type})")
            print(f"  ✅ Special Abilities: {len(abilities)}")
            for ability in abilities:
                print(f"     - {ability.name}")
            if spellcaster:
                print(f"  ✅ Spellcaster: Level {spellcaster.level}")
        except Exception as e:
            print(f"  ❌ Error: {e}")


def test_json_extraction():
    """Test of automatic extraction from JSON"""
    print("\n" + "=" * 80)
    print("TEST 2: Automatic Extraction from JSON")
    print("=" * 80)

    # These monsters do not have manual definitions
    # but should be in bestiary-sublist-data.json
    json_monsters = [
        "Doppelganger",
        "Xvart",
        "Kobold Inventor"
    ]

    for monster_name in json_monsters:
        print(f"\n{monster_name}:")
        try:
            actions, abilities, spellcaster = get_special_monster_actions(monster_name)
            print(f"  ✅ Actions (JSON): {len(actions)}")
            for action in actions:
                print(f"     - {action.name} ({action.type.value if hasattr(action.type, 'value') else action.type})")
            print(f"  ✅ Special Abilities (JSON): {len(abilities)}")
            for ability in abilities:
                print(f"     - {ability.name}")
            if spellcaster:
                print(f"  ✅ Spellcaster: Level {spellcaster.level}")
        except Exception as e:
            print(f"  ❌ Error: {e}")


def test_fallback_behavior():
    """Test of fallback behavior"""
    print("\n" + "=" * 80)
    print("TEST 3: Fallback Behavior")
    print("=" * 80)

    # Test with a monster that does not exist anywhere
    print("\nNon-existent monster:")
    try:
        actions, abilities, spellcaster = get_special_monster_actions("Monster That Does Not Exist")
        if not actions and not abilities and not spellcaster:
            print("  ✅ Correctly returns empty lists")
        else:
            print("  ❌ Should return empty lists")
    except Exception as e:
        print(f"  ❌ Error: {e}")

    # Test with JSON fallback disabled
    print("\nGoblin Boss (JSON fallback disabled):")
    try:
        actions, abilities, spellcaster = get_special_monster_actions("Goblin Boss", use_json_fallback=False)
        print(f"  ✅ Actions: {len(actions)} (manual definition)")
    except Exception as e:
        print(f"  ❌ Error: {e}")


def main():
    """Runs all tests"""
    print("\n" + "🧪" * 40)
    print("TESTS: Extraction Actions of Extended Monsters")
    print("🧪" * 40 + "\n")

    test_manual_definitions()
    test_json_extraction()
    test_fallback_behavior()

    print("\n" + "=" * 80)
    print("✅ Tests completed")
    print("=" * 80)


if __name__ == "__main__":
    main()
