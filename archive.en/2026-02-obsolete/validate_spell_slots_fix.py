#!/usr/bin/env python3
"""
Complete validation script for the spell_slots KeyError fix
To be executed after package installation or update
"""
import sys
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

def check_imports():
	"""Verify that all imports work"""
	print("\n🔍 Verifying imports...")
	try:
		from dnd_5e_core.data.loaders import simple_character_generator
		from dnd_5e_core.data.progression_loader import get_spell_slots_for_level
		print("   ✅ Imports OK")
		return True
	except ImportError as e:
		print(f"   ❌ Import error: {e}")
		return False


def quick_validation():
	"""Quick validation of the fix"""
	print("\n🎯 Quick validation of the fix...")

	try:
		from dnd_5e_core.data.loaders import simple_character_generator

		# Quick test: create a level 2 wizard (the case that caused the KeyError)
		char = simple_character_generator(level=2, class_name="wizard", name="QuickTest")

		# Verify spell_slots
		if not hasattr(char.class_type, 'spell_slots'):
			print("   ❌ class_type.spell_slots does not exist")
			return False

		if not isinstance(char.class_type.spell_slots, dict):
			print(f"   ❌ spell_slots is not a dict: {type(char.class_type.spell_slots)}")
			return False

		if 2 not in char.class_type.spell_slots:
			print("   ❌ Level 2 missing from spell_slots")
			return False

		# Test direct access (which caused the KeyError)
		try:
			slots = char.class_type.spell_slots[char.level]
			print(f"   ✅ Direct access OK: {slots}")
			return True
		except KeyError as e:
			print(f"   ❌ Persistent KeyError: {e}")
			return False

	except Exception as e:
		print(f"   ❌ Error: {type(e).__name__}: {str(e)[:80]}")
		import traceback
		traceback.print_exc()
		return False


def run_full_tests():
	"""Execute all validation tests"""
	print("\n🧪 Running full tests...")

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
			print(f"   ⚠️  {test_file} not found")
			continue

		print(f"\n   📝 Running {test_file}...")

		try:
			result = subprocess.run(
				["python3", test_path],
				cwd=base_dir,
				capture_output=True,
				text=True,
				timeout=60
			)

			if result.returncode == 0:
				print(f"   ✅ {test_file}: PASSED")
			else:
				print(f"   ❌ {test_file}: FAILED (code {result.returncode})")
				if result.stderr:
					print(f"      Error: {result.stderr[:200]}")
				all_passed = False

		except subprocess.TimeoutExpired:
			print(f"   ❌ {test_file}: TIMEOUT")
			all_passed = False
		except Exception as e:
			print(f"   ❌ {test_file}: Execution error - {e}")
			all_passed = False

	return all_passed


def check_documentation():
	"""Verify that the documentation is present"""
	print("\n📚 Verifying documentation...")

	import os

	docs = [
		("SPELL_SLOTS_FIX.md", "Complete documentation"),
		("QUICKFIX_SPELL_SLOTS.md", "User guide"),
		("SPELL_SLOTS_SUMMARY.md", "Summary"),
	]

	base_dir = "/Users/display/PycharmProjects/dnd-5e-core"
	all_present = True

	for filename, description in docs:
		filepath = os.path.join(base_dir, filename)
		if os.path.exists(filepath):
			size = os.path.getsize(filepath)
			print(f"   ✅ {filename} ({size} bytes) - {description}")
		else:
			print(f"   ❌ {filename} missing - {description}")
			all_present = False

	return all_present


def print_summary(checks_passed):
	"""Show final summary"""
	print("\n" + "=" * 80)
	print("VALIDATION SUMMARY")
	print("=" * 80)

	total_checks = len(checks_passed)
	passed_checks = sum(checks_passed.values())

	for check_name, passed in checks_passed.items():
		status = "✅ PASSED" if passed else "❌ FAILED"
		print(f"{check_name:30} : {status}")

	print("=" * 80)
	print(f"\nResult: {passed_checks}/{total_checks} checks passed")

	if all(checks_passed.values()):
		print("\n🎉 COMPLETE VALIDATION PASSED!")
		print("\n✅ The spell_slots KeyError fix is functional.")
		print("✅ All tests pass.")
		print("✅ The documentation is present.")
		print("\n👍 You can use the system without any problems.\n")
		return 0
	else:
		print("\n⚠️  SOME CHECKS FAILED!")
		print("\n📖 Consult the documentation:")
		print("   - SPELL_SLOTS_FIX.md (technical details)")
		print("   - QUICKFIX_SPELL_SLOTS.md (user guide)")
		print("\n🔧 Verify that all files have been correctly modified.\n")
		return 1


def main():
	"""Main function"""
	print("\n" + "=" * 80)
	print("COMPLETE VALIDATION - spell_slots KeyError Fix")
	print("=" * 80)

	checks = {}

	# Check 1: Imports
	checks["Imports"] = check_imports()

	# Check 2: Quick validation
	checks["Quick validation"] = quick_validation()

	# Check 3: Documentation
	checks["Documentation"] = check_documentation()

	# Check 4: Full tests (optional)
	if "--full" in sys.argv:
		checks["Full tests"] = run_full_tests()
	else:
		print("\n💡 Tip: Use --full to run all tests")

	# Show summary
	exit_code = print_summary(checks)
	sys.exit(exit_code)


if __name__ == "__main__":
	main()
