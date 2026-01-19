#!/usr/bin/env python3
"""
Script pour générer le fichier bestiary-sublist-data.json
à partir des fichiers individuels de monstres
"""
import json
import os
from pathlib import Path


def generate_bestiary_data():
    """Génère le fichier bestiary-sublist-data.json"""
    monsters_dir = Path("data/monsters")

    if not monsters_dir.exists():
        print(f"Erreur: Le dossier {monsters_dir} n'existe pas")
        return

    monsters = []

    # Parcourir tous les fichiers JSON dans le dossier monsters
    for json_file in sorted(monsters_dir.glob("*.json")):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                monster_data = json.load(f)

                # Créer une entrée simplifiée pour la liste
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
                    "source": "MM",  # Par défaut Monster Manual
                    "str": monster_data.get("strength", 10),
                    "dex": monster_data.get("dexterity", 10),
                    "con": monster_data.get("constitution", 10),
                    "int": monster_data.get("intelligence", 10),
                    "wis": monster_data.get("wisdom", 10),
                    "cha": monster_data.get("charisma", 10),
                }

                monsters.append(monster_entry)

        except json.JSONDecodeError as e:
            print(f"Erreur lors du chargement de {json_file}: {e}")
        except Exception as e:
            print(f"Erreur inattendue pour {json_file}: {e}")

    # Sauvegarder le fichier compilé
    output_file = monsters_dir / "bestiary-sublist-data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(monsters, f, indent=2, ensure_ascii=False)

    print(f"✓ Fichier généré: {output_file}")
    print(f"✓ Nombre de monstres: {len(monsters)}")


if __name__ == "__main__":
    generate_bestiary_data()

