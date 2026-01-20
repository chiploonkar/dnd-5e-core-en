"""
Test d'intégration des ClassAbilities et RacialTraits
Phase 1: Vérifier que les capacités sont appliquées automatiquement
"""

import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loaders import simple_character_generator


def test_fighter_extra_attack():
    """Test que le fighter niveau 5+ a Extra Attack"""
    print("\n" + "="*80)
    print("TEST 1: Fighter Extra Attack")
    print("="*80)

    # Level 1 fighter - pas d'Extra Attack
    fighter1 = simple_character_generator(level=1, class_name='fighter', name='Fighter1')
    print(f"\n✅ {fighter1.name} (Level {fighter1.level})")
    print(f"   Multi-attacks: {fighter1.multi_attacks}")
    assert fighter1.multi_attacks == 1, "Level 1 fighter should have 1 attack"

    # Level 5 fighter - Extra Attack
    fighter5 = simple_character_generator(level=5, class_name='fighter', name='Fighter5')
    print(f"\n✅ {fighter5.name} (Level {fighter5.level})")
    print(f"   Multi-attacks: {fighter5.multi_attacks}")
    assert fighter5.multi_attacks == 2, "Level 5 fighter should have 2 attacks (Extra Attack)"

    # Level 11 fighter - 3 attacks
    fighter11 = simple_character_generator(level=11, class_name='fighter', name='Fighter11')
    print(f"\n✅ {fighter11.name} (Level {fighter11.level})")
    print(f"   Multi-attacks: {fighter11.multi_attacks}")
    assert fighter11.multi_attacks == 3, "Level 11 fighter should have 3 attacks"

    print("\n✅ TEST FIGHTER EXTRA ATTACK: SUCCÈS")


def test_barbarian_rage():
    """Test que le barbarian a le système de rage"""
    print("\n" + "="*80)
    print("TEST 2: Barbarian Rage")
    print("="*80)

    barbarian = simple_character_generator(level=5, class_name='barbarian', name='Grok')
    print(f"\n✅ {barbarian.name} (Level {barbarian.level} Barbarian)")

    # Vérifier que les attributs de rage existent
    assert hasattr(barbarian, 'rage_active'), "Barbarian should have rage_active attribute"
    assert hasattr(barbarian, 'rage_uses_left'), "Barbarian should have rage_uses_left attribute"

    print(f"   Rage Active: {barbarian.rage_active}")
    print(f"   Rage Uses Left: {barbarian.rage_uses_left}")
    print(f"   Has Class Abilities: {barbarian.has_class_abilities}")

    # Level 5 = 3 rages par jour
    assert barbarian.rage_uses_left == 3, f"Level 5 barbarian should have 3 rages, got {barbarian.rage_uses_left}"

    print("\n✅ TEST BARBARIAN RAGE: SUCCÈS")


def test_rogue_sneak_attack():
    """Test que le rogue a Sneak Attack"""
    print("\n" + "="*80)
    print("TEST 3: Rogue Sneak Attack")
    print("="*80)

    rogue = simple_character_generator(level=5, class_name='rogue', name='Bilbo')
    print(f"\n✅ {rogue.name} (Level {rogue.level} Rogue)")

    assert hasattr(rogue, 'sneak_attack_dice'), "Rogue should have sneak_attack_dice attribute"

    print(f"   Sneak Attack Dice: {rogue.sneak_attack_dice}d6")
    print(f"   Has Class Abilities: {rogue.has_class_abilities}")

    # Level 5 = 3d6 sneak attack
    expected_dice = (5 + 1) // 2
    assert rogue.sneak_attack_dice == expected_dice, f"Level 5 rogue should have {expected_dice}d6 sneak attack"

    print("\n✅ TEST ROGUE SNEAK ATTACK: SUCCÈS")


def test_elf_darkvision():
    """Test que l'elfe a Darkvision"""
    print("\n" + "="*80)
    print("TEST 4: Elf Darkvision & Fey Ancestry")
    print("="*80)

    elf = simple_character_generator(level=5, race_name='elf', name='Legolas')
    print(f"\n✅ {elf.name} (Elf)")

    assert hasattr(elf, 'darkvision'), "Elf should have darkvision attribute"
    assert hasattr(elf, 'fey_ancestry'), "Elf should have fey_ancestry attribute"
    assert hasattr(elf, 'trance'), "Elf should have trance attribute"
    assert hasattr(elf, 'has_racial_traits'), "Elf should have has_racial_traits flag"

    print(f"   Darkvision: {elf.darkvision} ft")
    print(f"   Fey Ancestry: {elf.fey_ancestry}")
    print(f"   Trance: {elf.trance}")
    print(f"   Has Racial Traits: {elf.has_racial_traits}")

    assert elf.darkvision == 60, "Elf should have 60 ft darkvision"
    assert elf.fey_ancestry == True, "Elf should have Fey Ancestry"

    print("\n✅ TEST ELF TRAITS: SUCCÈS")


