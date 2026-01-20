"""
D&D 5e Core - Extended Monster Parser
Parse 5etools format monsters to official API format
"""
import re
from typing import Dict, List, Any, Optional


def normalize_extended_monster_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize extended monster format (5etools) to official API format.

    Args:
        data: Monster data in 5etools format

    Returns:
        Monster data in official API format
    """
    normalized = {}

    # Basic fields (same in both formats)
    normalized['index'] = data.get('index', data.get('name', '').lower().replace(' ', '-'))
    normalized['name'] = data.get('name', 'Unknown')
    normalized['source'] = data.get('source', None)

    # Abilities - convert from {str, dex, con, int, wis, cha} to {strength, dexterity, ...}
    if 'abilities' in data and isinstance(data['abilities'], dict):
        abilities = data['abilities']
        normalized['strength'] = abilities.get('str', 10)
        normalized['dexterity'] = abilities.get('dex', 10)
        normalized['constitution'] = abilities.get('con', 10)
        normalized['intelligence'] = abilities.get('int', 10)
        normalized['wisdom'] = abilities.get('wis', 10)
        normalized['charisma'] = abilities.get('cha', 10)
    else:
        # Fallback if already in official format
        normalized['strength'] = data.get('strength', 10)
        normalized['dexterity'] = data.get('dexterity', 10)
        normalized['constitution'] = data.get('constitution', 10)
        normalized['intelligence'] = data.get('intelligence', 10)
        normalized['wisdom'] = data.get('wisdom', 10)
        normalized['charisma'] = data.get('charisma', 10)

    # Hit points - convert from {average, formula} to average
    if 'hit_points' in data:
        hp_data = data['hit_points']
        if isinstance(hp_data, dict):
            normalized['hit_points'] = hp_data.get('average', 1)
            normalized['hit_dice'] = hp_data.get('formula', '1d8')
        else:
            normalized['hit_points'] = hp_data
            normalized['hit_dice'] = data.get('hit_dice', '1d8')
    else:
        normalized['hit_points'] = 1
        normalized['hit_dice'] = '1d8'

    # Armor class
    if 'armor_class' in data:
        ac_data = data['armor_class']
        if isinstance(ac_data, list) and len(ac_data) > 0:
            # Sometimes AC is [{ac: 17, from: ["natural armor"]}]
            normalized['armor_class'] = ac_data[0].get('ac', 10) if isinstance(ac_data[0], dict) else ac_data[0]
        elif isinstance(ac_data, dict):
            normalized['armor_class'] = ac_data.get('ac', 10)
        else:
            normalized['armor_class'] = ac_data
    else:
        normalized['armor_class'] = 10

    # Speed - convert from {walk: 25, climb: 25} to standard format
    if 'speed' in data:
        speed_data = data['speed']
        if isinstance(speed_data, dict):
            # Priority: fly > walk > other
            speed_val = (speed_data.get('fly') or
                        speed_data.get('walk') or
                        speed_data.get('burrow') or
                        speed_data.get('swim') or 30)
            if isinstance(speed_val, str):
                normalized['speed'] = {'walk': speed_val}
            else:
                normalized['speed'] = {'walk': f'{speed_val} ft.'}
        else:
            normalized['speed'] = speed_data
    else:
        normalized['speed'] = {'walk': '30 ft.'}

    # Challenge rating
    normalized['challenge_rating'] = data.get('challenge_rating', data.get('cr', 0))

    # XP - can be calculated from CR if not present
    normalized['xp'] = data.get('xp', _calculate_xp_from_cr(normalized['challenge_rating']))

    # Actions - simplified for now, just create basic structure
    # Full parsing of {@atk mw}, {@damage ...} etc. will be added later
    actions = []
    if 'action' in data:
        for action_data in data['action']:
            action = _parse_extended_action(action_data)
            if action:
                actions.append(action)
    normalized['actions'] = actions

    # Proficiencies
    proficiencies = []

    # Saving throws
    if 'saving_throws' in data or 'save' in data:
        saves = data.get('saving_throws', data.get('save', {}))
        for save_name, save_bonus in saves.items():
            proficiencies.append({
                'proficiency': {
                    'index': f'saving-throw-{save_name}',
                    'name': f'{save_name.upper()} save'
                },
                'value': int(save_bonus.replace('+', '')) if isinstance(save_bonus, str) else save_bonus
            })

    # Skills
    if 'skills' in data or 'skill' in data:
        skills = data.get('skills', data.get('skill', {}))
        for skill_name, skill_bonus in skills.items():
            proficiencies.append({
                'proficiency': {
                    'index': f'skill-{skill_name}',
                    'name': skill_name.capitalize()
                },
                'value': int(skill_bonus.replace('+', '')) if isinstance(skill_bonus, str) else skill_bonus
            })

    normalized['proficiencies'] = proficiencies

    # Special abilities - simplified
    special_abilities = []
    if 'trait' in data:
        for trait in data['trait']:
            # For now, just store as basic special ability without full parsing
            pass  # TODO: Parse traits into special abilities

    # Legendary actions
    if 'legendary' in data:
        # TODO: Parse legendary actions
        pass

    # Spellcasting
    if 'spellcasting' in data and data['spellcasting']:
        # TODO: Parse spellcasting
        pass

    return normalized


def _parse_extended_action(action_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Parse an extended format action.

    Args:
        action_data: Action in 5etools format with 'entries'

    Returns:
        Action in official API format
    """
    name = action_data.get('name', 'Unknown Action')
    entries = action_data.get('entries', [])

    if not entries:
        return None

    # Join all entries into description text
    desc = ' '.join(str(entry) for entry in entries)

    # Try to parse attack information from description
    # Pattern: {@atk mw} {@hit 7} to hit, reach 5 ft., one target. {@h}19 ({@damage 3d10 + 3}) piercing damage

    attack_bonus = None
    damage_dice = None
    damage_type = None

    # Extract attack bonus: {@hit 7}
    hit_match = re.search(r'\{@hit (\d+)\}', desc)
    if hit_match:
        attack_bonus = int(hit_match.group(1))

    # Extract damage: {@damage XdY + Z} damage_type
    damage_match = re.search(r'\{@damage ([^}]+)\}\s+(\w+)', desc)
    if damage_match:
        damage_dice_raw = damage_match.group(1)
        damage_type = damage_match.group(2)

    # Clean description of special tags
    clean_desc = re.sub(r'\{@[^}]+\}', '', desc)
    clean_desc = re.sub(r'\s+', ' ', clean_desc).strip()

    # Create action structure
    action = {
        'name': name,
        'desc': clean_desc
    }

    if attack_bonus is not None:
        action['attack_bonus'] = attack_bonus

    if damage_dice and damage_type:
        action['damage'] = [{
            'damage_dice': damage_dice_raw,
            'damage_type': {
                'index': damage_type.lower(),
                'name': damage_type.capitalize()
            }
        }]

    return action


def _calculate_xp_from_cr(cr: float) -> int:
    """
    Calculate XP from challenge rating.

    Args:
        cr: Challenge rating

    Returns:
        XP value
    """
    xp_table = {
        0: 10,
        0.125: 25,
        0.25: 50,
        0.5: 100,
        1: 200,
        2: 450,
        3: 700,
        4: 1100,
        5: 1800,
        6: 2300,
        7: 2900,
        8: 3900,
        9: 5000,
        10: 5900,
        11: 7200,
        12: 8400,
        13: 10000,
        14: 11500,
        15: 13000,
        16: 15000,
        17: 18000,
        18: 20000,
        19: 22000,
        20: 25000,
        21: 33000,
        22: 41000,
        23: 50000,
        24: 62000,
        25: 75000,
        26: 90000,
        27: 105000,
        28: 120000,
        29: 135000,
        30: 155000
    }

    return xp_table.get(cr, 0)
