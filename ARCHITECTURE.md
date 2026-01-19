# Architecture du Package dnd-5e-core

## 📁 Structure du Projet

```
dnd-5e-core/
├── dnd_5e_core/              # Package principal
│   ├── __init__.py
│   ├── abilities/            # Système de caractéristiques
│   ├── classes/              # Classes de personnages
│   ├── combat/               # Système de combat
│   │   ├── combat_system.py
│   │   ├── condition.py      # Conditions (Restrained, Poisoned, etc.)
│   │   └── special_ability.py
│   ├── data/                 # ⭐ DONNÉES JSON (incluses dans le package)
│   │   ├── loader.py         # Fonctions de chargement
│   │   ├── loaders.py        # Générateurs de personnages
│   │   ├── monsters/         # 332+ monstres JSON
│   │   ├── spells/           # 319 sorts JSON
│   │   ├── equipment/        # Armes, armures, objets
│   │   ├── magic-items/      # Objets magiques
│   │   ├── classes/          # Données des classes
│   │   ├── races/            # Données des races
│   │   └── ...
│   ├── entities/             # Character, Monster, Sprite
│   ├── equipment/            # Weapon, Armor, MagicItem
│   ├── mechanics/            # Dice, CR, encounter building
│   ├── races/                # Race definitions
│   ├── spells/               # Spell system
│   └── utils/                # Utilities
├── setup.py
├── MANIFEST.in              # Inclut tous les JSON
└── README.md
```

## 🎯 Changement Majeur (v0.2.3)

### Avant
- Données dans `data/` à la racine (non incluses dans le package)
- Nécessitait configuration manuelle avec `set_data_directory()`
- Ne fonctionnait pas après installation pip

### Maintenant ✅
- **Toutes les données dans `dnd_5e_core/data/`**
- **Automatiquement incluses dans le package installé**
- **Fonctionne immédiatement après `pip install dnd-5e-core`**
- Aucune configuration nécessaire

## 📦 Utilisation

### Installation
```bash
pip install dnd-5e-core
```

### Chargement Automatique des Données
```python
from dnd_5e_core.data import load_monster, load_spell

# Charge automatiquement depuis dnd_5e_core/data/monsters/
goblin = load_monster("goblin")
print(f"{goblin.name} - CR {goblin.challenge_rating}")

# Charge depuis dnd_5e_core/data/spells/
fireball = load_spell("fireball")
print(f"{fireball.name} - Level {fireball.level}")
```

### Données Disponibles

Le package inclut **toutes** les données D&D 5e :
- ✅ **332 monstres** (dnd_5e_core/data/monsters/)
- ✅ **319 sorts** (dnd_5e_core/data/spells/)
- ✅ **Armes et armures** (dnd_5e_core/data/equipment/)
- ✅ **Objets magiques** (dnd_5e_core/data/magic-items/)
- ✅ **Classes** (dnd_5e_core/data/classes/)
- ✅ **Races** (dnd_5e_core/data/races/)
- ✅ **Tables de rencontre** (intégrées dans le code)

## 🔧 Développement

### Mode Éditable
```bash
git clone https://github.com/codingame-team/dnd-5e-core.git
cd dnd-5e-core
pip install -e .
```

En mode éditable, les modifications dans `dnd_5e_core/data/` sont immédiatement disponibles.

### Ajouter des Données

Pour ajouter un nouveau monstre :
1. Créer `dnd_5e_core/data/monsters/mon-monstre.json`
2. Utiliser le format JSON standard D&D 5e API
3. Le monstre sera automatiquement disponible via `load_monster("mon-monstre")`

## 🌐 100% Offline

Toutes les données sont **embarquées dans le package**. Aucune connexion Internet requise après installation.

## 📊 Taille du Package

- Package complet : ~15 MB (avec tous les JSON)
- Wheel (.whl) : ~2 MB (compressé)
- Source (.tar.gz) : ~2 MB

Les données JSON sont essentielles au fonctionnement du package, c'est pourquoi elles sont toutes incluses.
