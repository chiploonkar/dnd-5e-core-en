# 🤖 Quick Start pour IA Agentiques
**dnd-5e-core** est maintenant entièrement documenté pour l'utilisation par des IA agentiques !
## 📖 Documentation Disponible
### Guide Principal (Recommandé)
**[AI_AGENT_GUIDE.md](AI_AGENT_GUIDE.md)** - Guide complet avec 100+ exemples
- Installation et setup
- Concepts fondamentaux
- 10 patterns d'utilisation
- API complète par module
- Gestion des 7 erreurs courantes
- 3 cas d'usage avancés
- Intégration PyQt/Pygame/Flask
- Debug et validation
### Instructions GitHub Copilot
**[.copilot-instructions.md](.copilot-instructions.md)** - Référence rapide
- 4 principes clés
- Patterns essentiels
- Prérequis de classes
## ⚡ Démarrage Rapide
### Installation
```bash
pip install dnd-5e-core
```
### Premier Exemple
```python
from dnd_5e_core.data.loaders import simple_character_generator
from dnd_5e_core import load_monster
from dnd_5e_core.combat import CombatSystem
# Créer un personnage
hero = simple_character_generator(5, "human", "fighter", "Conan")
# Charger un monstre
orc = load_monster("orc")
# Combat
damage = hero.attack(orc)
print(f"Damage: {damage}, Orc HP: {orc.hit_points}")
```
## �## �## �## �## �## �## �butant** → Lire [AI_AGENT_GUIDE.md](AI_AGENT_GUIDE.md) sections 1-5
2. **Intermédiaire** → Consulter la section "Patterns d'Utilisation"
3. **Avancé** → Explorer les "Cas d'Usage Avancés"
## 📚 Ressources
- **API Reference**: [docs/API_REFERENCE.md](docs/API_REFERENCE.md)
- **Examples**: [examples/](examples/)
- **Tests**: [tests/](tests/)
---
**Version**: 0.4.3 | **Licence**: MIT
