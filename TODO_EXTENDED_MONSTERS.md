# TODO: Fix Extended Monsters Support

## Problèmes identifiés

### 1. Encounter Builder ne fonctionne pas avec monstres étendus ❌
- **Cause:** challenge_rating parfois en float, parfois en string
- **Solution:** S'assurer que load_monster convertit toujours en Fraction

### 2. Tokens monstres étendus manquants ❌
- **Localisation:** PyQt frontend
- **Solution:** Télécharger les tokens pour tous les monstres extended
- **Marqueur:** Ajouter indicateur visuel "source" sur le token

### 3. Objets magiques non chargés dans boltac_tp_pygame.py ❌
- **Cause:** Load magic items pas implémenté
- **Solution:** Charger les magic items depuis dnd-5e-core

### 4. Armures magiques manquantes ❌
- **Solution:** Implémenter MagicArmor class et loader

## Plan d'action

### Phase 1: Fix challenge_rating pour encounter_builder
1. Vérifier loader.py _create_monster_from_data()
2. S'assurer conversion vers Fraction
3. Tester avec monstres étendus

### Phase 2: Télécharger tokens monstres étendus  
1. Étendre token_downloader.py
2. Gérer les monstres extended/
3. Ajouter fallback si token manquant

### Phase 3: Marqueur source dans PyQt
1. Lire champ "source" depuis JSON
2. Stocker dans Monster.source
3. Afficher badge sur token dans interface

### Phase 4: Magic items dans pygame
1. Implémenter load_magic_items()
2. Ajouter dans boltac shop inventory
3. Test d'achat/vente

### Phase 5: Magic armors
1. Créer MagicArmor class extends Armor
2. Loader pour magic armors
3. Intégration dans tous frontends

## Fichiers à modifier

- dnd_5e_core/data/loader.py
- dnd_5e_core/entities/monster.py
- dnd_5e_core/utils/token_downloader.py
- dnd_5e_core/equipment/magic_item.py (nouveau?)
- dnd_5e_core/equipment/armor.py
- DnD-5th-Edition-API/boltac_tp_pygame.py
- DnD-5th-Edition-API/pyQTApp/ (pour marqueur source)
