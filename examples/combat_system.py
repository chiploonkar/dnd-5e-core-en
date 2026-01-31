"""
Combat System Examples

Demonstrates the automated combat system with spellcasting, equipment, and tactics.
"""

from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core import load_monster, load_weapon, load_armor
from dnd_5e_core.combat import CombatSystem
from dnd_5e_core.equipment import get_magic_item, get_special_weapon


def setup_party():
	"""Create a balanced party for combat."""
	party = [simple_character_generator(5, "human", "fighter", "Conan"), simple_character_generator(5, "dwarf", "cleric", "Gimli"), simple_character_generator(5, "halfling", "rogue", "Bilbo"), simple_character_generator(5, "elf", "wizard", "Gandalf")]

	# Equip the fighter with better gear
	fighter = party[0]
	longsword = load_weapon("longsword")
	chain_mail = load_armor("chain-mail")

	if longsword and fighter.inventory:
		for i, item in enumerate(fighter.inventory):
			if item is None:
				fighter.inventory[i] = longsword
				fighter.equip(longsword)
				break

	if chain_mail and fighter.inventory:
		for i, item in enumerate(fighter.inventory):
			if item is None:
				fighter.inventory[i] = chain_mail
				fighter.equip(chain_mail)
				break

	# Give wizard a magic item
	wizard = party[3]
	wand = get_magic_item("wand-of-magic-missiles")
	if wand and wizard.inventory:
		for i, item in enumerate(wizard.inventory):
			if item is None:
				wizard.inventory[i] = wand
				wizard.equip(wand)
				break

	return party


def example_basic_combat():
	"""Demonstrate basic combat between party and monsters."""
	print("=== Basic Combat Example ===")

	# Setup
	party = setup_party()
	monsters = [load_monster("orc"), load_monster("orc")]

	print(f"Party Formation:")
	for i, char in enumerate(party):
		position = "Front Row" if i < 3 else "Back Row (Spells)"
		print(f"  {i}: {char.name} ({char.class_type.name}) - {position}")

	print(f"Enemies: {[m.name for m in monsters]}")

	# Combat
	combat = CombatSystem(verbose=True)
	alive_chars = [c for c in party if c.hit_points > 0]
	alive_monsters = [m for m in monsters if m.hit_points > 0]

	round_num = 1
	while alive_chars and alive_monsters and round_num <= 5:
		print(f"=== Round {round_num} ===")

		# Character turns
		for char in alive_chars[:]:
			if not alive_monsters:
				break
			if char.hit_points <= 0:
				if char in alive_chars:
					alive_chars.remove(char)
				continue

			print(f"{char.name}'s turn:")
			combat.character_turn(character=char, alive_chars=alive_chars, alive_monsters=alive_monsters, party=party)

		# Monster turns
		for monster in alive_monsters[:]:
			if not alive_chars:
				break
			if monster.hit_points <= 0:
				if monster in alive_monsters:
					alive_monsters.remove(monster)
				continue

			print(f"{monster.name}'s turn:")
			combat.monster_turn(monster=monster, alive_monsters=alive_monsters, alive_chars=alive_chars, party=party, round_num=round_num)

		round_num += 1

	# Results
	if alive_chars:
		print(f"✅ VICTORY! Remaining party members: {len(alive_chars)}")
	else:
		print(f"💀 DEFEAT! All party members fallen.")


def example_spellcaster_combat():
	"""Demonstrate combat focusing on spellcasting."""
	print("=== Spellcaster Combat Example ===")

	# Create spellcaster-heavy party
	party = [simple_character_generator(5, "human", "fighter", "Tank"), simple_character_generator(5, "elf", "wizard", "Fireball"), simple_character_generator(5, "human", "cleric", "Healer"), simple_character_generator(5, "halfling", "bard", "Support")]

	# Face a tough enemy
	monster = load_monster("ogre")

	print(f"Spellcaster Party vs {monster.name}")
	print(f"Party Spellcasters: {len([c for c in party if c.is_spell_caster])}")

	# Show initial spell slots
	for char in party:
		if char.is_spell_caster and char.sc:
			print(f"  {char.name}: Spell slots {char.sc.spell_slots[1:4]}")

	# Combat
	combat = CombatSystem(verbose=True)
	alive_chars = party[:]
	alive_monsters = [monster]

	for round_num in range(1, 4):  # 3 rounds max
		if not alive_chars or not alive_monsters:
			break

		print(f"=== Round {round_num} ===")

		# Character turns (focus on spellcasting)
		for char in alive_chars:
			if not alive_monsters:
				break

			print(f"{char.name} ({char.class_type.name}):")
			if char.is_spell_caster:
				print(f"  Remaining spell slots: {char.sc.spell_slots[1:4]}")

			combat.character_turn(character=char, alive_chars=alive_chars, alive_monsters=alive_monsters, party=party)

		# Monster turn
		if alive_monsters and alive_monsters[0].hit_points > 0:
			print(f"{monster.name}'s turn:")
			combat.monster_turn(monster=monster, alive_monsters=alive_monsters, alive_chars=alive_chars, party=party, round_num=round_num)
		else:
			alive_monsters = []

	# Show final spell usage
	print(f"Final Spell Slot Usage:")
	for char in party:
		if char.is_spell_caster and char.sc:
			print(f"  {char.name}: {char.sc.spell_slots[1:4]}")


