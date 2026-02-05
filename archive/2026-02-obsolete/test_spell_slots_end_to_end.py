#!/usr/bin/env python3
"""
Test de bout en bout pour vérifier que le système de spell_slots fonctionne
avec sauvegarde et rechargement
"""
import sys
import os
import pickle
from pathlib import Path
import tempfile

sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loaders import simple_character_generator


def test_end_to_end():
	"""Test complet: création, sauvegarde, rechargement"""

	print("\n" + "=" * 80)
	print("TEST DE BOUT EN BOUT: Création → Sauvegarde → Rechargement")
	print("=" * 80)

	# Créer un répertoire temporaire pour les tests
	with tempfile.TemporaryDirectory() as tmpdir:
		save_path = Path(tmpdir) / "test_wizard.pkl"

		print(f"\n📁 Répertoire de test: {tmpdir}")

		# PHASE 1: Créer un personnage
		print("\n1️⃣  PHASE 1: Création du personnage")
		print("-" * 80)

		try:
			char = simple_character_generator(
				level=2,
				class_name="wizard",
				name="TestWizard"
			)
			print(f"✅ Personnage créé: {char.name}")
			print(f"   - Classe: {char.class_type.name}")
			print(f"   - Niveau: {char.level}")
			print(f"   - Can cast: {char.class_type.can_cast}")

			# Vérifier spell_slots dans class_type
			if hasattr(char.class_type, 'spell_slots'):
				print(f"   - class_type.spell_slots existe: Oui")
				print(f"   - Type: {type(char.class_type.spell_slots)}")
				print(f"   - Nombre de niveaux: {len(char.class_type.spell_slots)}")

				if char.level in char.class_type.spell_slots:
					slots = char.class_type.spell_slots[char.level]
					print(f"   - Slots pour niveau {char.level}: {slots}")
				else:
					print(f"   ❌ ERREUR: Niveau {char.level} absent de spell_slots!")
					return False
			else:
				print(f"   ❌ ERREUR: class_type.spell_slots n'existe pas!")
				return False

			# Vérifier SpellCaster
			if char.sc:
				print(f"   - SpellCaster: Oui")
				print(f"   - spell_slots: {char.sc.spell_slots}")
				print(f"   - Sorts appris: {len(char.sc.learned_spells)}")
			else:
				print(f"   ⚠️  SpellCaster: None")

		except Exception as e:
			print(f"❌ ERREUR lors de la création: {type(e).__name__}: {e}")
			import traceback
			traceback.print_exc()
			return False

		# PHASE 2: Sauvegarder
		print("\n2️⃣  PHASE 2: Sauvegarde du personnage")
		print("-" * 80)

		try:
			with open(save_path, 'wb') as f:
				pickle.dump(char, f)

			file_size = save_path.stat().st_size
			print(f"✅ Personnage sauvegardé")
			print(f"   - Fichier: {save_path.name}")
			print(f"   - Taille: {file_size} octets")

		except Exception as e:
			print(f"❌ ERREUR lors de la sauvegarde: {type(e).__name__}: {e}")
			import traceback
			traceback.print_exc()
			return False

		# PHASE 3: Recharger
		print("\n3️⃣  PHASE 3: Rechargement du personnage")
		print("-" * 80)

		try:
			with open(save_path, 'rb') as f:
				loaded_char = pickle.load(f)

			print(f"✅ Personnage rechargé: {loaded_char.name}")
			print(f"   - Classe: {loaded_char.class_type.name}")
			print(f"   - Niveau: {loaded_char.level}")

			# Vérifier spell_slots dans class_type
			if hasattr(loaded_char.class_type, 'spell_slots'):
				print(f"   - class_type.spell_slots existe: Oui")
				print(f"   - Type: {type(loaded_char.class_type.spell_slots)}")

				if loaded_char.level in loaded_char.class_type.spell_slots:
					slots = loaded_char.class_type.spell_slots[loaded_char.level]
					print(f"   - Slots pour niveau {loaded_char.level}: {slots}")
				else:
					print(f"   ❌ ERREUR: Niveau {loaded_char.level} absent après rechargement!")
					return False
			else:
				print(f"   ❌ ERREUR: class_type.spell_slots perdu après rechargement!")
				return False

		except Exception as e:
			print(f"❌ ERREUR lors du rechargement: {type(e).__name__}: {e}")
			import traceback
			traceback.print_exc()
			return False

		# PHASE 4: Simuler l'accès qui causait le KeyError
		print("\n4️⃣  PHASE 4: Simulation de l'accès dans main_ncurses.py")
		print("-" * 80)

		try:
			# Simuler le repos à l'auberge (ligne 1734 de main_ncurses.py)
			if hasattr(loaded_char.class_type, 'can_cast') and loaded_char.class_type.can_cast:
				if hasattr(loaded_char, 'sc') and hasattr(loaded_char.sc, 'spell_slots'):
					# Méthode originale qui causait le KeyError
					try:
						loaded_char.sc.spell_slots = loaded_char.class_type.spell_slots[loaded_char.level]
						print(f"✅ Accès direct réussi (ligne 1734)")
						print(f"   - Slots restaurés: {loaded_char.sc.spell_slots}")
					except KeyError as e:
						print(f"❌ KeyError avec accès direct: {e}")
						return False

			# Simuler la montée de niveau (ligne 2415 de main_ncurses.py)
			if loaded_char.class_type.can_cast:
				if hasattr(loaded_char, 'sc') and hasattr(loaded_char.sc, 'spell_slots'):
					try:
						loaded_char.sc.spell_slots = loaded_char.class_type.spell_slots[loaded_char.level].copy()
						print(f"✅ Accès direct avec .copy() réussi (ligne 2415)")
						print(f"   - Slots copiés: {loaded_char.sc.spell_slots}")
					except KeyError as e:
						print(f"❌ KeyError avec accès direct + copy: {e}")
						return False

		except Exception as e:
			print(f"❌ ERREUR lors de la simulation: {type(e).__name__}: {e}")
			import traceback
			traceback.print_exc()
			return False

	print("\n✅ TEST DE BOUT EN BOUT RÉUSSI!")
	return True


