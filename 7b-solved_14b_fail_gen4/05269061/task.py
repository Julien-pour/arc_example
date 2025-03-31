# Correct code (7b):
def transform(grid):
    rows, cols = (len(grid), len(grid[0]))
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                for k in range(rows):
                    for l in range(cols):
                        if (k - i + l - j) % 3 == 0:
                            grid[k][l] = grid[i][j]
    return grid


# Not correct code (14b) for gen 4:
def transform(grid):
    n = len(grid)
    first_row = grid[0]
    non_zero_elements = [x for x in first_row if x != 0]
    if not non_zero_elements:
        non_zero_elements = [2, 4, 1]
    m = len(non_zero_elements)
    for i in range(n):
        for j in range(n):
            grid[i][j] = non_zero_elements[(i + j) % m]
    return grid