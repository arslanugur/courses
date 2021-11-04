#we simulate a dice throw 100000 times and compute the average value. 

from random import randint, seed
from datetime import datetime

seed(datetime.now())

num_rounds = 10**5
sum_of_values = 0

for _ in range(num_rounds):
    sum_of_values += randint(1, 6)
    
print("The average is {}".format(sum_of_values/(num_rounds*1.0)))

"""
OUTPUT: The average is 3.49693
"""

