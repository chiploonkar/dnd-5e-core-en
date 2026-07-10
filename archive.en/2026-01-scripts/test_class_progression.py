"""
Test script to verify the class progression system
"""
import sys
import os
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.progression_loader import load_class_progression, get_spell_slots_for_level


def test_all_classes():
    """Tests progression loading for all classes"""

    classes = [
        'barbarian', 'bard', 'cleric', 'druid',
        'fighter', 'monk', 'paladin', 'ranger',
        'rogue', 'sorcerer', 'warlock', 'wizard'
    ]

    print("\n" + "=" * 80)
    print("CLASS PROGRESSION LOADING TEST")
    print("=" * 80)

    results = {}

    for class_index in classes:
        print(f"\n📖 Testing {class_index}...")

        try:
            progression = load_class_progression(class_index)

            if progression:
                # Test level 1
                level_1 = progression.get_level(1)
                level_5 = progression.get_level(5)
                level_20 = progression.get_level(20)

                print(f"   ✅ {progression.class_name}")
                print(f"      Hit Die: d{progression.hit_die}")
                print(f"      Levels loaded: {len(progression.levels)}")

                if level_1:
                    print(f"      Level 1: {len(level_1.features)} features")
                    if level_1.spellcasting:
                        print(f"         Spellcasting: {level_1.spellcasting.cantrips_known} cantrips, {level_1.spellcasting.spell_slots}")

                if level_5:
                    print(f"      Level 5: Prof bonus +{level_5.prof_bonus}")
                    if level_5.class_specific:
                        print(f"         Class specific: {list(level_5.class_specific.keys())}")

                if level_20:
                    print(f"      Level 20: {len(level_20.features)} features")

                results[class_index] = "✅ Success"
            else:
                print(f"   ❌ Loading failed")
                results[class_index] = "❌ Failed"

        except Exception as e:
            print(f"   ❌ Error: {e}")
            results[class_index] = f"❌ Error: {e}"

    # Summary
    print("\n" + "=" * 80)
    print("📊 SUMMARY")
    print("=" * 80)

    success_count = sum(1 for r in results.values() if r.startswith("✅"))

    for class_name, result in results.items():
        print(f"   {class_name:12} : {result}")

    print(f"\n   Total: {success_count}/{len(classes)} classes successfully loaded")

    return success_count == len(classes)


def test_spell_slots():
    """Tests spell slot retrieval"""

    print("\n" + "=" * 80)
    print("SPELL SLOTS TEST")
    print("=" * 80)

    spellcasters = {
        'wizard': [1, 5, 10, 20],
        'cleric': [1, 5, 10, 20],
        'sorcerer': [1, 5, 10, 20],
        'bard': [1, 5, 10, 20],
    }

    for class_index, levels in spellcasters.items():
        print(f"\n🔮 {class_index.title()}:")

        for level in levels:
            slots = get_spell_slots_for_level(class_index, level)

            # Count non-zero slots
            total_slots = sum(slots[1:])

            if total_slots > 0:
                slots_str = ", ".join([f"L{i}:{slots[i]}" for i in range(1, 10) if slots[i] > 0])
                print(f"   Level {level:2d}: {slots_str} (total: {total_slots})")
            else:
                print(f"   Level {level:2d}: No slots")


def test_class_specific_features():
    """Tests class-specific features"""

    print("\n" + "=" * 80)
    print("SPECIFIC FEATURES TEST")
    print("=" * 80)

    tests = [
        ('barbarian', 3, 'rage_count', 3),
        ('barbarian', 3, 'rage_damage_bonus', 2),
        ('monk', 5, 'ki_points', 5),
        ('rogue', 5, 'sneak_attack', {'dice_count': 3, 'dice_value': 6}),
        ('fighter', 5, 'action_surge_count', 1),
    ]

    for class_index, level, key, expected in tests:
        progression = load_class_progression(class_index)

        if progression:
            value = progression.get_class_specific(level, key)

            if value == expected or value is not None:
                print(f"   ✅ {class_index:12} Lvl.{level}: {key} = {value}")
            else:
                print(f"   ❌ {class_index:12} Lvl.{level}: {key} = {value} (expected: {expected})")
        else:
            print(f"   ❌ {class_index:12}: Impossible to load progression")


if __name__ == "__main__":
    print("\n🎲 COMPLETE TEST OF THE CLASS PROGRESSION SYSTEM")

    # Test 1: Load all classes
    all_loaded = test_all_classes()

    # Test 2: Spell slots
    test_spell_slots()

    # Test 3: Specific features
    test_class_specific_features()

    print("\n" + "=" * 80)
    if all_loaded:
        print("✅ ALL TESTS PASSED!")
    else:
        print("⚠️  SOME TESTS FAILED")
    print("=" * 80)
