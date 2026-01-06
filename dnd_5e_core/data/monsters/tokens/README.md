# Monster Tokens

Ce dossier contient les images de tokens pour les monstres D&D 5e.

## Note importante

⚠️ **Les images de tokens ne sont pas incluses dans le package PyPI** en raison des limitations de taille (102 MB de tokens vs limite de 100 MB).

## Comment télécharger les tokens

Vous pouvez télécharger les tokens de deux façons :

### Option 1 : Utiliser le script de téléchargement

Le package inclut un utilitaire pour télécharger tous les tokens :

```python
from dnd_5e_core.utils.token_downloader import download_all_tokens

# Télécharger tous les tokens
download_all_tokens()
```

### Option 2 : Téléchargement manuel

Les tokens sont disponibles sur le dépôt GitHub :
https://github.com/codingame-team/dnd-5e-core/tree/main/dnd_5e_core/data/monsters/tokens

Vous pouvez cloner le dépôt ou télécharger les fichiers individuellement.

## Structure des fichiers

Chaque monstre a un token au format WebP :
- `aboleth.webp`
- `goblin.webp`
- `ancient-red-dragon.webp`
- etc.

Total : 541 fichiers d'images (~102 MB)

## Utilisation

Les tokens peuvent être utilisés avec la classe `MonsterSprite` :

```python
from dnd_5e_core.entities.sprite import MonsterSprite

sprite = MonsterSprite("goblin")
sprite.display()
```

Si le token n'est pas disponible localement, un placeholder sera utilisé.

