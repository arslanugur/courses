'''
WEEK II
Learning Objectives
    Compute binomial coefficients
    Compute number of subsets
    Apply the binomial theorem
    Develop programs for generating combinatorial objects

COMBINATIONS
# Number of Segments and Diagonals
What is the number of segments in the picture below? (Each segment joins two circles.)
Ans: 6 
It is equal to (4 matrix 2) = 6

What is the number of segments in the picture below? (Each segment joins two circles.)
Ans: 91
It is (14 matrix 2) = 14 × 132 / 2 = 91

A polygonal diagonal is a line segment connecting two nonadjacent vertices of a polygon. 
Compute the number of diagonals of the following polygon with 16 vertices (and 16 edges).
Ans: 104
One can compute it either as 16 × 13 / 2 (each of 16 vertices is joined to 13 other vertices; 
each diagonal is counted twice this way) or as (16 matrix 2) − 16 (all the segments except for the edges).

# Forming Sport Teams
In how many ways can one select a team of five students out of ten students?
Ans: 252
It is just (10 matrix 5).

In how many ways can one partition ten students into two teams of size five?
Ans: 126
There are (10 matrix 5) = 252 ways of selecting the first team. 
When the first team is selected, the second team is uniquely determined. 
But this way, each pair of teams (A,B) is counted twice: 
when A is selected as the first team and when B is selected as the first team. 
Thus, the resulting count should be divided by two. 
This finally gives (10 matrix 5) / 2 = 126.
'''

# Number of Iterations of Nested For Loops

What will the following program print?
n = 10
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j and j < k:
                count += 1

print(count)  #output: 120

What will the following program print? Note that n is large in this case, making this code too slow.
n = 1000
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j and j < k:
                count += 1

print(count)   #output: 166167000
# Here we are counting all triples of different integers i,j,k such that 1 ≤ i < j < k ≤ 1000. 
# It is the same as the number of ways of selecting three different integers out of 1000 
# since one can always arrange them in decreasing order. 
# Thus, the answer is (1000 matrix 3) = 1000 × 999 × 998 / 2 × 3 = 166167000.


'''
PASCAL'S TRIANGLE
# Sum of the First Six Rows of Pascal's Triangle
What is the sum of all the elements from the first six rows of Pascal's triangle?
Ans: It is 1+2+4+8+16+32 = 2^0+2^1+2^2+2^3+2^4+2^5=2^6−1 = 63.

# Expanding (3a-2b)^k
Find the coefficients of the expansion of (3a−2b)^3. 
That is, represent (3a−2b)^3 as 
      α_0a^3 + α_1a^2b^1+α_2a^1b^2 + α_3b^3.
Try to compute these coefficients using the binomial theorem (instead of multiplying (3a−2b) by itself two times).
Enter the values α_0,α_1,α_2,α_3. Separate the values by commas, avoid spaces, do not include plus signs.
For example, for the question (3a−2b)^2 the answer would be: 9,-12,4
Ans: 27,-54,36,-8

Find the coefficients of the expansion of (3a−2b)^7. 
That is, represent (3a−2b)^7 as 
			α_0a^7 + α_1a^6b^1 + α_2a^5b^2 + α_3a^4b^3 + α_4a^3b^3 + α_5a^2b^5 + α_6ab^6 + α_7b^7.
Enter the values α_0,α_1,α_2,α_3,α_4,α_5,α_6,α_7. 
Separate the values by commas, avoid spaces, do not include plus signs.
For example, for the question (3a−2b)^2 the answer would be: 9,-12,4
Ans: 2187,-10206,20412,-22680,15120,-6048,1344,-128


Practice Counting
# Practice Counting
What is the number of 6-card hands with three hearts and three spades?
Ans: 81796
It is (13 matrix 3) × (13 matrix 3) = 286^2 = 81796.

What is the number of bit-strings (that is, strings consisting of 0's and 1's) 
of length 6 where the number of 0's is equal to the number of 1's?
For example, there are two such strings of length two: 01 and 10.
Ans: 20
We just need to select three (out of six positions) of 0's.

What is the number of sequences of six digits where the number of even digits is equal to the number of odd digits?
For example, there are 50 such sequences of length two: 01, 03, 05, 07, 09, 10, 12, 14, 16, 18, ..., 90, 92, 94, 96, 98.
Ans: 312500
We first select three positions for odd digits. For each of these three positions, we select one of five odd digits. 
For each of the remaining three positions, we select one of the five even digits. Overall, this gives binom{6}{3} x 5^3 x 5^3.

In how many ways one can get from the bottom left cell to top right cell of a 9×9 grid, 
if each move is either two cells up or three cells to the right?
Ans: 0
One cannot reach the rightmost column.

In how many ways one can get from the bottom left cell to the top right cell of a 13×13 grid, 
if each move is either two cells up or three cells to the right?
Ans: 210
We need six moves up and four steps to the right. Hence, binom{10}{4} = 210.
'''
