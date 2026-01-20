#!/usr/bin/env python3
"""
Script pour télécharger les tokens de tous les monstres extended
"""
import os
import sys
from pathlib import Path

# Ajouter le chemin du package
sys.path.insert(0, str(Path(__file__).parent.parent))

from dnd_5e_core.data.loader import list_json_files, load_monster
from dnd_5e_core.utils.token_downloader import download_monster_token_auto


def download_all_extended_tokens(save_folder: str = None):
    """
    Télécharge les tokens de tous les monstres extended.

    :param save_folder: Dossier de destination (par défaut: data/monsters/tokens)
    """
    if save_folder is None:
        # Utiliser le dossier tokens dans data/monsters/
        data_dir = Path(__file__).parent.parent / "dnd_5e_core" / "data" / "monsters" / "tokens"
        save_folder = str(data_dir)

    # Créer le dossier s'il n'existe pas
    os.makedirs(save_folder, exist_ok=True)

    print("=" * 80)
    print("TÉLÉCHARGEMENT DES TOKENS - MONSTRES EXTENDED")
    print("=" * 80)
    print()

    # Lister tous les monstres extended
    extended_monsters = list_json_files("monsters/extended")

    print(f"Monstres extended trouvés: {len(extended_monsters)}")
    print()

    # Demander confirmation
    response = input("Continuer le téléchargement? (y/n): ")
    if response.lower() != 'y':
        print("Téléchargement annulé.")
        return

    print()
    print("Téléchargement en cours...")
    print()

    results = {
        'success': 0,
        'failed': 0,
        'skipped': 0
    }

    failed_monsters = []

    for i, monster_index in enumerate(extended_monsters, 1):
        # Charger le monstre pour obtenir son nom et sa source
        try:
            monster = load_monster(monster_index)
        except Exception as e:
            print(f"[{i}/{len(extended_monsters)}] ⚠️  Erreur chargement: {monster_index} - {str(e)[:50]}")
            results['skipped'] += 1
            continue

        if not monster:
            print(f"[{i}/{len(extended_monsters)}] ⚠️  Impossible de charger: {monster_index}")
            results['skipped'] += 1
            continue

        # Vérifier si le token existe déjà
        token_path = Path(save_folder) / f"{monster_index}.webp"
        if token_path.exists():
            # Token déjà téléchargé, on skip
            if i % 100 == 0:
                print(f"[{i}/{len(extended_monsters)}] ✓ {results['success']} réussis, {results['failed']} échoués, {results['skipped']} skipped")
            results['skipped'] += 1
            continue

        # Télécharger le token
        try:
            status = download_monster_token_auto(monster, save_folder)
        except Exception as e:
            print(f"[{i}/{len(extended_monsters)}] ❌ Erreur téléchargement: {monster.name} - {str(e)[:50]}")
            results['failed'] += 1
            failed_monsters.append((monster.name, monster.source or 'Unknown', monster_index))
            continue

        if status == 200:
            results['success'] += 1
            if i % 10 == 0:
                print(f"[{i}/{len(extended_monsters)}] ✅ {monster.name} [{monster.source}]")
        else:
            results['failed'] += 1
            failed_monsters.append((monster.name, monster.source or 'Unknown', monster_index))
            if i % 10 == 0:
                print(f"[{i}/{len(extended_monsters)}] ❌ {monster.name} [{monster.source}] (HTTP {status})")

    print()
    print("=" * 80)
    print("RÉSUMÉ")
    print("=" * 80)
    print(f"✅ Réussis: {results['success']}")
    print(f"❌ Échoués: {results['failed']}")
    print(f"⏭️  Skipped (déjà existants): {results['skipped']}")
    print()

    if failed_monsters:
        print("Monstres échoués:")
        for name, source, index in failed_monsters[:20]:  # Afficher max 20
            print(f"  - {name} [{source}] ({index})")
        if len(failed_monsters) > 20:
            print(f"  ... et {len(failed_monsters) - 20} autres")

    print()
    print(f"Tokens sauvegardés dans: {save_folder}")


if __name__ == "__main__":
    download_all_extended_tokens()
