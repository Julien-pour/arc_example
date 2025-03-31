# Correct code (32b_gen1):
def transform(grid):

    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (grid[x][y] == 8)

    def flood_fill(x, y, block):
        if is_valid(x, y) and (x, y) not in block:
            block.append((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                flood_fill(x + dx, y + dy, block)
    blocks = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == 8:
                block = []
                flood_fill(i, j, block)
                blocks.append(block)
                visited.update(block)
    for block in blocks:
        min_x = min((x for x, y in block))
        max_x = max((x for x, y in block))
        min_y = min((y for x, y in block))
        max_y = max((y for x, y in block))
        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                if (i, j) not in block and 0 <= i < len(grid) and (0 <= j < len(grid[0])):
                    grid[i][j] = 2
    return grid


# Not correct code (32b_gen0):
def transform(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 1):
            if grid[i][j] == 8 and grid[i][j + 1] != 8:
                grid[i][j] = 2
    return grid