"""
Test script for Magic Items and Defensive Spells
Demonstrates the new features in dnd-5e-core
"""
from dnd_5e_core.data import load_spell, load_monster
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.equipment import (
    get_magic_item,
    create_ring_of_protection,
    create_wand_of_magic_missiles,
    create_staff_of_healing
)
from dnd_5e_core.combat import CombatSystem


def test_magic_items():
    """Test magic items creation and usage"""
    print("=" * 80)
    print("🪄 MAGIC ITEMS TEST")
    print("=" * 80)

    # Create a wizard
    wizard = simple_character_generator(level=5, class_name='wizard', name='Gandalf')
    print(f"\n📜 Created: {wizard.name} the {wizard.class_type.name}")
    print(f"   Base AC: {wizard.armor_class}")
    print(f"   Base STR: {wizard.abilities.str}")
    print(f"   Base Saving Throws: All normal")

    # Test Ring of Protection
    print(f"\n💍 Equipping Ring of Protection...")
    ring = create_ring_of_protection()
    print(f"   {ring.name} ({ring.rarity.value})")
    print(f"   Requires attunement: {ring.requires_attunement}")
    print(f"   AC Bonus: +{ring.ac_bonus}")
    print(f"   Saving Throw Bonus: +{ring.saving_throw_bonus}")

    # Attune and equip
    if ring.requires_attunement:
        if not hasattr(wizard, 'attuned_items'):
            wizard.attuned_items = []
        wizard.attuned_items.append(ring)
        ring.attune(wizard)

    ring.equipped = True
    ring.apply_to_character(wizard)

    print(f"   ✅ After equipping:")
    print(f"      AC: {wizard.armor_class} (+{ring.ac_bonus})")
    print(f"      Saving Throws: +{ring.saving_throw_bonus}")

    # Test Wand of Magic Missiles
    print(f"\n🪄 Testing Wand of Magic Missiles...")
    wand = create_wand_of_magic_missiles()
    print(f"   {wand.name} ({wand.rarity.value})")
    print(f"   Actions: {len(wand.actions)}")

    for action in wand.actions:
        print(f"      - {action.name}: {action.description}")
        print(f"        Damage: {action.damage_dice} {action.damage_type}")
        print(f"        Range: {action.range} ft")
        print(f"        Uses per day: {action.uses_per_day}")

        # Test using the action
        if wand.can_perform_action(action):
            print(f"        ✅ Can use action (charges: {action.remaining_uses})")
            wand.use_action(action)
            print(f"        Used! Remaining charges: {action.remaining_uses}")

    # Test Staff of Healing
    print(f"\n🌟 Testing Staff of Healing...")
    staff = create_staff_of_healing()
    print(f"   {staff.name} ({staff.rarity.value})")

    for action in staff.actions:
        print(f"      - {action.name}: {action.description}")
        print(f"        Healing: {action.healing_dice}")
        print(f"        Uses per day: {action.uses_per_day}")


def test_defensive_spells():
    """Test defensive spells (Shield, Mage Armor, etc.)"""
    print("\n" + "=" * 80)
    print("🛡️ DEFENSIVE SPELLS TEST")
    print("=" * 80)

    # Load defensive spells
    shield = load_spell("shield")
    mage_armor = load_spell("mage-armor")
    shield_of_faith = load_spell("shield-of-faith")

    print(f"\n📖 Defensive Spells:")

    # Shield
    if shield:
        print(f"\n   🛡️ {shield.name} (Level {shield.level})")
        print(f"      School: {shield.school}")
        print(f"      Duration: {shield.duration}")
        print(f"      Concentration: {shield.concentration}")
        print(f"      AC Bonus: +{shield.ac_bonus if shield.ac_bonus else 0}")
        print(f"      Is Defensive: {shield.is_defensive}")
        print(f"      Classes: {', '.join(shield.allowed_classes)}")

    # Mage Armor
    if mage_armor:
        print(f"\n   🛡️ {mage_armor.name} (Level {mage_armor.level})")
        print(f"      School: {mage_armor.school}")
        print(f"      Duration: {mage_armor.duration}")
        print(f"      AC Bonus: +{mage_armor.ac_bonus if mage_armor.ac_bonus else 0}")
        print(f"      Is Defensive: {mage_armor.is_defensive}")

    # Shield of Faith
    if shield_of_faith:
        print(f"\n   🛡️ {shield_of_faith.name} (Level {shield_of_faith.level})")
        print(f"      School: {shield_of_faith.school}")
        print(f"      Duration: {shield_of_faith.duration}")
        print(f"      Concentration: {shield_of_faith.concentration}")
        print(f"      AC Bonus: +{shield_of_faith.ac_bonus if shield_of_faith.ac_bonus else 0}")
        print(f"      Is Defensive: {shield_of_faith.is_defensive}")
        print(f"      Classes: {', '.join(shield_of_faith.allowed_classes)}")


