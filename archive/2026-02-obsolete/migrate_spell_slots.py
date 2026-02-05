#!/usr/bin/env python3
"""
Script de migration pour mettre à jour les personnages sauvegardés avec le nouveau système de spell_slots
"""
import sys
import os
import pickle
from pathlib import Path

sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

def find_saved_games_dirs():
	"""Trouve tous les répertoires de sauvegarde possibles"""
	possible_dirs = [
		Path.home() / "Saved_Games_DnD_5th",
		Path("/Users/display/PycharmProjects/DnD-5th-Edition-API/Saved_Games_DnD_5th"),
	]

	existing_dirs = [d for d in possible_dirs if d.exists()]
	return existing_dirs


def migrate_character_spell_slots(char):
	"""
	Migre un personnage vers le nouveau système de spell_slots

	Returns:
		bool: True si des modifications ont été apportées
	"""
	modified = False

	# Vérifier si c'est un lanceur de sorts
	if not hasattr(char, 'class_type') or not hasattr(char.class_type, 'can_cast'):
		return False

	if not char.class_type.can_cast:
		return False

	# Vérifier si spell_slots est vide ou mal formé
	if not hasattr(char.class_type, 'spell_slots'):
		print(f"   ⚠️  {char.name}: Pas de spell_slots dans class_type")
		char.class_type.spell_slots = {}
		modified = True

	if not isinstance(char.class_type.spell_slots, dict):
		print(f"   ⚠️  {char.name}: spell_slots n'est pas un dict")
		char.class_type.spell_slots = {}
		modified = True

	if not char.class_type.spell_slots or char.level not in char.class_type.spell_slots:
		print(f"   🔧 {char.name}: Reconstruction de spell_slots (niveau {char.level})")

		# Reconstruire spell_slots pour tous les niveaux
		try:
			from dnd_5e_core.data.progression_loader import get_spell_slots_for_level

			char.class_type.spell_slots = {}
			for lvl in range(1, 21):
				char.class_type.spell_slots[lvl] = get_spell_slots_for_level(char.class_type.index, lvl)

			print(f"      ✅ spell_slots reconstruit avec succès")
			modified = True

		except Exception as e:
			print(f"      ❌ Erreur lors de la reconstruction: {e}")
			return False

	# Mettre à jour char.sc.spell_slots si nécessaire
	if hasattr(char, 'sc') and char.sc is not None:
		if hasattr(char.sc, 'spell_slots'):
			# S'assurer que les spell_slots du personnage correspondent à son niveau
			expected_slots = char.class_type.spell_slots.get(char.level, [0] * 10)

			# Vérifier si les slots actuels sont vides ou incorrects
			if not char.sc.spell_slots or char.sc.spell_slots == [0] * 10:
				char.sc.spell_slots = expected_slots.copy()
				print(f"      ✅ Restauration des spell_slots du SpellCaster")
				modified = True

	return modified


def migrate_saved_games(save_dir, dry_run=False):
	"""
	Migre tous les personnages sauvegardés dans un répertoire

	Args:
		save_dir: Chemin du répertoire de sauvegarde
		dry_run: Si True, ne fait que lister sans modifier
	"""
	print(f"\n📁 Analyse de: {save_dir}")

	# Chercher tous les fichiers .pkl dans le répertoire
	char_files = list(save_dir.glob("*.pkl"))

	if not char_files:
		print("   ℹ️  Aucun fichier de sauvegarde trouvé")
		return

	print(f"   Trouvé {len(char_files)} fichier(s) de sauvegarde")

	migrated_count = 0
	error_count = 0

	for char_file in char_files:
		try:
			# Charger le personnage
			with open(char_file, 'rb') as f:
				char = pickle.load(f)

			# Vérifier si c'est bien un personnage
			if not hasattr(char, 'name') or not hasattr(char, 'class_type'):
				print(f"   ⚠️  {char_file.name}: Ne semble pas être un personnage valide")
				continue

			print(f"\n   🔍 {char.name} ({char.class_type.name} Niv.{char.level})")

			# Tenter la migration
			if dry_run:
				print(f"      [DRY RUN] Analyse seulement")
				modified = migrate_character_spell_slots(char)
				if modified:
					print(f"      🔧 Nécessite une migration")
					migrated_count += 1
			else:
				modified = migrate_character_spell_slots(char)

				if modified:
					# Sauvegarder le personnage modifié
					backup_file = char_file.with_suffix('.pkl.bak')

					# Créer une sauvegarde
					import shutil
					shutil.copy2(char_file, backup_file)
					print(f"      💾 Backup créé: {backup_file.name}")

					# Sauvegarder le personnage migré
					with open(char_file, 'wb') as f:
						pickle.dump(char, f)

					print(f"      ✅ Migration réussie!")
					migrated_count += 1
				else:
					print(f"      ℹ️  Aucune modification nécessaire")

		except Exception as e:
			print(f"   ❌ Erreur avec {char_file.name}: {type(e).__name__}: {e}")
			error_count += 1

	print(f"\n   📊 Résumé: {migrated_count} migré(s), {error_count} erreur(s)")


def main():
	"""Fonction principale"""
	print("\n" + "=" * 80)
	print("MIGRATION DES SPELL_SLOTS POUR LES PERSONNAGES SAUVEGARDÉS")
	print("=" * 80)

	# Chercher les répertoires de sauvegarde
	save_dirs = find_saved_games_dirs()

	if not save_dirs:
		print("\n⚠️  Aucun répertoire de sauvegarde trouvé!")
		print("\nEmplacements recherchés:")
		print("  - ~/Saved_Games_DnD_5th")
		print("  - /Users/display/PycharmProjects/DnD-5th-Edition-API/Saved_Games_DnD_5th")
		return

	print(f"\n✅ Trouvé {len(save_dirs)} répertoire(s) de sauvegarde")

	# Demander confirmation
	if len(sys.argv) > 1 and sys.argv[1] == '--dry-run':
		print("\n🔍 MODE DRY-RUN: Analyse seulement, aucune modification")
		dry_run = True
	else:
		print("\n⚠️  Cette opération va modifier les fichiers de sauvegarde.")
		print("   Des backups (.pkl.bak) seront créés automatiquement.")

		response = input("\nContinuer? [o/N] ")
		if response.lower() != 'o':
			print("\n❌ Opération annulée")
			return

		dry_run = False

	# Migrer chaque répertoire
	for save_dir in save_dirs:
		migrate_saved_games(save_dir, dry_run=dry_run)

	print("\n" + "=" * 80)
	print("✅ MIGRATION TERMINÉE")
	print("=" * 80 + "\n")


if __name__ == "__main__":
	main()
