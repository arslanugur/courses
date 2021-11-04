#Rule of sum
print(['Alice', 'Bob', 'Charlie']  + [0, 1, 2, 3, 4])

#OUTPUT
"""
['Alice', 'Bob', 'Charlie', 0, 1, 2, 3, 4]
"""

##############################################

#Rule of product
from itertools import product
for p in product(['a', 'b', 'c'], ['x', 'y']):
  print("".join(p))

#OUTPUT
"""
ax
ay
bx
by
cx
cy
"""

##############################################

#Tuples
from itertools import product
for p in product("ab", repeat=3):
  print("".join(p))

#OUTPUT
"""
aaa
aab
aba
abb
baa
bab
bba
bbb
"""

##############################################

#Permutations
from itertools import permutations
for p in permutations("abcd", 2):
  print("".join(p))
  
#OUTPUT
"""
ab
ac
ad
ba
bc
bd
ca
cb
cd
da
db
dc
"""

