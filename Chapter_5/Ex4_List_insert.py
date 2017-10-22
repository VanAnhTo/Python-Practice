inv = {'gold coin': 42,  'gold coin 1': -1}
#dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope', 'dagger', 'dagger']
dragonLoot =[1,2,3,4]
for i in range(len(dragonLoot)):
    if dragonLoot[i] in inv:
        inv[dragonLoot[i]] = inv[dragonLoot[i]] + 1
    else:
        inv.setdefault(dragonLoot[i],1)
print(inv)