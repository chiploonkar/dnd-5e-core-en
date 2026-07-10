#!/usr/bin/env python3
"""
Migration script to update saved characters with the new spell_slots system
"""
import sys
import os
import pickle
from pathlib import Path

sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

def find_saved_games_dirs():
	"""Finds all possible save directories"""
	possible_dirs = [
		Path.home() / "Saved_Games_DnD_5th",
		Path("/Users/display/PycharmProjects/DnD-5th-Edition-API/Saved_Games_DnD_5th"),
	]

	existing_dirs = [d for d in possible_dirs if d.exists()]
	return existing_dirs


def migrate_character_spell_slots(char):
	"""
	Migrates a character to the new spell_slots system

	Returns:
		bool: True if modifications were made
	"""
	modified = False

	# Verify if it is a spellcaster
	if not hasattr(char, 'class_type') or not hasattr(char.class_type, 'can_cast'):
		return False

	if not char.class_type.can_cast:
		return False

	# Verify if spell_slots is empty or malformed
	if not hasattr(char.class_type, 'spell_slots'):
		print(f"   ⚠️  {char.name}: No spell_slots in class_type")
		char.class_type.spell_slots = {}
		modified = True

	if not isinstance(char.class_type.spell_slots, dict):
		print(f"   ⚠️  {char.name}: spell_slots is not a dict")
		char.class_type.spell_slots = {}
		modified = True

	if not char.class_type.spell_slots or char.level not in char.class_type.spell_slots:
		print(f"   🔧 {char.name}: Rebuilding of spell_slots (level {char.level})")

		# Rebuild spell_slots for all levels
		try:
			from dnd_5e_core.data.progression_loader import get_spell_slots_for_level

			char.class_type.spell_slots = {}
			for lvl in range(1, 21):
				char.class_type.spell_slots[lvl] = get_spell_slots_for_level(char.class_type.index, lvl)

			print(f"      ✅ spell_slots rebuilt successfully")
			modified = True

		except Exception as e:
			print(f"      ❌ Error during rebuilding: {e}")
			return False

	# Update char.sc.spell_slots if necessary
	if hasattr(char, 'sc') and char.sc is not None:
		if hasattr(char.sc, 'spell_slots'):
			# Ensure character spell_slots match their level
			expected_slots = char.class_type.spell_slots.get(char.level, [0] * 10)

			# Verify if current slots are empty or incorrect
			if not char.sc.spell_slots or char.sc.spell_slots == [0] * 10:
				char.sc.spell_slots = expected_slots.copy()
				print(f"      ✅ Restoration of SpellCaster spell_slots")
				modified = True

	return modified


def migrate_saved_games(save_dir, dry_run=False):
	"""
	Migrates all saved characters in a directory

	Args:
		save_dir: Path of the save directory
		dry_run: If True, only lists without modifying
	"""
	print(f"\n📁 Analyzing: {save_dir}")

	# Find all .pkl files in the directory
	char_files = list(save_dir.glob("*.pkl"))

	if not char_files:
		print("   ℹ️  No save files found")
		return

	print(f"   Found {len(char_files)} save file(s)")

	migrated_count = 0
	error_count = 0

	for char_file in char_files:
		try:
			# Load character
			with open(char_file, 'rb') as f:
				char = pickle.load(f)

			# Verify if it is indeed a character
			if not hasattr(char, 'name') or not hasattr(char, 'class_type'):
				print(f"   ⚠️  {char_file.name}: Does not seem to be a valid character")
				continue

			print(f"\n   🔍 {char.name} ({char.class_type.name} Niv.{char.level})")

			# Try migration
			if dry_run:
				print(f"      [DRY RUN] Analysis only")
				modified = migrate_character_spell_slots(char)
				if modified:
					print(f"      🔧 Requires migration")
					migrated_count += 1
			else:
				modified = migrate_character_spell_slots(char)

				if modified:
					# Save the modified character
					backup_file = char_file.with_suffix('.pkl.bak')

					# Create a backup
					import shutil
					shutil.copy2(char_file, backup_file)
					print(f"      💾 Backup created: {backup_file.name}")

					# Save the migrated character
					with open(char_file, 'wb') as f:
						pickle.dump(char, f)

					print(f"      ✅ Migration successful!")
					migrated_count += 1
				else:
					print(f"      ℹ️  No modification necessary")

		except Exception as e:
			print(f"   ❌ Error with {char_file.name}: {type(e).__name__}: {e}")
			error_count += 1

	print(f"\n   📊 Summary: {migrated_count} migrated, {error_count} error(s)")


def main():
	"""Main function"""
	print("\n" + "=" * 80)
	print("MIGRATION OF SPELL_SLOTS FOR SAVED CHARACTERS")
	print("=" * 80)

	# Find save directories
	save_dirs = find_saved_games_dirs()

	if not save_dirs:
		print("\n⚠️  No save directory found!")
		print("\nSearched locations:")
		print("  - ~/Saved_Games_DnD_5th")
		print("  - /Users/display/PycharmProjects/DnD-5th-Edition-API/Saved_Games_DnD_5th")
		return

	print(f"\n✅ Found {len(save_dirs)} save directory/directories")

	# Request confirmation
	if len(sys.argv) > 1 and sys.argv[1] == '--dry-run':
		print("\n🔍 DRY-RUN MODE: Analysis only, no modifications")
		dry_run = True
	else:
		print("\n⚠️  This operation will modify the save files.")
		print("   Backups (.pkl.bak) will be created automatically.")

		response = input("\nContinue? [y/N] ")
		if response.lower() != 'y' and response.lower() != 'o':
			print("\n❌ Operation cancelled")
			return

		dry_run = False

	# Migrate each directory
	for save_dir in save_dirs:
		migrate_saved_games(save_dir, dry_run=dry_run)

	print("\n" + "=" * 80)
	print("✅ MIGRATION COMPLETED")
	print("=" * 80 + "\n")


if __name__ == "__main__":
	main()
