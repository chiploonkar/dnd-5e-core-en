"""
Test script for monster conditions and magic items with conditions
Demonstrates the new parsing and application system
"""
from dnd_5e_core.data import load_monster
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core.combat import ConditionParser
from dnd_5e_core.equipment import (
    create_wand_of_paralysis,
    create_staff_of_entanglement,
    create_ring_of_blinding,
    create_poisoned_dagger
)


def test_monster_conditions():
    """Test automatic condition parsing from monster actions"""
    print("=" * 80)
    print("TEST 1: MONSTER CONDITIONS PARSING")
    print("=" * 80)

    # Load a monster with condition-applying attacks
    spider = load_monster('giant-spider')

    if spider:
        print(f"\n🕷️  Loaded: {spider.name}")
        print(f"   CR: {spider.challenge_rating}, HP: {spider.hit_points}, AC: {spider.armor_class}")

        # Check actions for conditions
        print(f"\n   Actions ({len(spider.actions)}):")
        for action in spider.actions:
            print(f"   - {action.name} ({action.type.value})")
            if action.effects:
                print(f"     Conditions: {', '.join([e.name for e in action.effects])}")
                for effect in action.effects:
                    print(f"       • {effect.name}: {effect.desc}")
                    if effect.dc_type and effect.dc_value:
                        print(f"         DC {effect.dc_value} {effect.dc_type.value} save")

    # Test with another monster
    print("\n" + "-" * 80)

    medusa = load_monster('medusa')
    if medusa:
        print(f"\n🐍 Loaded: {medusa.name}")
        print(f"   CR: {medusa.challenge_rating}, HP: {medusa.hit_points}, AC: {medusa.armor_class}")

        print(f"\n   Actions ({len(medusa.actions)}):")
        for action in medusa.actions:
            print(f"   - {action.name}")
            if action.effects:
                print(f"     Applies: {', '.join([e.name for e in action.effects])}")

    print()


def test_magic_items_with_conditions():
    """Test magic items that apply conditions"""
    print("=" * 80)
    print("TEST 2: MAGIC ITEMS WITH CONDITIONS")
    print("=" * 80)

    # Create magic items
    wand = create_wand_of_paralysis()
    staff = create_staff_of_entanglement()
    ring = create_ring_of_blinding()
    dagger = create_poisoned_dagger()

    items = [wand, staff, ring, dagger]

    for item in items:
        print(f"\n✨ {item.name}")
        print(f"   Rarity: {item.rarity.value}, Type: {item.item_type.value}")
        print(f"   Requires Attunement: {item.requires_attunement}")

        if item.actions:
            for action in item.actions:
                print(f"\n   Action: {action.name}")
                print(f"   Description: {action.description}")
                print(f"   Uses per day: {action.uses_per_day}")
                print(f"   Recharges: {action.recharge}")

                if action.save_dc and action.save_ability:
                    print(f"   Save: DC {action.save_dc} {action.save_ability.upper()}")

                if action.damage_dice:
                    print(f"   Damage: {action.damage_dice} {action.damage_type or ''}")

                if action.conditions:
                    print(f"   Applies conditions:")
                    for condition in action.conditions:
                        print(f"     • {condition.name}: {condition.desc}")

    print()


