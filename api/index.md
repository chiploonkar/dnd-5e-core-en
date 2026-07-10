# dnd-5e-core API Reference

Welcome to the **dnd-5e-core** English API documentation! This site provides a clean, fully-translated reference for the core Python modules of the D&D 5e engine.

---

!!! info "Important Notice: Fork & Translation Information"
    This repository is an independent fork of the original project: **[codingame-team/dnd-5e-core](https://github.com/codingame-team/dnd-5e-core)**.
    
    * **Fork Repository:** [chiploonkar/dnd-5e-core-en/tree/main](https://github.com/chiploonkar/dnd-5e-core-en/tree/main)
    * **English Translation:** This scoped version was translated from French to English using [Google Antigravity](https://antigravity.google/).
    * **Documentation Port:** The documentation has been modernized and ported to [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
    * **Theme & Styling:** Styled with the **Catppuccin Mocha** color palette from the [Catppuccin](https://catppuccin.com/) project.

!!! danger "No Support or Maintenance"
    **Absolutely no assistance, maintenance, or troubleshooting will be provided within this ported English repository.**
    
    For all original content (in both English and French), bug reports, feature requests, or general inquiries, please visit the official upstream repository: **[codingame-team/dnd-5e-core](https://github.com/codingame-team/dnd-5e-core)**.

---

## Core Engine Modules

The documentation is organized around the core engine modules that form the backbone of the D&D 5e Python system:

### [Combat](core/combat.md)
The **Combat** module implements the full initiative tracker, turn sequences, action economy management, damage resolution, and active combat state.

### [Customization](core/customization.md)
The **Customization** module provides character customization systems, managing racial features, class progression, subraces, and multiclassing rules.

### [Data Loading](core/data-loading.md)
The **Data Loading** module reads game files and JSON databases into native Python entities, managing collections and automated indexing.

### [Entities](core/entities.md)
The **Entities** module models the core actors of the system, including characters, monsters, and base stats.

### [Equipment](core/equipment.md)
The **Equipment** module manages items, inventories, weights, weapons, armor, and custom items.

### [Magic & Spells](core/magic-spells.md)
The **Magic & Spells** module contains spelling casting systems, spell slots, active spell lists, and magical effect trackers.

### [Rules & Mechanics](core/rules-mechanics.md)
The **Rules & Mechanics** module implements the core game systems, dice rollers, ability checks, and saving throw rules.

### [UI & Utilities](core/ui-utilities.md)
The **UI & Utilities** module contains helper scripts, ncurses UI layout configurations, and basic standard terminal outputs.
