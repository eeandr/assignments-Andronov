import random

count = 0
win_1 = 0
win_2 = 0

while count < 1000:
    count += 1
    prize = ['goat', 'goat', 'auto']  #  shuffle prizes
    random.seed()
    random.shuffle(prize)

    dict_prize = {}   #  Numers of doors and prizes
    for i in xrange(1,4):
        dict_prize[i] = prize[i-1]

# Player 1, does not change the door
    if dict_prize[(random.choice([1,2,3]))] is 'auto':
        win_1 += 1

#  Player 2, changes door
    if dict_prize[(random.choice([1,2,3]))] is 'goat':
        win_2 += 1

print(win_1, win_2)
