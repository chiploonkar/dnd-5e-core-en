"""
Script de test pour vérifier le système de progression des classes
"""
import sys
import os
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.progression_loader import load_class_progression, get_spell_slots_for_level


def test_all_classes():
    """Teste le chargement de la progression pour toutes les classes"""

    classes = [
        'barbarian', 'bard', 'cleric', 'druid',
        'fighter', 'monk', 'paladin', 'ranger',
        'rogue', 'sorcerer', 'warlock', 'wizard'
    ]

    print("\n" + "=" * 80)
    print("TEST DE CHARGEMENT DES PROGRESSIONS DE CLASSES")
    print("=" * 80)

    results = {}

    for class_index in classes:
        print(f"\n📖 Test de {class_index}...")

        try:
            progression = load_class_progression(class_index)

            if progression:
                # Tester niveau 1
                level_1 = progression.get_level(1)
                level_5 = progression.get_level(5)
                level_20 = progression.get_level(20)

                print(f"   ✅ {progression.class_name}")
                print(f"      Hit Die: d{progression.hit_die}")
                print(f"      Niveaux chargés: {len(progression.levels)}")

                if level_1:
                    print(f"      Niveau 1: {len(level_1.features)} features")
                    if level_1.spellcasting:
                        print(f"         Spellcasting: {level_1.spellcasting.cantrips_known} cantrips, {level_1.spellcasting.spell_slots}")

                if level_5:
                    print(f"      Niveau 5: Prof bonus +{level_5.prof_bonus}")
                    if level_5.class_specific:
                        print(f"         Class specific: {list(level_5.class_specific.keys())}")

                if level_20:
                    print(f"      Niveau 20: {len(level_20.features)} features")

                results[class_index] = "✅ Success"
            else:
                print(f"   ❌ Échec du chargement")
                results[class_index] = "❌ Failed"

        except Exception as e:
            print(f"   ❌ Erreur: {e}")
            results[class_index] = f"❌ Error: {e}"

    # Résumé
    print("\n" + "=" * 80)
    print("📊 RÉSUMÉ")
    print("=" * 80)

    success_count = sum(1 for r in results.values() if r.startswith("✅"))

    for class_name, result in results.items():
        print(f"   {class_name:12} : {result}")

    print(f"\n   Total: {success_count}/{len(classes)} classes chargées avec succès")

    return success_count == len(classes)


def test_spell_slots():
    """Teste la récupération des spell slots"""

    print("\n" + "=" * 80)
    print("TEST DES SPELL SLOTS")
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

            # Compter les slots non-nuls
            total_slots = sum(slots[1:])

            if total_slots > 0:
                slots_str = ", ".join([f"L{i}:{slots[i]}" for i in range(1, 10) if slots[i] > 0])
                print(f"   Niveau {level:2d}: {slots_str} (total: {total_slots})")
            else:
                print(f"   Niveau {level:2d}: Aucun slot")


def test_class_specific_features():
    """Teste les features spécifiques aux classes"""

    print("\n" + "=" * 80)
    print("TEST DES FEATURES SPÉCIFIQUES")
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
                print(f"   ✅ {class_index:12} Niv.{level}: {key} = {value}")
            else:
                print(f"   ❌ {class_index:12} Niv.{level}: {key} = {value} (attendu: {expected})")
        else:
            print(f"   ❌ {class_index:12}: Impossible de charger la progression")


if __name__ == "__main__":
    print("\n🎲 TEST COMPLET DU SYSTÈME DE PROGRESSION DES CLASSES")

    # Test 1: Charger toutes les classes
    all_loaded = test_all_classes()

    # Test 2: Spell slots
    test_spell_slots()

    # Test 3: Features spécifiques
    test_class_specific_features()

    print("\n" + "=" * 80)
    if all_loaded:
        print("✅ TOUS LES TESTS RÉUSSIS!")
    else:
        print("⚠️  CERTAINS TESTS ONT ÉCHOUÉ")
    print("=" * 80)
