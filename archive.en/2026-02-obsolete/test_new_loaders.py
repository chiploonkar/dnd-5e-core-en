#!/usr/bin/env python3
"""Test of new loaders in dnd-5e-core"""

import sys
import os

# Add dnd-5e-core to path
sys.path.insert(0, '/Users/display/PycharmProjects/dnd-5e-core')

def test_import():
    """Test 1: Import dnd-5e-core"""
    print('Test 1: Import dnd-5e-core...')
    import dnd_5e_core
    print('OK: dnd-5e-core imported successfully')
    return True

def test_new_loaders():
    """Test 2: Test of new JSON loaders"""
    print('\nTest 2: Test of new JSON loaders...')
    from dnd_5e_core.data import load_damage_type, load_condition, load_trait

    dt = load_damage_type('fire')
    print(f'OK: load_damage_type("fire"): {dt.name if dt else "None"}')

    cond = load_condition('blinded')
    print(f'OK: load_condition("blinded"): {cond.name if cond else "None"}')

    trait = load_trait('darkvision')
    print(f'OK: load_trait("darkvision"): {trait.name if trait else "None"}')

    return True

def test_names_module():
    """Test 3: Test module names"""
    print('\nTest 3: Test module names...')
    from dnd_5e_core.data import load_names, load_human_names

    dwarf_names = load_names('dwarf')
    print(f'OK: load_names("dwarf"): {len(dwarf_names)} genders')

    human_names = load_human_names()
    print(f'OK: load_human_names(): {len(human_names)} ethnic groups')

    return True

def test_tables_module():
    """Test 4: Test module tables"""
    print('\nTest 4: Test module tables...')
    from dnd_5e_core.data import load_height_weight_table, load_xp_levels_table

    hw_table = load_height_weight_table()
    print(f'OK: load_height_weight_table(): {len(hw_table)} races')

    xp_table = load_xp_levels_table()
    print(f'OK: load_xp_levels_table(): {len(xp_table)} levels')

    return True

def test_list_functions():
    """Test 5: Test list functions"""
    print('\nTest 5: Test list functions...')
    from dnd_5e_core.data import list_damage_types, list_conditions, list_traits

    damage_types = list_damage_types()
    print(f'OK: list_damage_types(): {len(damage_types)} types')

    conditions = list_conditions()
    print(f'OK: list_conditions(): {len(conditions)} conditions')

    traits = list_traits()
    print(f'OK: list_traits(): {len(traits)} traits')

    return True

def main():
    """Execute all tests"""
    print('='*60)
    print('TEST OF NEW DND-5E-CORE LOADERS')
    print('='*60)

    tests = [
        test_import,
        test_new_loaders,
        test_names_module,
        test_tables_module,
        test_list_functions
    ]

    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f'ERROR: {e}')
            results.append(False)

    print('\n' + '='*60)
    if all(results):
        print('ALL TESTS PASSED!')
        print('='*60)
        return 0
    else:
        print('SOME TESTS FAILED!')
        print('='*60)
        return 1

if __name__ == '__main__':
    sys.exit(main())
