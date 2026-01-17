# dnd-5e-core - Documentation Index

Guide complet pour naviguer dans la documentation du package.

## 📚 Documentation Principale

### Pour Commencer
1. **[README.md](README.md)** - Vue d'ensemble du package
   - Installation
   - Fonctionnalités
   - Quick Start
   - Exemples

2. **[COMBAT_EXAMPLES.md](COMBAT_EXAMPLES.md)** - Exemples de combat complets
   - Combat avec spellcasting
   - Équipement d'armes et armures
   - Formation de groupe
   - Exemples prêts à copier

3. **[CHANGELOG.md](CHANGELOG.md)** - Historique des versions
   - Nouvelles fonctionnalités
   - Corrections de bugs
   - Changements importants

### Documentation API Complète

**[docs/](docs/)** - Documentation technique détaillée :
- **[docs/api/](docs/api/)** - Documentation de chaque module
  - [entities.md](docs/api/entities.md) - Characters & Monsters
  - [combat.md](docs/api/combat.md) - Combat System
  - [spells.md](docs/api/spells.md) - Magic System
  - [equipment.md](docs/api/equipment.md) - Weapons, Armor, Items
  - [mechanics.md](docs/api/mechanics.md) - Game Mechanics
  - [data.md](docs/api/data.md) - Data Loading
  - Et plus...

### Pour Contribuer

**[CONTRIBUTING.md](CONTRIBUTING.md)** - Guide de contribution
- Comment contribuer
- Standards de code
- Process de PR
- Tests requis

## 🧪 Tests et Exemples

**[tests/](tests/)** - Scripts de test et exemples

**[tests/README.md](tests/README.md)** - Guide des tests
- Tests unitaires
- Exemples d'utilisation
- Comment exécuter les tests
- **[tests/examples/](tests/examples/)** - Exemples de code

### Principaux Tests
- `test_spell_loading.py` - Chargement des sorts
- `test_extended_monsters.py` - Monstres étendus
- `test_collections_migration.py` - Collections
- `verify_package.py` - Vérification d'installation

## 📦 Structure du Projet

```
dnd-5e-core/
├── README.md              # Documentation principale
├── CHANGELOG.md           # Historique des versions
├── COMBAT_EXAMPLES.md     # Exemples de combat
├── CONTRIBUTING.md        # Guide de contribution
├── INDEX.md               # Ce fichier
│
├── dnd_5e_core/          # Code du package
│   ├── abilities/        # Système de capacités
│   ├── classes/          # Classes de personnages
│   ├── combat/           # Système de combat
│   ├── data/             # Chargeurs de données
│   ├── entities/         # Personnages, monstres
│   ├── equipment/        # Équipement
│   ├── mechanics/        # Mécaniques de jeu
│   ├── races/            # Races
│   ├── spells/           # Système de sorts
│   └── ui/               # Utilitaires UI
│
├── data/                 # Données D&D 5e (8.7 MB)
├── docs/                 # Documentation API
├── tests/                # Tests et exemples
│   ├── examples/         # Exemples d'utilisation
│   └── *.py              # Scripts de test
│
└── archive/              # Documents historiques
```

## 🎯 Par Cas d'Usage

### Je veux créer un personnage
→ [README.md - Create a Character](README.md#create-a-character)
→ [docs/api/entities.md](docs/api/entities.md)

### Je veux faire un combat
→ [COMBAT_EXAMPLES.md](COMBAT_EXAMPLES.md)
→ [docs/api/combat.md](docs/api/combat.md)

### Je veux utiliser des sorts
→ [COMBAT_EXAMPLES.md - Spellcasting](COMBAT_EXAMPLES.md#spellcaster-vs-spellcaster-combat)
→ [docs/api/spells.md](docs/api/spells.md)

### Je veux charger des monstres
→ [README.md - Load D&D 5e Data](README.md#load-dd-5e-data)
→ [docs/api/data.md](docs/api/data.md)

### Je veux générer des rencontres
→ [README.md - Encounter System](README.md#new-in-v017-official-dd-5e-encounter-system)
→ [docs/api/mechanics.md](docs/api/mechanics.md)

### Je veux voir des exemples
→ [COMBAT_EXAMPLES.md](COMBAT_EXAMPLES.md)
→ [tests/examples/](tests/examples/)

### Je veux contribuer
→ [CONTRIBUTING.md](CONTRIBUTING.md)

## 📖 Ressources Externes

### Projets Utilisant dnd-5e-core
- **[DnD5e-Scenarios](https://github.com/codingame-team/DnD5e-Scenarios)** - Scénarios et exemples
- **[DnD-5th-Edition-API](https://github.com/codingame-team/DnD-5th-Edition-API)** - Applications complètes

### Données D&D 5e
- **[D&D 5e API](https://www.dnd5eapi.co/)** - Source de données
- **[5e.tools](https://5e.tools/)** - Monstres étendus

## 📝 Notes

- **archive/** contient l'historique de développement (non nécessaire pour l'utilisation)
- **docs/** contient la documentation API technique
- **tests/** contient tous les tests et exemples
- **data/** contient les données D&D 5e bundlées (auto-détecté)

## 🔍 Recherche Rapide

| Sujet | Fichier |
|-------|---------|
| Installation | [README.md](README.md#installation) |
| Quick Start | [README.md](README.md#quick-start) |
| Combat | [COMBAT_EXAMPLES.md](COMBAT_EXAMPLES.md) |
| API Reference | [docs/api/](docs/api/) |
| Tests | [tests/README.md](tests/README.md) |
| Changelog | [CHANGELOG.md](CHANGELOG.md) |
| Contribution | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Historique | [archive/](archive/) |

---

**Pour commencer** : Lisez [README.md](README.md) puis [COMBAT_EXAMPLES.md](COMBAT_EXAMPLES.md)

