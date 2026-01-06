# Bugfix: AttributeError dans DamageDice.score()
## 🐛 Problème
```
AttributeError: 'NoneType' object has no attribute 'lower'
```
**Fichier:** `dnd_5e_core/mechanics/dice.py`  
**Méthode:** `DamageDice.score()`  
**Ligne:** 138
### Contexte de l'Erreur
Lors de l'utilisation de `combat_system.py`, certaines attaques spéciales de monstres ont un attribut `dc_success` qui peut être `None`. Quand cette valeur est passée à la méthode `score()`, l'appel à `.lower()` sur `None` provoque une erreur.
**Traceback complet:**
```python
File "dnd_5e_core/combat/combat_system.py", line 175, in <lambda>
    key=lambda a: sum([d.dd.score(success_type=a.dc_success)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "dnd_5e_core/mechanics/dice.py", line 138, in score
    factor = 1.0 if success_type.lower() == "none" else 0.5
                    ^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'lower'
```
---
## ✅ Solution
### Changements Apportés
1. **Changement du type de paramètre:**
   - Avant: `success_type: str = "none"`
   - Après: `success_type: Optional[str] = "none"`
2. **Ajout de vérification:**
   ```python
   # Handle None or empty success_type
   if success_type is None or not success_type:
       success_type = "none"
   ```
3. **Mise à jour de la docstring:**
   - Ajout de la mention que `None` est traité comme `"none"`
### Code Modifié
```python
def score(self, success_type: Optional[str] = "none") -> float:
    """
    Calculate expected score with succ    Calculate expec    Args:
        success_type: "none" (full damage), "half" (half damage on save), or None (treated as "none")
    Returns:
        float: Expected score value
    """
    # Handle None or empty success_type
    if success_type is None or not success_type:
                                                                   factor = 1.0 if success_type.lower() == "none" else 0.5
        return (int(self.dice) + self.bonus) * factor
    dice_count, dice_sides = map(int, self.dice.split("d"))
    factor = 1.0 if success_type.lower() == "none" else 0.5
    expected = (self.bonus + dice_sides * (1     expected = (self.bonus +    return expec    expected = (self.bonus + dice_siTous les scripts de combat ont été testés avec succès:
1. ✅ `combat.py` - Combat simple 1v1
2. ✅ `party_combat.py` - Groupe de 6 aventuriers (manuels)
3. ✅ `demo_quick_combat.py` - Démo rapide avec personnages aléatoires
4. ✅ `auto_random_combat.py` - Combat automatique avec personnages aléatoires
5. ✅ `advanced_random_combat.py` - Version avancée avec stats détaillées
**Résultat:** Aucune erreur détectée. Les combats se déroulent normalement, y compris avec les monstres utilisant des attaques spéciales.
---
## 📝 Impact
### Avant le Fix
- ❌ Crash lors de combats avec certains monstres ayant `dc_success = None`
- ❌ Impossible de terminer certains combats
- ❌ Scripts de combat aléatoires non fonctionnels
### Après le Fix
- ✅ Tous les monstres gérés correctement
- ✅ Attaques spéciales fonctionnent sans erreur
- ✅ Tous les scripts de combat opérationnels
---
## 🔍 Monstres Concernés
Les monstres avec des attaques spéciales sans `dc_success` défini, par exemple:
- Black Dragon Wyrmling (Acid Breath)
- White Dragon Wyrmling (Cold Breath)
- Et potentiellement d'autres avec des capacités spéciales
---
## 📅 Date du Fix
6 janvier 2026
---
## 🎯 Prochaine Version
Ce fix devrait être inclus dans la prochaine version de `dnd-5e-core` (0.1.4 ou patch).
