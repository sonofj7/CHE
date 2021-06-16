dragonLoot = ['gold coin', 'dagger', 
              'gold coin', 'gold coin',
              'ruby']
inv = {}

# creates a dict
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory
addToInventory(inv,dragonLoot)

# reads the dictionary
def totalInventory(inventory):
    a = 0
    for item, quantity in inventory.items():
        print(str(quantity) + ' ' + item)
        a += quantity
    return a

print('Total items: ' + str(totalInventory(inv)))