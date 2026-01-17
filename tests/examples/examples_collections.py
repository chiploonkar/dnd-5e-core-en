"""
Exemples d'Utilisation des Nouvelles Fonctions de Collections
===============================================================

Ce script montre comment utiliser les nouvelles fonctions de chargement
d'objets depuis collections.py
"""

from dnd_5e_core.data import (
    load_all_monsters, filter_monsters,
    load_all_spells, filter_spells
)


def example_1_load_all():
    """Exemple 1: Charger tous les monstres"""
    print("=" * 60)
    print("EXEMPLE 1: Charger tous les monstres")
    print("=" * 60)

    monsters = load_all_monsters()
    print(f"\nTotal: {len(monsters)} monstres chargés")

    print("\n5 premiers monstres:")
    for monster in monsters[:5]:
        print(f"  - {monster.name}: CR {monster.challenge_rating}, HP {monster.hit_points}")


def example_2_filter_by_cr():
    """Exemple 2: Filtrer par Challenge Rating"""
    print("\n" + "=" * 60)
    print("EXEMPLE 2: Filtrer par Challenge Rating")
    print("=" * 60)

    # Monstres débutants (CR 0-1)
    beginner_monsters = filter_monsters(max_cr=1)
    print(f"\nMonstres débutants (CR 0-1): {len(beginner_monsters)} trouvés")
    for monster in beginner_monsters[:5]:
        print(f"  - {monster.name}: CR {monster.challenge_rating}")

    # Monstres niveau moyen (CR 5-10)
    mid_level = filter_monsters(min_cr=5, max_cr=10)
    print(f"\nMonstres niveau moyen (CR 5-10): {len(mid_level)} trouvés")
    for monster in mid_level[:5]:
        print(f"  - {monster.name}: CR {monster.challenge_rating}")


def example_3_filter_by_name():
    """Exemple 3: Rechercher par nom"""
    print("\n" + "=" * 60)
    print("EXEMPLE 3: Rechercher par nom")
    print("=" * 60)

    # Tous les dragons
    dragons = filter_monsters(name_contains="dragon")
    print(f"\nDragons: {len(dragons)} trouvés")
    for dragon in dragons[:5]:
        print(f"  - {dragon.name}: CR {dragon.challenge_rating}")

    # Tous les gobelins
    goblins = filter_monsters(name_contains="goblin")
    print(f"\nGobelins: {len(goblins)} trouvés")
    for goblin in goblins:
        print(f"  - {goblin.name}: CR {goblin.challenge_rating}")


def example_4_spells_by_level():
    """Exemple 4: Sorts par niveau"""
    print("\n" + "=" * 60)
    print("EXEMPLE 4: Sorts par niveau")
    print("=" * 60)

    # Cantrips de wizard
    wizard_cantrips = filter_spells(level=0, class_name="wizard")
    print(f"\nCantrips de wizard: {len(wizard_cantrips)} trouvés")
    for spell in wizard_cantrips[:5]:
        print(f"  - {spell.name} ({spell.school})")

    # Sorts niveau 3
    level_3_spells = filter_spells(level=3)
    print(f"\nSorts niveau 3 (toutes classes): {len(level_3_spells)} trouvés")
    for spell in level_3_spells[:5]:
        print(f"  - {spell.name}")


def example_5_spells_by_school():
    """Exemple 5: Sorts par école de magie"""
    print("\n" + "=" * 60)
    print("EXEMPLE 5: Sorts par école de magie")
    print("=" * 60)

    # Sorts d'évocation
    evocation_spells = filter_spells(school="evocation")
    print(f"\nSorts d'évocation: {len(evocation_spells)} trouvés")
    for spell in evocation_spells[:5]:
        print(f"  - {spell.name} (Niveau {spell.level})")

    # Sorts de nécromancie
    necromancy_spells = filter_spells(school="necromancy")
    print(f"\nSorts de nécromancie: {len(necromancy_spells)} trouvés")
    for spell in necromancy_spells[:5]:
        print(f"  - {spell.name} (Niveau {spell.level})")


def example_6_combined_filters():
    """Exemple 6: Combinaison de filtres"""
    print("\n" + "=" * 60)
    print("EXEMPLE 6: Combinaison de filtres")
    print("=" * 60)

    # Dragons puissants (CR 15+)
    powerful_dragons = filter_monsters(min_cr=15, name_contains="dragon")
    print(f"\nDragons puissants (CR 15+): {len(powerful_dragons)} trouvés")
    for dragon in powerful_dragons:
        print(f"  - {dragon.name}: CR {dragon.challenge_rating}, HP {dragon.hit_points}")

    # Cantrips d'évocation pour wizard
    wizard_evocation_cantrips = filter_spells(
        level=0,
        school="evocation",
        class_name="wizard"
    )
    print(f"\nCantrips d'évocation (wizard): {len(wizard_evocation_cantrips)} trouvés")
    for spell in wizard_evocation_cantrips:
        print(f"  - {spell.name}")


def example_7_practical_use_case():
    """Exemple 7: Cas d'usage pratique - Générateur de rencontre"""
    print("\n" + "=" * 60)
    print("EXEMPLE 7: Générateur de rencontre aléatoire")
    print("=" * 60)

    import random

    party_level = 5
    print(f"\nGroupe de niveau {party_level}")

    # Trouver des monstres appropriés
    min_cr = max(0, party_level - 2)
    max_cr = party_level + 1

    suitable_monsters = filter_monsters(min_cr=min_cr, max_cr=max_cr)
    print(f"Monstres appropriés (CR {min_cr}-{max_cr}): {len(suitable_monsters)} disponibles")

    # Générer une rencontre aléatoire
    num_monsters = 3
    encounter = random.sample(suitable_monsters, min(num_monsters, len(suitable_monsters)))

    print(f"\nRencontre générée ({num_monsters} monstres):")
    total_xp = 0
    for monster in encounter:
        print(f"  - {monster.name}: CR {monster.challenge_rating}, XP {monster.xp}")
        total_xp += monster.xp

    print(f"\nXP total: {total_xp}")


if __name__ == "__main__":
    print("\n🎲 D&D 5e Core - Exemples d'Utilisation des Collections\n")

    example_1_load_all()
    example_2_filter_by_cr()
    example_3_filter_by_name()
    example_4_spells_by_level()
    example_5_spells_by_school()
    example_6_combined_filters()
    example_7_practical_use_case()

    print("\n" + "=" * 60)
    print("✅ Tous les exemples exécutés avec succès!")
    print("=" * 60)

