#!/usr/bin/env python3
"""
Script pour analyser tous les monstres et identifier ceux qui appliquent des conditions
"""
import json
from pathlib import Path
from dnd_5e_core.data import load_monster

def analyze_monsters_with_conditions():
    """Analyse tous les monstres et liste ceux avec des conditions"""

    monsters_dir = Path('dnd_5e_core/data/monsters')
    condition_keywords = [
        'restrained', 'grappled', 'poisoned', 'paralyzed', 'stunned',
        'frightened', 'prone', 'blinded', 'charmed', 'petrified', 'incapacitated'
    ]

    monsters_with_conditions = {}
    total_monsters = 0

    print("=" * 80)
    print("ANALYSE DES MONSTRES AVEC CONDITIONS")
    print("=" * 80)
    print()

    for monster_file in sorted(monsters_dir.glob('*.json')):
        if monster_file.name in ['bestiary-sublist-data.json', 'bestiary-sublist-data-all-monsters.json']:
            continue

        total_monsters += 1

        try:
            with open(monster_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            monster_name = data.get('name', '')
            monster_index = data.get('index', '')
            actions = data.get('actions', [])
            special_abilities = data.get('special_abilities', [])

            # Analyser les actions
            for action in actions:
                action_name = action.get('name', '')
                desc = action.get('desc', '')
                desc_lower = desc.lower() if isinstance(desc, str) else ''

                found_conditions = [kw for kw in condition_keywords if kw in desc_lower]

                if found_conditions:
                    if monster_index not in monsters_with_conditions:
                        monsters_with_conditions[monster_index] = {
                            'name': monster_name,
                            'actions': []
                        }

                    monsters_with_conditions[monster_index]['actions'].append({
                        'name': action_name,
                        'type': 'action',
                        'conditions': found_conditions,
                        'desc': desc,
                        'has_dc': 'dc' in action
                    })

            # Analyser les capacités spéciales
            for ability in special_abilities:
                ability_name = ability.get('name', '')
                desc = ability.get('desc', '')
                desc_lower = desc.lower() if isinstance(desc, str) else ''

                found_conditions = [kw for kw in condition_keywords if kw in desc_lower]

                if found_conditions:
                    if monster_index not in monsters_with_conditions:
                        monsters_with_conditions[monster_index] = {
                            'name': monster_name,
                            'actions': []
                        }

                    monsters_with_conditions[monster_index]['actions'].append({
                        'name': ability_name,
                        'type': 'special_ability',
                        'conditions': found_conditions,
                        'desc': desc,
                        'has_dc': 'dc' in ability
                    })

        except Exception as e:
            print(f"⚠️  Erreur lors de l'analyse de {monster_file.name}: {e}")

    print(f"📊 Statistiques:")
    print(f"   Total monstres analysés: {total_monsters}")
    print(f"   Monstres avec conditions: {len(monsters_with_conditions)}")
    print()

    return monsters_with_conditions


def test_condition_extraction():
    """Teste l'extraction des conditions avec le loader"""

    print("=" * 80)
    print("TEST DE L'EXTRACTION AUTOMATIQUE DES CONDITIONS")
    print("=" * 80)
    print()

    # Monstres connus pour avoir des conditions
    test_monsters = [
        'giant-spider',
        'giant-constrictor-snake',
        'gelatinous-cube',
        'basilisk',
        'medusa',
        'ghoul',
        'mummy',
        'cockatrice',
        'ettercap',
        'vine-blight'
    ]

    results = []

    for monster_index in test_monsters:
        try:
            monster = load_monster(monster_index)

            if not monster:
                results.append({
                    'index': monster_index,
                    'status': '❌ Not loaded',
                    'actions_with_conditions': 0
                })
                continue

            actions_with_conditions = [a for a in monster.actions if a.effects]

            results.append({
                'index': monster_index,
                'name': monster.name,
                'status': '✅' if actions_with_conditions else '⚠️',
                'actions_with_conditions': len(actions_with_conditions),
                'total_actions': len(monster.actions),
                'actions': actions_with_conditions
            })

        except Exception as e:
            results.append({
                'index': monster_index,
                'status': f'❌ Error: {e}',
                'actions_with_conditions': 0
            })

    # Afficher les résultats
    for result in results:
        print(f"{result['status']} {result.get('name', result['index'])}")
        if 'actions' in result and result['actions']:
            for action in result['actions']:
                print(f"   Action: {action.name}")
                if action.effects:
                    for effect in action.effects:
                        print(f"      • {effect.name}")
        elif result.get('actions_with_conditions', 0) == 0 and result.get('total_actions', 0) > 0:
            print(f"   ⚠️  {result.get('total_actions', 0)} actions mais aucune condition extraite")
        print()

    return results


def main():
    """Fonction principale"""

    # Analyser tous les monstres
    monsters_data = analyze_monsters_with_conditions()

    # Afficher les 20 premiers
    print("=" * 80)
    print("TOP 20 MONSTRES AVEC CONDITIONS")
    print("=" * 80)
    print()

    for i, (index, data) in enumerate(sorted(monsters_data.items())[:20], 1):
        print(f"{i}. {data['name']} ({index})")
        for action in data['actions']:
            dc_str = " [DC in data]" if action['has_dc'] else ""
            print(f"   • {action['name']} ({action['type']}){dc_str}")
            print(f"     Conditions: {', '.join(action['conditions'])}")
        print()

    # Tester l'extraction
    print()
    test_results = test_condition_extraction()

    # Résumé final
    print()
    print("=" * 80)
    print("RÉSUMÉ")
    print("=" * 80)

    success_count = sum(1 for r in test_results if r.get('actions_with_conditions', 0) > 0)
    total_tested = len(test_results)

    print(f"✅ Extraction réussie: {success_count}/{total_tested} monstres testés")
    print(f"📋 Total monstres avec conditions: {len(monsters_data)}")

    # Monstres nécessitant une attention
    needs_work = [r for r in test_results if r.get('status') == '⚠️']
    if needs_work:
        print()
        print("⚠️  Monstres nécessitant une vérification:")
        for r in needs_work:
            print(f"   - {r.get('name', r['index'])}")


if __name__ == "__main__":
    main()
