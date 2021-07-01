shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI will sort shoplist')
shoplist.sort()
print('Sorted shoplist is now:', shoplist)

print('\nI also want to buy rice')
shoplist.append('rice')
print('My shopping list is now:', shoplist)

print('The first item I will buy is:', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

