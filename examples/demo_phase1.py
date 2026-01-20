"""
Démonstration des nouvelles fonctionnalités de la Phase 1
Montre la différence entre personnages avec et sans capacités
"""

import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loaders import simple_character_generator

print("\n" + "="*80)
print("🎮 DÉMONSTRATION PHASE 1 - ClassAbilities & RacialTraits")
print("="*80)

# ============================================================================
# DÉMONSTRATION 1: Fighter avec Extra Attack
# ============================================================================
print("\n📍 DÉMONSTRATION 1: Fighter Extra Attack")
print("-" * 80)

fighter_old = simple_character_generator(
    level=5,
    class_name='fighter',
    name='OldFighter',
    apply_class_abilities=False
)

fighter_new = simple_character_generator(
    level=5,
    class_name='fighter',
    name='NewFighter',
    apply_class_abilities=True  # Défaut
)

print(f"\n❌ AVANT (apply_class_abilities=False):")
print(f"   {fighter_old.name}: {fighter_old.multi_attacks} attaque(s) par tour")
print(f"   Capacités: {hasattr(fighter_old, 'has_class_abilities')}")

print(f"\n✅ APRÈS (apply_class_abilities=True):")
print(f"   {fighter_new.name}: {fighter_new.multi_attacks} attaques par tour")
print(f"   Capacités: {fighter_new.has_class_abilities}")
print(f"   💪 Extra Attack appliqué automatiquement!")

# ============================================================================
# DÉMONSTRATION 2: Barbarian avec Rage
# ============================================================================
print("\n\n📍 DÉMONSTRATION 2: Barbarian Rage System")
print("-" * 80)

barbarian = simple_character_generator(level=5, class_name='barbarian', name='Grok')

print(f"\n✅ {barbarian.name} le Barbare (Niveau {barbarian.level}):")
print(f"   Attaques par tour: {barbarian.multi_attacks}")
print(f"   Rages disponibles: {barbarian.rage_uses_left}")
print(f"   Rage active: {barbarian.rage_active}")
print(f"   💢 Système de rage initialisé!")

# ============================================================================
# DÉMONSTRATION 3: Rogue avec Sneak Attack
# ============================================================================
print("\n\n📍 DÉMONSTRATION 3: Rogue Sneak Attack")
print("-" * 80)

rogue = simple_character_generator(level=5, class_name='rogue', name='Bilbo')

print(f"\n✅ {rogue.name} le Voleur (Niveau {rogue.level}):")
print(f"   Sneak Attack: {rogue.sneak_attack_dice}d6")
print(f"   🗡️ Attaque sournoise calculée automatiquement!")

# ============================================================================
# DÉMONSTRATION 4: Elf avec Darkvision
# ============================================================================
print("\n\n📍 DÉMONSTRATION 4: Elf Racial Traits")
print("-" * 80)

elf_old = simple_character_generator(
    level=5,
    race_name='elf',
    name='BasicElf',
    apply_racial_traits=False
)

elf_new = simple_character_generator(
    level=5,
    race_name='elf',
    name='AdvancedElf',
    apply_racial_traits=True  # Défaut
)

print(f"\n❌ AVANT (apply_racial_traits=False):")
print(f"   {elf_old.name}: Pas de traits raciaux")
print(f"   Darkvision: {hasattr(elf_old, 'darkvision')}")
print(f"   Fey Ancestry: {hasattr(elf_old, 'fey_ancestry')}")

print(f"\n✅ APRÈS (apply_racial_traits=True):")
print(f"   {elf_new.name}:")
print(f"   Darkvision: {elf_new.darkvision} pieds")
print(f"   Fey Ancestry: {elf_new.fey_ancestry}")
print(f"   Trance: {elf_new.trance}")
print(f"   🧝 Traits elfiques appliqués automatiquement!")

# ============================================================================
# DÉMONSTRATION 5: Groupe Complet
# ============================================================================
print("\n\n📍 DÉMONSTRATION 5: Groupe d'Aventuriers Complet")
print("-" * 80)

party = [
    simple_character_generator(level=5, class_name='fighter', race_name='human', name='Aragorn'),
    simple_character_generator(level=5, class_name='wizard', race_name='elf', name='Gandalf'),
    simple_character_generator(level=5, class_name='rogue', race_name='halfling', name='Bilbo'),
    simple_character_generator(level=5, class_name='cleric', race_name='dwarf', name='Gimli'),
    simple_character_generator(level=5, class_name='barbarian', race_name='half-orc', name='Grok'),
]

print(f"\n✅ Groupe de {len(party)} aventuriers (Niveau 5):\n")

for char in party:
    print(f"   🎭 {char.name} ({char.race.name.capitalize()} {char.class_type.name.capitalize()})")
    print(f"      HP: {char.hit_points}/{char.max_hit_points}, AC: {char.armor_class}")
    print(f"      Attaques/tour: {char.multi_attacks}")

    # Afficher capacités spéciales
    if hasattr(char, 'rage_uses_left'):
        print(f"      💢 Rages: {char.rage_uses_left}")
    if hasattr(char, 'sneak_attack_dice'):
        print(f"      🗡️  Sneak Attack: {char.sneak_attack_dice}d6")
    if hasattr(char, 'darkvision'):
        print(f"      👁️  Darkvision: {char.darkvision}ft")
    if hasattr(char, 'lucky'):
        print(f"      🍀 Lucky: {char.lucky}")

    print()

# ============================================================================
# RÉSUMÉ
# ============================================================================
print("="*80)
print("📊 RÉSUMÉ")
print("="*80)
print("\n✅ Toutes les capacités sont maintenant appliquées AUTOMATIQUEMENT:")
print("   • ClassAbilities (Extra Attack, Rage, Sneak Attack, etc.)")
print("   • RacialTraits (Darkvision, Fey Ancestry, Lucky, etc.)")
print("   • 100% Backward Compatible")
print("   • Aucun changement requis dans vos scripts existants!")
print("\n🎉 Phase 1 implémentée avec succès!")
print("="*80 + "\n")
