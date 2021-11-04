n = 5
tar = 16
# we put a frame around the matrix to simplify code, that's way matrix dimensions are (n+2) * (n+2)
matrix = [[-1 for x in range(n+2)] for y in range(n+2)]


def can_extend(r, c):
    if matrix[r][c] == -1:
        return True
    if matrix[r][c] == 0:
        return matrix[r-1][c+1] != 0 and matrix[r-1][c]!=1 and matrix[r][c-1]!=1
    if matrix[r][c] == 1:
        return matrix[r-1][c]!=0 and matrix[r-1][c-1]!=1 and matrix[r][c-1]!=0
        
    
# cnt_free : the number of decided empty cells. If this number is n^2-tar, then I can't add a new empty cell
def extend(r, c, cnt_free = 0):
    if r > n:
        for row in matrix[1:n+1]:
            print(row[1:n+1])
        print()
        return
    
    # determine next cell 
    if c == n:
        nr, nc = r+1, 1
    else:
        nr, nc = r, c+1
    
    # Option of leaving cur square empty is valid iff number of remaining square is at least tar
    if cnt_free + tar < n*n:
        matrix[r][c] = -1
        extend(nr, nc, cnt_free+1)
        
    # try both options
    for i in [0, 1]:
        matrix[r][c] = i
        if can_extend(r,c):
            extend(nr,nc,cnt_free)

        

extend(r=1,c=1)

