# Correct code (32b_gen3):
def transform(grid):
    output_grid = [[0 for _ in range(10)] for _ in range(10)]
    color_positions = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for i in range(10):
        for j in range(10):
            if grid[i][j] != 0 and grid[i][j] != 8:
                color_positions[grid[i][j]].append((i, j))
    positions_8 = []
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 8:
                positions_8.append((i, j))
    for color, positions in color_positions.items():
        for pos in positions:
            if positions_8:
                nearest_8 = min(positions_8, key=lambda x: abs(x[0] - pos[0]) + abs(x[1] - pos[1]))
                output_grid[nearest_8[0]][nearest_8[1]] = color
                positions_8.remove(nearest_8)
    return output_grid


# Not correct code (32b_gen2):
def transform(grid):
    output = [[0] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if grid[i][j] != 0:
                if i < 5:
                    row = 4
                else:
                    row = 5
                if j < 5:
                    col = 4
                else:
                    col = 5
                if grid[i][j] != 8:
                    while output[row][col] != 0:
                        if col == 5:
                            col = 4
                            row += 1
                        else:
                            col += 1
                    output[row][col] = grid[i][j]
    return output