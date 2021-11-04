# WEEK I
# Learning Objectives
#     Use basic methods of combinatorics to count objects
#     Count the number of objects in basic combinatorial settings
#     Categorize counting problems into basic combinatorial settings
#     Apply standard operations to sets of objects

# COUNTING
# Rule of Sum in Programming

      #Example:
for _ in range(3):
  print("Hi!")
for _ in range(5):
  print("Hi!") # output: 8
  
      #Example:
for _ in range(8):
  print("Hi!")
for _ in range(4):
  print("Hi!") 
for _ in range(7):
  print("Hi!") # output: 19

# Numbers Divisible by 2 or 3  
# How many numbers from 1 to 10, inclusive, are divisible by 2?
# Ans: 5

# How many numbers from 1 to 10 are divisible by 3?
# Ans: 3
  
# How many numbers from 1 to 10 are divisible by 2 or by 3?
# Ans: 7
  
  
# Operations with Sets
# Consider the sets A = {1,2,4,6,7} and B = {1,2,3,5,7}. 
# What is the intersection A ∩ B of sets A and B?
# Ans: A ∩ B = {1,2,7}
# Intersection is the set of all elements that belong both to A and B.

# Consider the sets A = {1,2,4,6,7} and B = {1,2,3,5,7}. 
# What is the union A ∪ B of sets A and B?
# Ans: A ∪ B = {1,2,3,4,5,6,7}
# Union is the set of all elements that belong to at least one of the sets A and B.

'''
Consider the sets A = {1,3,4,6,7,8} and B – the set of all even natural numbers. 
What is the size |A ∩ B| of intersection of sets A and B?
Ans: 3
Indeed, the intersection consists of all elements that belong to both sets. 
The only even numbers in A are 4, 6 and 8. 
So the intersections consists of three elements.

# Generalized Rule of Sum
There are 25 students in the class. 
Each student should take at least one of the two foreign languages, French and German, 
and students are allowed to take both courses. 
It is known that 17 students signed up for the French language course 
and 14 students signed up for German language course. 
How many students signed up for both courses?
Ans: 6
Indeed, we can denote by AAA the set of all students that have signed up for French language course 
and denote by B the set of all students that signed up for German language course. 
Then since each student of the class takes at least one of the courses the union A∪B consists of all students in the class. 
On the other hand, the intersection A ∩ B consists of students who signed up for both courses. 
Now, we know from the previous video that the following relation between the sizes of the sets holds : 
    ∣A∪B∣=∣A∣+∣B∣−∣A∩B∣. 
We also know that |A| = 17, |B| = 14 and ∣A ∪ B∣ = 25. 
Overall we can conclude that ∣A ∩ B∣ = ∣A∣ + ∣B∣ − ∣A ∪ B∣ = 17+14−25 = 6.
  

How many integer numbers from 1 to  1000 are divisible by 2 or by 3?
Ans: 667
Indeed, we can use the generalized version of rule of sum here. 
Let A be the set of all numbers from 1 to 1000 divisible by 2 
and B be the set of all numbers from 1 to 1000 that are divisible by 3. 
Then A ∪ B is the set of numbers that are divisible by 2 or by 3. 
And the set A ∩ B is the set of numbers that are divisible by 2 and by 3. 
These are exactly the numbers that are divisible by 6. 
Now, note that |A| = 500 since every other number from 1 to 1000 is divisible by 2. 
Also |B| = 333, since the numbers divisible by 3 are 3, 6, 9, 12 and so on till 999. 
So every third number from 1 to 999 is divisible by 3. 
Finally, |A ∩ B|=166 since the numbers divisible by 6 are 6, 12, 18, 24, 30 and so on till 996. 
So every 6-th number from 1 to 996 is divisible by 6. 
So it remains now to apply the formula that we showed in the previous video: 
          ∣A∪B∣ = ∣A∣+∣B∣−∣A∩B∣ = 500+333–166 = 667 
  
How many integer numbers from 1 to  1000 are not divisible neither by 2, nor by 3?  
Ans: 333
Indeed, the requirement in this problem is exactly the opposite to the requirement of the previous problems. 
So to count them we can subtract the number of all numbers 
from the previous problem from the number of all numbers from 1 to 1000. 
So the answer is 1000-667=333.
'''

# RECURSIVE COUNTING
# Rule of Product in Programming
      # Example:
for _ in range(5):
        for _ in range(7):
                print("Hi!")
