# Correct code (32b_gen1):
def transform(grid):
    output_size = 20
    output_grid = [[0] * output_size for _ in range(output_size)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                for x in range(max(0, i * 2 - 2), min(output_size, i * 2 + 2)):
                    for y in range(max(0, j * 2 - 2), min(output_size, j * 2 + 2)):
                        output_grid[x][y] = grid[i][j]
    return output_grid


# Not correct code (32b_gen0):
def transform(grid):
    n = len(grid)
    new_grid = [[0] * (n * 2) for _ in range(n * 2)]
    for i in range(n):
        for j in range(n):
            color = grid[i][j]
            if color != 0:
                new_grid[i * 2][j * 2] = color
    return new_grid