def test_dwarf_resilience():
    """Test que le dwarf a Dwarven Resilience"""
    print("\n" + "="*80)
    print("TEST 5: Dwarf Dwarven Resilience")
    print("="*80)

    dwarf = simple_character_generator(level=5, race_name='dwarf', name='Gimli')
    print(f"\n✅ {dwarf.name} (Dwarf)")

    assert hasattr(dwarf, 'darkvision'), "Dwarf should have darkvision attribute"
    assert hasattr(dwarf, 'dwarven_resilience'), "Dwarf should have dwarven_resilience attribute"
    assert hasattr(dwarf, 'has_racial_traits'), "Dwarf should have has_racial_traits flag"

    print(f"   Darkvision: {dwarf.darkvision} ft")
    print(f"   Dwarven Resilience: {dwarf.dwarven_resilience}")
    print(f"   Has Racial Traits: {dwarf.has_racial_traits}")

    assert dwarf.dwarven_resilience == True, "Dwarf should have Dwarven Resilience"

    print("\n✅ TEST DWARF TRAITS: SUCCÈS")


def test_halfling_lucky():
    """Test que le halfling a Lucky"""
    print("\n" + "="*80)
    print("TEST 6: Halfling Lucky & Brave")
    print("="*80)

    halfling = simple_character_generator(level=5, race_name='halfling', name='Frodo')
    print(f"\n✅ {halfling.name} (Halfling)")

    assert hasattr(halfling, 'lucky'), "Halfling should have lucky attribute"
    assert hasattr(halfling, 'brave'), "Halfling should have brave attribute"
    assert hasattr(halfling, 'has_racial_traits'), "Halfling should have has_racial_traits flag"

    print(f"   Lucky: {halfling.lucky}")
    print(f"   Brave: {halfling.brave}")
    print(f"   Has Racial Traits: {halfling.has_racial_traits}")

    assert halfling.lucky == True, "Halfling should have Lucky trait"
    assert halfling.brave == True, "Halfling should have Brave trait"

    print("\n✅ TEST HALFLING TRAITS: SUCCÈS")


def test_wizard_spellcasting():
    """Test que le wizard a des sorts"""
    print("\n" + "="*80)
    print("TEST 7: Wizard Spellcasting")
    print("="*80)

    wizard = simple_character_generator(level=5, class_name='wizard', name='Gandalf')
    print(f"\n✅ {wizard.name} (Level {wizard.level} Wizard)")

    assert wizard.sc is not None, "Wizard should have SpellCaster"
    assert hasattr(wizard.sc, 'learned_spells'), "Wizard should have learned_spells"

    print(f"   Spellcaster: {wizard.sc is not None}")
    print(f"   Learned Spells: {len(wizard.sc.learned_spells)}")
    print(f"   Spell Slots: {wizard.sc.spell_slots[1:6]}")

    assert len(wizard.sc.learned_spells) > 0, "Wizard should have learned spells"
    assert wizard.sc.spell_slots[1] > 0, "Wizard should have 1st level spell slots"

    print("\n✅ TEST WIZARD SPELLCASTING: SUCCÈS")


def test_disable_abilities():
    """Test que les capacités peuvent être désactivées"""
    print("\n" + "="*80)
    print("TEST 8: Disable Abilities & Traits")
    print("="*80)

    fighter = simple_character_generator(
        level=5,
        class_name='fighter',
        name='BasicFighter',
        apply_class_abilities=False,
        apply_racial_traits=False
    )

    print(f"\n✅ {fighter.name} (abilities disabled)")
    print(f"   Multi-attacks: {fighter.multi_attacks}")
    print(f"   Has Class Abilities: {hasattr(fighter, 'has_class_abilities')}")
    print(f"   Has Racial Traits: {hasattr(fighter, 'has_racial_traits')}")

    # Sans le flag has_class_abilities, utilise le calcul par défaut (niveau 5 fighter = 2 attaques)
    assert fighter.multi_attacks == 2, "Level 5 fighter uses default calculation (2 attacks)"
    assert not hasattr(fighter, 'has_class_abilities'), "Should not have has_class_abilities flag"
    assert not hasattr(fighter, 'has_racial_traits'), "Should not have has_racial_traits flag"

    # Vérifier qu'il n'a pas les attributs de rage (si c'était un barbare)
    assert not hasattr(fighter, 'rage_active'), "Should not have barbarian abilities"

    print("\n✅ TEST DISABLE ABILITIES: SUCCÈS")


def run_all_tests():
    """Exécuter tous les tests"""
    print("\n" + "🧪"*40)
    print("PHASE 1 - INTEGRATION TESTS")
    print("🧪"*40)

    try:
        test_fighter_extra_attack()
        test_barbarian_rage()
        test_rogue_sneak_attack()
        test_elf_darkvision()
        test_dwarf_resilience()
        test_halfling_lucky()
        test_wizard_spellcasting()
        test_disable_abilities()

        print("\n" + "="*80)
        print("🎉 TOUS LES TESTS RÉUSSIS!")
        print("="*80)
        print("\n✅ Phase 1 Implémentée avec Succès:")
        print("   - ClassAbilities automatiquement appliquées")
        print("   - RacialTraits automatiquement appliqués")
        print("   - Backward compatibility préservée")
        print("   - 8 tests passés")

        return True

    except AssertionError as e:
        print(f"\n❌ TEST ÉCHOUÉ: {e}")
        import traceback
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"\n❌ ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
