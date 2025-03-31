# Correct code (32b_gen2):
def transform(grid):
    output_grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        row = grid[i]
        output_row = output_grid[i]
        for j in range(10, 14):
            output_row[j - 10] = row[j]
        for j in range(4):
            if row[j] != 0:
                output_row[j] = row[j]
            elif row[j + 5] != 0:
                output_row[j] = row[j + 5]
            else:
                output_row[j] = row[j + 10]
    return output_grid


# Not correct code (32b_gen1):
def transform(grid):
    output_grid = [[0] * 4 for _ in range(4)]
    positions = [(0, 5), (0, 1), (0, 0), (0, 3), (1, 0), (1, 1), (1, 7), (1, 8), (2, 0), (2, 10), (2, 11), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
    for i in range(4):
        for j in range(4):
            output_grid[i][j] = grid[positions[i * 4 + j][0]][positions[i * 4 + j][1]]
    return output_grid