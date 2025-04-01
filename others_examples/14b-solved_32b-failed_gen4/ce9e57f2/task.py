# Correct code (14b):
def transform(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                for k in range(i + 1, len(grid)):
                    if grid[k][j] != 2:
                        break
                    if k == len(grid) - 1 or grid[k + 1][j] != 2:
                        grid[k][j] = 8
    return grid


# Not correct code (32b) for gen 4:
def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(4, rows):
        for c in range(1, cols - 1):
            if grid[r][c] == 2:
                if r > 4 and grid[r - 1][c] == 2 and (grid[r - 2][c] == 2):
                    grid[r][c] = 8
                elif r > 3 and grid[r - 1][c] == 2 and (grid[r - 3][c] == 2):
                    grid[r][c] = 8
                elif r > 2 and grid[r - 1][c] == 2 and (grid[r - 2][c] == 2) and (grid[r - 3][c] == 8):
                    grid[r][c] = 8
                if grid[r - 1][c] == 8 or grid[r - 2][c] == 8 or grid[r - 3][c] == 8:
                    grid[r][c] = 8
    return grid