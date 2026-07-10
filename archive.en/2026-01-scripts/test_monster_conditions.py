#!/usr/bin/env python3
"""
Verification script for condition extraction for key monsters
"""

from dnd_5e_core.data import load_monster

# List of monsters to test (by condition)
TEST_MONSTERS = {
    'Restrained': [
        'giant-spider',
        'giant-constrictor-snake',
        'ettercap',
        'gelatinous-cube',
        'roper',
    ],
    'Grappled': [
        'giant-octopus',
        'giant-toad',
        'mimic',
    ],
    'Poisoned': [
        'giant-poisonous-snake',
        'giant-centipede',
        'giant-scorpion',
        'ettercap',
    ],
    'Paralyzed': [
        'ghoul',
        'gelatinous-cube',
    ],
    'Frightened': [
        'mummy',
        'ancient-red-dragon',
    ],
    'Petrified': [
        'basilisk',
        'medusa',
        'cockatrice',
    ],
    'Charmed': [
        'vampire',
        'dryad',
        'lamia',
    ],
}


def test_monster_condition_extraction():
    """Tests the extraction of conditions for each monster"""

    print("=" * 100)
    print("CONDITION EXTRACTION TEST - KEY MONSTERS")
    print("=" * 100)
    print()

    results = {
        'success': [],
        'partial': [],
        'failed': [],
        'not_loaded': []
    }

    for condition_name, monster_indices in TEST_MONSTERS.items():
        print(f"\n{'='*100}")
        print(f"🎯 CONDITION: {condition_name.upper()}")
        print('=' * 100)

        for monster_index in monster_indices:
            print(f"\n📋 Testing: {monster_index}")
            print("-" * 100)

            try:
                monster = load_monster(monster_index)

                if not monster:
                    print(f"   ❌ Monster not loaded")
                    results['not_loaded'].append(monster_index)
                    continue

                print(f"   ✅ Loaded: {monster.name}")
                print(f"   📊 Actions: {len(monster.actions)}")

                # Check actions with conditions
                actions_with_effects = []
                for action in monster.actions:
                    if action.effects:
                        actions_with_effects.append(action)
                        print(f"\n   ⚡ Action: {action.name}")
                        print(f"      Type: {action.type.value}")
                        print(f"      Conditions ({len(action.effects)}):")
                        for effect in action.effects:
                            dc_str = f"DC {effect.dc_value} {effect.dc_type.value}" if effect.dc_value and effect.dc_type else "No DC"
                            print(f"         • {effect.name} ({dc_str})")
                            print(f"           {effect.desc[:80]}...")

                if actions_with_effects:
                    # Check if the expected condition is present
                    all_condition_names = [
                        e.name.lower()
                        for a in actions_with_effects
                        for e in a.effects
                    ]

                    if condition_name.lower() in all_condition_names:
                        print(f"\n   ✅ SUCCESS: Condition '{condition_name}' correctly extracted")
                        results['success'].append({
                            'monster': monster_index,
                            'condition': condition_name,
                            'actions': len(actions_with_effects)
                        })
                    else:
                        print(f"\n   ⚠️  PARTIAL: Actions with conditions, but '{condition_name}' not found")
                        print(f"      Conditions found: {', '.join(set(all_condition_names))}")
                        results['partial'].append({
                            'monster': monster_index,
                            'condition': condition_name,
                            'found': list(set(all_condition_names))
                        })
                else:
                    print(f"\n   ❌ FAILED: No conditions extracted")
                    print(f"      Available actions:")
                    for action in monster.actions:
                        print(f"         - {action.name}")
                    results['failed'].append({
                        'monster': monster_index,
                        'condition': condition_name
                    })

            except Exception as e:
                print(f"   ❌ ERROR: {e}")
                results['failed'].append({
                    'monster': monster_index,
                    'condition': condition_name,
                    'error': str(e)
                })

    # Final summary
    print("\n\n" + "=" * 100)
    print("📊 FINAL SUMMARY")
    print("=" * 100)

    total_tested = sum(len(results[k]) for k in results)
    success_count = len(results['success'])
    partial_count = len(results['partial'])
    failed_count = len(results['failed'])
    not_loaded_count = len(results['not_loaded'])

    print(f"\n✅ Complete success: {success_count}/{total_tested} ({success_count*100//total_tested if total_tested else 0}%)")
    print(f"⚠️  Partial success: {partial_count}/{total_tested} ({partial_count*100//total_tested if total_tested else 0}%)")
    print(f"❌ Failures: {failed_count}/{total_tested} ({failed_count*100//total_tested if total_tested else 0}%)")
    print(f"⚠️  Not loaded: {not_loaded_count}/{total_tested}")

    # Failure details
    if results['failed']:
        print("\n\n❌ MONSTERS REQUIRING A FIX:")
        print("-" * 100)
        for item in results['failed']:
            error_str = f" - {item.get('error', 'Unknown')}" if 'error' in item else ""
            print(f"   • {item['monster']} (attendu: {item['condition']}){error_str}")

    # Partial success details
    if results['partial']:
        print("\n\n⚠️  MONSTERS WITH PARTIAL EXTRACTION:")
        print("-" * 100)
        for item in results['partial']:
            print(f"   • {item['monster']} (attendu: {item['condition']})")
            print(f"     Trouvé: {', '.join(item['found'])}")

    # List of successes
    if results['success']:
        print("\n\n✅ CORRECTLY PARSED MONSTERS:")
        print("-" * 100)
        by_condition = {}
        for item in results['success']:
            cond = item['condition']
            if cond not in by_condition:
                by_condition[cond] = []
            by_condition[cond].append(item['monster'])

        for condition, monsters in sorted(by_condition.items()):
            print(f"\n   {condition}:")
            for monster in monsters:
                print(f"      • {monster}")

    return results


if __name__ == "__main__":
    results = test_monster_condition_extraction()

    # Exit code based on results
    if results['failed'] or results['not_loaded']:
        exit(1)
    else:
        exit(0)
