"""
Demonstration script for the class progression system
Shows integration with simple_character_generator and level up
"""
import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loaders import simple_character_generator, level_up_character


def demo_character_creation_with_progression():
    """Demo of character creation with automatic progression"""

    print("\n" + "🎲" * 40)
    print("DEMONSTRATION OF THE INTEGRATED PROGRESSION SYSTEM")
    print("🎲" * 40)

    # =============================================================================
    # PART 1: Creation of a level 1 Wizard
    # =============================================================================
    print("\n📖 PART 1: CREATION OF A LEVEL 1 WIZARD")
    print("=" * 80)

    wizard = simple_character_generator(1, 'elf', 'wizard', 'Gandalf')

    print(f"✨ {wizard.name} created!")
    print(f"   Race: {wizard.race.name}")
    print(f"   Class: {wizard.class_type.name}")
    print(f"   Level: {wizard.level}")
    print(f"   HP: {wizard.hit_points}/{wizard.max_hit_points}")
    print(f"   AC: {wizard.armor_class}")

    if hasattr(wizard, 'sc') and wizard.sc:
        print(f"   🔮 Spellcaster: Yes")
        print(f"      Spell slots: {wizard.sc.spell_slots[1:6]}")
        print(f"      Spells known: {len(wizard.sc.spells_known)}")

    # =============================================================================
    # PART 2: Level Up to level 2
    # =============================================================================
    print("\n📖 PART 2: LEVEL UP TO LEVEL 2")
    print("=" * 80)

    wizard = level_up_character(wizard, 2, verbose=True)

    print(f"\n   Current status:")
    print(f"   Level: {wizard.level}")
    print(f"   HP: {wizard.hit_points}/{wizard.max_hit_points}")

    if hasattr(wizard, 'sc') and wizard.sc:
        print(f"   Spell slots: {wizard.sc.spell_slots[1:6]}")

    # =============================================================================
    # PART 3: Progression up to level 5
    # =============================================================================
    print("\n📖 PART 3: PROGRESSION UP TO LEVEL 5")
    print("=" * 80)

    for new_level in [3, 4, 5]:
        print(f"\n--- Leveling up to level {new_level} ---")
        wizard = level_up_character(wizard, new_level, verbose=True)

    print(f"\n   Final status:")
    print(f"   {wizard.name} - Level {wizard.level} {wizard.class_type.name}")
    print(f"   HP: {wizard.hit_points}/{wizard.max_hit_points}")
    print(f"   AC: {wizard.armor_class}")

    if hasattr(wizard, 'sc') and wizard.sc:
        total_slots = sum(wizard.sc.spell_slots[1:])
        print(f"   Spell slots: {wizard.sc.spell_slots[1:6]} (total: {total_slots})")

    # =============================================================================
    # PART 4: Test with other classes
    # =============================================================================
    print("\n📖 PART 4: TEST WITH OTHER CLASSES")
    print("=" * 80)

    test_classes = [
        ('fighter', 'Conan'),
        ('cleric', 'Gimli'),
        ('rogue', 'Bilbo'),
        ('barbarian', 'Grok'),
    ]

    for class_name, name in test_classes:
        print(f"\n🎭 Creation of a {class_name}: {name}")

        char = simple_character_generator(5, 'human', class_name, name)

        print(f"   Level: {char.level}")
        print(f"   HP: {char.hit_points}/{char.max_hit_points}")
        print(f"   Hit Die: d{char.class_type.hit_die}")

        if hasattr(char, 'sc') and char.sc:
            total_slots = sum(char.sc.spell_slots[1:])
            print(f"   Spellcaster: Yes ({total_slots} spell slots)")
        else:
            print(f"   Spellcaster: No")

    print("\n" + "=" * 80)
    print("✅ DEMONSTRATION COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    demo_character_creation_with_progression()
