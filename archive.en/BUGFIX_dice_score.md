# Bugfix: AttributeError in DamageDice.score()
## 🐛 Issue
```
AttributeError: 'NoneType' object has no attribute 'lower'
```
**File:** `dnd_5e_core/mechanics/dice.py`  
**Method:** `DamageDice.score()`  
**Line:** 138
### Error Context
When using `combat_system.py`, some special monster attacks have a `dc_success` attribute that can be `None`. When this value is passed to the `score()` method, calling `.lower()` on `None` causes an error.
**Complete Traceback:**
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
### Changes Made
1. **Parameter type change:**
   - Before: `success_type: str = "none"`
   - After: `success_type: Optional[str] = "none"`
2. **Validation check added:**
   ```python
   # Handle None or empty success_type
   if success_type is None or not success_type:
       success_type = "none"
   ```
3. **Docstring update:**
   - Added note that `None` is treated as `"none"`
### Modified Code
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
    expected = (self.bonus + dice_sides * (1     expected = (self.bonus +    return expec    expected = (self.bonus + dice_siAll combat scripts were successfully tested:
```
1. ✅ `combat.py` - Simple 1v1 combat
2. ✅ `party_combat.py` - Group of 6 adventurers (manual)
3. ✅ `demo_quick_combat.py` - Quick demo with random characters
4. ✅ `auto_random_combat.py` - Auto combat with random characters
5. ✅ `advanced_random_combat.py` - Advanced version with detailed stats
**Result:** No errors detected. Combats proceed normally, including with monsters using special attacks.
---
## 📝 Impact
### Before the Fix
- ❌ Crash during combat with certain monsters having `dc_success = None`
- ❌ Impossible to finish certain combats
- ❌ Random combat scripts not functional
### After the Fix
- ✅ All monsters handled correctly
- ✅ Special attacks work without error
- ✅ All combat scripts operational
---
## 🔍 Affected Monsters
Monsters with special attacks without defined `dc_success`, for example:
- Black Dragon Wyrmling (Acid Breath)
- White Dragon Wyrmling (Cold Breath)
- And potentially others with special abilities
---
## 📅 Fix Date
January 6, 2026
---
## 🎯 Next Version
This fix should be included in the next version of `dnd-5e-core` (0.1.4 or patch).