def test_combat_with_conditions():
    """Test a combat scenario with conditions being applied"""
    print("=" * 80)
    print("TEST 3: COMBAT WITH CONDITIONS")
    print("=" * 80)

    # Create a character
    fighter = simple_character_generator(
        level=5,
        race_name='human',
        class_name='fighter',
        name='Sir Galahad'
    )

    # Load a monster
    spider = load_monster('giant-spider')

    if not spider or not fighter:
        print("❌ Could not load spider or create fighter")
        return

    print(f"\n⚔️  Combat: {fighter.name} vs {spider.name}")
    print(f"   Fighter: HP {fighter.hit_points}/{fighter.max_hit_points}, AC {fighter.armor_class}")
    print(f"   Spider:  HP {spider.hit_points}/{spider.max_hit_points}, AC {spider.armor_class}")

    # Spider attacks
    print(f"\n🕷️  {spider.name} attacks with web...")

    # Find web attack
    web_action = next((a for a in spider.actions if 'web' in a.name.lower()), None)

    if web_action:
        messages, damage = spider.attack(fighter, [web_action], distance=5.0, verbose=False)
        print(messages)

        # Check if fighter is restrained
        if fighter.conditions:
            print(f"\n   {fighter.name}'s conditions:")
            for condition in fighter.conditions:
                print(f"   🔴 {condition.name}: {condition.desc}")

                # Try to save
                print(f"\n   {fighter.name} attempts to break free...")
                if condition.attempt_save(fighter):
                    print(f"   ✅ {fighter.name} succeeds!")
                else:
                    print(f"   ❌ {fighter.name} remains {condition.name}!")
    else:
        print("   (No web attack found)")

    print()


def test_magic_item_combat():
    """Test using magic items in combat"""
    print("=" * 80)
    print("TEST 4: MAGIC ITEM COMBAT")
    print("=" * 80)

    # Create wizard
    wizard = simple_character_generator(
        level=7,
        race_name='elf',
        class_name='wizard',
        name='Merlin'
    )

    # Create goblin
    goblin = load_monster('goblin')

    if not wizard or not goblin:
        print("❌ Could not create wizard or load goblin")
        return

    print(f"\n✨ {wizard.name} (Wizard) vs {goblin.name}")
    print(f"   Wizard: HP {wizard.hit_points}, AC {wizard.armor_class}")
    print(f"   Goblin: HP {goblin.hit_points}, AC {goblin.armor_class}")

    # Give wizard a wand
    wand = create_wand_of_paralysis()
    wand.attuned = True
    wand.equipped = True

    print(f"\n{wizard.name} wields {wand.name}")

    # Use the wand
    action = wand.actions[0]
    print(f"\n⚡ Using {action.name}...")

    messages, damage, healing = wand.perform_action(action, goblin, wizard, verbose=False)
    print(messages)

    # Check goblin's conditions
    if hasattr(goblin, 'conditions') and goblin.conditions:
        print(f"\n{goblin.name}'s conditions:")
        for condition in goblin.conditions:
            print(f"   🔴 {condition.name}")

    print(f"\nWand uses remaining: {action.remaining_uses}/{action.uses_per_day}")

    print()


def test_condition_parser():
    """Test the condition parser directly"""
    print("=" * 80)
    print("TEST 5: CONDITION PARSER")
    print("=" * 80)

    test_descriptions = [
        "Target must make a DC 15 Constitution saving throw or be paralyzed for 1 minute.",
        "On hit, the target is restrained. DC 13 Strength check to escape.",
        "Creatures in the area must make a DC 14 Wisdom saving throw or be frightened.",
        "The target is grappled and takes 2d6 poison damage. DC 12 Constitution save or poisoned.",
    ]

    for i, desc in enumerate(test_descriptions, 1):
        print(f"\nTest {i}: '{desc}'")
        conditions = ConditionParser.parse_condition_from_description(desc)

        if conditions:
            print(f"   Found {len(conditions)} condition(s):")
            for condition in conditions:
                dc_str = f"DC {condition.dc_value} {condition.dc_type.value}" if condition.dc_type and condition.dc_value else "No DC"
                print(f"   • {condition.name} ({dc_str})")
        else:
            print("   No conditions found")

    print()


def main():
    """Run all tests"""
    print("\n" + "🎲" * 40)
    print("MONSTER CONDITIONS & MAGIC ITEMS - TEST SUITE")
    print("🎲" * 40 + "\n")

    test_monster_conditions()
    test_magic_items_with_conditions()
    test_combat_with_conditions()
    test_magic_item_combat()
    test_condition_parser()

    print("=" * 80)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    main()
