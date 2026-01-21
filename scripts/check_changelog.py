#!/usr/bin/env python3
"""Vérifier que CHANGELOG.md contient une entrée pour la version actuelle.
Usage: python3 scripts/check_changelog.py
Sortie: code 0 si OK, code 2 si l'entrée est manquante, code 1 pour d'autres erreurs.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
CHANGELOG = ROOT / "CHANGELOG.md"

if not PYPROJECT.exists():
    print("ERROR: pyproject.toml introuvable", file=sys.stderr)
    sys.exit(1)

if not CHANGELOG.exists():
    print("ERROR: CHANGELOG.md introuvable", file=sys.stderr)
    sys.exit(1)

# Lire la version dans pyproject.toml (recherche simple)
text = PYPROJECT.read_text(encoding='utf-8')
match = re.search(r"^version\s*=\s*[\"']([^\"']+)[\"']", text, re.MULTILINE)
if not match:
    print("ERROR: Impossible de trouver la clé 'version' dans pyproject.toml", file=sys.stderr)
    sys.exit(1)

version = match.group(1).strip()

# Lire le changelog et chercher une entrée '## [<version>]'
changelog_text = CHANGELOG.read_text(encoding='utf-8')
pattern = r"^## \[{}\]".format(re.escape(version))
if re.search(pattern, changelog_text, re.MULTILINE):
    print(f"OK: CHANGELOG.md contient bien une entrée pour la version {version}")
    sys.exit(0)
else:
    print("\n❌ ERREUR: CHANGELOG.md ne contient PAS d'entrée pour la version actuelle:")
    print(f"   version attendue: {version}\n")
    print("Actions recommandées:")
    print("  1) Ajouter une section dans CHANGELOG.md en respectant le format Keep a Changelog:\n")
    print("     ## [<version>] - YYYY-MM-DD\n\n     - Added: ...\n     - Fixed: ...\n")
    print("  2) Committer la modification et ré-exécuter la publication")
    print("  3) Si vous publiez une version mineure/patch sans changelog volontairement, ajoutez une courte note 'No notable changes' pour garder l'historique clair.")
    print("\nExemple rapide (copier-coller) :\n\n## [" + version + "] - 2026-01-21\n\n### Added\n- Brève description des changements\n")
    sys.exit(2)
