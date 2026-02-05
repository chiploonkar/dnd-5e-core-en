#!/usr/bin/env python3
"""
Test pour vérifier que spell_slots est correctement initialisé pour tous les niveaux
"""
import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

from dnd_5e_core.data.loaders import simple_character_generator

def test_spell_slots_all_levels():
	"""Test que spell_slots est présent pour tous les niveaux 1-20"""

	print("\n" + "=" * 80)
	print("TEST: Vérification de spell_slots pour toutes les classes de lanceurs de sorts")
	print("=" * 80)

	spellcasting_classes = ["wizard", "cleric", "druid", "sorcerer", "bard", "warlock", "paladin", "ranger"]
	test_levels = [1, 2, 5, 10, 15, 20]

	all_passed = True

	for class_name in spellcasting_classes:
		print(f"\n🔮 Classe: {class_name.upper()}")

		for level in test_levels:
			try:
				# Créer un personnage
				char = simple_character_generator(
					level=level,
					class_name=class_name,
					name=f"Test{class_name.capitalize()}{level}"
				)

				# Vérifier que spell_slots existe dans class_type
				if not hasattr(char.class_type, 'spell_slots'):
					print(f"   ❌ Niveau {level}: class_type.spell_slots n'existe pas!")
					all_passed = False
					continue

				if not isinstance(char.class_type.spell_slots, dict):
					print(f"   ❌ Niveau {level}: spell_slots n'est pas un dict! Type: {type(char.class_type.spell_slots)}")
					all_passed = False
					continue

				# Vérifier que le niveau existe dans le dictionnaire
				if level not in char.class_type.spell_slots:
					print(f"   ❌ Niveau {level}: clé manquante dans spell_slots dict!")
					print(f"      Clés disponibles: {sorted(char.class_type.spell_slots.keys())}")
					all_passed = False
					continue

				# Récupérer les slots
				slots = char.class_type.spell_slots[level]

				# Vérifier que c'est une liste
				if not isinstance(slots, list):
					print(f"   ❌ Niveau {level}: spell_slots[{level}] n'est pas une liste! Type: {type(slots)}")
					all_passed = False
					continue

				# Vérifier la longueur (devrait être 10: index 0 + niveaux 1-9)
				if len(slots) != 10:
					print(f"   ❌ Niveau {level}: spell_slots a {len(slots)} éléments au lieu de 10!")
					all_passed = False
					continue

				# Afficher les slots non-nuls
				non_zero_slots = [(i, slots[i]) for i in range(1, 10) if slots[i] > 0]
				slots_str = ", ".join([f"L{lvl}:{count}" for lvl, count in non_zero_slots])

				# Vérifier SpellCaster
				if char.sc is None:
					print(f"   ⚠️  Niveau {level}: char.sc est None!")
				elif not hasattr(char.sc, 'spell_slots'):
					print(f"   ⚠️  Niveau {level}: char.sc.spell_slots n'existe pas!")
				else:
					print(f"   ✅ Niveau {level}: {slots_str or 'Aucun slot (normal pour non-casters)'}")

			except Exception as e:
				print(f"   ❌ Niveau {level}: ERREUR - {type(e).__name__}: {str(e)[:80]}")
				import traceback
				traceback.print_exc()
				all_passed = False

	print("\n" + "=" * 80)
	if all_passed:
		print("✅ TOUS LES TESTS ONT RÉUSSI!")
	else:
		print("❌ CERTAINS TESTS ONT ÉCHOUÉ!")
	print("=" * 80 + "\n")

	return all_passed


def test_access_simulation():
	"""Simule l'accès qui causait le KeyError dans main_ncurses.py"""

	print("\n" + "=" * 80)
	print("TEST: Simulation de l'accès dans main_ncurses.py")
	print("=" * 80)

	try:
		# Créer un personnage niveau 2 (le niveau qui causait l'erreur)
		char = simple_character_generator(level=2, class_name="wizard", name="TestWizard2")

		print(f"\n📋 Personnage créé: {char.name} (Niveau {char.level}, {char.class_type.name})")

		# Simuler l'accès qui causait le KeyError
		print(f"\n🔍 Test de l'accès: char.class_type.spell_slots[char.level]")

		# Méthode 1: Accès direct (devrait marcher maintenant)
		try:
			slots_direct = char.class_type.spell_slots[char.level]
			print(f"   ✅ Accès direct réussi: {slots_direct}")
		except KeyError as e:
			print(f"   ❌ KeyError avec accès direct: {e}")
			return False

		# Méthode 2: Accès sécurisé avec .get() (méthode recommandée)
		slots_safe = char.class_type.spell_slots.get(char.level, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		print(f"   ✅ Accès sécurisé réussi: {slots_safe}")

		# Vérifier char.sc
		if char.sc:
			print(f"\n🔮 SpellCaster:")
			print(f"   - spell_slots: {char.sc.spell_slots}")
			print(f"   - learned_spells: {len(char.sc.learned_spells)} sorts")
			print(f"   - dc_value: {char.sc.dc_value}")
		else:
			print(f"\n⚠️  char.sc est None!")

		print("\n✅ Simulation réussie!")
		return True

	except Exception as e:
		print(f"\n❌ ERREUR pendant la simulation: {type(e).__name__}: {e}")
		import traceback
		traceback.print_exc()
		return False


if __name__ == "__main__":
	print("\n🎲 TEST COMPLET DE LA CORRECTION DES SPELL SLOTS\n")

	test1_passed = test_spell_slots_all_levels()
	test2_passed = test_access_simulation()

	print("\n" + "=" * 80)
	print("RÉSUMÉ DES TESTS")
	print("=" * 80)
	print(f"Test 1 (spell_slots pour tous les niveaux): {'✅ RÉUSSI' if test1_passed else '❌ ÉCHOUÉ'}")
	print(f"Test 2 (simulation accès main_ncurses): {'✅ RÉUSSI' if test2_passed else '❌ ÉCHOUÉ'}")
	print("=" * 80 + "\n")

	if test1_passed and test2_passed:
		print("🎉 TOUS LES TESTS ONT RÉUSSI! La correction est fonctionnelle.\n")
		sys.exit(0)
	else:
		print("⚠️  CERTAINS TESTS ONT ÉCHOUÉ. Vérification nécessaire.\n")
		sys.exit(1)
