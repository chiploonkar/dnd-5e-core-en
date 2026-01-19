"""
Script pour télécharger les données de progression par niveau pour chaque classe D&D 5e
Basé sur l'API: https://5e-bits.github.io/docs/api/get-all-level-resources-for-a-class
"""
import json
import os
import requests
from pathlib import Path


def download_class_levels(class_index: str, output_dir: str = "dnd_5e_core/data/class_levels"):
    """
    Télécharge les données de progression par niveau pour une classe

    Args:
        class_index: Index de la classe (ex: 'wizard', 'fighter', 'cleric')
        output_dir: Répertoire de sortie pour les fichiers JSON
    """
    url = f"https://www.dnd5eapi.co/api/classes/{class_index}/levels"

    print(f"📥 Téléchargement des niveaux pour {class_index}...")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Créer le répertoire si nécessaire
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        # Sauvegarder les données
        output_file = os.path.join(output_dir, f"{class_index}_levels.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"   ✅ {len(data)} niveaux sauvegardés dans {output_file}")
        return True

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return False


def download_all_class_levels():
    """Télécharge les niveaux pour toutes les classes D&D 5e"""

    classes = [
        'barbarian',
        'bard',
        'cleric',
        'druid',
        'fighter',
        'monk',
        'paladin',
        'ranger',
        'rogue',
        'sorcerer',
        'warlock',
        'wizard'
    ]

    print("\n" + "=" * 80)
    print("TÉLÉCHARGEMENT DES DONNÉES DE PROGRESSION PAR NIVEAU")
    print("=" * 80)

    success_count = 0

    for class_name in classes:
        if download_class_levels(class_name):
            success_count += 1

    print(f"\n📊 Résultat: {success_count}/{len(classes)} classes téléchargées")
    print("=" * 80)


def download_class_features():
    """Télécharge les features de chaque classe"""

    print("\n" + "=" * 80)
    print("TÉLÉCHARGEMENT DES FEATURES DE CLASSES")
    print("=" * 80)

    # Obtenir la liste de toutes les features
    url = "https://www.dnd5eapi.co/api/features"

    try:
        response = requests.get(url)
        response.raise_for_status()
        features_list = response.json()

        output_dir = "dnd_5e_core/data/features"
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        print(f"📥 Téléchargement de {len(features_list['results'])} features...")

        for feature in features_list['results'][:20]:  # Limiter pour test
            feature_index = feature['index']
            feature_url = f"https://www.dnd5eapi.co{feature['url']}"

            try:
                feat_response = requests.get(feature_url)
                feat_response.raise_for_status()
                feat_data = feat_response.json()

                output_file = os.path.join(output_dir, f"{feature_index}.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(feat_data, f, indent=2, ensure_ascii=False)

                print(f"   ✅ {feature_index}")

            except Exception as e:
                print(f"   ❌ {feature_index}: {e}")

        print(f"\n✅ Features téléchargées dans {output_dir}")

    except Exception as e:
        print(f"❌ Erreur: {e}")


def download_traits():
    """Télécharge les traits de races"""

    print("\n" + "=" * 80)
    print("TÉLÉCHARGEMENT DES TRAITS DE RACES")
    print("=" * 80)

    url = "https://www.dnd5eapi.co/api/traits"

    try:
        response = requests.get(url)
        response.raise_for_status()
        traits_list = response.json()

        output_dir = "dnd_5e_core/data/traits"
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        print(f"📥 Téléchargement de {len(traits_list['results'])} traits...")

        for trait in traits_list['results']:
            trait_index = trait['index']
            trait_url = f"https://www.dnd5eapi.co{trait['url']}"

            try:
                trait_response = requests.get(trait_url)
                trait_response.raise_for_status()
                trait_data = trait_response.json()

                output_file = os.path.join(output_dir, f"{trait_index}.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(trait_data, f, indent=2, ensure_ascii=False)

                print(f"   ✅ {trait_index}")

            except Exception as e:
                print(f"   ❌ {trait_index}: {e}")

        print(f"\n✅ Traits téléchargés dans {output_dir}")

    except Exception as e:
        print(f"❌ Erreur: {e}")


def download_subclasses():
    """Télécharge les sous-classes de toutes les classes"""

    print("\n" + "=" * 80)
    print("TÉLÉCHARGEMENT DES SOUS-CLASSES")
    print("=" * 80)

    url = "https://www.dnd5eapi.co/api/subclasses"

    try:
        response = requests.get(url)
        response.raise_for_status()
        subclasses_list = response.json()

        output_dir = "dnd_5e_core/data/subclasses"
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        print(f"📥 Téléchargement de {len(subclasses_list['results'])} sous-classes...")

        for subclass in subclasses_list['results']:
            subclass_index = subclass['index']
            subclass_url = f"https://www.dnd5eapi.co{subclass['url']}"

            try:
                subclass_response = requests.get(subclass_url)
                subclass_response.raise_for_status()
                subclass_data = subclass_response.json()

                output_file = os.path.join(output_dir, f"{subclass_index}.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(subclass_data, f, indent=2, ensure_ascii=False)

                print(f"   ✅ {subclass_index}")

            except Exception as e:
                print(f"   ❌ {subclass_index}: {e}")

        print(f"\n✅ Sous-classes téléchargées dans {output_dir}")

    except Exception as e:
        print(f"❌ Erreur: {e}")


def download_subraces():
    """Télécharge les sous-races"""

    print("\n" + "=" * 80)
    print("TÉLÉCHARGEMENT DES SOUS-RACES")
    print("=" * 80)

    url = "https://www.dnd5eapi.co/api/subraces"

    try:
        response = requests.get(url)
        response.raise_for_status()
        subraces_list = response.json()

        output_dir = "dnd_5e_core/data/subraces"
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        print(f"📥 Téléchargement de {len(subraces_list['results'])} sous-races...")

        for subrace in subraces_list['results']:
            subrace_index = subrace['index']
            subrace_url = f"https://www.dnd5eapi.co{subrace['url']}"

            try:
                subrace_response = requests.get(subrace_url)
                subrace_response.raise_for_status()
                subrace_data = subrace_response.json()

                output_file = os.path.join(output_dir, f"{subrace_index}.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(subrace_data, f, indent=2, ensure_ascii=False)

                print(f"   ✅ {subrace_index}")

            except Exception as e:
                print(f"   ❌ {subrace_index}: {e}")

        print(f"\n✅ Sous-races téléchargées dans {output_dir}")

    except Exception as e:
        print(f"❌ Erreur: {e}")


if __name__ == "__main__":
    # Changer vers le répertoire du package
    os.chdir("/Users/display/PycharmProjects/dnd-5e-core")

    # 1. Télécharger les niveaux de toutes les classes
    download_all_class_levels()

    # 2. Télécharger quelques features pour exemple
    download_class_features()

    # 3. Télécharger les traits de races
    download_traits()

    # 4. Télécharger les sous-classes (NEW)
    download_subclasses()

    # 5. Télécharger les sous-races (NEW)
    download_subraces()

    print("\n✅ TÉLÉCHARGEMENT TERMINÉ!")
