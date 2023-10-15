
smiths = {

}

items = ["Sword", "Armor", "Shield"]
costs = [100, 200, 300]

def display_items():
  print("Blacksmith Shop")
  print("----------------")
  for i, item in enumerate(items):
    print(f"{i+1}. {item} - {costs[i]} coins")

def upgrade(item_index, coins):
  if item_index < 0 or item_index >= len(items):
    print("Invalid item.")
    return
  
  if coins < costs[item_index]:
    print("You do not have enough coins to upgrade this item.")
    return
  
  print(f"Upgraded {items[item_index]} for {costs[item_index]} coins.")

display_items()
item = int(input("Enter the number of the item you want to upgrade: "))
upgrade(item-1, 150)
