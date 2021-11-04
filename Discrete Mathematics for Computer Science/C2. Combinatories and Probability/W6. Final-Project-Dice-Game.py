# Project Overview
"""
In this series of three programming tasks, 
we will implement together a program that will play optimally in a tricky dice game! 
You program will be given a list of dices and will decide who chooses the dice first (you or your opponent).
When the dices are chosen, we will simulate 10000 throws. 
Each time your number is greater, you get $1 from your opponent. 
Conversely, each time your number is smaller, you pay $1 to your opponent.
Your ultimate goal is to implement a program that always wins in such a simulation.
"""


# First Task: Compare Two Dices
"""
Implement a function that takes two dices as input and computes two values: 
the first value is the number of times the first dice wins (out of all possible 36 choices), 
the second value is the number of times the second dice wins. 
We say that a dice wins if the number on it is greater than the number on the other dice.
To debug your implementation, use the following test cases:
Sample 1
Input: dice1 = [1, 2, 3, 4, 5, 6], dice2 = [1, 2, 3, 4, 5, 6]
Output: (15, 15)
Sample 2
Input: dice1 = [1, 1, 6, 6, 8, 8], dice2 = [2, 2, 4, 4, 9, 9]
Output: (16, 20)
"""  
# TASK 1
# find the better dice with greater probability to win
def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    # check all possibilities
    for i in range(6):
        for j in range(6):
            if dice1[i]>dice2[j]:
                dice1_wins+=1
            elif dice1[i]<dice2[j]:
                dice2_wins+=1

    return (dice1_wins, dice2_wins)

# print(count_wins([1,1,6,6,8,8],[2,2,4,4,9,9]))
# print(count_wins([2,2,4,4,9,9],[3,3,5,5,7,7]))
# output: (16, 20)


# Second Task: Is there the Best Dice?
"""
Now, your goal is to check whether among the three given dices there is one that is better than the remaining two dices.
Implement a function that takes a list of dices and checks 
whether there is dice (in this list) that is better than all other dices. 
We say that a dice is better than another one, 
if it wins more frequently 
(that is, out of all 36 possibilities, it wins in aa cases, while the second one wins in bb cases, and a > b). 
If there is such a dice, return its (0-based) index. Otherwise, return -1.
Use the following datasets for debugging:
Sample 1
Input: [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
Output: -1
Sample 2
Input: [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
Output: 2
Sample 3
Input: [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]
Output: -1
"""
# task 2 - with mistake
def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    p=tuple()
    q=tuple()
    p=count_wins(dices[0],dices[1])
    q=count_wins(dices[0],dices[2])
    if p[0]>p[1]>q[1]:
        return 0
    p=count_wins(dices[1],dices[0])
    q=count_wins(dices[1],dices[2])
    if p[0] > p[1] > q[1]:
        return 1
    p = count_wins(dices[2], dices[0])
    q = count_wins(dices[2], dices[1])
    if p[0] > p[1] > q[1]:
        return 2
    return -1
dices=list()
# dices.append([1,1,6,6,8,8])
# dices.append([2,2,4,4,9,9])
# dices.append([3,3,5,5,7,7])

# dices.append([1,1,2,4,5,7])
# dices.append([1,2,2,3,4,7])
# dices.append([1,2,3,4,5,6])
# print(find_the_best_dice(dices))
# t=tuple()
# t=count_wins(dices[0],dices[1])
# print(t[0])



# Third Task: Implement a Strategy
"""
Ready to play!
Implement a function that takes a list of dices (possibly more than three) and returns a strategy. 
The strategy is a dictionary:
If, after analyzing the given list of dices, 
you decide to choose a dice first, set strategy["choose_first"] to True 
and set strategy["first_dice"] to be the (0-based) index of the dice you would like to choose
If you would like to be the second one to choose a dice, set strategy["choose_first"] to False. 
Then, specify, for each dice that your opponent may take, the dice that you would take in return. 
Namely, for each i from 0 to len(dices)-1, set strategy[i] to an index j of the dice that
you would take if the opponent takes the i-th dice first.
Use the following datasets for debugging:
Sample 1
Input: [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
Output: {'choose_first': False, 0: 1, 1: 2, 2: 0}
Sample 2
Input: [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
Output: {'choose_first': True, 'first_dice': 1}
Note that your answers do not have to coincide with the answers above. 
First, the order of elements does not matter in the dictionary. 
Second, the dictionary might contain extra information that is not required in the statement of the problem. 
For example, {0: 3, 'first_dice': 1, 'choose_first': True} is also a correct output in Sample 2.
"""
def compute_strategy(dices):
  assert all(len(dice) == 6 for dice in dices)

  strategy = dict()
  strategy["choose_first"] = True
  strategy["first_dice"] = 0
  for i in range(len(dices)):
    strategy[i] = (i + 1) % len(dices)
        
  # write your code here
  res = find_the_best_dice(dices)
  if res != -1:
    strategy["first_dice"] = res
  else:
    strategy["choose_first"] = False
    for i in range(len(dices)):
      for j in range(len(dices)):
        if i != j:
          dice1_wins, dice2_ins = count_wins(dices[i], dices[j])
          if dice1_wins < dice2_wins:
            break
      strategy[i] = j
	
  return strategy

