# Correct code (14b):
def transform(grid):
    num_rows = len(grid)
    num_columns = len(grid[0])
    new_grid = [[0] * num_columns for _ in range(num_rows)]
    start_index = num_rows - 1
    column_sequence = list(range(num_columns)) + list(range(num_columns - 2, 0, -1))
    for i in range(num_rows):
        adjusted_index = (i - start_index) % (2 * num_columns - 2)
        target_column = column_sequence[adjusted_index]
        new_grid[i][target_column] = 1
    return new_grid


# Not correct code (32b) for gen 0:
def transform(grid):
    rows, cols = (len(grid), len(grid[0]))
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        col = (9 - i) % cols
        result[i][col] = 1
    return result