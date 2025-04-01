# Correct code (14b):
def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    transformed_grid = [[0] * cols for _ in range(rows)]
    target_numbers = {3, 8, 2, 6, 7}
    for i in range(rows):
        if grid[i][0] in target_numbers and grid[i][cols - 1] in target_numbers:
            transformed_grid[i] = [grid[i][0]] * cols
    for j in range(cols):
        if grid[0][j] in target_numbers and grid[rows - 1][j] in target_numbers:
            for i in range(rows):
                transformed_grid[i][j] = grid[0][j]
    return transformed_grid


# Not correct code (32b) for gen 4:
def transform(grid):
    rows, cols = (len(grid), len(grid[0]))
    result = [[0] * cols for _ in range(rows)]
    rows_with_3 = [i for i, row in enumerate(grid) if 3 in row]
    cols_with_3 = [j for j, col in enumerate(zip(*grid)) if 3 in col]
    rows_with_8 = [i for i, row in enumerate(grid) if 8 in row]
    cols_with_8 = [j for j, col in enumerate(zip(*grid)) if 8 in col]
    if rows_with_3:
        middle_row_3 = rows_with_3[len(rows_with_3) // 2]
        result[middle_row_3] = [3] * cols
    if cols_with_3:
        middle_col_3 = cols_with_3[len(cols_with_3) // 2]
        for i in range(rows):
            result[i][middle_col_3] = 3
    if rows_with_8:
        middle_row_8 = rows_with_8[len(rows_with_8) // 2]
        result[middle_row_8] = [8] * cols
    if cols_with_8:
        middle_col_8 = cols_with_8[len(cols_with_8) // 2]
        for i in range(rows):
            result[i][middle_col_8] = 8
    return result