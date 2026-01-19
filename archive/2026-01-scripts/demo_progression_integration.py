"""
Script de démonstration du système de progression des classes
Montre l'intégration avec simple_character_generator et le level up
"""
import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loaders import simple_character_generator, level_up_character


def demo_character_creation_with_progression():
    """Démo de création de personnage avec progression automatique"""

    print("\n" + "🎲" * 40)
    print("DÉMONSTRATION DU SYSTÈME DE PROGRESSION INTÉGRÉ")
    print("🎲" * 40)

    # =============================================================================
    # PARTIE 1: Création d'un Wizard niveau 1
    # =============================================================================
    print("\n📖 PARTIE 1: CRÉATION D'UN WIZARD NIVEAU 1")
    print("=" * 80)

    wizard = simple_character_generator(1, 'elf', 'wizard', 'Gandalf')

    print(f"✨ {wizard.name} créé!")
    print(f"   Race: {wizard.race.name}")
    print(f"   Classe: {wizard.class_type.name}")
    print(f"   Niveau: {wizard.level}")
    print(f"   HP: {wizard.hit_points}/{wizard.max_hit_points}")
    print(f"   AC: {wizard.armor_class}")

    if hasattr(wizard, 'sc') and wizard.sc:
        print(f"   🔮 Spellcaster: Oui")
        print(f"      Spell slots: {wizard.sc.spell_slots[1:6]}")
        print(f"      Sorts connus: {len(wizard.sc.spells_known)}")

    # =============================================================================
    # PARTIE 2: Level Up au niveau 2
    # =============================================================================
    print("\n📖 PARTIE 2: LEVEL UP AU NIVEAU 2")
    print("=" * 80)

    wizard = level_up_character(wizard, 2, verbose=True)

    print(f"\n   Statut actuel:")
    print(f"   Niveau: {wizard.level}")
    print(f"   HP: {wizard.hit_points}/{wizard.max_hit_points}")

    if hasattr(wizard, 'sc') and wizard.sc:
        print(f"   Spell slots: {wizard.sc.spell_slots[1:6]}")

    # =============================================================================
    # PARTIE 3: Progression jusqu'au niveau 5
    # =============================================================================
    print("\n📖 PARTIE 3: PROGRESSION JUSQU'AU NIVEAU 5")
    print("=" * 80)

    for new_level in [3, 4, 5]:
        print(f"\n--- Passage au niveau {new_level} ---")
        wizard = level_up_character(wizard, new_level, verbose=True)

    print(f"\n   Statut final:")
    print(f"   {wizard.name} - Niveau {wizard.level} {wizard.class_type.name}")
    print(f"   HP: {wizard.hit_points}/{wizard.max_hit_points}")
    print(f"   AC: {wizard.armor_class}")

    if hasattr(wizard, 'sc') and wizard.sc:
        total_slots = sum(wizard.sc.spell_slots[1:])
        print(f"   Spell slots: {wizard.sc.spell_slots[1:6]} (total: {total_slots})")

    # =============================================================================
    # PARTIE 4: Test avec d'autres classes
    # =============================================================================
    print("\n📖 PARTIE 4: TEST AVEC D'AUTRES CLASSES")
    print("=" * 80)

    test_classes = [
        ('fighter', 'Conan'),
        ('cleric', 'Gimli'),
        ('rogue', 'Bilbo'),
        ('barbarian', 'Grok'),
    ]

    for class_name, name in test_classes:
        print(f"\n🎭 Création d'un {class_name}: {name}")

        char = simple_character_generator(5, 'human', class_name, name)

        print(f"   Niveau: {char.level}")
        print(f"   HP: {char.hit_points}/{char.max_hit_points}")
        print(f"   Hit Die: d{char.class_type.hit_die}")

        if hasattr(char, 'sc') and char.sc:
            total_slots = sum(char.sc.spell_slots[1:])
            print(f"   Spellcaster: Oui ({total_slots} spell slots)")
        else:
            print(f"   Spellcaster: Non")

    print("\n" + "=" * 80)
    print("✅ DÉMONSTRATION TERMINÉE")
    print("=" * 80)


if __name__ == "__main__":
    demo_character_creation_with_progression()
