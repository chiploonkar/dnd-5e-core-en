"""
Test et démonstration du système de sous-classes et multiclassing
"""
import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.mechanics.subclass_system import (
    load_subclass,
    load_subrace,
    list_subclasses_for_class,
    list_subraces_for_race,
    MulticlassCharacter
)


def test_subclasses():
    """Teste le chargement des sous-classes"""

    print("\n" + "=" * 80)
    print("TEST DES SOUS-CLASSES")
    print("=" * 80)

    test_cases = [
        ('wizard', ['abjuration', 'evocation', 'necromancy']),
        ('fighter', ['champion', 'battle-master', 'eldritch-knight']),
        ('cleric', ['life', 'war', 'light']),
        ('rogue', ['thief', 'assassin', 'arcane-trickster']),
    ]

    for class_index, expected_subclasses in test_cases:
        print(f"\n📖 Sous-classes de {class_index.title()}:")

        # Lister toutes les sous-classes
        available = list_subclasses_for_class(class_index)
        print(f"   Disponibles: {len(available)}")

        # Tester le chargement de quelques sous-classes
        for subclass_index in expected_subclasses:
            subclass = load_subclass(subclass_index)

            if subclass:
                print(f"   ✅ {subclass.name}")
                print(f"      Flavor: {subclass.subclass_flavor[:60]}...")
                print(f"      Niveaux: {subclass.subclass_levels}")
            else:
                print(f"   ❌ {subclass_index} - Non trouvé")


def test_subraces():
    """Teste le chargement des sous-races"""

    print("\n" + "=" * 80)
    print("TEST DES SOUS-RACES")
    print("=" * 80)

    test_cases = [
        ('elf', ['high-elf', 'wood-elf', 'dark-elf']),
        ('dwarf', ['hill-dwarf', 'mountain-dwarf']),
        ('halfling', ['lightfoot-halfling', 'stout-halfling']),
    ]

    for race_index, expected_subraces in test_cases:
        print(f"\n📖 Sous-races de {race_index.title()}:")

        # Lister toutes les sous-races
        available = list_subraces_for_race(race_index)
        print(f"   Disponibles: {len(available)}")

        # Tester le chargement
        for subrace_index in expected_subraces:
            subrace = load_subrace(subrace_index)

            if subrace:
                print(f"   ✅ {subrace.name}")
                if subrace.ability_bonuses:
                    bonuses = [f"+{ab.get('bonus', 0)} {ab.get('ability_score', {}).get('index', '')}"
                              for ab in subrace.ability_bonuses]
                    print(f"      Bonus: {', '.join(bonuses)}")
            else:
                print(f"   ❌ {subrace_index} - Non trouvé")


def test_multiclassing():
    """Teste le système de multiclassing"""

    print("\n" + "=" * 80)
    print("TEST DU MULTICLASSING")
    print("=" * 80)

    # Exemple 1: Fighter/Wizard classique
    print(f"\n🎭 Exemple 1: Gish (Fighter/Wizard)")
    gish = MulticlassCharacter("Elric")

    # 5 niveaux de Fighter
    for _ in range(5):
        gish.add_class_level('fighter')
    gish.add_class_level('fighter', 'battle-master')  # Choisir sous-classe

    # 3 niveaux de Wizard
    for _ in range(3):
        gish.add_class_level('wizard')

    print(f"   {gish}")
    print(f"   Niveau total: {gish.get_total_level()}")
    print(f"   Classe primaire: {gish.get_primary_class()}")
    print(f"   Fighter level: {gish.get_class_level('fighter')}")
    print(f"   Wizard level: {gish.get_class_level('wizard')}")

    spell_slots = gish.get_spell_slots_multiclass()
    print(f"   Spell slots: {spell_slots[1:5]}")

    # Exemple 2: Paladin/Warlock
    print(f"\n🎭 Exemple 2: Hexadin (Paladin/Warlock)")
    hexadin = MulticlassCharacter("Arthas")

    # 6 niveaux de Paladin
    for _ in range(6):
        hexadin.add_class_level('paladin')

    # 2 niveaux de Warlock
    for _ in range(2):
        hexadin.add_class_level('warlock')

    print(f"   {hexadin}")
    print(f"   Niveau total: {hexadin.get_total_level()}")
    print(f"   Spell slots: {hexadin.get_spell_slots_multiclass()[1:5]}")

    # Exemple 3: Triple multiclass
    print(f"\n🎭 Exemple 3: Absurde mais possible (Fighter/Rogue/Wizard)")
    triple = MulticlassCharacter("Jack")

    for _ in range(4):
        triple.add_class_level('fighter')
    for _ in range(3):
        triple.add_class_level('rogue')
    for _ in range(3):
        triple.add_class_level('wizard')

    print(f"   {triple}")
    print(f"   Niveau total: {triple.get_total_level()}")


def demo_complete():
    """Démonstration complète"""

    print("\n" + "🎲" * 40)
    print("DÉMONSTRATION COMPLÈTE - SUBCLASSES & MULTICLASSING")
    print("🎲" * 40)

    # Test 1: Sous-classes
    test_subclasses()

    # Test 2: Sous-races
    test_subraces()

    # Test 3: Multiclassing
    test_multiclassing()

    print("\n" + "=" * 80)
    print("✅ DÉMONSTRATION TERMINÉE")
    print("=" * 80)


if __name__ == "__main__":
    demo_complete()
