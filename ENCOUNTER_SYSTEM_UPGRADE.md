# Amélioration du Système de Challenge Rating

## 🎯 Problème Identifié

Le système de Challenge Rating dans `dnd_5e_core` utilisait une approche **simplifiée** qui ne suivait pas fidèlement les règles D&D 5e officielles, contrairement à la fonction `generate_encounter()` dans `main.py` qui utilise les **tables de rencontres précises** du Dungeon Master's Guide.

### Ancien Système (Simplifié)
```python
def get_appropriate_cr_range(party_level: int) -> Tuple[float, float]:
    min_cr = max(0, party_level - 3)
    max_cr = party_level + 3
    return (min_cr, max_cr)
```

**Problèmes:**
- ❌ Utilise seulement un range ±3 autour du niveau du groupe
- ❌ Ne tient pas compte du **nombre de monstres**
- ❌ Pas de structure de groupe ou paire
- ❌ Peut générer des rencontres déséquilibrées
- ❌ Ne suit pas les tables officielles D&D 5e

### Système de main.py (Correct)
- ✅ Utilise le fichier `Encounter_Levels.csv` basé sur les règles D&D 5e
- ✅ Prend en compte le nombre de monstres (1, 2, 3, 4, 5-6, 7-9, 10-12)
- ✅ Génère des paires de monstres de CR différents OU des groupes homogènes
- ✅ Ajuste les CR selon la taille du groupe
- ✅ Distribution de difficulté réaliste (30% facile, 50% moyen, 15% difficile, 5% mortel)

---

## ✅ Solution Implémentée

### Nouveau Module: `encounter_builder.py`

Création d'un nouveau module dans `dnd_5e_core/mechanics/encounter_builder.py` qui implémente le système exact de `main.py`.

**Fonctionnalités:**

1. **ENCOUNTER_TABLE**: Table complète des rencontres pour les niveaux 1-20
   - Basée sur `Encounter_Levels.csv`
   - Pour chaque niveau: paires de CR + options de groupes

2. **generate_encounter_distribution()**: Distribution de difficulté
   - 30% rencontres faciles (< party_level)
   - 50% rencontres moyennes (= party_level)
   - 15% rencontres difficiles (+1-4)
   - 5% rencontres mortelles (+5-20)

3. **select_monsters_by_encounter_table()**: Sélection intelligente
   - Génère des paires ou des groupes selon la table
   - Respecte les CR appropriés
   - Gère le cas où le CR exact n'existe pas (trouve le plus proche)

4. **get_encounter_info()**: Informations de rencontre
   - Retourne les options disponibles pour un niveau donné

---

## 📊 Comparaison

### Exemple: Groupe de Niveau 5

**Ancien système:**
```python
min_cr, max_cr = get_appropriate_cr_range(5)  # (2, 8)
# Sélectionne n'importe quel monstre entre CR 2 et 8
# Pas de structure, pas de nombre optimal
```

**Nouveau système:**
```python
monsters, type = select_monsters_by_encounter_table(5, monsters_db)

# Options possibles:
# PAIRES: CR 4 + CR 2
# GROUPES:
#   - 1x monstre CR 4-6
#   - 2x monstres CR 3
#   - 3x monstres CR 2
#   - 4x monstres CR 1-2
#   - 5-6x monstres CR 1
#   - 7-9x monstres CR 0.5
#   - 10-12x monstres CR 0.5
```

**Résultats:**
- ✅ Plus équilibré et varié
- ✅ Suit exactement les règles D&D 5e
- ✅ Génère des rencontres appropriées

---

## 🔧 Utilisation

### Importer le nouveau système

```python
from dnd_5e_core.mechanics import (
    select_monsters_by_encounter_table,
    generate_encounter_distribution,
    get_encounter_info,
    ENCOUNTER_TABLE
)
```

### Générer une rencontre

```python
# Charger les monstres
monsters_db = load_monsters()

# Générer une rencontre pour un groupe de niveau 5
party_level = 5
monsters, encounter_type = select_monsters_by_encounter_table(
    encounter_level=party_level,
    available_monsters=monsters_db,
    spell_casters_only=False,  # Optionnel
    allow_pairs=True  # True = peut générer des paires, False = seulement des groupes
)

# Résultat
if encounter_type == "pair":
    print(f"Paire: {monsters[0].name} + {monsters[1].name}")
else:
    print(f"Groupe: {len(monsters)}x {monsters[0].name}")
```

