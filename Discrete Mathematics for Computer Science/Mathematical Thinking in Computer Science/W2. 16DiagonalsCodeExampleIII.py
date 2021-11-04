from collections import Counter
from time import time

def can_be_extended_to_solution(mat,n, dig):
    d = Counter(mat)
    if (d[1]+d[-1] + n*n - len(mat) < dig):
        return False
    if len(mat) > 1:
        if (mat[-2] ==  -mat[-1]):
            return False
        if len(mat)>n:
            if (mat[-1] == -mat[-1-n]):
                return False
            if (len(mat)>n) and (len(mat)%n != 0):
                if ((mat[-1] == 1) and (mat[-1-n+1] == 1)):
                    return False
            if (len(mat)>n) and (len(mat)%n != 1):
                if ((mat[-1] == -1) and (mat[-1-n-1] == -1)):
                    return False            
                
                
    return True


def extend(mat,n, dig):
    d = Counter(mat)
    if (len(mat) == n*n) and (d[1]+d[-1]==dig):
        print (time() - start_time)
        print(mat)
        exit()
    
    
    for k in [1,-1,0]:
        if len(mat) != n*n:
            mat.append(k)
            if k == 0 or can_be_extended_to_solution(mat, n, dig):
                extend(mat, n, dig)
            mat.pop()
            
start_time = time()
extend([],5,16)

