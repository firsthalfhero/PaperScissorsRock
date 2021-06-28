import random

pick = random.randrange(0,2,1)
array = ['item1', 'item2', 'item3']
pickarray = ['item1', 'item2', 'item3']
random.shuffle(array)

while pick <3:
    pick = random.randrange(0,2,1)
    array = ['item1', 'item2', 'item3']
    pickarray = ['item1', 'item2', 'item3']
    random.shuffle(array)
    print(array[0])
    print(pickarray[pick])
    
    

# print(array)
# print(pickarray)
# print(array[0])
# print(pickarray[pick])