# Correct code (7b):
def transform(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                continue
            for x in range(len(grid)):
                if x == i:
                    continue
                if grid[x][j] == grid[i][j]:
                    for y in range(len(grid[0])):
                        if y == j:
                            continue
                        if grid[i][y] == grid[i][j]:
                            grid[x][y] = grid[i][j]
    return grid


# Not correct code (14b) for gen 4:
def transform(grid):
    pattern_rows = 12
    pattern_cols = 21
    pattern = [[3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5], [6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2], [5, 2, 1, 2, 5, 4, 5, 2, 1, 2, 5, 4, 5, 2, 1, 2, 5, 4, 5, 2, 1], [6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2], [3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5], [2, 5, 4, 5, 2, 1, 2, 5, 4, 5, 2, 1, 2, 5, 4, 5, 2, 1, 2, 5, 4], [3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5], [6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2], [5, 2, 1, 2, 5, 4, 5, 2, 1, 2, 5, 4, 5, 2, 1, 2, 5, 4, 5, 2, 1], [6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2], [3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5, 6, 3, 2, 3, 6, 5], [2, 5, 4, 5, 2, 1, 2, 5, 4, 5, 2, 1, 2, 5, 4, 5, 2, 1, 2, 5, 4]]
    transformed_grid = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                pattern_i = i % pattern_rows
                pattern_j = j % pattern_cols
                transformed_grid[i][j] = pattern[pattern_i][pattern_j]
    return transformed_grid