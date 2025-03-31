# Correct code (7b):
def transform(grid):
    transformed = [[0] * 4 for _ in range(4)]
    color_map = {0: 2, 1: 0, 2: 2, 3: 0, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}
    for i in range(8):
        for j in range(4):
            if i < 4:
                transformed[i][j] = color_map[grid[i][j]]
            elif grid[i][j] == 1:
                transformed[i - 4][j] = 0
    return transformed


# Not correct code (14b) for gen 4:
def transform(grid):
    output_grid = [[0] * 4 for _ in range(4)]
    for i in range(8):
        for j in range(4):
            if grid[i][j] == 3 and (i == 1 or i == 2) and (j == 1 or j == 2):
                output_grid[i - 4][j - 1] = 2
    return output_grid