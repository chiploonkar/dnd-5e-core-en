"""
Display all available equipment in dnd-5e-core package
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dnd_5e_core.equipment import (
    SPECIAL_ARMORS,
    SPECIAL_WEAPONS,
    MAGIC_ITEMS_REGISTRY,
)


def main():
    print("=" * 80)
    print("DND 5E CORE - COMPLETE EQUIPMENT CATALOG")
    print("=" * 80)

    # Special Armors
    print(f"\n🛡️  SPECIAL ARMORS ({len(SPECIAL_ARMORS)} items)")
    print("-" * 80)
    for i, (index, factory) in enumerate(SPECIAL_ARMORS.items(), 1):
        armor = factory()
        ac = armor.armor_class.get('base', '?')
        cost = armor.cost.quantity
        print(f"{i:2}. {armor.name:40} AC: {ac:2}  Cost: {cost:>7,} gp")

    # Special Weapons
    print(f"\n⚔️  SPECIAL WEAPONS ({len(SPECIAL_WEAPONS)} items)")
    print("-" * 80)
    for i, (index, factory) in enumerate(SPECIAL_WEAPONS.items(), 1):
        weapon = factory()
        damage = str(weapon.damage_dice)
        cost = weapon.cost.quantity
        print(f"{i:2}. {weapon.name:40} Dmg: {damage:6}  Cost: {cost:>7,} gp")

    # Magic Items
    print(f"\n✨ MAGIC ITEMS ({len(MAGIC_ITEMS_REGISTRY)} items)")
    print("-" * 80)

    # Group by category
    categories = {}
    for index, factory in MAGIC_ITEMS_REGISTRY.items():
        item = factory()
        cat = item.item_type.value
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(item)

    for category, items in sorted(categories.items()):
        print(f"\n  {category.upper()} ({len(items)} items):")
        for item in sorted(items, key=lambda x: x.cost.quantity, reverse=True):
            cost = item.cost.quantity
            rarity = item.rarity.value
            attunement = " (attunement)" if item.requires_attunement else ""
            print(f"    • {item.name:35} {cost:>6} gp  [{rarity}]{attunement}")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"  Special Armors:    {len(SPECIAL_ARMORS):3}")
    print(f"  Special Weapons:   {len(SPECIAL_WEAPONS):3}")
    print(f"  Magic Items:       {len(MAGIC_ITEMS_REGISTRY):3}")
    print(f"  " + "-" * 30)
    print(f"  TOTAL:             {len(SPECIAL_ARMORS) + len(SPECIAL_WEAPONS) + len(MAGIC_ITEMS_REGISTRY):3}")
    print("=" * 80)


if __name__ == "__main__":
    main()