### Générer une distribution de rencontres

```python
party_level = 5
encounter_levels = generate_encounter_distribution(party_level)
# Retourne 20 niveaux de rencontre avec la distribution:
# 30% faciles, 50% moyennes, 15% difficiles, 5% mortelles
```

### Obtenir les infos d'un niveau

```python
info = get_encounter_info(party_level=5)
# Retourne:
# {
#     'level': 5,
#     'pair_crs': (Fraction(4), Fraction(2)),
#     'group_options': {
#         '1': [4, 5, 6],
#         '2': [3],
#         '3': [2],
#         ...
#     }
# }
```

---

## 📝 Exemple Complet

```python
from dnd_5e_core.mechanics import select_monsters_by_encounter_table
from main import request_monster, populate

# Charger les monstres
monster_names = populate(collection_name="monsters", key_name="results")
monsters_db = [request_monster(name) for name in monster_names if request_monster(name)]

# Groupe de niveau 8
party_level = 8

# Générer 5 rencontres différentes
for i in range(5):
    monsters, enc_type = select_monsters_by_encounter_table(
        party_level, monsters_db, allow_pairs=True
    )
    
    if enc_type == "pair":
        print(f"{i+1}. PAIRE: {monsters[0].name} (CR {monsters[0].challenge_rating}) "
              f"+ {monsters[1].name} (CR {monsters[1].challenge_rating})")
    else:
        print(f"{i+1}. GROUPE: {len(monsters)}x {monsters[0].name} "
              f"(CR {monsters[0].challenge_rating})")

# Exemple de sortie:
# 1. GROUPE: 3x Young Green Dragon (CR 8)
# 2. PAIRE: Stone Giant (CR 7) + Air Elemental (CR 5)
# 3. GROUPE: 2x Medusa (CR 6)
# 4. PAIRE: Fire Giant (CR 9) + Gladiator (CR 5)
# 5. GROUPE: 4x Young Green Dragon (CR 8)
```

---

## 🎯 Recommandations

1. **Pour les nouveaux scripts**: Utilisez `select_monsters_by_encounter_table()`
2. **Migration**: Remplacez `get_appropriate_cr_range()` par le nouveau système
3. **Avantages**:
   - Rencontres plus équilibrées
   - Suit les règles officielles D&D 5e
   - Plus de variété (paires vs groupes)
   - Distribution de difficulté réaliste

---

## 📁 Fichiers Modifiés/Créés

1. **Nouveau**: `dnd_5e_core/mechanics/encounter_builder.py` (510 lignes)
   - Table ENCOUNTER_TABLE complète
   - Fonctions de génération de rencontres

2. **Modifié**: `dnd_5e_core/mechanics/__init__.py`
   - Ajout des imports du nouveau module
   - Export des nouvelles fonctions

3. **Modifié**: `dnd_5e_core/mechanics/dice.py`
   - Bugfix: gestion de `success_type=None`

4. **Nouveau**: `DnD5e-Test/demo_encounter_systems.py`
   - Script de démonstration et comparaison

---

## 🧪 Tests

Le script `demo_encounter_systems.py` démontre la différence entre les deux systèmes pour les niveaux 1, 3, 5, 10, 15 et 20.

**Exécuter:**
```bash
cd /Users/display/PycharmProjects/DnD5e-Test
python3 demo_encounter_systems.py
```

---

## ✅ Conclusion

Le package `dnd_5e_core` utilise maintenant le **même système de génération de rencontres** que `main.py`, basé sur les **tables D&D 5e officielles**. Ceci garantit des rencontres équilibrées et conformes aux règles du jeu.

**L'ancien système reste disponible** pour la compatibilité ascendante, mais le nouveau système est **fortement recommandé** pour tous les nouveaux développements.

---

**Date:** 6 janvier 2026  
**Version:** dnd-5e-core 0.1.4