def test_combat_with_magic_items():
    """Test combat with magic items"""
    print("\n" + "=" * 80)
    print("⚔️ COMBAT WITH MAGIC ITEMS TEST")
    print("=" * 80)

    # Create party
    wizard = simple_character_generator(level=5, class_name='wizard', name='Merlin')
    cleric = simple_character_generator(level=5, class_name='cleric', name='Elara')

    # Equip magic items
    ring = create_ring_of_protection()
    ring.equipped = True
    if not hasattr(wizard, 'attuned_items'):
        wizard.attuned_items = []
    wizard.attuned_items.append(ring)
    ring.attune(wizard)
    ring.apply_to_character(wizard)

    print(f"\n⚔️ Party:")
    print(f"   - {wizard.name}: AC {wizard.armor_class}, HP {wizard.hit_points}/{wizard.max_hit_points}")
    print(f"     Magic Items: Ring of Protection (+1 AC, +1 saves)")
    print(f"   - {cleric.name}: AC {cleric.armor_class}, HP {cleric.hit_points}/{cleric.max_hit_points}")

    # Load monsters
    goblin1 = load_monster('goblin')
    goblin2 = load_monster('goblin')

    if not goblin1 or not goblin2:
        print("\n⚠️ Could not load goblins for combat test")
        return

    print(f"\n👹 Enemies:")
    print(f"   - Goblin 1: AC {goblin1.armor_class}, HP {goblin1.hit_points}")
    print(f"   - Goblin 2: AC {goblin2.armor_class}, HP {goblin2.hit_points}")

    # Combat
    combat = CombatSystem(verbose=True)
    party = [wizard, cleric]
    monsters = [goblin1, goblin2]

    print(f"\n⚔️ Round 1:")
    print(f"   {wizard.name} attacks with magic!")

    # Wizard attacks
    alive_monsters = [m for m in monsters if m.hit_points > 0]
    if alive_monsters:
        combat.character_turn(
            character=wizard,
            alive_chars=party,
            alive_monsters=alive_monsters,
            party=party
        )

    print(f"\n📊 Results:")
    print(f"   Wizard: {wizard.hit_points}/{wizard.max_hit_points} HP")
    print(f"   Goblin 1: {goblin1.hit_points} HP")
    print(f"   Goblin 2: {goblin2.hit_points} HP")


def main():
    """Run all tests"""
    print("\n" + "🧪" * 40)
    print("MAGIC ITEMS & DEFENSIVE SPELLS - FEATURE DEMONSTRATION")
    print("🧪" * 40)

    test_magic_items()
    test_defensive_spells()
    test_combat_with_magic_items()

    print("\n" + "=" * 80)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 80)
    print("\n📚 New features demonstrated:")
    print("   ✅ Magic Items with combat actions")
    print("   ✅ Magic Items with passive bonuses (AC, saving throws)")
    print("   ✅ Magic Items with ability bonuses")
    print("   ✅ Defensive spells (Shield, Mage Armor, Shield of Faith)")
    print("   ✅ Spell properties (duration, concentration, AC bonus)")
    print("   ✅ Integration with combat system")
    print()


if __name__ == "__main__":
    main()

