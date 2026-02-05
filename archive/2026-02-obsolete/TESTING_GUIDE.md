# Scripts de test et validation - Correction spell_slots

Ce répertoire contient plusieurs scripts pour tester et valider la correction du KeyError sur `spell_slots`.

## 📋 Scripts disponibles

### 1. `validate_spell_slots_fix.py` ⭐ (RECOMMANDÉ)
**Script de validation rapide** - À exécuter pour vérifier que tout fonctionne.

```bash
# Validation rapide (imports, accès basique, documentation)
python3 validate_spell_slots_fix.py

# Validation complète avec tous les tests
python3 validate_spell_slots_fix.py --full
```

**Sortie attendue :**
```
✅ Imports                     : RÉUSSI
✅ Validation rapide           : RÉUSSI  
✅ Documentation              : RÉUSSI
🎉 VALIDATION COMPLÈTE RÉUSSIE!
```

---

### 2. `test_spell_slots_fix.py`
**Test détaillé de spell_slots** - Vérifie toutes les classes et tous les niveaux.

```bash
python3 test_spell_slots_fix.py
```

**Ce qu'il teste :**
- ✅ spell_slots existe pour toutes les classes de lanceurs (wizard, cleric, druid, sorcerer, bard, warlock, paladin, ranger)
- ✅ Tous les niveaux 1-20 sont présents dans le dictionnaire
- ✅ Accès direct à `char.class_type.spell_slots[char.level]` fonctionne
- ✅ SpellCaster est correctement initialisé

**Durée :** ~5-10 secondes

---

### 3. `test_spell_slots_end_to_end.py`
**Test de bout en bout** - Création, sauvegarde, rechargement.

```bash
python3 test_spell_slots_end_to_end.py
```

**Ce qu'il teste :**
- ✅ Création d'un personnage avec spell_slots
- ✅ Sauvegarde avec pickle
- ✅ Rechargement et vérification de l'intégrité
- ✅ Accès aux spell_slots après rechargement
- ✅ Test avec toutes les classes de lanceurs au niveau 2

**Durée :** ~10-15 secondes

---

### 4. `test_game_integration.py`
**Test d'intégration** - Simule les situations du jeu qui causaient le KeyError.

```bash
python3 test_game_integration.py
```

**Ce qu'il teste :**
- ✅ **Repos à l'auberge** (main_ncurses.py ligne 1734)
  - Utilisation de slots puis restauration
  - 7 classes testées (wizard, cleric, sorcerer, bard, paladin, ranger, warlock)
  
- ✅ **Montée de niveau** (main_ncurses.py ligne 2415)
  - Passage de niveau 1→2, 2→3, etc.
  - Mise à jour des spell_slots
  
- ✅ **Cas limites**
  - Niveau 20 (maximum)
  - Niveau 1 Paladin (pas de sorts encore)
  - Warlock niveau 5 (pact magic)

**Durée :** ~10-15 secondes

---

### 5. `migrate_spell_slots.py`
**Script de migration** - Pour les personnages sauvegardés existants.

```bash
# Mode dry-run (analyse seulement, pas de modification)
python3 migrate_spell_slots.py --dry-run

# Migration réelle (crée des backups automatiquement)
python3 migrate_spell_slots.py
```

**Ce qu'il fait :**
- 🔍 Recherche tous les fichiers .pkl dans `~/Saved_Games_DnD_5th/`
- 🔍 Vérifie si spell_slots est vide ou mal formé
- 🔧 Reconstruit spell_slots avec `get_spell_slots_for_level()`
- 💾 Crée des backups (.pkl.bak) avant modification
- ✅ Met à jour `char.sc.spell_slots` si nécessaire

**Quand l'utiliser :**
- Si vous avez des personnages créés AVANT la correction
- Si vous rencontrez encore des KeyError avec des personnages existants

---

## 🚀 Workflow recommandé

### Après installation ou mise à jour

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# 1. Validation rapide
python3 validate_spell_slots_fix.py

# 2. Si tout est OK, tester le jeu
cd /Users/display/PycharmProjects/DnD-5th-Edition-API
python3 main_ncurses.py
```

### Si vous avez des personnages existants

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# 1. Vérifier ce qui sera modifié
python3 migrate_spell_slots.py --dry-run

# 2. Si nécessaire, migrer
python3 migrate_spell_slots.py

# 3. Valider
python3 validate_spell_slots_fix.py
```

### Pour le développement

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# Exécuter tous les tests
python3 test_spell_slots_fix.py
python3 test_spell_slots_end_to_end.py
python3 test_game_integration.py

# Ou validation complète
python3 validate_spell_slots_fix.py --full
```

---

## 📊 Temps d'exécution

| Script | Durée | Quand l'utiliser |
|--------|-------|------------------|
| `validate_spell_slots_fix.py` | ~2 sec | ⭐ Toujours (validation rapide) |
| `validate_spell_slots_fix.py --full` | ~30 sec | Après modification du code |
| `test_spell_slots_fix.py` | ~10 sec | Développement |
| `test_spell_slots_end_to_end.py` | ~15 sec | Développement |
| `test_game_integration.py` | ~15 sec | Développement |
| `migrate_spell_slots.py` | Variable | Une seule fois pour personnages existants |

---

## ✅ Que faire si un test échoue ?

### Test d'import échoue
```
❌ Imports : ÉCHOUÉ
```
**Solution :** Vérifiez que vous êtes dans le bon répertoire et que les fichiers modifiés sont présents.

### Validation rapide échoue
```
❌ Validation rapide : ÉCHOUÉ
```
**Solutions possibles :**
1. Vérifiez que `dnd_5e_core/data/loaders.py` contient les modifications
2. Vérifiez que `get_spell_slots_for_level` est accessible
3. Relancez avec `python3 validate_spell_slots_fix.py --full` pour plus de détails

### Tests complets échouent
```
❌ test_game_integration.py : ÉCHOUÉ
```
**Solutions :**
1. Vérifiez les messages d'erreur détaillés
2. Consultez `SPELL_SLOTS_FIX.md` pour la documentation complète
3. Supprimez les personnages sauvegardés corrompus et recréez-les

---

## 📚 Documentation

- **`SPELL_SLOTS_FIX.md`** - Documentation technique complète
- **`QUICKFIX_SPELL_SLOTS.md`** - Guide utilisateur rapide
- **`SPELL_SLOTS_SUMMARY.md`** - Résumé en une page
- **`CHANGELOG.md`** - Historique des modifications

---

## 🆘 Support

Si vous rencontrez des problèmes persistants :

1. **Vérifiez les versions**
   ```bash
   git status
   git log --oneline -5
   ```

2. **Nettoyez les sauvegardes**
   ```bash
   # Sauvegardez vos personnages importants ailleurs !
   rm -rf ~/Saved_Games_DnD_5th/*.pkl
   ```

3. **Recréez un personnage de test**
   ```bash
   cd /Users/display/PycharmProjects/dnd-5e-core
   python3 -c "from dnd_5e_core.data.loaders import simple_character_generator; c = simple_character_generator(level=2, class_name='wizard'); print(c.class_type.spell_slots[2])"
   ```

Si la dernière commande affiche `[0, 3, 0, 0, 0, 0, 0, 0, 0, 0]`, la correction fonctionne !

---

**Dernière mise à jour :** 3 février 2026  
**Statut :** ✅ Tous les scripts fonctionnent et testés
