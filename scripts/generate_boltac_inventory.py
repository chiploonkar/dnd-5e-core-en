#!/usr/bin/env python3
"""
Script pour générer l'inventaire complet de Boltac avec tous les items magiques
"""

import sys
import os
import json

# Add dnd-5e-core to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from dnd_5e_core.equipment.weapon_factory import SPECIAL_WEAPONS, get_special_weapon
from dnd_5e_core.equipment.armor_factory import SPECIAL_ARMORS, get_special_armor
from dnd_5e_core.equipment.magic_item_factory import PREDEFINED_ITEMS
from dnd_5e_core.data import collections


def generate_boltac_inventory():
    """Génère l'inventaire complet de Boltac"""

    print("=" * 80)
    print("🏪 GÉNÉRATION DE L'INVENTAIRE DE BOLTAC")
    print("=" * 80)

    inventory = {
        "magic_weapons": [],
        "magic_armors": [],
        "magic_items": []
    }

    # 1. Armes magiques
    print("\n📦 Chargement des armes magiques...")
    for weapon_key in SPECIAL_WEAPONS.keys():
        try:
            weapon = get_special_weapon(weapon_key)
            if weapon:
                # Extract rarity properly
                rarity = getattr(weapon, 'rarity', 'unknown')
                if hasattr(rarity, 'value'):
                    rarity = rarity.value
                elif not isinstance(rarity, str):
                    rarity = str(rarity)

                inventory["magic_weapons"].append({
                    "index": weapon.index,
                    "name": weapon.name,
                    "cost_gp": weapon.cost.quantity if weapon.cost else 0,
                    "attack_bonus": getattr(weapon, 'attack_bonus', 0),
                    "damage_bonus": getattr(weapon, 'damage_bonus', 0),
                    "damage_dice": str(weapon.damage_dice) if hasattr(weapon, 'damage_dice') else "1d8",
                    "is_magic": True,
                    "rarity": rarity,
                    "description": weapon.desc[0] if weapon.desc else ""
                })
        except Exception as e:
            print(f"  ⚠️  Erreur chargement {weapon_key}: {e}")

    print(f"  ✅ {len(inventory['magic_weapons'])} armes magiques")

    # 2. Armures magiques
    print("\n📦 Chargement des armures magiques...")
    for armor_key in SPECIAL_ARMORS.keys():
        try:
            armor = get_special_armor(armor_key)
            if armor:
                # Extract rarity properly
                rarity = getattr(armor, 'rarity', 'unknown')
                if hasattr(rarity, 'value'):
                    rarity = rarity.value
                elif not isinstance(rarity, str):
                    rarity = str(rarity)

                inventory["magic_armors"].append({
                    "index": armor.index,
                    "name": armor.name,
                    "cost_gp": armor.cost.quantity if armor.cost else 0,
                    "armor_class_base": armor.armor_class.get('base', 10),
                    "armor_bonus": getattr(armor, 'armor_bonus', 0),
                    "is_magic": True,
                    "rarity": rarity,
                    "damage_resistances": getattr(armor, 'damage_resistances', []),
                    "damage_immunities": getattr(armor, 'damage_immunities', []),
                    "description": armor.desc[0] if armor.desc else ""
                })
        except Exception as e:
            print(f"  ⚠️  Erreur chargement {armor_key}: {e}")

    print(f"  ✅ {len(inventory['magic_armors'])} armures magiques")

    # 3. Objets magiques (anneaux, amulettes, etc.)
    print("\n📦 Chargement des objets magiques...")
    for item_name, item_factory in PREDEFINED_ITEMS.items():
        try:
            item = item_factory()
            if item:
                # Extract cost properly
                cost_value = 0
                if hasattr(item, 'cost'):
                    if hasattr(item.cost, 'quantity'):
                        cost_value = item.cost.quantity
                    elif isinstance(item.cost, (int, float)):
                        cost_value = item.cost

                # Extract rarity properly
                rarity = getattr(item, 'rarity', 'unknown')
                if hasattr(rarity, 'value'):
                    rarity = rarity.value
                elif not isinstance(rarity, str):
                    rarity = str(rarity)

                inventory["magic_items"].append({
                    "index": item.index,
                    "name": item.name,
                    "cost_gp": cost_value,
                    "ac_bonus": getattr(item, 'ac_bonus', 0),
                    "requires_attunement": getattr(item, 'requires_attunement', False),
                    "rarity": rarity,
                    "charges": getattr(item, 'charges', 0),
                    "description": getattr(item, 'description', '')
                })
        except Exception as e:
            print(f"  ⚠️  Erreur chargement {item_name}: {e}")

    print(f"  ✅ {len(inventory['magic_items'])} objets magiques")

    return inventory


def save_inventory(inventory, output_file):
    """Sauvegarde l'inventaire dans un fichier JSON"""
    print(f"\n💾 Sauvegarde de l'inventaire dans {output_file}...")

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=2, ensure_ascii=False)

    print("  ✅ Inventaire sauvegardé")


def display_inventory_summary(inventory):
    """Affiche un résumé de l'inventaire"""
    print("\n" + "=" * 80)
    print("📊 RÉSUMÉ DE L'INVENTAIRE DE BOLTAC")
    print("=" * 80)

    total_items = sum(len(items) for items in inventory.values())
    total_value = 0

    for category, items in inventory.items():
        value = sum(item.get('cost', 0) for item in items)
        total_value += value

        print(f"\n🔹 {category.replace('_', ' ').title()}")
        print(f"   Quantité: {len(items)}")
        print(f"   Valeur totale: {value:,} gp")

        # Top 3 items par catégorie
        if items:
            sorted_items = sorted(items, key=lambda x: x.get('cost', 0), reverse=True)[:3]
            print("   Top 3:")
            for item in sorted_items:
                cost = item.get('cost', 0)
                print(f"      - {item['name']}: {cost:,} gp")

    print("\n" + "-" * 80)
    print(f"📦 TOTAL: {total_items} items")
    print(f"💰 VALEUR TOTALE: {total_value:,} gp")
    print("=" * 80)


def main():
    """Point d'entrée principal"""
    inventory = generate_boltac_inventory()

    # Sauvegarder l'inventaire
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'boltac_inventory.json')

    save_inventory(inventory, output_file)
    display_inventory_summary(inventory)

    print("\n✅ Inventaire de Boltac généré avec succès!")
    print(f"📁 Fichier: {output_file}")


if __name__ == "__main__":
    main()
