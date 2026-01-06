# Guide : Chargement des données D&D 5e depuis JSON

## Situation actuelle

Le package `dnd-5e-core` installé via PyPI **ne contient pas** tous les fichiers de données JSON (races, classes, équipements, etc.) pour réduire la taille du package.

**Seules les données de monstres** sont incluses dans le package PyPI (`bestiary-sublist-data.json`).

## Options pour charger les données

### Option 1 : Création manuelle (Recommandé pour les exemples)

Créez vos objets manuellement comme dans `create_character.py` :

```python
from dnd_5e_core.races import Race
from dnd_5e_core.classes import ClassType

# Créer une race manuellement
elf = Race(
    index="elf",
    name="Elf",
    speed=30,
    ability_bonuses={"dex": 2},
    alignment="Chaotic Good",
    age="Elves can live to be 750 years old",
    size="Medium",
    size_description="Elves range from under 5 to over 6 feet tall",
    starting_proficiencies=[],
    starting_proficiency_options=[],
    languages=[],
    language_desc="You can speak, read, and write Common and Elvish",
    traits=[],
    subraces=[]
)
```

### Option 2 : Télécharger les fichiers JSON depuis GitHub

1. **Télécharger les données complètes** :
   ```bash
   git clone https://github.com/codingame-team/dnd-5e-core.git
   cd dnd-5e-core
   ```

2. **Copier les dossiers de données** :
   ```bash
   cp -r data /votre/projet/
   ```

3. **Configurer le répertoire de données** :
   ```python
   from dnd_5e_core.data import set_data_directory, load_race, load_class
   
   # Pointer vers votre dossier de données local
   set_data_directory("/chemin/vers/data")
   
   # Charger les données
   elf_data = load_race("elf")
   wizard_data = load_class("wizard")
   
   # Créer les objets (nécessite un parser pour convertir JSON → objets Python)
   # Note: Actuellement, il n'y a pas de méthode from_dict() automatique
   ```

### Option 3 : Utiliser l'API D&D 5e (En ligne)

Utilisez l'API officielle D&D 5e : https://www.dnd5eapi.co/

```python
import requests

def load_from_api(category: str, index: str):
    """Charger depuis l'API D&D 5e"""
    url = f"https://www.dnd5eapi.co/api/{category}/{index}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Exemple
elf_data = load_from_api("races", "elf")
wizard_data = load_from_api("classes", "wizard")
```

## Fichiers JSON disponibles dans le package PyPI

✅ **Inclus** :
- `dnd_5e_core/data/monsters/bestiary-sublist-data.json` (422 KB)
- `dnd_5e_core/data/monsters/bestiary-sublist-data-all-monsters.json` (8.5 MB)

❌ **Non inclus** (disponibles sur GitHub) :
- `data/races/*.json`
- `data/classes/*.json`
- `data/spells/*.json`
- `data/equipment/*.json`
- `data/weapons/*.json`
- `data/armors/*.json`
- `collections/*.json`
- Tokens d'images (102 MB)

## Pourquoi les données ne sont pas incluses ?

### Limite de taille PyPI
- Limite par défaut : **100 MB**
- Les tokens d'images seuls font **102 MB**
- Les données JSON complètes ajoutent plusieurs MB supplémentaires

### Solution appliquée
Pour respecter la limite PyPI, nous avons :
1. ✅ Inclus les données des monstres (essentielles pour `search_monsters()`)
2. ❌ Exclu les tokens d'images
3. ❌ Exclu les autres données JSON (races, classes, etc.)

Les utilisateurs peuvent télécharger ces fichiers depuis GitHub selon leurs besoins.

## Exemple complet avec données manuelles

Voir le fichier `create_character.py` pour un exemple fonctionnel qui :
- Crée un personnage Elf Wizard
- Définit les abilities
- Affiche les statistiques

Ce script fonctionne **sans avoir besoin de télécharger** les fichiers JSON supplémentaires.

## Fonction de chargement disponible

```python
from dnd_5e_core.data import (
    load_monster,   # ✅ Fonctionne (données incluses)
    load_race,      # ⚠️ Nécessite data/races/ localement
    load_class,     # ⚠️ Nécessite data/classes/ localement
    load_spell,     # ⚠️ Nécessite data/spells/ localement
    load_equipment, # ⚠️ Nécessite data/equipment/ localement
    load_weapon,    # ⚠️ Nécessite data/weapons/ localement
    load_armor,     # ⚠️ Nécessite data/armors/ localement
)
```

## Recommandations

### Pour tester rapidement
→ Utilisez la création manuelle (comme dans `create_character.py`)

### Pour un projet complet
→ Téléchargez les données depuis GitHub et configurez `set_data_directory()`

### Pour une application en production
→ Utilisez l'API D&D 5e en ligne (https://www.dnd5eapi.co/) avec cache local

## Liens utiles

- **Package PyPI** : https://pypi.org/project/dnd-5e-core/
- **GitHub Repository** : https://github.com/codingame-team/dnd-5e-core
- **Données JSON** : https://github.com/codingame-team/dnd-5e-core/tree/main/data
- **API D&D 5e** : https://www.dnd5eapi.co/
- **Documentation API** : https://www.dnd5eapi.co/docs/

