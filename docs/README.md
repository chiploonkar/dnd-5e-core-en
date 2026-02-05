# 📚 Documentation dnd-5e-core

Bienvenue dans la documentation du package **dnd-5e-core** !

## 📖 Documentation Principale

### Essentiels
- **[README.md](../README.md)** - Vue d'ensemble du package et guide d'utilisation
- **[AI_AGENT_GUIDE.md](../AI_AGENT_GUIDE.md)** - 🤖 **Guide complet pour IA agentiques**
- **[CHANGELOG.md](../CHANGELOG.md)** - Historique des versions et modifications
- **[CONTRIBUTING.md](../CONTRIBUTING.md)** - Guide pour contribuer au projet
- **[QUICK_START_DATA.md](../QUICK_START_DATA.md)** - Démarrage rapide avec les données

### Documentation IA
- **[AI_AGENT_GUIDE.md](../AI_AGENT_GUIDE.md)** - Guide complet pour intégration par IA (100+ exemples)
- **[.copilot-instructions.md](../.copilot-instructions.md)** - Instructions pour GitHub Copilot

### Données
- **[data/README.md](../data/README.md)** - Documentation du contenu des données JSON (2000+ fichiers)
- **[collections/README.md](../collections/README.md)** - Documentation des collections d'index de l'API

---

## 🔄 Documentation de Migration

### Migration Collections (Décembre 2025)
- **[COLLECTIONS_MIGRATION.md](COLLECTIONS_MIGRATION.md)** - Guide de migration des collections
- **[COLLECTIONS_COMPLETE.md](COLLECTIONS_COMPLETE.md)** - Résumé de la migration complète

### Migration Données (Décembre 2024)
Voir le dossier `archive/migration/` pour la documentation historique de la migration des données.

---

## 📁 Structure du Package

```
dnd-5e-core/
├── collections/              # Index des collections D&D 5e API
│   ├── README.md            # Documentation des collections
│   └── *.json               # 26 fichiers d'index (monsters, spells, etc.)
│
├── data/                    # Données JSON D&D 5e (2000+ fichiers)
│   ├── README.md            # Documentation des données
│   ├── monsters/            # 332 monstres
│   ├── spells/              # 319 sorts
│   ├── weapons/             # 65 armes
│   └── ...                  # 24+ autres catégories
│
├── dnd_5e_core/             # Code source du package
│   ├── abilities/           # Système de caractéristiques
│   ├── classes/             # Classes de personnage
│   ├── combat/              # Système de combat
│   ├── data/                # Chargement des données
│   │   ├── loader.py        # Chargement des fichiers data/
│   │   ├── collections.py   # Chargement des collections/
│   │   └── __init__.py      # API publique
│   ├── entities/            # Entités (Monster, Character, etc.)
│   ├── equipment/           # Équipement et items
│   ├── mechanics/           # Mécanique de jeu (dés, etc.)
│   ├── races/               # Races et sous-races
│   ├── spells/              # Système de sorts
│   └── utils/               # Utilitaires
│
├── tests/                   # Tests unitaires
│
└── docs/                    # Documentation (vous êtes ici!)
    ├── README.md            # Ce fichier
    ├── COLLECTIONS_MIGRATION.md
    ├── COLLECTIONS_COMPLETE.md
    └── archive/             # Documentation historique
```

---

## 🚀 Démarrage Rapide

### Installation

```bash
# Clone du dépôt
git clone <repo-url>
cd dnd-5e-core

# Installation en mode développement
pip install -e .
```

### Usage Basique

```python
# Charger des données
from dnd_5e_core.data import load_monster, load_spell

goblin = load_monster('goblin')
fireball = load_spell('fireball')

# Charger des collections
from dnd_5e_core.data import get_monsters_list, get_spells_list

all_monsters = get_monsters_list()
all_spells = get_spells_list()

# Créer des entités
from dnd_5e_core.entities import Monster, Character
from dnd_5e_core.races import Race

monster = Monster.from_json_data(goblin)
character = Character(name="Aragorn", race=Race(...))
```

---

## 📊 Contenu du Package

### Collections (26 fichiers)
- **332 monstres** indexés
- **319 sorts** indexés
- **12 classes** de personnage
- **9 races** jouables
- **237 équipements** indexés
- Et bien plus...

### Données (2000+ fichiers JSON)
- Détails complets de tous les monstres
- Descriptions complètes de tous les sorts
- Statistiques de toutes les armes et armures
- Règles complètes du jeu
- Et bien plus...

### Code Python
- **Entities** - Système d'entités complet
- **Combat** - Système de combat avec actions
- **Spells** - Système de sorts et emplacements
- **Equipment** - Gestion de l'équipement
- **Mechanics** - Mécanique de base (dés, jets, etc.)
- **Data Loaders** - Chargement automatique des données

---

## 🧪 Tests

```bash
# Lancer tous les tests
pytest

# Lancer un test spécifique
pytest tests/test_data_loader.py

# Avec couverture
pytest --cov=dnd_5e_core
```

---

## 📝 Guides et Tutoriels

### Pour les Développeurs
- **[CONTRIBUTING.md](../CONTRIBUTING.md)** - Comment contribuer
- **Migration depuis DnD-5th-Edition-API** - Voir `COLLECTIONS_MIGRATION.md`

### Pour les Utilisateurs
- **[QUICK_START_DATA.md](../QUICK_START_DATA.md)** - Démarrage rapide
- **[data/README.md](../data/README.md)** - Documentation des données
- **[collections/README.md](../collections/README.md)** - Documentation des collections

---

## 🗂️ Archive

La documentation historique du développement est archivée dans `archive/`:

### Migrations
- **DATA_MIGRATION_COMPLETE.md** - Migration des données JSON
- **MIGRATION_COMPLETE.md** - Finalisation de la migration
- **MIGRATION_GUIDE.md** - Guide de migration
- **MIGRATION_STATUS.md** - Status de la migration

### Progression
- **PROJECT_COMPLETE.md** - Complétion du projet
- **COMBAT_SPELLS_COMPLETE.md** - Système de combat et sorts
- **DATA_LOADERS_CORRECTED.md** - Corrections des loaders

Voir **[archive/README.md](archive/README.md)** pour plus de détails.

---

## 🔗 Liens Utiles

### Ressources D&D 5e
- [D&D 5e API](https://www.dnd5eapi.co/) - Source des données
- [Open Gaming License](https://dnd.wizards.com/resources/systems-reference-document) - Licence OGL

### Projets Liés
- **DnD-5th-Edition-API** - Projet utilisant dnd-5e-core
- **DnD-5e-ncurses** - Interface ncurses pour D&D 5e

---

## 📅 Historique des Versions

Voir **[CHANGELOG.md](../CHANGELOG.md)** pour l'historique complet des versions.

### Version Actuelle: Unreleased

Dernières fonctionnalités :
- ✅ Migration des collections (Décembre 2025)
- ✅ Module `collections.py` pour gérer les index
- ✅ Fonctions de convenance pour accès rapide
- ✅ Auto-détection des chemins

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez **[CONTRIBUTING.md](../CONTRIBUTING.md)** pour plus de détails.

### Processus de Contribution
1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

---

## 📄 Licence

Ce projet utilise les données sous **Open Gaming License (OGL)** et **System Reference Document (SRD)**.

---

## 📧 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur le dépôt GitHub.

---

**Dernière mise à jour:** 23 décembre 2025
