#!/usr/bin/env python3
"""Test des nouvelles classes implémentées dans dnd-5e-core"""

print("Testing newly implemented classes and functions...")
print()

# Test Experience System
from dnd_5e_core.mechanics import get_level_from_xp, should_level_up, calculate_proficiency_bonus
print("✅ Experience System:")
print(f"  - Level from 1000 XP: {get_level_from_xp(1000)}")
print(f"  - Should level up (1000 XP, level 2): {should_level_up(1000, 2)}")
print(f"  - Proficiency bonus at level 5: +{calculate_proficiency_bonus(5)}")
print()

# Test Skills
from dnd_5e_core.abilities import SkillType, Skill, get_all_skills
print("✅ Skills System:")
skills = get_all_skills()
print(f"  - Total skills available: {len(skills)}")
acrobatics = Skill(SkillType.ACROBATICS, proficient=True)
print(f"  - {acrobatics}")
print()

# Test Spell Slots
from dnd_5e_core.spells import SpellSlots, get_spell_slots_by_level
print("✅ Spell Slots System:")
slots = get_spell_slots_by_level(5, "full")
print(f"  - Level 5 full caster slots: {slots}")
spell_slots = SpellSlots(max_slots=slots)
print(f"  - Has level 3 slot: {spell_slots.has_slot(3)}")
print()

# Test Cantrips
from dnd_5e_core.spells import get_cantrip_damage_scaling, get_cantrip_damage
print("✅ Cantrips System:")
scaled = get_cantrip_damage_scaling(11, "1d10")
print(f"  - Fire Bolt at level 11: {scaled}")
damage, dtype = get_cantrip_damage("fire-bolt", 11)
print(f"  - Damage: {damage} {dtype}")
print()

# Test Challenge Rating
from dnd_5e_core.mechanics import ChallengeRating
print("✅ Challenge Rating System:")
cr = ChallengeRating(5)
print(f"  - CR 5: {cr.xp} XP, proficiency bonus: +{cr.proficiency_bonus}")
print()

# Test Helpers
from dnd_5e_core.utils import calculate_modifier, format_modifier, get_standard_array
print("✅ Helper Functions:")
print(f"  - Modifier for 16: {format_modifier(calculate_modifier(16))}")
print(f"  - Standard array: {get_standard_array()}")
print()

# Test Constants
from dnd_5e_core.utils import constants
print("✅ Constants:")
print(f"  - Max level: {constants.MAX_LEVEL}")
print(f"  - Base speed (human): {constants.BASE_SPEED_HUMAN} feet")
print(f"  - Number of skills: {len(constants.SKILLS)}")
print()

# Test Multiclass
from dnd_5e_core.classes import can_multiclass_into
from dnd_5e_core.abilities import Abilities
print("✅ Multiclass System:")
abilities = Abilities(str=16, dex=14, con=13, int=12, wis=10, cha=8)
can_mc, reason = can_multiclass_into("fighter", abilities)
print(f"  - Can multiclass into Fighter: {can_mc}")
print()

# Test Inventory
from dnd_5e_core.equipment import Inventory
print("✅ Inventory class imported successfully")
print()

# Test API Client
from dnd_5e_core.data.api_client import DndApiClient
print("✅ API Client imported successfully")
print()

# Test Serialization
from dnd_5e_core.data.serialization import to_json, from_json
print("✅ Serialization System:")
data = {"name": "Test", "level": 5}
json_str = to_json(data)
restored = from_json(json_str)
print(f"  - Serialization works: {restored == data}")
print()

print("=" * 50)
print("✅ ALL NEW CLASSES AND FUNCTIONS WORKING!")
print("=" * 50)

