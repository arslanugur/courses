#The following code simulates the game from the previous video for 100000 rounds. Run the code and observe the result.

from random import randint, seed
from datetime import datetime

seed(datetime.now())

dices = [
    [1, 1, 6, 6, 8, 8],
    [2, 2, 4, 4, 9, 9],
    [3, 3, 5, 5, 7, 7]
]

def compare_two_dices(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6

    num_rounds = 10**5
    num_dice1_wins = 0
    num_dice2_wins = 0

    for _ in range(num_rounds):
        dice1_result = dice1[randint(0, 5)]
        dice2_result = dice2[randint(0, 5)]

        if dice1_result > dice2_result:
            num_dice1_wins += 1
        elif dice2_result > dice1_result:
            num_dice2_wins += 1

    if num_dice1_wins > num_dice2_wins:
        print("The dice {} is better than {}: \nout of {} rounds it won {} times".format(dice1, dice2, num_rounds, num_dice1_wins))
    elif num_dice2_wins > num_dice1_wins:
        print("The dice {} is better than {}: \nout of {} rounds it won {} times".format(dice2, dice1, num_rounds, num_dice2_wins))
    else:
        print("A tie")


compare_two_dices(dices[0], dices[1])
compare_two_dices(dices[1], dices[2])
compare_two_dices(dices[2], dices[0])

"""
OUTPUT:
The dice [2, 2, 4, 4, 9, 9] is better than [1, 1, 6, 6, 8, 8]: 
out of 100000 rounds it won 55633 times
The dice [3, 3, 5, 5, 7, 7] is better than [2, 2, 4, 4, 9, 9]: 
out of 100000 rounds it won 55598 times
The dice [1, 1, 6, 6, 8, 8] is better than [3, 3, 5, 5, 7, 7]: 
out of 100000 rounds it won 55198 times
The dice [1, 1, 6, 6, 8, 8] is better than [3, 3, 5, 5, 7, 7]: 
out of 100000 rounds it won 55663 times
None
"""

