"""
Script to download level progression data for each D&D 5e class
Based on the API: https://5e-bits.github.io/docs/api/get-all-level-resources-for-a-class
"""
import json
import os
import requests
from pathlib import Path


def download_class_levels(class_index: str, output_dir: str = "dnd_5e_core/data/class_levels"):
    """
    Downloads level progression data for a class

    Args:
        class_index: Class index (e.g., 'wizard', 'fighter', 'cleric')
        output_dir: Output directory for JSON files
    """
    url = f"https://www.dnd5eapi.co/api/classes/{class_index}/levels"

    print(f"📥 Downloading levels for {class_index}...")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Create directory if necessary
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        # Save data
        output_file = os.path.join(output_dir, f"{class_index}_levels.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"   ✅ {len(data)} levels saved in {output_file}")
        return True

    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def download_all_class_levels():
    """Downloads levels for all D&D 5e classes"""

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
    print("DOWNLOADING LEVEL PROGRESSION DATA")
    print("=" * 80)

    success_count = 0

    for class_name in classes:
        if download_class_levels(class_name):
            success_count += 1

    print(f"\n📊 Result: {success_count}/{len(classes)} classes downloaded")
    print("=" * 80)


def download_class_features():
    """Downloads features for each class"""

    print("\n" + "=" * 80)
    print("DOWNLOADING CLASS FEATURES")
    print("=" * 80)

    # Get the list of all features
    url = "https://www.dnd5eapi.co/api/features"

    try:
        response = requests.get(url)
        response.raise_for_status()
        features_list = response.json()

        output_dir = "dnd_5e_core/data/features"
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        print(f"📥 Downloading {len(features_list['results'])} features...")

        for feature in features_list['results'][:20]:  # Limit for testing
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

        print(f"\n✅ Features downloaded to {output_dir}")

    except Exception as e:
        print(f"❌ Error: {e}")


def download_traits():
    """Downloads racial traits"""

    print("\n" + "=" * 80)
    print("DOWNLOADING RACIAL TRAITS")
    print("=" * 80)

    url = "https://www.dnd5eapi.co/api/traits"

    try:
        response = requests.get(url)
        response.raise_for_status()
        traits_list = response.json()

        output_dir = "dnd_5e_core/data/traits"
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        print(f"📥 Downloading {len(traits_list['results'])} traits...")

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

        print(f"\n✅ Traits downloaded to {output_dir}")

    except Exception as e:
        print(f"❌ Error: {e}")


def download_subclasses():
    """Downloads subclasses for all classes"""

    print("\n" + "=" * 80)
    print("DOWNLOADING SUBCLASSES")
    print("=" * 80)

    url = "https://www.dnd5eapi.co/api/subclasses"

    try:
        response = requests.get(url)
        response.raise_for_status()
        subclasses_list = response.json()

        output_dir = "dnd_5e_core/data/subclasses"
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        print(f"📥 Downloading {len(subclasses_list['results'])} subclasses...")

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

        print(f"\n✅ Subclasses downloaded to {output_dir}")

    except Exception as e:
        print(f"❌ Error: {e}")


def download_subraces():
    """Downloads subraces"""

    print("\n" + "=" * 80)
    print("DOWNLOADING SUBRACES")
    print("=" * 80)

    url = "https://www.dnd5eapi.co/api/subraces"

    try:
        response = requests.get(url)
        response.raise_for_status()
        subraces_list = response.json()

        output_dir = "dnd_5e_core/data/subraces"
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        print(f"📥 Downloading {len(subraces_list['results'])} subraces...")

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

        print(f"\n✅ Subraces downloaded to {output_dir}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    # Change to the package directory
    os.chdir("/Users/display/PycharmProjects/dnd-5e-core")

    # 1. Download levels for all classes
    download_all_class_levels()

    # 2. Download some features for example
    download_class_features()

    # 3. Download racial traits
    download_traits()

    # 4. Download subclasses (NEW)
    download_subclasses()

    # 5. Download subraces (NEW)
    download_subraces()

    print("\n✅ DOWNLOAD COMPLETE!")
