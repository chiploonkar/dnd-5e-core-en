"""
Test du module special_monster_actions avec extraction JSON
"""
import sys
from pathlib import Path

# Ajouter le chemin du package
sys.path.insert(0, str(Path(__file__).parent.parent))

from dnd_5e_core.entities import get_special_monster_actions


def test_manual_definitions():
    """Test des monstres avec définitions manuelles"""
    print("=" * 80)
    print("TEST 1: Monstres avec Définitions Manuelles")
    print("=" * 80)

    # Ces monstres ont des définitions manuelles dans populate_functions.py
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
            print(f"  ❌ Erreur: {e}")


def test_json_extraction():
    """Test de l'extraction automatique depuis JSON"""
    print("\n" + "=" * 80)
    print("TEST 2: Extraction Automatique depuis JSON")
    print("=" * 80)

    # Ces monstres n'ont pas de définitions manuelles
    # mais devraient être dans bestiary-sublist-data.json
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
            print(f"  ❌ Erreur: {e}")


def test_fallback_behavior():
    """Test du comportement fallback"""
    print("\n" + "=" * 80)
    print("TEST 3: Comportement Fallback")
    print("=" * 80)

    # Test avec un monstre qui n'existe nulle part
    print("\nMonstre inexistant:")
    try:
        actions, abilities, spellcaster = get_special_monster_actions("Monster That Does Not Exist")
        if not actions and not abilities and not spellcaster:
            print("  ✅ Retourne correctement des listes vides")
        else:
            print("  ❌ Devrait retourner des listes vides")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")

    # Test avec JSON fallback désactivé
    print("\nGoblin Boss (JSON fallback désactivé):")
    try:
        actions, abilities, spellcaster = get_special_monster_actions("Goblin Boss", use_json_fallback=False)
        print(f"  ✅ Actions: {len(actions)} (définition manuelle)")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")


def main():
    """Lance tous les tests"""
    print("\n" + "🧪" * 40)
    print("TESTS: Extraction Actions Monstres Étendus")
    print("🧪" * 40 + "\n")

    test_manual_definitions()
    test_json_extraction()
    test_fallback_behavior()

    print("\n" + "=" * 80)
    print("✅ Tests terminés")
    print("=" * 80)


if __name__ == "__main__":
    main()
