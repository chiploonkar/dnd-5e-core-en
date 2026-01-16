# Documentation dnd-5e-core - Guide complet

## 📋 Fichiers de documentation créés

Cette documentation complète couvre tous les modules du package `dnd-5e-core`.

### Structure de la documentation

```
docs/api/
├── README.md                        # Point d'entrée de la documentation
├── INDEX.md                         # Vue d'ensemble et quick start
├── entities.md                      # Personnages et monstres
├── combat.md                        # Système de combat
├── mechanics.md                     # Règles de jeu (dés, XP, CR)
├── equipment.md                     # Armes, armures, potions
├── spells.md                        # Système de magie
├── data.md                          # Chargement de données
├── races-classes-abilities.md       # Races, classes, caractéristiques
└── ui-utils.md                      # Interface et utilitaires
```

## 📖 Contenu par fichier

### README.md (Point d'entrée)
- Table des matières complète
- Guide de lecture
- Quick start
- Cas d'usage
- Liens vers projets d'exemple

### INDEX.md (Vue d'ensemble)
- Description complète du package
- Installation
- Quick start
- Structure du package
- Exemples d'utilisation
- Projets d'exemple

### entities.md
**Classes:**
- `Sprite` - Classe de base
- `Character` - Personnages joueurs
  - Création (aléatoire, manuelle)
  - Combat (attaques, sorts)
  - Équipement
  - Repos
  - Sérialisation
- `Monster` - Créatures
- `ExtendedMonsterLoader` - Bestiaire étendu

**Exemples:**
- Créer un groupe d'aventuriers
- Combat simple
- Sauvegarder/charger

### combat.md
**Classes:**
- `CombatSystem` - Gestionnaire de combat
  - Tour de joueur
  - Tour de monstre
  - Récompenses
- `Action` - Actions de combat
- `Damage` - Calcul des dégâts
- `Condition` - États (empoisonné, paralysé, etc.)
- `SpecialAbility` - Capacités spéciales

**Exemples:**
- Combat tour par tour
- Combat avec sorts
- Combat avec positionnement (front/back)
- Gestion des conditions

**Règles implémentées:**
- Attaques (mêlée, distance)
- Dégâts et critiques
- Sorts et jets de sauvegarde
- IA des monstres
- Récompenses (XP, or)

### mechanics.md
**Classes et fonctions:**
- `DamageDice` - Système de dés
  - Lancer de dés
  - Valeurs max/moyenne
  - Comparaison
- `experience` - Gestion de l'XP
  - XP par CR
  - Calcul de niveau
  - Seuils d'XP
- `challenge_rating` - Facteur de puissance
  - Génération de rencontres
  - Calcul de force du groupe
- `encounter_builder` - Construction de rencontres
- `level_up` - Montée de niveau
- `gold_rewards` - Récompenses en or

**Exemples:**
- Système de dés complet
- Gestion d'XP et niveaux
- Construction de rencontres
- Système de récompenses

**Constantes:**
- XP par CR (0-30)
- Seuils XP par niveau (1-20)

### equipment.md
**Classes:**
- `Weapon` - Armes
  - Propriétés (dégâts, portée)
  - Équipement
- `Armor` - Armures
  - Catégories (légère, moyenne, lourde)
  - Calcul de CA
- `HealingPotion` - Potions de soin
  - Raretés (commune → suprême)
- `SpeedPotion` - Potions de vitesse
- `StrengthPotion` - Potions de force
- `Inventory` - Gestion d'inventaire
- `Equipment` - Équipement général

**Exemples:**
- Équiper un personnage
- Armes par catégorie
- Armures par catégorie
- Système de potions

### spells.md
**Classes:**
- `Spell` - Sorts
  - Propriétés (niveau, école, etc.)
  - Dégâts par niveau
  - Soins par niveau
- `SpellCaster` - Lanceurs de sorts
  - Emplacements de sorts
  - Sorts connus/préparés
  - DD et bonus d'attaque
- `spell_slots` - Gestion des emplacements
- `cantrips` - Sorts mineurs

**Exemples:**
- Lanceur de sorts complet
- École de magie
- Système de soin magique
- Sorts de zone (AOE)

**Sorts par niveau:**
- Niveau 0 (cantrips)
- Niveaux 1-9 avec exemples

### data.md
**Fonctions de chargement:**
- `load_monster()` - Charger un monstre
- `load_spell()` - Charger un sort
- `load_weapon()` - Charger une arme
- `load_armor()` - Charger une armure

**Collections:**
- `ExtendedMonsterLoader` - Bestiaire complet
  - Recherche de monstres
  - Filtrage par CR
  - Statistiques

**Sérialisation:**
- Sauvegarder/charger personnages
- Sauvegarder/charger groupes
- Format JSON

**Exemples:**
- Charger toutes les données pour un scénario
- Construire un bestiaire
- Système de cache

**Sources de données:**
- API D&D 5e officielle
- Données locales enrichies
- Collections

### races-classes-abilities.md

