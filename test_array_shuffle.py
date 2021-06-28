import random
import time

# pick = random.randrange(0,2,1)

# random.shuffle(array)

# while pick <3:
#     pick = random.randrange(0,2,1)
#     array = ['item1', 'item2', 'item3']
#     pickarray = ['item1', 'item2', 'item3']
#     random.shuffle(array)
#     print(array[0])
#     print(pickarray[pick])
play = True

while play:
    
    array = ['item1', 'item2', 'item3']

    rand = random.randrange(0, 90, 1)

    if rand < 30:
        pick = 0
    elif 30 <= rand < 60:
        pick = 1
    elif rand >= 60:
        pick = 2

print(rand,"|",pick,"|",array[pick],"|")
    
    # time.sleep(1)

    

# print(array)
# print(pickarray)
# print(array[0])
# print(pickarray[pick])