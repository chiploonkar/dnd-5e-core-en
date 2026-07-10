"""
Test and demonstration of the subclasses and multiclassing system
"""
import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.mechanics.subclass_system import (
    load_subclass,
    load_subrace,
    list_subclasses_for_class,
    list_subraces_for_race,
    MulticlassCharacter
)


def test_subclasses():
    """Tests loading of subclasses"""

    print("\n" + "=" * 80)
    print("SUBCLASSES TEST")
    print("=" * 80)

    test_cases = [
        ('wizard', ['abjuration', 'evocation', 'necromancy']),
        ('fighter', ['champion', 'battle-master', 'eldritch-knight']),
        ('cleric', ['life', 'war', 'light']),
        ('rogue', ['thief', 'assassin', 'arcane-trickster']),
    ]

    for class_index, expected_subclasses in test_cases:
        print(f"\n📖 Subclasses of {class_index.title()}:")

        # List all subclasses
        available = list_subclasses_for_class(class_index)
        print(f"   Available: {len(available)}")

        # Test loading a few subclasses
        for subclass_index in expected_subclasses:
            subclass = load_subclass(subclass_index)

            if subclass:
                print(f"   ✅ {subclass.name}")
                print(f"      Flavor: {subclass.subclass_flavor[:60]}...")
                print(f"      Levels: {subclass.subclass_levels}")
            else:
                print(f"   ❌ {subclass_index} - Not found")


def test_subraces():
    """Tests loading of subraces"""

    print("\n" + "=" * 80)
    print("SUBRACES TEST")
    print("=" * 80)

    test_cases = [
        ('elf', ['high-elf', 'wood-elf', 'dark-elf']),
        ('dwarf', ['hill-dwarf', 'mountain-dwarf']),
        ('halfling', ['lightfoot-halfling', 'stout-halfling']),
    ]

    for race_index, expected_subraces in test_cases:
        print(f"\n📖 Subraces of {race_index.title()}:")

        # List all subraces
        available = list_subraces_for_race(race_index)
        print(f"   Available: {len(available)}")

        # Test loading
        for subrace_index in expected_subraces:
            subrace = load_subrace(subrace_index)

            if subrace:
                print(f"   ✅ {subrace.name}")
                if subrace.ability_bonuses:
                    bonuses = [f"+{ab.get('bonus', 0)} {ab.get('ability_score', {}).get('index', '')}"
                              for ab in subrace.ability_bonuses]
                    print(f"      Bonus: {', '.join(bonuses)}")
            else:
                print(f"   ❌ {subrace_index} - Not found")


def test_multiclassing():
    """Tests the multiclassing system"""

    print("\n" + "=" * 80)
    print("MULTICLASSING TEST")
    print("=" * 80)

    # Example 1: Classic Fighter/Wizard
    print(f"\n🎭 Example 1: Gish (Fighter/Wizard)")
    gish = MulticlassCharacter("Elric")

    # 5 levels of Fighter
    for _ in range(5):
        gish.add_class_level('fighter')
    gish.add_class_level('fighter', 'battle-master')  # Choose subclass

    # 3 levels of Wizard
    for _ in range(3):
        gish.add_class_level('wizard')

    print(f"   {gish}")
    print(f"   Total level: {gish.get_total_level()}")
    print(f"   Primary class: {gish.get_primary_class()}")
    print(f"   Fighter level: {gish.get_class_level('fighter')}")
    print(f"   Wizard level: {gish.get_class_level('wizard')}")

    spell_slots = gish.get_spell_slots_multiclass()
    print(f"   Spell slots: {spell_slots[1:5]}")

    # Example 2: Paladin/Warlock
    print(f"\n🎭 Example 2: Hexadin (Paladin/Warlock)")
    hexadin = MulticlassCharacter("Arthas")

    # 6 levels of Paladin
    for _ in range(6):
        hexadin.add_class_level('paladin')

    # 2 levels of Warlock
    for _ in range(2):
        hexadin.add_class_level('warlock')

    print(f"   {hexadin}")
    print(f"   Total level: {hexadin.get_total_level()}")
    print(f"   Spell slots: {hexadin.get_spell_slots_multiclass()[1:5]}")

    # Example 3: Triple multiclass
    print(f"\n🎭 Example 3: Absurd but possible (Fighter/Rogue/Wizard)")
    triple = MulticlassCharacter("Jack")

    for _ in range(4):
        triple.add_class_level('fighter')
    for _ in range(3):
        triple.add_class_level('rogue')
    for _ in range(3):
        triple.add_class_level('wizard')

    print(f"   {triple}")
    print(f"   Total level: {triple.get_total_level()}")


def demo_complete():
    """Complete demonstration"""

    print("\n" + "🎲" * 40)
    print("COMPLETE DEMONSTRATION - SUBCLASSES & MULTICLASSING")
    print("🎲" * 40)

    # Test 1: Subclasses
    test_subclasses()

    # Test 2: Subraces
    test_subraces()

    # Test 3: Multiclassing
    test_multiclassing()

    print("\n" + "=" * 80)
    print("✅ DEMONSTRATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    demo_complete()
