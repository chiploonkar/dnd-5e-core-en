from dnd_5e_core.data.loaders import simple_character_generator

print("Test 1: Wizard (full caster, Intelligence)")
print("=" * 60)
wizard = simple_character_generator(level=5, class_name='wizard', name='Gandalf')
print(f"✅ {wizard.name} - Level {wizard.level} {wizard.class_type.name}")
print(f"   Can cast: {wizard.class_type.can_cast}")
print(f"   Spellcasting ability: {wizard.class_type.spellcasting_ability}")
if wizard.sc:
    print(f"   DC Type: {wizard.sc.dc_type}")
    print(f"   DC Value: {wizard.sc.dc_value}")
    print(f"   Spell Slots: {wizard.sc.spell_slots}")
    print(f"   Learned Spells: {len(wizard.sc.learned_spells)} spells")
    if wizard.sc.learned_spells:
        print(f"   First 3 spells:")
        for spell in wizard.sc.learned_spells[:3]:
            print(f"      - {spell.name} (Level {spell.level})")
else:
    print("   ❌ ERROR: No SpellCaster!")

print("\nTest 2: Paladin (half caster, Charisma)")
print("=" * 60)
paladin = simple_character_generator(level=6, class_name='paladin', name='Arthur')
print(f"✅ {paladin.name} - Level {paladin.level} {paladin.class_type.name}")
print(f"   Can cast: {paladin.class_type.can_cast}")
print(f"   Spellcasting ability: {paladin.class_type.spellcasting_ability}")
if paladin.sc:
    print(f"   DC Type: {paladin.sc.dc_type}")
    print(f"   Spell Slots (half-caster): {paladin.sc.spell_slots}")
    print(f"   Learned Spells: {len(paladin.sc.learned_spells)} spells")
else:
    print("   ❌ ERROR: No SpellCaster!")

print("\nTest 3: Bard (full caster, Charisma)")
print("=" * 60)
bard = simple_character_generator(level=3, class_name='bard', name='Devin')
print(f"✅ {bard.name} - Level {bard.level} {bard.class_type.name}")
print(f"   Can cast: {bard.class_type.can_cast}")
print(f"   Spellcasting ability: {bard.class_type.spellcasting_ability}")
if bard.sc:
    print(f"   DC Type: {bard.sc.dc_type}")
    print(f"   Learned Spells: {len(bard.sc.learned_spells)} spells")
else:
    print("   ❌ ERROR: No SpellCaster!")

print("\nTest 4: Fighter (non-caster)")
print("=" * 60)
fighter = simple_character_generator(level=5, class_name='fighter', name='Conan')
print(f"✅ {fighter.name} - Level {fighter.level} {fighter.class_type.name}")
print(f"   Can cast: {fighter.class_type.can_cast}")
print(f"   SpellCaster: {fighter.sc}")
if fighter.sc is None:
    print("   ✅ Correct: No spellcasting for fighter!")

print("\n✅ All tests completed!")

