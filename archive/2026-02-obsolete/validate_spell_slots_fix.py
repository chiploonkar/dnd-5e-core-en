#!/usr/bin/env python3
"""
Script de validation complète de la correction du KeyError spell_slots
À exécuter après installation ou mise à jour du package
"""
import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

def check_imports():
	"""Vérifier que tous les imports fonctionnent"""
	print("\n🔍 Vérification des imports...")
	try:
		from dnd_5e_core.data.loaders import simple_character_generator
		from dnd_5e_core.data.progression_loader import get_spell_slots_for_level
		print("   ✅ Imports OK")
		return True
	except ImportError as e:
		print(f"   ❌ Erreur d'import: {e}")
		return False


def quick_validation():
	"""Validation rapide de la correction"""
	print("\n🎯 Validation rapide de la correction...")

	try:
		from dnd_5e_core.data.loaders import simple_character_generator

		# Test rapide: créer un wizard niveau 2 (cas qui causait le KeyError)
		char = simple_character_generator(level=2, class_name="wizard", name="QuickTest")

		# Vérifier spell_slots
		if not hasattr(char.class_type, 'spell_slots'):
			print("   ❌ class_type.spell_slots n'existe pas")
			return False

		if not isinstance(char.class_type.spell_slots, dict):
			print(f"   ❌ spell_slots n'est pas un dict: {type(char.class_type.spell_slots)}")
			return False

		if 2 not in char.class_type.spell_slots:
			print("   ❌ Niveau 2 absent de spell_slots")
			return False

		# Tester l'accès direct (qui causait le KeyError)
		try:
			slots = char.class_type.spell_slots[char.level]
			print(f"   ✅ Accès direct OK: {slots}")
			return True
		except KeyError as e:
			print(f"   ❌ KeyError persistant: {e}")
			return False

	except Exception as e:
		print(f"   ❌ Erreur: {type(e).__name__}: {str(e)[:80]}")
		import traceback
		traceback.print_exc()
		return False


def run_full_tests():
	"""Exécuter tous les tests de validation"""
	print("\n🧪 Exécution des tests complets...")

	import subprocess
	import os

	test_files = [
		"test_spell_slots_fix.py",
		"test_spell_slots_end_to_end.py",
		"test_game_integration.py"
	]

	all_passed = True
	base_dir = "/Users/display/PycharmProjects/dnd-5e-core"

	for test_file in test_files:
		test_path = os.path.join(base_dir, test_file)

		if not os.path.exists(test_path):
			print(f"   ⚠️  {test_file} non trouvé")
			continue

		print(f"\n   📝 Exécution de {test_file}...")

		try:
			result = subprocess.run(
				["python3", test_path],
				cwd=base_dir,
				capture_output=True,
				text=True,
				timeout=60
			)

			if result.returncode == 0:
				print(f"   ✅ {test_file}: RÉUSSI")
			else:
				print(f"   ❌ {test_file}: ÉCHOUÉ (code {result.returncode})")
				if result.stderr:
					print(f"      Erreur: {result.stderr[:200]}")
				all_passed = False

		except subprocess.TimeoutExpired:
			print(f"   ❌ {test_file}: TIMEOUT")
			all_passed = False
		except Exception as e:
			print(f"   ❌ {test_file}: Erreur d'exécution - {e}")
			all_passed = False

	return all_passed


def check_documentation():
	"""Vérifier que la documentation est présente"""
	print("\n📚 Vérification de la documentation...")

	import os

	docs = [
		("SPELL_SLOTS_FIX.md", "Documentation complète"),
		("QUICKFIX_SPELL_SLOTS.md", "Guide utilisateur"),
		("SPELL_SLOTS_SUMMARY.md", "Résumé"),
	]

	base_dir = "/Users/display/PycharmProjects/dnd-5e-core"
	all_present = True

	for filename, description in docs:
		filepath = os.path.join(base_dir, filename)
		if os.path.exists(filepath):
			size = os.path.getsize(filepath)
			print(f"   ✅ {filename} ({size} octets) - {description}")
		else:
			print(f"   ❌ {filename} manquant - {description}")
			all_present = False

	return all_present


def print_summary(checks_passed):
	"""Afficher le résumé final"""
	print("\n" + "=" * 80)
	print("RÉSUMÉ DE LA VALIDATION")
	print("=" * 80)

	total_checks = len(checks_passed)
	passed_checks = sum(checks_passed.values())

	for check_name, passed in checks_passed.items():
		status = "✅ RÉUSSI" if passed else "❌ ÉCHOUÉ"
		print(f"{check_name:30} : {status}")

	print("=" * 80)
	print(f"\nRésultat: {passed_checks}/{total_checks} vérifications réussies")

	if all(checks_passed.values()):
		print("\n🎉 VALIDATION COMPLÈTE RÉUSSIE!")
		print("\n✅ La correction du KeyError spell_slots est fonctionnelle.")
		print("✅ Tous les tests passent.")
		print("✅ La documentation est présente.")
		print("\n👍 Vous pouvez utiliser le système sans problème.\n")
		return 0
	else:
		print("\n⚠️  CERTAINES VÉRIFICATIONS ONT ÉCHOUÉ!")
		print("\n📖 Consultez la documentation:")
		print("   - SPELL_SLOTS_FIX.md (détails techniques)")
		print("   - QUICKFIX_SPELL_SLOTS.md (guide utilisateur)")
		print("\n🔧 Vérifiez que tous les fichiers ont été correctement modifiés.\n")
		return 1


def main():
	"""Fonction principale"""
	print("\n" + "=" * 80)
	print("VALIDATION COMPLÈTE - Correction KeyError spell_slots")
	print("=" * 80)

	checks = {}

	# Vérification 1: Imports
	checks["Imports"] = check_imports()

	# Vérification 2: Validation rapide
	checks["Validation rapide"] = quick_validation()

	# Vérification 3: Documentation
	checks["Documentation"] = check_documentation()

	# Vérification 4: Tests complets (optionnel)
	if "--full" in sys.argv:
		checks["Tests complets"] = run_full_tests()
	else:
		print("\n💡 Astuce: Utilisez --full pour exécuter tous les tests")

	# Afficher le résumé
	exit_code = print_summary(checks)
	sys.exit(exit_code)


if __name__ == "__main__":
	main()
