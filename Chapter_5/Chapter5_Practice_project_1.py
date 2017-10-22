#list = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def listDisplay(list):
    print('List item: ')
    item_total = 0
    for k, v in list.items():
        print(str(v)+' '+ k)
        item_total = item_total + int(v)
    print("Total number of items: " + str(item_total))


def addToList(inv, dragonLoot):
    for i in range(len(dragonLoot)):
        if dragonLoot[i] in inv:
            inv[dragonLoot[i]] = inv[dragonLoot[i]] + 1
        else:
            inv.setdefault(dragonLoot[i], 1)
    return inv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToList(inv, dragonLoot)

print(listDisplay(inv))
