# Correct code (32b):
def transform(grid):
    rows, cols = (len(grid), len(grid[0]))
    result = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                result[r][c] = 2

    def find_symmetric_position(r, c, red_positions):
        min_dist = float('inf')
        symmetric_pos = None
        for red_r, red_c in red_positions:
            dist = abs(r - red_r) + abs(c - red_c)
            if dist < min_dist:
                min_dist = dist
                symmetric_pos = (2 * red_r - r, 2 * red_c - c)
        return symmetric_pos
    red_positions = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 5:
                symmetric_pos = find_symmetric_position(r, c, red_positions)
                if symmetric_pos:
                    sym_r, sym_c = symmetric_pos
                    if 0 <= sym_r < rows and 0 <= sym_c < cols:
                        result[sym_r][sym_c] = 5
    return result


# Not correct code (14b) for gen 4:
def transform(grid):
    rows, cols = (len(grid), len(grid[0]))
    fives = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 5]
    for r, c in fives:
        grid[r][c] = 0
    for r, c in fives:
        if r + 1 < rows:
            grid[r + 1][c] = 5
        if r - 1 >= 0:
            grid[r - 1][c] = 5
    return grid