"""
If we run this code, how many times the word 'Hi!' will be printed?
Ans: 35
Indeed, the outer cycle runs 5 times and the inner cycle runs 7 times. 
Each application of the `print' command is associated 
with a pair consisting of the number of the run of the first cycle 
and the number of the run of the second cycle. 
By the product rule the number of such pairs is 5x7=35. 
So we will go through the printing line 35 times.
"""

      # Example:
for _ in range(3):
        for _ in range(4):
                for _ in range(5):
                        print("Hi!")
"""
If we run this code, how many times the word 'Hi!' will be printed? 
Ans: 60
Indeed, the first cycle runs 3 times, the second cycle runs 4 times and the third cycle runs 5 times. 
So by the application of the product rule two times we will go through the printing line 3x4x5=60 times
"""

      # Example:  
for _ in range(2):
        for _ in range(6):
                print("Hi!")
for _ in range(3):
        for _ in range(5):
                print("Hi!")
"""
If we run this code, how many times the word 'Hi!' will be printed? 
Ans: 27
By the rule of product the print function is called 2x6=12 times in the first pair of cycles. 
It is called 3x5=15 times in the second pair of cycle. 
By the rule of sum it is called 12+15=27 times in total.
"""

# Applications of the Rule of Product
'''
Suppose there are five teams in some sport participating in some tournament. 
Each team contains 8 players. 
We would like to choose one of the players of one of the teams to lead an opening ceremony. 
How many ways do we have to do it?
Ans: 40
This is exactly the number of players participating in the tournament. 
We can also think of this in the following way. 
We have actually to make two sequential choices: first we need to pick a team and then one player in it. 
And we are actually computing pairs of these choices. 
We can make the first choice in 5 ways and the second choice in 8 ways. 
Then by the product rule we have 5x8=40 possible choices in total.


Suppose you are picking a t-shirt in some online store. 
The t-shirt comes in 5 possible colours, 7 possible sizes and 2 neck types (crewneck and v-neck). 
How many possible variants of the t-shirt are there?
Ans: 70
Indeed, we have to make three choices, with 5, 7 and 2 options respectively. 
But the rule of product there are 5x7x2=70 options in total.


Suppose each circle on the top is connected to each circle on the bottom. 
So to pick a segment we need to pick one circle on the top and one circle on the bottom. 
There are 7 circles on the top and 8 circles on the bottom. 
So by the rule of product the number of segments is 7×8=56.


TUPLES AND PERMUTATIONS
# Number of Passwords
What is the number of 5-symbol passwords where each symbol is one of the 26 lower case Latin letters?
Ans: see next video
      
# Tuples
Linguists are studying texts in some ancient language with 25 letters. 
They want to compute how often different 3-letter combinations occur in texts in this language. 
For this they first need to list all 3-letter combinations. How many combinations will they have?
Ans: 15625
Indeed, we have to pick ordered sequences of length 3 out of 25 possible letters. 
So, we are dealing with tuples and the answer is 25*25*25 = 15625


# Counting with Restrictions
How many 3-digit numbers are there that have digits 1, 2 and 3 (each of them exactly once)?
Ans: 6
We have to pick which of three numbers we can place on the first position, 
which of the remaining two numbers we will place on the second position 
and then we will place the remaining number on the third position. 
We are dealing with permutations of numbers 1, 2 and 3 here and the answer is 3*2*1=6.

      
A board of 15 people has to pick a chairman of the board, a vice-chairman and a secretary among themselves. 
All three should be different persons. How many ways do they have to do it?
Ans: 2730
We have 15 options for a chairman, 
there are 14 options left for a vice-chairman and there are 13 options left for a secretary. 
We thus have a 3-permutation of 15 elements. 
And the answer is 15*14*13=2730


There are five different tables in the class and five students. 
Each table can be occupied by only one student. Their studying year consists of 200 days. 
As a small prank on their teacher students would like to sit in a new way every day, 
so there are no two days during their studying year such that all students are occupying the same tables. 
They would like to see whether this is possible. 
How many ways are there for them to sit in the class?
Ans: 120 
The first person can pick a table in 5 possible ways. 
Then the second person remains with 4 possible options, the third person remains with 3 options and so on. 
We are dealing with permutations of five people between five places to sit 
and there are 5*4*3*2*1=120 such permutations.


      
How many integer numbers between 0 and 9999 are there that have exactly one digit 1 and exactly one digit 3?
Ans: 768
Indeed, there are 4 ways to pick the position for digit 1. 
Then there are 3 positions remaining for digit 3. 
And then we can pick each of the remaining digits in 8 possible ways (digits 1 and 3 are forbidden). 
Thus by the rule of product there are 4x3x8x8=768 possible numbers.
'''
