# Correct code (32b_gen1):
def transform(grid):
    non_zero_positions = [(i, j) for i in range(6) for j in range(6) if grid[i][j] != 0]
    if not non_zero_positions:
        return grid
    min_i = min((i for i, _ in non_zero_positions))
    max_i = max((i for i, _ in non_zero_positions))
    min_j = min((j for _, j in non_zero_positions))
    max_j = max((j for _, j in non_zero_positions))
    top_left_i, top_left_j = (max(0, min_i - 2), max(0, min_j - 2))
    bottom_right_i, bottom_right_j = (min(5, max_i + 2), min(5, max_j + 2))
    result = [[0] * 6 for _ in range(6)]
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            result[i][j] = grid[i][j]
    for i in range(top_left_i, min_i):
        for j in range(top_left_j, min_j):
            result[i][j] = grid[max_i][max_j]
    for i in range(top_left_i, min_i):
        for j in range(max_j + 1, bottom_right_j + 1):
            result[i][j] = grid[max_i][min_j]
    for i in range(max_i + 1, bottom_right_i + 1):
        for j in range(top_left_j, min_j):
            result[i][j] = grid[min_i][max_j]
    for i in range(max_i + 1, bottom_right_i + 1):
        for j in range(max_j + 1, bottom_right_j + 1):
            result[i][j] = grid[min_i][min_j]
    return result


# Not correct code (32b_gen0):
def transform(grid):
    import numpy as np
    grid = np.array(grid)
    center_block = grid[2:4, 2:4]
    top_left = center_block[0, 0]
    top_right = center_block[0, 1]
    bottom_left = center_block[1, 0]
    bottom_right = center_block[1, 1]
    new_grid = np.zeros((6, 6), dtype=int)
    new_grid[0:2, 0:2] = bottom_right
    new_grid[0:2, 4:6] = bottom_left
    new_grid[4:6, 0:2] = top_right
    new_grid[4:6, 4:6] = top_left
    new_grid[2:4, 2:4] = center_block
    return new_grid.tolist()