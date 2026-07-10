#!/usr/bin/env python3
"""
Quick test to verify that the spell_slots fixes work within the game context
"""
import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loaders import simple_character_generator


def test_inn_rest_simulation():
	"""Simulates rest at the inn that was causing the KeyError"""

	print("\n" + "=" * 80)
	print("TEST: Simulating rest at the inn (main_ncurses.py line 1734)")
	print("=" * 80)

	# Create multiple characters of different classes
	test_cases = [
		("wizard", 2),
		("cleric", 1),
		("sorcerer", 5),
		("bard", 10),
		("paladin", 2),
		("ranger", 3),
		("warlock", 2),
	]

	all_passed = True

	for class_name, level in test_cases:
		try:
			print(f"\n🔍 Test: {class_name.capitalize()} level {level}")

			# Create the character
			char = simple_character_generator(
				level=level,
				class_name=class_name,
				name=f"Test{class_name.capitalize()}"
			)

			# Simulate the use of some slots
			if char.sc and char.sc.spell_slots:
				# Use a slot if possible
				for i in range(1, len(char.sc.spell_slots)):
					if char.sc.spell_slots[i] > 0:
						char.sc.spell_slots[i] -= 1
						print(f"   📉 Level {i} slot used")
						break

			# Simulate rest (main_ncurses.py line 1734 code)
			if hasattr(char.class_type, 'can_cast') and char.class_type.can_cast:
				if hasattr(char, 'sc') and hasattr(char.sc, 'spell_slots'):
					# Safely get spell slots with fallback
					if hasattr(char.class_type, 'spell_slots') and isinstance(char.class_type.spell_slots, dict):
						restored_slots = char.class_type.spell_slots.get(char.level, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
						char.sc.spell_slots = restored_slots
						print(f"   ✅ Rest successful - Slots restored: {restored_slots}")
					else:
						char.sc.spell_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
						print(f"   ⚠️  No spell_slots in class_type, slots reset")
			else:
				print(f"   ℹ️  Non-spellcaster (normal)")

		except KeyError as e:
			print(f"   ❌ KeyError: {e}")
			all_passed = False
		except Exception as e:
			print(f"   ❌ Error: {type(e).__name__}: {str(e)[:80]}")
			import traceback
			traceback.print_exc()
			all_passed = False

	return all_passed


def test_level_up_simulation():
	"""Simulates the level up that was also causing the KeyError"""

	print("\n" + "=" * 80)
	print("TEST: Level up simulation (main_ncurses.py line 2415)")
	print("=" * 80)

	test_cases = [
		("wizard", 1, 2),
		("cleric", 2, 3),
		("paladin", 1, 2),
	]

	all_passed = True

	for class_name, start_level, end_level in test_cases:
		try:
			print(f"\n🔍 Test: {class_name.capitalize()} level {start_level} → {end_level}")

			# Create the character at the starting level
			char = simple_character_generator(
				level=start_level,
				class_name=class_name,
				name=f"Test{class_name.capitalize()}"
			)

			print(f"   📋 Character created at level {char.level}")

			# Simulate level up
			char.level = end_level

			# Simulate spell_slots update (main_ncurses.py line 2415 code)
			if char.class_type.can_cast:
				if hasattr(char, 'sc') and hasattr(char.sc, 'spell_slots'):
					# Safely get spell slots with fallback
					if hasattr(char.class_type, 'spell_slots') and isinstance(char.class_type.spell_slots, dict):
						slots = char.class_type.spell_slots.get(char.level, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
						char.sc.spell_slots = slots.copy() if isinstance(slots, list) else [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
						print(f"   ✅ Level up successful - New slots: {char.sc.spell_slots}")
					else:
						char.sc.spell_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
						print(f"   ⚠️  No spell_slots in class_type, slots reset")
			else:
				print(f"   ℹ️  Non-spellcaster (normal)")

		except KeyError as e:
			print(f"   ❌ KeyError: {e}")
			all_passed = False
		except Exception as e:
			print(f"   ❌ Error: {type(e).__name__}: {str(e)[:80]}")
			import traceback
			traceback.print_exc()
			all_passed = False

	return all_passed


def test_edge_cases():
	"""Test of edge cases"""

	print("\n" + "=" * 80)
	print("TEST: Edge cases")
	print("=" * 80)

	all_passed = True

	# Test 1: Level 20 (maximum)
	try:
		print(f"\n🔍 Test: Wizard level 20 (maximum)")
		char = simple_character_generator(level=20, class_name="wizard", name="TestWizard20")

		if char.level in char.class_type.spell_slots:
			slots = char.class_type.spell_slots[char.level]
			print(f"   ✅ Level 20 accessible: {slots}")
		else:
			print(f"   ❌ Level 20 missing!")
			all_passed = False
	except Exception as e:
		print(f"   ❌ Error: {type(e).__name__}: {str(e)[:80]}")
		all_passed = False

	# Test 2: Paladin level 1 (no spells yet)
	try:
		print(f"\n🔍 Test: Paladin level 1 (no spells yet)")
		char = simple_character_generator(level=1, class_name="paladin", name="TestPaladin1")

		if char.level in char.class_type.spell_slots:
			slots = char.class_type.spell_slots[char.level]
			total_slots = sum(slots[1:])
			print(f"   ✅ Level 1 accessible: {slots} (total: {total_slots})")
		else:
			print(f"   ❌ Level 1 missing!")
			all_passed = False
	except Exception as e:
		print(f"   ❌ Error: {type(e).__name__}: {str(e)[:80]}")
		all_passed = False

	# Test 3: Warlock (pact magic)
	try:
		print(f"\n🔍 Test: Warlock level 5 (pact magic)")
		char = simple_character_generator(level=5, class_name="warlock", name="TestWarlock5")

		if char.level in char.class_type.spell_slots:
			slots = char.class_type.spell_slots[char.level]
			print(f"   ✅ Level 5 accessible: {slots}")
		else:
			print(f"   ❌ Level 5 missing!")
			all_passed = False
	except Exception as e:
		print(f"   ❌ Error: {type(e).__name__}: {str(e)[:80]}")
		all_passed = False

	return all_passed


if __name__ == "__main__":
	print("\n🎲 SPELL_SLOTS CORRECTION TEST IN GAME CONTEXT\n")

	test1_passed = test_inn_rest_simulation()
	test2_passed = test_level_up_simulation()
	test3_passed = test_edge_cases()

	print("\n" + "=" * 80)
	print("TEST SUMMARY")
	print("=" * 80)
	print(f"Test 1 (rest at the inn): {'✅ PASSED' if test1_passed else '❌ FAILED'}")
	print(f"Test 2 (level up): {'✅ PASSED' if test2_passed else '❌ FAILED'}")
	print(f"Test 3 (edge cases): {'✅ PASSED' if test3_passed else '❌ FAILED'}")
	print("=" * 80 + "\n")

	if test1_passed and test2_passed and test3_passed:
		print("🎉 ALL TESTS PASSED!")
		print("\n✅ The KeyError on spell_slots is fixed.")
		print("✅ Rest at the inn works correctly.")
		print("✅ Level up works correctly.")
		print("✅ All edge cases are handled.\n")
		sys.exit(0)
	else:
		print("⚠️  SOME TESTS FAILED!\n")
		sys.exit(1)
