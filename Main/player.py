"""
here will be the file that will define all player logic
17th of october: making the player class basics and trying to make an inventory system for the player
the idea for the inventory is as follows: 
- I wanted to make an inventory class that will work more or less the same for all the things that have one
  with the player and player stashes (idk if they will be added or not) to be always saved in the save of the game
  and called for when needed (when crafting or when opening up the inventory)
  npc inventories are another thing, I don't want to have them loaded on the RAM for the entire game so a similar
  thing of loading on interaction will be made, I think for example shops will have a loot table to get what they
  sell and after its loaded they get a seed of sorts that will be placed in a JSON file with their npc ID
  so when you go to interact with them, they can decipher the seed and load the inventory meaning you need to keep
  track of fewer things in the save file, that should be simple.
  a similar system can be used to the players inventory whe I think about it, more heavy on the cpu but less ram usage
  I mean come on how hard would it be to decipher the first letter of an item and a number lol
  as per saving prices that will come later, today I focus on the player and try to make a general inventory class
"""