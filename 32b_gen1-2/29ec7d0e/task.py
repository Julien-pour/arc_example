# Correct code (32b_gen2):
def transform(grid):
    max_value = max((max(row) for row in grid))
    pattern = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                pattern.append((i, j, grid[i][j]))
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                new_grid[i][j] = grid[i][j]
            else:
                for pi, pj, val in pattern:
                    if pi % max_value == i % max_value and pj % max_value == j % max_value:
                        new_grid[i][j] = val
                        break
    return new_grid


# Not correct code (32b_gen1):
def transform(grid):
    transformed_grid = []
    patterns = []
    for row in grid:
        if 0 not in row:
            patterns.append(row)
    for row in grid:
        if 0 in row:
            best_pattern = min(patterns, key=lambda pattern: sum((abs(a - b) for a, b in zip(row, pattern) if a != 0)))
            transformed_grid.append(best_pattern)
        else:
            transformed_grid.append(row)
    return transformed_grid