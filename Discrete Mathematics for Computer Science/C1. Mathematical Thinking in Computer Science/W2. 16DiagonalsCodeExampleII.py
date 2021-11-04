from datetime import datetime

N = 5
D = 16
values = [1, 2, 0]

# 1 - ⧄ value
# 2 - ⧅ value
# 0 - ⧈ value

def get_value(arr, i, j):
    if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[i]):
        return 0
    return arr[i][j]

# Pretty print result
def print_result(arr, t):
    print('Spend:', datetime.now() - t)

    for i in range(len(arr)):
        row = '  '
        for j in range(len(arr[i])):
            value = arr[i][j]

            if value == 1:
                row += '⧄'
            elif value == 2:
                row += '⧅'
            else:
                row += '⧈'

        print(row)


# Check is value available for cell
def is_available_value(arr, i, j, v):
    if v == 0:
        return True

    tl = get_value(arr, i - 1, j - 1)
    tc = get_value(arr, i - 1, j)
    tr = get_value(arr, i - 1, j + 1)
    cl = get_value(arr, i, j - 1)

    if v == 1:
        return tc != 2 and tr != 1 and cl != 2

    # 2 value
    return tl != 2 and tc != 1 and cl != 1


def fill_next_cell(arr, i, j, count_left, t):
    # found solution
    if count_left == 0:
        print_result(arr, t)
        exit()

    # move to the next row
    if j > len(arr[i]) - 1:
        i += 1
        j = 0

    # end of array
    if i > len(arr) - 1:
        return

    # iterate over values
    for v in values:
        if is_available_value(arr, i, j, v):
            arr[i][j] = v
            count_left = count_left - 1 if v != 0 else count_left
            fill_next_cell(arr, i, j + 1, count_left, t)
            count_left += 1


# initial matrix
arr = [[0 for i in range(N)] for j in range(N)]

t = datetime.now()

fill_next_cell(arr, 0, 0, D, t)

