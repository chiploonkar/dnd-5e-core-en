#!/usr/bin/env python3
"""
Utility script to download the tokens of all implemented monsters from 5e.tools

Usage:
    python download_all_tokens.py [--output FOLDER]

Options:
    --output FOLDER    Destination folder for tokens (default: ./tokens)
    --help            Show this help
"""
import sys
import argparse
from pathlib import Path

# Add the parent directory to PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent))

from dnd_5e_core.entities import get_extended_monster_loader
from dnd_5e_core.utils import download_tokens_batch


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Downloads tokens of all implemented monsters from 5e.tools"
    )
    parser.add_argument(
        '--output', '-o',
        default='./tokens',
        help='Destination folder for tokens (default: ./tokens)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show monsters that would be downloaded without downloading them'
    )

    args = parser.parse_args()

    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 16 + "DOWNLOADING TOKENS FROM 5E.TOOLS" + " " * 20 + "║")
    print("╚" + "═" * 68 + "╝")
    print()

    # Load monsters
    print("[1] Loading monster list...")
    loader = get_extended_monster_loader()
    monsters = loader.load_implemented_monsters()

    print(f"    ✓ {len(monsters)} monsters found")
    print()

    # Create the list of tuples (name, source)
    monster_list = []
    for monster in monsters:
        name = monster.get('name')
        source = monster.get('source', 'MM')
        if name:
            monster_list.append((name, source))

    print(f"[2] Preparing to download {len(monster_list)} tokens...")
    print(f"    Destination: {args.output}")
    print()

    if args.dry_run:
        print("[DRY RUN] Monsters that would be downloaded:")
        print("-" * 70)
        for i, (name, source) in enumerate(monster_list, 1):
            print(f"  {i:3d}. {name:40s} [{source}]")
        print("-" * 70)
        print(f"\nTotal: {len(monster_list)} tokens")
        print("\nTo actually download, rerun without --dry-run")
        return

    # Download tokens
    print("[3] Download in progress...")
    print("-" * 70)

    results = download_tokens_batch(monster_list, save_folder=args.output)

    print("-" * 70)
    print()

    # Show failures
    failed = [(name, code) for name, code in results.items() if code != 200]
    if failed:
        print("[4] Download failures:")
        for name, code in failed:
            print(f"    ✗ {name} (HTTP {code})")
        print()

    print("✓ Download complete!")
    print(f"  Tokens saved in: {args.output}")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Download interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
