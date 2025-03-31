# Correct code (32b_gen1):
def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [row[:] for row in grid]
    inner_top = 1
    inner_bottom = rows - 2
    inner_left = 1
    inner_right = cols - 2
    for i in range(inner_top, inner_bottom + 1):
        for j in range(inner_left, inner_right + 1):
            if result[i][j] == 0:
                if all((grid[x][j] == 0 for x in range(inner_top, inner_bottom + 1))) or all((grid[i][y] == 0 for y in range(inner_left, inner_right + 1))):
                    result[i][j] = 3
                elif i > 1 and grid[i - 1][j] == 3 or (i < inner_bottom and grid[i + 1][j] == 3) or (j > 1 and grid[i][j - 1] == 3) or (j < inner_right and grid[i][j + 1] == 3):
                    result[i][j] = 3
    return result


# Not correct code (32b_gen0):
def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 0:
                grid[i][j] = 3
    return grid


