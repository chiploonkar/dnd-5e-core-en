# Plan de migration des monstres extended

## État actuel
Les monstres extended utilisent le format 5etools qui est très différent du format API officiel D&D 5e.

## Problèmes identifiés

###  1. Structure différente
- **Abilities**: `{str: 17, dex: 8, ...}` vs `{strength: 17, dexterity: 8, ...}`
- **Hit Points**: `{average: 114, formula: "12d10+48"}` vs `114`
- **Actions**: `action: [{name, entries: [...]}]` vs `actions: [{name, desc, damage: [...]}]`
- **Texte formaté**: Utilise des tags spéciaux `{@atk mw}`, `{@hit 7}`, `{@damage 3d10+3}`, `{@condition grappled}`

### 2. Parsing requis
Les actions sont en texte narratif au lieu d'être structurées:
```json
{
  "name": "Bite",
  "entries": [
    "{@atk mw} {@hit 7} to hit, reach 5 ft., one target. {@h}19 ({@damage 3d10 + 3}) piercing damage."
  ]
}
```

Il faut extraire:
- Type d'attaque (mw = melee weapon)
- Bonus d'attaque (+7)
- Portée (5 ft.)
- Dégâts (3d10+3 piercing)

### 3. Challenge rating
Le CR est en float (11.0) ce qui est correct, la conversion `Fraction(str(11.0))` fonctionne.

## Solutions

### Option A: Convertir au format officiel
Créer un parser qui transforme le format 5etools vers le format API officiel.

**Avantages:**
- Réutilisation du code existant _create_monster_from_data()
- Cohérence avec les monstres officiels

**Inconvénients:**
- Parsing complexe des tags de texte
- Perte potentielle d'informations

### Option B: Créer un parser dédié
Créer _create_extended_monster_from_data() séparé.

**Avantages:**
- Peut gérer les spécificités du format extended
- Pas de conversion risquée

**Inconvénients:**
- Code dupliqué
- Maintenance de 2 parsers

### Option C: Hybrid (RECOMMANDÉ)
1. Normaliser les champs simples (abilities, hit_points, etc.)
2. Parser les actions avec regex pour extraire les infos
3. Passer au _create_monster_from_data() existant

**Avantages:**
- Meilleur des deux mondes
- Code réutilisé
- Format normalisé

## Implémentation recommandée

```python
def _normalize_extended_monster_data(data: Dict) -> Dict:
    """
    Normalize extended monster format to official API format.
    """
    normalized = data.copy()
    
    # Normalize abilities
    if 'abilities' in data and isinstance(data['abilities'], dict):
        normalized['strength'] = data['abilities'].get('str', 10)
        normalized['dexterity'] = data['abilities'].get('dex', 10)
        normalized['constitution'] = data['abilities'].get('con', 10)
        normalized['intelligence'] = data['abilities'].get('int', 10)
        normalized['wisdom'] = data['abilities'].get('wis', 10)
        normalized['charisma'] = data['abilities'].get('cha', 10)
    
    # Normalize hit points
    if 'hit_points' in data and isinstance(data['hit_points'], dict):
        normalized['hit_points'] = data['hit_points'].get('average', 1)
        normalized['hit_dice'] = data['hit_points'].get('formula', '1d8')
    
    # Normalize actions
    if 'action' in data:
        normalized['actions'] = _parse_extended_actions(data['action'])
    
    return normalized

def _parse_extended_actions(action_list: List[Dict]) -> List[Dict]:
    """
    Parse extended action format with special tags.
    """
    actions = []
    for action_data in action_list:
        # Parse entry text to extract attack info
        # {@atk mw} = melee weapon attack
        # {@hit 7} = +7 to hit
        # {@damage 3d10 + 3} = damage dice
        ...
    return actions
```

## Fichier à créer
`dnd_5e_core/data/extended_monster_parser.py`