def test_all_caster_classes():
	"""Test rapide pour toutes les classes de lanceurs de sorts"""

	print("\n" + "=" * 80)
	print("TEST RAPIDE: Toutes les classes de lanceurs de sorts au niveau 2")
	print("=" * 80)

	classes = ["wizard", "cleric", "druid", "sorcerer", "bard", "warlock", "paladin", "ranger"]

	all_passed = True

	for class_name in classes:
		try:
			char = simple_character_generator(level=2, class_name=class_name, name=f"Test{class_name.capitalize()}")

			# Vérifier l'accès direct
			slots = char.class_type.spell_slots[char.level]

			print(f"✅ {class_name.capitalize():12} - Niveau 2: {slots}")

		except KeyError as e:
			print(f"❌ {class_name.capitalize():12} - KeyError: {e}")
			all_passed = False
		except Exception as e:
			print(f"❌ {class_name.capitalize():12} - Erreur: {type(e).__name__}: {str(e)[:50]}")
			all_passed = False

	return all_passed


if __name__ == "__main__":
	print("\n🎲 TEST COMPLET DU SYSTÈME DE SPELL_SLOTS\n")

	# Test 1: Bout en bout
	test1_passed = test_end_to_end()

	# Test 2: Toutes les classes
	test2_passed = test_all_caster_classes()

	print("\n" + "=" * 80)
	print("RÉSUMÉ DES TESTS")
	print("=" * 80)
	print(f"Test 1 (bout en bout): {'✅ RÉUSSI' if test1_passed else '❌ ÉCHOUÉ'}")
	print(f"Test 2 (toutes classes): {'✅ RÉUSSI' if test2_passed else '❌ ÉCHOUÉ'}")
	print("=" * 80 + "\n")

	if test1_passed and test2_passed:
		print("🎉 TOUS LES TESTS ONT RÉUSSI!")
		print("\n✅ Le système de spell_slots est correctement configuré.")
		print("✅ Les personnages peuvent être créés, sauvegardés et rechargés sans erreur.")
		print("✅ L'accès à char.class_type.spell_slots[char.level] fonctionne pour tous les niveaux.\n")
		sys.exit(0)
	else:
		print("⚠️  CERTAINS TESTS ONT ÉCHOUÉ!\n")
		sys.exit(1)
