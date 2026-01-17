# Mise à jour du module loader - Retour d'objets au lieu de dictionnaires

## Date: 17 janvier 2026

## Changement majeur

Le module `dnd_5e_core.data.loader` a été mis à jour pour retourner des **objets de classe** au lieu de **dictionnaires JSON**.

### Avant (v0.1.0 - v0.1.6)

```python
from dnd_5e_core.data import load_monster

goblin = load_monster("goblin")
print(goblin["name"])  # Accès dict
print(goblin.get("challenge_rating"))  # Utilisation de .get()
```

### Après (v0.1.7+)

```python
from dnd_5e_core.data import load_monster

goblin = load_monster("goblin")  # Retourne un objet Monster
print(goblin.name)  # Accès propriété
print(goblin.challenge_rating)  # Accès direct
print(goblin.is_alive)  # Utilisation des méthodes de l'objet
```

## Fonctions modifiées

### `load_monster(index: str) -> Optional[Monster]`

- **Avant**: Retournait `Dict[str, Any]`
- **Après**: Retourne `Monster` (objet de la classe `Monster`)
- **Bénéfice**: Accès direct aux méthodes comme `hp_roll()`, `saving_throw()`, `is_spell_caster`, etc.

### `load_spell(index: str) -> Optional[Spell]`

- **Avant**: Retournait `Dict[str, Any]`
- **Après**: Retourne `Spell` (objet de la classe `Spell`)
- **Bénéfice**: Accès aux propriétés comme `is_cantrip`, `is_damaging`, `requires_save`, etc.

### `load_weapon(index: str) -> Optional[Weapon]`

- **Avant**: Retournait `Dict[str, Any]`
- **Après**: Retourne `Weapon` (objet de la classe `Weapon`)
- **Bénéfice**: Accès aux propriétés comme `is_melee`, `is_ranged`, `has_property()`, etc.

### `load_armor(index: str) -> Optional[Armor]`

- **Avant**: Retournait `Dict[str, Any]`
- **Après**: Retourne `Armor` (objet de la classe `Armor`)
- **Bénéfice**: Accès direct aux propriétés `armor_class`, `stealth_disadvantage`, etc.

## Nouvelles fonctions internes

Deux nouvelles fonctions helper ont été ajoutées pour convertir les données JSON en objets:

- `_create_monster_from_data(index: str, data: Dict) -> Monster`
- `_create_spell_from_data(index: str, data: Dict) -> Spell`

Ces fonctions gèrent:
- La conversion des données JSON en objets Python
- La création des sous-objets (Abilities, Actions, Damages, etc.)
- La gestion des cas spéciaux (Spellcasting, Multiattack, Special Abilities)

## Compatibilité

### Code à mettre à jour

Si votre code utilisait les anciennes fonctions qui retournaient des dictionnaires:

```python
# AVANT - À REMPLACER
monster_data = load_monster("goblin")
name = monster_data.get("name")
cr = monster_data.get("challenge_rating")

# APRÈS - NOUVEAU CODE
monster = load_monster("goblin")
name = monster.name
cr = monster.challenge_rating
```

### Migration automatique

Pour les projets utilisant le package, cherchez et remplacez:

```bash
# Rechercher les usages de .get() sur les résultats de load_*
grep -r "load_monster.*\.get\|load_spell.*\.get" .
```

## Avantages de ce changement

1. **Typage fort**: Les IDE peuvent maintenant auto-compléter les propriétés
2. **Moins d'erreurs**: Plus de `KeyError` ou de `None` inattendus
3. **Meilleure documentation**: Les signatures de fonctions sont plus claires
4. **Méthodes utilitaires**: Accès direct aux méthodes de chaque classe
5. **Cohérence**: Même interface que les autres modules du package

## Impact sur les projets

### DnD5e-Scenarios
✅ Les scénarios utilisent déjà `Monster` et `Spell` - pas d'impact

### DnD-5th-Edition-API
⚠️ Certains scripts utilisent `populate_functions.request_monster()` qui retourne déjà des objets
- Les scripts migrant vers `dnd_5e_core` bénéficieront de ce changement

## Tests

Les fonctions ont été testées avec succès:

```bash
✅ load_monster fonctionne:
   Nom: Goblin
   CR: 0.25
   HP: 7
   Type: Monster

✅ load_spell fonctionne:
   Nom: Fireball
   Niveau: 3
   École: evocation
   Type: Spell
```

## Documentation mise à jour

- ✅ `dnd_5e_core/data/loader.py` - Docstrings mis à jour
- ✅ `docs/api/data.md` - Documentation complète avec exemples
- ✅ Signatures de type ajoutées pour tous les retours

## Prochaines étapes

1. Tester les scénarios avec les nouvelles fonctions
2. Migrer les scripts restants de DnD-5th-Edition-API
3. Publier la version 0.1.7 du package
4. Mettre à jour le README.md principal avec des exemples

