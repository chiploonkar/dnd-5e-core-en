#!/usr/bin/env python3
"""
Script de vérification du package dnd-5e-core
Vérifie que le package est autonome et n'a pas de dépendances externes
"""
import sys
import os
from pathlib import Path

def check_external_dependencies():
    """Vérifie qu'il n'y a pas de dépendances à des modules externes"""
    package_root = Path(__file__).parent / "dnd_5e_core"
    bad_imports = []

    # Modules externes interdits
    forbidden_modules = [
        "populate_functions",
        "populate_rpg_functions",
        "dao_classes",
        "dao_rpg_classes_tk",
        "game_entity",
    ]

    # Parcourir tous les fichiers Python du package
    for filepath in package_root.rglob("*.py"):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for module in forbidden_modules:
            if f"from {module} import" in content or f"import {module}" in content:
                bad_imports.append((filepath, module))

    return bad_imports

def check_package_structure():
    """Vérifie la structure du package"""
    package_root = Path(__file__).parent / "dnd_5e_core"

    required_modules = [
        "__init__.py",
        "abilities/__init__.py",
        "equipment/__init__.py",
        "spells/__init__.py",
        "combat/__init__.py",
        "combat/combat_system.py",
        "classes/__init__.py",
        "data/__init__.py",
        "data/loader.py",
        "data/collections.py",
        "entities/__init__.py",
        "entities/character.py",
        "entities/monster.py",
        "entities/extended_monsters.py",
        "mechanics/__init__.py",
        "mechanics/challenge_rating.py",
        "mechanics/dice.py",
        "races/__init__.py",
    ]

    missing = []
    for module in required_modules:
        if not (package_root / module).exists():
            missing.append(module)

    return missing

def test_imports():
    """Test d'import des modules principaux"""
    errors = []

    try:
        from dnd_5e_core import Character, Monster, Abilities
    except ImportError as e:
        errors.append(f"Entités de base: {e}")

    try:
        from dnd_5e_core.combat import CombatSystem
    except ImportError as e:
        errors.append(f"Combat: {e}")

    try:
        from dnd_5e_core.data import load_monster, load_spell
    except ImportError as e:
        errors.append(f"Data: {e}")

    try:
        from dnd_5e_core.mechanics import calculate_encounter_difficulty
    except ImportError as e:
        errors.append(f"Mechanics: {e}")

    try:
        from dnd_5e_core.entities import FiveEToolsMonsterLoader
    except ImportError as e:
        errors.append(f"Extended Monsters: {e}")

    return errors

def check_data_files():
    """Vérifie la présence des fichiers de données"""
    data_dir = Path(__file__).parent / "dnd_5e_core" / "data"

    required_files = [
        "monsters",
        "spells",
        "equipment",
        "classes",
        "races",
    ]

    missing = []
    for dirname in required_files:
        dir_path = data_dir / dirname
        if not dir_path.exists():
            missing.append(dirname)
        elif not any(dir_path.glob("*.json")):
            missing.append(f"{dirname} (vide)")

    return missing

def main():
    print("=" * 70)
    print("  VÉRIFICATION DU PACKAGE dnd-5e-core")
    print("=" * 70)

    # 1. Vérifier les dépendances externes
    print("\n📋 Vérification des dépendances externes...")
    bad_imports = check_external_dependencies()

    if bad_imports:
        print(f"❌ {len(bad_imports)} dépendance(s) externe(s) trouvée(s):")
        for filepath, module in bad_imports:
            print(f"   - {filepath.name}: imports {module}")
        sys.exit(1)
    else:
        print("✅ Aucune dépendance externe détectée")

    # 2. Vérifier la structure du package
    print("\n📋 Vérification de la structure du package...")
    missing_modules = check_package_structure()

    if missing_modules:
        print(f"⚠️  {len(missing_modules)} module(s) manquant(s):")
        for module in missing_modules:
            print(f"   - {module}")
    else:
        print("✅ Tous les modules requis sont présents")

    # 3. Test d'import
    print("\n📋 Test d'import des modules principaux...")
    errors = test_imports()

    if errors:
        print(f"❌ {len(errors)} erreur(s) d'import:")
        for error in errors:
            print(f"   - {error}")
        sys.exit(1)
    else:
        print("✅ Tous les modules s'importent correctement")

    # 4. Vérifier les fichiers de données
    print("\n📋 Vérification des fichiers de données...")
    missing_data = check_data_files()

    if missing_data:
        print(f"⚠️  {len(missing_data)} répertoire(s) de données manquant(s):")
        for dirname in missing_data:
            print(f"   - {dirname}")
    else:
        print("✅ Tous les fichiers de données sont présents")

    # 5. Vérifier les fichiers de configuration
    print("\n📋 Vérification des fichiers de configuration...")
    package_root = Path(__file__).parent

    config_files = [
        "setup.py",
        "pyproject.toml",
        "README.md",
        "LICENSE",
        "requirements.txt",
    ]

    missing_config = []
    for filename in config_files:
        if not (package_root / filename).exists():
            missing_config.append(filename)

    if missing_config:
        print(f"⚠️  {len(missing_config)} fichier(s) de config manquant(s):")
        for filename in missing_config:
            print(f"   - {filename}")
    else:
        print("✅ Tous les fichiers de configuration sont présents")

    # Résultat final
    print("\n" + "=" * 70)
    print("  ✅ VÉRIFICATION COMPLÈTE - PACKAGE PRÊT")
    print("=" * 70)
    print("\nLe package dnd-5e-core est autonome et prêt à être publié ✨")
    print("Aucune dépendance externe détectée ✨")

    # Afficher la version
    try:
        from dnd_5e_core import __version__
        print(f"\nVersion actuelle: {__version__}")
    except:
        print("\n⚠️  Version non définie dans __init__.py")

if __name__ == "__main__":
    main()

