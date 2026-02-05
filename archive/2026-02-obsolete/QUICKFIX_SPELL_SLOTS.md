# Guide de correction rapide - KeyError spell_slots

## 🐛 Problème

Erreur lors du repos à l'auberge ou de la montée de niveau :
```
KeyError: 2
char.sc.spell_slots = char.class_type.spell_slots[char.level]
```

## ✅ Solution

La correction a été appliquée automatiquement dans les fichiers suivants :
- `dnd_5e_core/data/loaders.py`
- `main_ncurses.py`
- `main.py`
- `dungeon_pygame.py`

## 🚀 Utilisation

### Pour les nouveaux personnages

Rien à faire ! Les nouveaux personnages créés auront automatiquement la structure `spell_slots` correcte.

### Pour les personnages existants (optionnel)

Si vous avez des personnages sauvegardés qui rencontrent des problèmes :

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# 1. Vérifier ce qui sera modifié (sans modification)
python3 migrate_spell_slots.py --dry-run

# 2. Appliquer la migration (crée des backups automatiquement)
python3 migrate_spell_slots.py
```

Le script :
- ✅ Recherche automatiquement vos personnages sauvegardés
- ✅ Crée des backups (.pkl.bak) avant toute modification
- ✅ Reconstruit la structure spell_slots manquante
- ✅ Met à jour les spell_slots du SpellCaster

## 🧪 Vérification

Pour vérifier que tout fonctionne :

```bash
cd /Users/display/PycharmProjects/dnd-5e-core

# Test complet
python3 test_spell_slots_fix.py
python3 test_spell_slots_end_to_end.py
python3 test_game_integration.py
```

Tous les tests doivent afficher : **✅ TOUS LES TESTS ONT RÉUSSI!**

## 📝 Que faire si j'ai encore des problèmes ?

1. **Vérifier la version du package**
   ```bash
   cd /Users/display/PycharmProjects/dnd-5e-core
   git status
   ```
   Assurez-vous que les modifications dans `dnd_5e_core/data/loaders.py` sont présentes.

2. **Supprimer les personnages corrompus**
   Si un personnage pose toujours problème, vous pouvez :
   - Le supprimer du répertoire `~/Saved_Games_DnD_5th/`
   - Créer un nouveau personnage avec les mêmes caractéristiques

3. **Nettoyer et recréer**
   ```bash
   # Sauvegarder vos personnages importants ailleurs
   # Puis supprimer le répertoire de sauvegarde
   rm -rf ~/Saved_Games_DnD_5th/
   
   # Relancer le jeu pour recréer le répertoire
   ```

## 📚 Documentation complète

Pour plus de détails, consultez : `SPELL_SLOTS_FIX.md`

## ✨ Résumé

- ✅ **Le bug est corrigé** : Plus de KeyError sur spell_slots
- ✅ **Compatibilité totale** : Fonctionne avec tous les frontends
- ✅ **Testé et validé** : 100% des tests passent
- ✅ **Migration disponible** : Pour les personnages existants
- ✅ **Backups automatiques** : Vos données sont protégées

**Vous pouvez maintenant jouer sans rencontrer cette erreur !** 🎉
