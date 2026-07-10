#!/usr/bin/env python3
"""
Script to generate the bestiary-sublist-data.json file
from individual monster files
"""
import json
import os
from pathlib import Path


def generate_bestiary_data():
    """Generates the bestiary-sublist-data.json file"""
    monsters_dir = Path("data/monsters")

    if not monsters_dir.exists():
        print(f"Error: The directory {monsters_dir} does not exist")
        return

    monsters = []

    # Iterate over all JSON files in the monsters directory
    for json_file in sorted(monsters_dir.glob("*.json")):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                monster_data = json.load(f)

                # Create a simplified entry for the list
                monster_entry = {
                    "index": monster_data.get("index", ""),
                    "name": monster_data.get("name", ""),
                    "size": monster_data.get("size", ""),
                    "type": monster_data.get("type", ""),
                    "subtype": monster_data.get("subtype"),
                    "alignment": monster_data.get("alignment", ""),
                    "cr": monster_data.get("challenge_rating", 0),
                    "xp": monster_data.get("xp", 0),
                    "hp": {
                        "average": monster_data.get("hit_points", 0),
                        "dice": monster_data.get("hit_dice", "")
                    },
                    "ac": monster_data.get("armor_class", 10),
                    "source": "MM",  # Defaults to Monster Manual
                    "str": monster_data.get("strength", 10),
                    "dex": monster_data.get("dexterity", 10),
                    "con": monster_data.get("constitution", 10),
                    "int": monster_data.get("intelligence", 10),
                    "wis": monster_data.get("wisdom", 10),
                    "cha": monster_data.get("charisma", 10),
                }

                monsters.append(monster_entry)

        except json.JSONDecodeError as e:
            print(f"Error loading {json_file}: {e}")
        except Exception as e:
            print(f"Unexpected error for {json_file}: {e}")

    # Save the compiled file
    output_file = monsters_dir / "bestiary-sublist-data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(monsters, f, indent=2, ensure_ascii=False)

    print(f"✓ File generated: {output_file}")
    print(f"✓ Number of monsters: {len(monsters)}")


if __name__ == "__main__":
    generate_bestiary_data()