**Module races:**
- `Race` - Races de personnages
  - Races standards (elfe, nain, etc.)
  - Bonus de caractéristiques
  - Traits raciaux
- `SubRace` - Sous-races
- `Trait` - Traits raciaux
- `Language` - Langages

**Module classes:**
- `ClassType` - Classes de personnages
  - 12 classes standard
  - Dés de vie
  - Maîtrises
- `Proficiency` - Maîtrises
  - Types (armures, armes, compétences)
- `multiclass` - Multiclassage

**Module abilities:**
- `Abilities` - Six caractéristiques
  - Valeurs et modificateurs
  - Lancer aléatoire
- `AbilityType` - Types de caractéristiques
- `Skill` - Compétences
  - Par caractéristique
- `Saving Throw` - Jets de sauvegarde

**Exemples:**
- Créer un personnage complet
- Afficher toutes les races
- Afficher toutes les classes

### ui-utils.md

**Module ui:**
- `Color` - Couleurs ANSI
  - Couleurs standards
  - Couleurs vives
  - Couleurs de fond
  - Styles
- `color()` - Coloriser du texte
- `cprint()` - Affichage coloré

**Module utils:**
- `constants` - Constantes du jeu
  - Tailles de créatures
  - Types de créatures
  - Alignements
- `helpers` - Fonctions utilitaires
  - Calculer modificateurs
  - Formater nombres
  - Valider dés
- `token_downloader` - Téléchargement de tokens

**Exemples:**
- Affichage de combat coloré
- Barre de vie colorée
- Fiche de personnage formatée
- Système de menu coloré
- Logger de combat

## 🎯 Utilisation de la documentation

### Pour les débutants
1. Lire `README.md` pour comprendre l'organisation
2. Consulter `INDEX.md` pour le quick start
3. Suivre les exemples dans `entities.md`
4. Expérimenter avec `data.md`

### Pour les développeurs
1. Consulter la documentation du module spécifique
2. Utiliser les exemples comme base
3. Référencer les constantes et règles

### Pour les intégrateurs
1. Lire `combat.md` pour le système de combat
2. Consulter `ui-utils.md` pour l'interface
3. Adapter les exemples à votre UI

## 📊 Statistiques de la documentation

- **10 fichiers Markdown** complets
- **8 modules** documentés
- **50+ classes et fonctions** expliquées
- **100+ exemples** de code
- **Toutes les règles D&D 5e** couvertes

## 🔗 Liens rapides

### Documentation
- [Point d'entrée](./README.md)
- [Vue d'ensemble](./INDEX.md)

### Modules principaux
- [Personnages et monstres](./entities.md)
- [Combat](./combat.md)
- [Règles de jeu](./mechanics.md)

### Modules secondaires
- [Équipement](./equipment.md)
- [Sorts](./spells.md)
- [Données](./data.md)

### Personnalisation
- [Races, Classes, Caractéristiques](./races-classes-abilities.md)
- [UI et Utilitaires](./ui-utils.md)

## ✅ Checklist de lecture

- [ ] README.md - Comprendre la structure
- [ ] INDEX.md - Quick start
- [ ] entities.md - Personnages et monstres
- [ ] data.md - Charger des données
- [ ] combat.md - Système de combat
- [ ] mechanics.md - Règles de jeu
- [ ] spells.md - Système de magie
- [ ] equipment.md - Armes et armures
- [ ] races-classes-abilities.md - Personnalisation
- [ ] ui-utils.md - Interface

## 🎓 Niveau de détail par fichier

| Fichier | Lignes | Classes | Exemples | Niveau |
|---------|--------|---------|----------|--------|
| README.md | ~150 | - | 3 | Débutant |
| INDEX.md | ~250 | 10+ | 10+ | Débutant |
| entities.md | ~400 | 3 | 10+ | Intermédiaire |
| combat.md | ~450 | 5 | 12+ | Intermédiaire |
| mechanics.md | ~350 | 1+API | 15+ | Avancé |
| equipment.md | ~300 | 6 | 8+ | Débutant |
| spells.md | ~250 | 3 | 10+ | Intermédiaire |
| data.md | ~300 | 1+API | 8+ | Débutant |
| races-classes-abilities.md | ~300 | 9 | 6+ | Intermédiaire |
| ui-utils.md | ~250 | 2+API | 10+ | Débutant |

## 📝 Maintenance

Pour maintenir la documentation à jour:

1. **Nouveaux modules**: Créer un nouveau fichier `.md` dans `docs/api/`
2. **Nouvelles classes**: Ajouter dans le fichier du module correspondant
3. **Nouveaux exemples**: Tester et ajouter dans les sections appropriées
4. **Mises à jour**: Synchroniser avec les changements du code

## 🤝 Contribution

Pour contribuer à la documentation:
1. Vérifier que tous les exemples fonctionnent
2. Maintenir le même format que les fichiers existants
3. Ajouter des exemples concrets et testés
4. Mettre à jour cette table des matières

---

**Documentation générée pour dnd-5e-core v0.1.7+**  
Dernière mise à jour: Janvier 2026

