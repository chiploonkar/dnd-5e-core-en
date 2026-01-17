# Tests - Scripts de Test et Exemples

Ce dossier contient tous les scripts de test et exemples pour le package `dnd-5e-core`.

## Structure

```
tests/
├── examples/           # Exemples d'utilisation
│   └── examples_collections.py
├── test_collections_migration.py
├── test_extended_monsters.py
├── test_migration.py
├── test_new_classes.py
├── test_spell_loading.py
└── verify_package.py
```

## Scripts de Test

### Tests Unitaires

**test_collections_migration.py**
- Test de migration des collections
- Vérification des objets retournés
- Test des loaders

**test_extended_monsters.py**
- Test des monstres étendus (5e.tools)
- Vérification des 89+ monstres additionnels
- Test de recherche et filtrage

**test_migration.py**
- Tests de migration générale
- Vérification de compatibilité

**test_new_classes.py**
- Test des nouvelles classes
- Vérification des attributs
- Test de création

**test_spell_loading.py**
- Test du chargement des sorts
- Vérification des spell slots
- Test de spellcasting pour toutes les classes

### Vérification

**verify_package.py**
- Vérification de l'installation du package
- Test de tous les imports
- Vérification des données bundlées

## Exemples

### examples/examples_collections.py
Exemples d'utilisation des collections :
- Chargement de monstres
- Chargement de sorts
- Chargement d'équipement
- Utilisation des loaders

## Exécution des Tests

### Tous les tests
```bash
pytest tests/
```

### Test spécifique
```bash
pytest tests/test_spell_loading.py -v
```

### Vérification du package
```bash
python tests/verify_package.py
```

### Exemples
```bash
python tests/examples/examples_collections.py
```

## Tests PyTest

Le dossier contient aussi des tests PyTest dans la structure standard :
```
tests/
├── __init__.py
├── test_abilities.py
├── test_character.py
└── ...
```

Configuration : `pytest.ini` à la racine du projet

## Notes

- Les tests utilisent les données bundlées du package
- Aucune connexion externe nécessaire
- Tous les tests doivent passer avant publication

## Contribution

Pour ajouter des tests :
1. Créer un fichier `test_*.py`
2. Utiliser pytest pour la structure
3. Documenter le test
4. S'assurer que tous les tests passent

Voir **CONTRIBUTING.md** pour plus de détails.

