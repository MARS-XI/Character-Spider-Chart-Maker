# **Character Spider Chart Maker**


## Description
Tool to visualize the D&D-like stats of a player's character.  
The stats are Strength (STR), Dexterity (DEX), Constitution (CON), Intelligence (INT), Wisdom (WIS) and Charisma (CHA).

## Console Inputs (can do multiple charcters)
- character's name
- list of character stats
- new list of stats to display (change default stats)
## GUI Inputs (single character, no personalized stats)
- character's name, level, gender, species and class
- character's stats
---
## Input Specifics
The character's name can be uppercase or lowercase and can contain numbers. In general any Unicode character is accepted.  
The stats must be numbers, integrers or decimals.

**Console Application:**  
After the inputs the user is asked if they want to insert another character's stats.  
The answer must be of the type (y/n).
## Output
One (or more) graphs displaying each character stats in a spider chart (AKA radar chart).
  
**GUI:**  
Chart can be saved in a file named "CharacterSpiderChart_{character's name}_{date}".  
Date's format is YYYY-MM-DD

