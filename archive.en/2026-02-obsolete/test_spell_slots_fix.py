#!/usr/bin/env python3
"""
Test to verify that spell_slots is correctly initialized for all levels
"""
import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loaders import simple_character_generator

def test_spell_slots_all_levels():
	"""Test that spell_slots is present for all levels 1-20"""

	print("\n" + "=" * 80)
	print("TEST: Verification of spell_slots for all spellcasting classes")
	print("=" * 80)

	spellcasting_classes = ["wizard", "cleric", "druid", "sorcerer", "bard", "warlock", "paladin", "ranger"]
	test_levels = [1, 2, 5, 10, 15, 20]

	all_passed = True

	for class_name in spellcasting_classes:
		print(f"\n🔮 Class: {class_name.upper()}")

		for level in test_levels:
			try:
				# Create a character
				char = simple_character_generator(
					level=level,
					class_name=class_name,
					name=f"Test{class_name.capitalize()}{level}"
				)

				# Verify that spell_slots exists in class_type
				if not hasattr(char.class_type, 'spell_slots'):
					print(f"   ❌ Level {level}: class_type.spell_slots does not exist!")
					all_passed = False
					continue

				if not isinstance(char.class_type.spell_slots, dict):
					print(f"   ❌ Level {level}: spell_slots is not a dict! Type: {type(char.class_type.spell_slots)}")
					all_passed = False
					continue

				# Verify that the level exists in the dictionary
				if level not in char.class_type.spell_slots:
					print(f"   ❌ Level {level}: missing key in spell_slots dict!")
					print(f"      Available keys: {sorted(char.class_type.spell_slots.keys())}")
					all_passed = False
					continue

				# Get slots
				slots = char.class_type.spell_slots[level]

				# Verify that it is a list
				if not isinstance(slots, list):
					print(f"   ❌ Level {level}: spell_slots[{level}] is not a list! Type: {type(slots)}")
					all_passed = False
					continue

				# Verify length (should be 10: index 0 + levels 1-9)
				if len(slots) != 10:
					print(f"   ❌ Level {level}: spell_slots has {len(slots)} elements instead of 10!")
					all_passed = False
					continue

				# Display non-zero slots
				non_zero_slots = [(i, slots[i]) for i in range(1, 10) if slots[i] > 0]
				slots_str = ", ".join([f"L{lvl}:{count}" for lvl, count in non_zero_slots])

				# Verify SpellCaster
				if char.sc is None:
					print(f"   ⚠️  Level {level}: char.sc is None!")
				elif not hasattr(char.sc, 'spell_slots'):
					print(f"   ⚠️  Level {level}: char.sc.spell_slots does not exist!")
				else:
					print(f"   ✅ Level {level}: {slots_str or 'No slots (normal for non-casters)'}")

			except Exception as e:
				print(f"   ❌ Level {level}: ERROR - {type(e).__name__}: {str(e)[:80]}")
				import traceback
				traceback.print_exc()
				all_passed = False

	print("\n" + "=" * 80)
	if all_passed:
		print("✅ ALL TESTS PASSED!")
	else:
		print("❌ SOME TESTS FAILED!")
	print("=" * 80 + "\n")

	return all_passed


def test_access_simulation():
	"""Simulates the access that caused the KeyError in main_ncurses.py"""

	print("\n" + "=" * 80)
	print("TEST: Simulation of access in main_ncurses.py")
	print("=" * 80)

	try:
		# Create a level 2 character (the level that caused the error)
		char = simple_character_generator(level=2, class_name="wizard", name="TestWizard2")

		print(f"\n📋 Character created: {char.name} (Level {char.level}, {char.class_type.name})")

		# Simulate the access that caused the KeyError
		print(f"\n🔍 Test access: char.class_type.spell_slots[char.level]")

		# Method 1: Direct access (should work now)
		try:
			slots_direct = char.class_type.spell_slots[char.level]
			print(f"   ✅ Direct access successful: {slots_direct}")
		except KeyError as e:
			print(f"   ❌ KeyError with direct access: {e}")
			return False

		# Method 2: Secure access with .get() (recommended method)
		slots_safe = char.class_type.spell_slots.get(char.level, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		print(f"   ✅ Secure access successful: {slots_safe}")

		# Verify char.sc
		if char.sc:
			print(f"\n🔮 SpellCaster:")
			print(f"   - spell_slots: {char.sc.spell_slots}")
			print(f"   - learned_spells: {len(char.sc.learned_spells)} spells")
			print(f"   - dc_value: {char.sc.dc_value}")
		else:
			print(f"\n⚠️  char.sc is None!")

		print("\n✅ Simulation successful!")
		return True

	except Exception as e:
		print(f"\n❌ ERROR during simulation: {type(e).__name__}: {e}")
		import traceback
		traceback.print_exc()
		return False


if __name__ == "__main__":
	print("\n🎲 COMPLETE SPELL SLOTS FIX TEST\n")

	test1_passed = test_spell_slots_all_levels()
	test2_passed = test_access_simulation()

	print("\n" + "=" * 80)
	print("TEST SUMMARY")
	print("=" * 80)
	print(f"Test 1 (spell_slots for all levels): {'✅ PASSED' if test1_passed else '❌ FAILED'}")
	print(f"Test 2 (simulation of main_ncurses access): {'✅ PASSED' if test2_passed else '❌ FAILED'}")
	print("=" * 80 + "\n")

	if test1_passed and test2_passed:
		print("🎉 ALL TESTS PASSED! The fix is functional.\n")
		sys.exit(0)
	else:
		print("⚠️  SOME TESTS FAILED. Verification needed.\n")
		sys.exit(1)
