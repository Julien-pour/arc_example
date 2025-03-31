# Correct code (14b):
import numpy as np
from collections import Counter

def transform(grid):
    grid = np.array(grid)
    flat_grid = grid.flatten()
    count = Counter(flat_grid)
    unique_values = np.unique(grid)
    sorted_values = sorted(unique_values, key=lambda x: (-count[x], x))
    if len(sorted_values) < 3:
        return grid.tolist()
    largest_value = sorted_values[0]
    second_largest_value = sorted_values[1]
    third_largest_value = sorted_values[2]
    transformation_dict = {largest_value: third_largest_value, second_largest_value: largest_value, third_largest_value: second_largest_value}
    transformed_grid = np.vectorize(lambda x: transformation_dict.get(x, x))(grid)
    return transformed_grid.tolist()




# Not correct code (32b) for gen 0:
def transform(grid):
    n = len(grid)
    outer_layer_value = grid[n // 2][n // 2]
    inner_border_value = grid[0][0]
    innermost_value = grid[1][1]
    transformed_grid = [[outer_layer_value] * n for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            transformed_grid[i][j] = inner_border_value
    if n > 3:
        for i in range(2, n - 2):
            for j in range(2, n - 2):
                transformed_grid[i][j] = innermost_value
    return transformed_grid
import numpy as np