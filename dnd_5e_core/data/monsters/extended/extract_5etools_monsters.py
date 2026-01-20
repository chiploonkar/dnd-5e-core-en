#!/usr/bin/env python3
"""
Script pour extraire et convertir les monstres 5e.tools vers le format dnd-5e-core

Ce script:
1. Lit le fichier bestiary-sublist-data.json (2228 monstres)
2. Convertit chaque monstre au format compatible Monster class
3. Extrait chaque monstre en fichier JSON individuel
4. Génère un rapport de conversion
"""
import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional


class FiveEToolsToMonsterConverter:
    """Convertit les données 5e.tools vers le format Monster de dnd-5e-core"""

    def __init__(self):
        self.stats_converted = 0
        self.errors = []
        self.warnings = []

    def normalize_filename(self, name: str) -> str:
        """Créer un nom de fichier normalisé"""
        filename = name.lower()
        filename = filename.replace(' ', '-')
        filename = filename.replace("'", '')
        filename = filename.replace('"', '')
        filename = filename.replace(',', '')
        filename = filename.replace('(', '')
        filename = filename.replace(')', '')
        filename = filename.replace('/', '-')
        filename = filename.replace('\\', '-')
        filename = filename.replace(':', '')
        filename = filename.replace(';', '')
        # Nettoyer caractères spéciaux
        filename = re.sub(r'[^a-z0-9-]', '', filename)
        # Supprimer tirets multiples
        filename = re.sub(r'-+', '-', filename)
        filename = filename.strip('-')
        return f"{filename}.json"

    def convert_cr(self, cr_data: Any) -> float:
        """Convertit le CR au format numérique"""
        if cr_data is None:
            return 0.0

        if isinstance(cr_data, (int, float)):
            return float(cr_data)

        if isinstance(cr_data, str):
            # Gérer les fractions comme "1/8", "1/4", etc.
            if '/' in cr_data:
                parts = cr_data.split('/')
                return float(parts[0]) / float(parts[1])
            try:
                return float(cr_data)
            except ValueError:
                return 0.0

        if isinstance(cr_data, dict):
            # 5e.tools peut avoir un objet avec 'cr' et 'xp'
            return self.convert_cr(cr_data.get('cr', 0))

        return 0.0

    def convert_speed(self, speed_data: Any) -> Dict[str, int]:
        """Convertit les données de vitesse"""
        if not speed_data:
            return {"walk": 30}

        if isinstance(speed_data, dict):
            result = {}
            for key, value in speed_data.items():
                if isinstance(value, dict):
                    # 5e.tools: {"walk": {"number": 30, "condition": "..."}}
                    result[key] = value.get('number', 30)
                elif isinstance(value, (int, float)):
                    result[key] = int(value)
                elif isinstance(value, str):
                    # Extraire le nombre (ex: "30 ft.")
                    match = re.search(r'(\d+)', value)
                    if match:
                        result[key] = int(match.group(1))
            return result if result else {"walk": 30}

        return {"walk": 30}

    def convert_abilities(self, monster: Dict[str, Any]) -> Dict[str, int]:
        """Convertit les caractéristiques"""
        return {
            "str": monster.get('str', 10),
            "dex": monster.get('dex', 10),
            "con": monster.get('con', 10),
            "int": monster.get('int', 10),
            "wis": monster.get('wis', 10),
            "cha": monster.get('cha', 10)
        }

    def convert_hp(self, hp_data: Any) -> Dict[str, Any]:
        """Convertit les points de vie"""
        if not hp_data:
            return {"average": 10, "formula": "2d8"}

        if isinstance(hp_data, dict):
            return {
                "average": hp_data.get('average', 10),
                "formula": hp_data.get('formula', '2d8')
            }

        if isinstance(hp_data, int):
            return {"average": hp_data, "formula": "2d8"}

        return {"average": 10, "formula": "2d8"}

    def convert_ac(self, ac_data: Any) -> int:
        """Convertit l'armure"""
        if not ac_data:
            return 10

        if isinstance(ac_data, int):
            return ac_data

        if isinstance(ac_data, list) and len(ac_data) > 0:
            # Prendre la première valeur d'AC
            first_ac = ac_data[0]
            if isinstance(first_ac, dict):
                return first_ac.get('ac', 10)
            if isinstance(first_ac, int):
                return first_ac

        return 10

    def parse_damage_from_text(self, text: str) -> Optional[Dict[str, Any]]:
        """Parse les dégâts depuis le texte 5e.tools"""
        # Pattern: {@damage 1d6 + 3} ou {@hit 4}
        damage_match = re.search(r'\{@damage ([^}]+)\}', text)
        if damage_match:
            damage_str = damage_match.group(1)
            # Extraire dés et bonus (ex: "1d6 + 3")
            dice_match = re.match(r'(\d+d\d+)\s*\+?\s*(\d*)', damage_str)
            if dice_match:
                dice = dice_match.group(1)
                bonus = int(dice_match.group(2)) if dice_match.group(2) else 0
                return {"dice": dice, "bonus": bonus}

        return None

    def convert_actions(self, actions_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Convertit les actions"""
        if not actions_data:
            return []

        converted_actions = []
        for action in actions_data:
            name = action.get('name', 'Unknown')
            entries = action.get('entries', [])

            # Concatener les entrées en description
            desc_parts = []
            for entry in entries:
                if isinstance(entry, str):
                    desc_parts.append(entry)
                elif isinstance(entry, dict) and 'text' in entry:
                    desc_parts.append(entry['text'])

            description = ' '.join(desc_parts)

            converted_actions.append({
                "name": name,
                "desc": description,
                # TODO: Parser attack_bonus, damage, etc. depuis description
            })

        return converted_actions

    def convert_monster(self, monster_data: Dict[str, Any]) -> Dict[str, Any]:
        """Convertit un monstre 5e.tools vers le format Monster"""
        try:
            name = monster_data.get('name', 'Unknown Monster')

            # Structure de base compatible avec Monster class
            converted = {
                "name": name,
                "size": monster_data.get('size', ['M'])[0] if isinstance(monster_data.get('size'), list) else monster_data.get('size', 'M'),
                "type": monster_data.get('type', 'humanoid'),
                "alignment": monster_data.get('alignment', ['N'])[0] if isinstance(monster_data.get('alignment'), list) else monster_data.get('alignment', 'N'),
                "armor_class": self.convert_ac(monster_data.get('ac')),
                "hit_points": self.convert_hp(monster_data.get('hp')),
                "speed": self.convert_speed(monster_data.get('speed')),
                "abilities": self.convert_abilities(monster_data),
                "challenge_rating": self.convert_cr(monster_data.get('cr')),
                "source": monster_data.get('source', 'Unknown'),

                # Données optionnelles
                "saving_throws": monster_data.get('save', {}),
                "skills": monster_data.get('skill', {}),
                "damage_vulnerabilities": monster_data.get('vulnerable', []),
                "damage_resistances": monster_data.get('resist', []),
                "damage_immunities": monster_data.get('immune', []),
                "condition_immunities": monster_data.get('conditionImmune', []),
                "senses": monster_data.get('senses', []),
                "languages": monster_data.get('languages', []),

                # Actions et capacités (format 5e.tools préservé pour parsing ultérieur)
                "trait": monster_data.get('trait', []),
                "action": monster_data.get('action', []),
                "reaction": monster_data.get('reaction', []),
                "legendary": monster_data.get('legendary', []),
                "spellcasting": monster_data.get('spellcasting', []),

                # Métadonnées 5e.tools
                "_5etools": {
                    "page": monster_data.get('page'),
                    "otherSources": monster_data.get('otherSources', []),
                    "environment": monster_data.get('environment', []),
                    "soundClip": monster_data.get('soundClip'),
                    "isNpc": monster_data.get('isNpc', False),
                }
            }

            self.stats_converted += 1
            return converted

        except Exception as e:
            error_msg = f"Erreur conversion {monster_data.get('name', 'Unknown')}: {e}"
            self.errors.append(error_msg)
            return None

    def extract_monsters(self, input_file: Path, output_dir: Path) -> Dict[str, Any]:
        """Extrait et convertit tous les monstres"""
        print(f"📖 Lecture de {input_file}...")

        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                monsters_data = json.load(f)
        except json.JSONDecodeError as e:
            return {"error": f"Erreur lecture JSON: {e}", "success": False}

        if not isinstance(monsters_data, list):
            return {"error": "Le fichier doit contenir une liste de monstres", "success": False}

        print(f"✅ {len(monsters_data)} monstres trouvés")
        print(f"📁 Extraction vers {output_dir}/")
        print()

        # Créer le répertoire de sortie
        output_dir.mkdir(parents=True, exist_ok=True)

        # Statistiques
        total = len(monsters_data)
        converted = 0
        skipped = 0

        # Extraire chaque monstre
        for i, monster_data in enumerate(monsters_data, 1):
            name = monster_data.get('name', f'Unknown-{i}')

            # Convertir
            converted_monster = self.convert_monster(monster_data)

            if converted_monster is None:
                skipped += 1
                continue

            # Créer nom de fichier
            filename = self.normalize_filename(name)
            filepath = output_dir / filename

            # Écrire le fichier
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(converted_monster, f, indent=2, ensure_ascii=False)
                converted += 1

                # Afficher progression
                if i % 100 == 0 or i == total:
                    print(f"  [{i}/{total}] {name:50s} → {filename}")

            except Exception as e:
                error_msg = f"Erreur écriture {filename}: {e}"
                self.errors.append(error_msg)
                skipped += 1

        # Rapport final
        report = {
            "success": True,
            "total": total,
            "converted": converted,
            "skipped": skipped,
            "errors": self.errors,
            "warnings": self.warnings
        }

        return report


def main():
    """Point d'entrée principal"""
    print("=" * 80)
    print("🐉 EXTRACTION MONSTRES 5e.tools → dnd-5e-core")
    print("=" * 80)
    print()

    # Chemins
    script_dir = Path(__file__).parent
    input_file = script_dir / "bestiary-sublist-data.json"
    output_dir = script_dir

    # Vérifier que le fichier existe
    if not input_file.exists():
        print(f"❌ Fichier non trouvé: {input_file}")
        print()
        print("Placez le fichier bestiary-sublist-data.json (2228 monstres)")
        print("dans le même répertoire que ce script.")
        return 1

    # Créer le convertisseur
    converter = FiveEToolsToMonsterConverter()

    # Extraire
    report = converter.extract_monsters(input_file, output_dir)

    # Afficher le rapport
    print()
    print("=" * 80)
    print("📊 RAPPORT DE CONVERSION")
    print("=" * 80)

    if not report.get("success"):
        print(f"❌ {report.get('error')}")
        return 1

    print(f"✅ Total de monstres: {report['total']}")
    print(f"✅ Convertis avec succès: {report['converted']}")
    if report['skipped'] > 0:
        print(f"⚠️  Ignorés (erreurs): {report['skipped']}")

    if report['errors']:
        print()
        print(f"❌ Erreurs ({len(report['errors'])}):")
        for error in report['errors'][:10]:  # Afficher max 10 erreurs
            print(f"  • {error}")
        if len(report['errors']) > 10:
            print(f"  ... et {len(report['errors']) - 10} autres erreurs")

    if report['warnings']:
        print()
        print(f"⚠️  Avertissements ({len(report['warnings'])}):")
        for warning in report['warnings'][:10]:
            print(f"  • {warning}")

    print()
    print("=" * 80)
    print("✅ EXTRACTION TERMINÉE!")
    print("=" * 80)
    print()
    print(f"📁 Fichiers créés dans: {output_dir}/")
    print(f"📄 Format: nom-du-monstre.json")
    print()

    return 0


if __name__ == "__main__":
    exit(main())