def example_manual_combat():
	"""Demonstrate manual combat control."""
	print("=== Manual Combat Example ===")

	# Simple 1v1
	fighter = simple_character_generator(5, "human", "fighter", "Hero")
	orc = load_monster("orc")

	print(f"{fighter.name} vs {orc.name}")
	print(f"Fighter: HP {fighter.hit_points}, AC {fighter.armor_class}")
	print(f"Orc: HP {orc.hit_points}, AC {orc.armor_class}")

	round_num = 1
	while fighter.hit_points > 0 and orc.hit_points > 0 and round_num <= 5:
		print(f"--- Round {round_num} ---")

		# Fighter attacks
		damage = fighter.attack(orc)
		print(f"{fighter.name} attacks for {damage} damage!")
		print(f"  {orc.name} HP: {orc.hit_points}")

		if orc.hit_points <= 0:
			print(f"  {orc.name} is defeated!")
			break

		# Orc attacks back
		damage = orc.attack(fighter)
		print(f"{orc.name} attacks for {damage} damage!")
		print(f"  {fighter.name} HP: {fighter.hit_points}")

		round_num += 1

	if fighter.hit_points > 0:
		print(f"✅ {fighter.name} wins!")
	else:
		print(f"💀 {fighter.name} is defeated!")


def example_magic_items_combat():
	"""Demonstrate combat with magic items."""
	print("=== Magic Items Combat Example ===")

	# Create character with magic items
	paladin = simple_character_generator(5, "human", "paladin", "Sir Arthur")

	# Add magic items
	flame_tongue = get_special_weapon("flame-tongue")
	defender = get_special_weapon("defender")
	ring_protection = get_magic_item("ring-of-protection")
	staff_of_healing = get_magic_item("staff-of-healing")	# BUGGY
	necklace_of_fireballs = get_magic_item("necklace-of-fireballs")
	wand_of_magic_missiles = get_magic_item("wand-of-magic-missiles")
	belt_of_giant_strength_storm = get_magic_item('belt-of-storm-giant-strength')
	magic_items = [defender, ring_protection, necklace_of_fireballs]

	# Add normal items
	chain_mail = load_armor('chain-mail')
	free_slot = min([i for i, inv_item in enumerate(paladin.inventory) if inv_item is None])
	paladin.inventory[free_slot] = chain_mail
	messages, success = paladin.equip(chain_mail)
	print(messages)


	print(f"Equipping {paladin.name} with magic items...")

	for magic_item in magic_items:
		for i, item in enumerate(paladin.inventory):
			if item is None:
				paladin.inventory[i] = magic_item
				messages, success = paladin.equip_magic_item(magic_item)
				print(messages)
				break

	print(f"  Final AC: {paladin.armor_class}")

	# Fight a tough enemy
	troll = load_monster("troll")

	print(f"{paladin.name} (with magic items) vs {troll.name}")

	# Quick combat simulation
	combat = CombatSystem(verbose=True)

	for round_num in range(1, 4):
		if paladin.hit_points <= 0 or troll.hit_points <= 0:
			break

		print(f"--- Round {round_num} ---")

		# Paladin turn
		combat.character_turn(character=paladin, alive_chars=[paladin], alive_monsters=[troll], party=[paladin])

		if troll.hit_points <= 0:
			break

		# Troll turn
		combat.monster_turn(monster=troll, alive_monsters=[troll], alive_chars=[paladin], party=[paladin], round_num=round_num)

	print(f"Final Status:")
	print(f"  {paladin.name}: {paladin.hit_points} HP")
	print(f"  {troll.name}: {troll.hit_points} HP")


if __name__ == "__main__":
	print("D&D 5e Combat System Examples")
	print("=" * 40)

	# example_basic_combat()
	# example_spellcaster_combat()
	# example_manual_combat()
	example_magic_items_combat()

	print("" + "=" * 40)
	print("Combat examples completed!")