print(compute_strategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]))
print(compute_strategy([[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]))

# Full Code:
def count_wins(dice1, dice2):
  assert len(dice1) == 6 and len(dice2) == 6
  dice1_wins, dice2_wins == 0, 0

	#write your code here
  equal = 0
  for i in range(6):
    for j in range(6):
      if dice1[i] > dice2[j]:
        dice1_wins += 1
      if dice1[i] == dice2[j]:
        equal += 1

  dice2_wins = 36 - dice1_wins - equal
  return (dice1_wins, dice2_wins)

# with mistake
def find_the_best_dice(dices):
  assert all(len(dice) == 6 for dice in dices)
  
  # write your code here
  # use your implementation of count_wins method if necessary
  for i in range(len(dices)):
    status = []
    for j in range(len(dices)):
      if i != j:
        dice1_wins, dice2_wins = count_wins(dices[i], dices[j])
        if dice1_ins > dice2_wins:
          status.append(1)
    if status.count(1) == len(dices) - 1:
      return i

  return -1

# with mistake
def compute_strategy(dices):
  assert all(len(dice) == 6 for dice in dices)

  strategy = dict()
  strategy["choose_first"] = True
  strategy["first_dice"] = 0
  for i in range(len(dices)):
    strategy[i] = (i + 1) % len(dices)
        
  # write your code here
  res = find_the_best_dice(dices)
  if res != -1:
    strategy["first_dice"] = res
  else:
    strategy["choose_first"] = False
    for i in range(len(dices)):
      for j in range(len(dices)):
        if i != j:
          dice1_wins, dice2_ins = count_wins(dices[i], dices[j])
          if dice1_wins < dice2_wins:
            break
      strategy[i] = j
	
  return strategy

print(compute_strategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]))
print(compute_strategy([[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]))




# task 3 - with mistake
from random import randint,seed
from datetime import datetime

seed(datetime.now())

def compute(a,b):
    assert len(a) == 6 and len(b) == 6
    num1 = 0
    num2 = 0
    rounds = 10 * 20000
    for i in range(rounds):
       result1 = a[randint(0, 5)]
       result2 = b[randint(0, 5)]
       if result1 > result2:
         num1 += 1
       else:
         num2 += 1
    return (num1,num2)

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    for i in range(len(dices)):
        c = 0
        for j in range(len(dices)):
            p=tuple()
            p=count_wins(dices[i],dices[j])
            if p[1]>p[0]:
                c=-1
                break
        if c==0:
            strategy["first_dice"] = i
            return strategy

    strategy=dict()
    strategy["choose_first"] = False
    for i in range(len(dices)):
        for j in range(len(dices)):
            p=count_wins(dices[i],dices[j])
            if p[0] > p[1]:
               if i!=(j+1)%len(dices):
                   strategy[i] = (j + 1) % len(dices)
                   break
               else:
                   strategy[i] = (i+1) % len(dices)
                   break
            else:
                continue

    return strategy
# dices.append([4,4,4,4,0,0])
# dices.append([7,7,3,3,3,3])
# dices.append([6,6,2,2,2,2])
# dices.append([5,5,5,1,1,1])
# print(compute_strategy(dices))

# dices.append([1,1,6,6,8,8])
# dices.append([3,3,5,5,7,7])
# dices.append([2,2,4,4,9,9])
# print(compute_strategy(dices))

# dices.append([1,1,4,6,7,8])
# dices.append([2,2,2,6,7,7])
# dices.append([3,3,3,5,5,8])
# print(compute_strategy(dices))

dices=list()
dices.append([4,4,4,4,0,0])
dices.append([3,3,3,3,3,3])
dices.append([6,6,2,2,2,2])
dices.append([5,5,5,1,1,1])
print(compute_strategy(dices))



----------
"""Dice game
"""
import itertools as it


def count_wins(dice1, dice2):
    """List all outcome when throw dices, calculate number
    of outcomes to dice 1 is winner or dice 2 is winner
    :param: dice1, list
    :param: dice2, list
    :return: tuple of int
    """
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for outcome in it.product(dice1, dice2):
        if outcome[0] > outcome[1]:
            dice1_wins += 1
        elif outcome[1] > outcome[0]:
            dice2_wins += 1

    return (dice1_wins, dice2_wins)


# def find_the_best_dice(dices):
#     """Find best of dice, which have highest probability occur win
#     If exist, return index of dict, else return -1
#     :param: dices, 2d array of int
#     :return: int
#     """
#     assert all(len(dice) == 6 for dice in dices)
#     dice_wins = {}
#     for i in range(len(dices)):
#         dice_wins[i] = []
#
#     for i in range(len(dices)-1):
#         for j in range(i+1, len(dices)):
#             dice_i_wins, dice_j_wins = count_wins(dices[i], dices[j])
#             if dice_i_wins > dice_j_wins:
#                 dice_wins[i].append(j)
#             elif dice_j_wins > dice_i_wins:
#                 dice_wins[j].append(i)
#
#     for i in range(len(dices)):
#         if i not in dice_wins:
#             continue
#         for loser in dice_wins[i]:
#             if loser not in dice_wins:
#                 continue
#             if i in dice_wins[loser]:
#                 return -1
#             dice_wins[i] += dice_wins[loser]
#             dice_wins.pop(loser)
#
#     return list(dice_wins.keys())[0]

# with mistake
def find_the_best_dice(dices):
    """Find best of dice, which have highest probability occur win
    If exist, return index of dict, else return -1
    :param: dices, 2d array of int
    :return: int
    """
    assert all(len(dice) == 6 for dice in dices)
    dice_wins = {}
    for i in range(len(dices)):
        dice_wins[i] = []

    for i in range(len(dices)-1):
        for j in range(i+1, len(dices)):
            dice_i_wins, dice_j_wins = count_wins(dices[i], dices[j])
            if dice_i_wins > dice_j_wins:
                dice_wins[i].append(j)
            elif dice_j_wins > dice_i_wins:
                dice_wins[j].append(i)

    for i in range(len(dices)):
        if i not in dice_wins:
            continue
        for loser in dice_wins[i]:
            if loser not in dice_wins:
                continue
            if i in dice_wins[loser]:
                return -1
            dice_wins[i] += dice_wins[loser]
            dice_wins.pop(loser)

    return list(dice_wins.keys())[0]

# with mistake
def compute_strategy(dices):
    """Compute strategy
    If best dice exist, this return choose_first = True and
    first_dice is index of best dice
    Else, it return choose_first is False and strategy for
    choose dice after opponient choose
    :param: dices, 2d array of int
    :param: dict
    """
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0

    result = find_the_best_dice(dices)
    if result != -1:
        strategy["first_dice"] = result
    else:
        strategy = dict()
        strategy["choose_first"] = False
        for i in range(len(dices)):
            for j in range(len(dices)):
                if i != j:
                    dice_i_wins, dice_j_wins = count_wins(dices[i], dices[j])
                    if dice_j_wins > dice_i_wins:
                        break
            strategy[i] = j
    return strategy


dices = list()
dices.append([4, 4, 4, 4, 0, 0])
dices.append([7, 7, 3, 3, 3, 3])
dices.append([6, 6, 2, 2, 2, 2])
dices.append([5, 5, 5, 1, 1, 1])
print(compute_strategy(dices))

# dices.append([1,1,6,6,8,8])
# dices.append([3,3,5,5,7,7])
# dices.append([2,2,4,4,9,9])
# print(compute_strategy(dices))

# dices.append([1,1,4,6,7,8])
# dices.append([2,2,2,6,7,7])
# dices.append([3,3,3,5,5,8])
# print(compute_strategy(dices))

# dices=list()
# dices.append([4,4,4,4,0,0])
# dices.append([3,3,3,3,3,3])
# dices.append([6,6,2,2,2,2])
# dices.append([5,5,5,1,1,1])
# print(compute_strategy(dices))


