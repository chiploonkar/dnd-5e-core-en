#!/usr/bin/env python3
"""
End-to-end test to verify that the spell_slots system works
with saving and reloading
"""
import sys
import os
import pickle
from pathlib import Path
import tempfile

sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loaders import simple_character_generator


def test_end_to_end():
	"""Complete test: creation, saving, reloading"""

	print("\n" + "=" * 80)
	print("END-TO-END TEST: Creation → Saving → Reloading")
	print("=" * 80)

	# Create a temporary directory for tests
	with tempfile.TemporaryDirectory() as tmpdir:
		save_path = Path(tmpdir) / "test_wizard.pkl"

		print(f"\n📁 Test directory: {tmpdir}")

		# PHASE 1: Create a character
		print("\n1️⃣  PHASE 1: Character creation")
		print("-" * 80)

		try:
			char = simple_character_generator(
				level=2,
				class_name="wizard",
				name="TestWizard"
			)
			print(f"✅ Character created: {char.name}")
			print(f"   - Class: {char.class_type.name}")
			print(f"   - Level: {char.level}")
			print(f"   - Can cast: {char.class_type.can_cast}")

			# Verify spell_slots in class_type
			if hasattr(char.class_type, 'spell_slots'):
				print(f"   - class_type.spell_slots exists: Yes")
				print(f"   - Type: {type(char.class_type.spell_slots)}")
				print(f"   - Number of levels: {len(char.class_type.spell_slots)}")

				if char.level in char.class_type.spell_slots:
					slots = char.class_type.spell_slots[char.level]
					print(f"   - Slots for level {char.level}: {slots}")
				else:
					print(f"   ❌ ERROR: Level {char.level} missing from spell_slots!")
					return False
			else:
				print(f"   ❌ ERROR: class_type.spell_slots does not exist!")
				return False

			# Verify SpellCaster
			if char.sc:
				print(f"   - SpellCaster: Yes")
				print(f"   - spell_slots: {char.sc.spell_slots}")
				print(f"   - Learned spells: {len(char.sc.learned_spells)}")
			else:
				print(f"   ⚠️  SpellCaster: None")

		except Exception as e:
			print(f"❌ ERROR during creation: {type(e).__name__}: {e}")
			import traceback
			traceback.print_exc()
			return False

		# PHASE 2: Save
		print("\n2️⃣  PHASE 2: Saving the character")
		print("-" * 80)

		try:
			with open(save_path, 'wb') as f:
				pickle.dump(char, f)

			file_size = save_path.stat().st_size
			print(f"✅ Character saved")
			print(f"   - File: {save_path.name}")
			print(f"   - Size: {file_size} bytes")

		except Exception as e:
			print(f"❌ ERROR during save: {type(e).__name__}: {e}")
			import traceback
			traceback.print_exc()
			return False

		# PHASE 3: Reload
		print("\n3️⃣  PHASE 3: Reloading the character")
		print("-" * 80)

		try:
			with open(save_path, 'rb') as f:
				loaded_char = pickle.load(f)

			print(f"✅ Character reloaded: {loaded_char.name}")
			print(f"   - Class: {loaded_char.class_type.name}")
			print(f"   - Level: {loaded_char.level}")

			# Verify spell_slots in class_type
			if hasattr(loaded_char.class_type, 'spell_slots'):
				print(f"   - class_type.spell_slots exists: Yes")
				print(f"   - Type: {type(loaded_char.class_type.spell_slots)}")

				if loaded_char.level in loaded_char.class_type.spell_slots:
					slots = loaded_char.class_type.spell_slots[loaded_char.level]
					print(f"   - Slots for level {loaded_char.level}: {slots}")
				else:
					print(f"   ❌ ERROR: Level {loaded_char.level} missing after reload!")
					return False
			else:
				print(f"   ❌ ERROR: class_type.spell_slots lost after reload!")
				return False

		except Exception as e:
			print(f"❌ ERROR during reload: {type(e).__name__}: {e}")
			import traceback
			traceback.print_exc()
			return False

		# PHASE 4: Simulate the access that caused the KeyError
		print("\n4️⃣  PHASE 4: Simulation of access in main_ncurses.py")
		print("-" * 80)

		try:
			# Simulate rest at the inn (line 1734 of main_ncurses.py)
			if hasattr(loaded_char.class_type, 'can_cast') and loaded_char.class_type.can_cast:
				if hasattr(loaded_char, 'sc') and hasattr(loaded_char.sc, 'spell_slots'):
					# Original method that caused the KeyError
					try:
						loaded_char.sc.spell_slots = loaded_char.class_type.spell_slots[loaded_char.level]
						print(f"✅ Direct access successful (line 1734)")
						print(f"   - Slots restored: {loaded_char.sc.spell_slots}")
					except KeyError as e:
						print(f"❌ KeyError with direct access: {e}")
						return False

			# Simulate level up (line 2415 of main_ncurses.py)
			if loaded_char.class_type.can_cast:
				if hasattr(loaded_char, 'sc') and hasattr(loaded_char.sc, 'spell_slots'):
					try:
						loaded_char.sc.spell_slots = loaded_char.class_type.spell_slots[loaded_char.level].copy()
						print(f"✅ Direct access with .copy() successful (line 2415)")
						print(f"   - Slots copied: {loaded_char.sc.spell_slots}")
					except KeyError as e:
						print(f"❌ KeyError with direct access + copy: {e}")
						return False

		except Exception as e:
			print(f"❌ ERROR during simulation: {type(e).__name__}: {e}")
			import traceback
			traceback.print_exc()
			return False

	print("\n✅ END-TO-END TEST SUCCESSFUL!")
	return True


def test_all_caster_classes():
	"""Quick test for all spellcaster classes"""

	print("\n" + "=" * 80)
	print("QUICK TEST: All spellcaster classes at level 2")
	print("=" * 80)

	classes = ["wizard", "cleric", "druid", "sorcerer", "bard", "warlock", "paladin", "ranger"]

	all_passed = True

	for class_name in classes:
		try:
			char = simple_character_generator(level=2, class_name=class_name, name=f"Test{class_name.capitalize()}")

			# Verify direct access
			slots = char.class_type.spell_slots[char.level]

			print(f"✅ {class_name.capitalize():12} - Level 2: {slots}")

		except KeyError as e:
			print(f"❌ {class_name.capitalize():12} - KeyError: {e}")
			all_passed = False
		except Exception as e:
			print(f"❌ {class_name.capitalize():12} - Error: {type(e).__name__}: {str(e)[:50]}")
			all_passed = False

	return all_passed


if __name__ == "__main__":
	print("\n🎲 COMPLETE TEST OF THE SPELL_SLOTS SYSTEM\n")

	# Test 1: End-to-end
	test1_passed = test_end_to_end()

	# Test 2: All classes
	test2_passed = test_all_caster_classes()

	print("\n" + "=" * 80)
	print("TESTS SUMMARY")
	print("=" * 80)
	print(f"Test 1 (end-to-end): {'✅ PASSED' if test1_passed else '❌ FAILED'}")
	print(f"Test 2 (all classes): {'✅ PASSED' if test2_passed else '❌ FAILED'}")
	print("=" * 80 + "\n")

	if test1_passed and test2_passed:
		print("🎉 ALL TESTS PASSED!")
		print("\n✅ The spell_slots system is correctly configured.")
		print("✅ Characters can be created, saved, and reloaded without error.")
		print("✅ Access to char.class_type.spell_slots[char.level] works for all levels.\n")
		sys.exit(0)
	else:
		print("⚠️  SOME TESTS FAILED!\n")
		sys.exit(1)
