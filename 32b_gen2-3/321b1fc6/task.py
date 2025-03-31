# Correct code (32b_gen3):
def transform(grid):
    rows, cols = (len(grid), len(grid[0]))
    result = [[0] * cols for _ in range(rows)]
    positions_of_8 = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 8]
    for r, c in positions_of_8:
        top = r
        while top > 0 and grid[top - 1][c] == 8:
            top -= 1
        left = c
        while left > 0 and grid[r][left - 1] == 8:
            left -= 1
        block_height = 0
        for i in range(top, rows):
            if grid[i][left] != 8:
                break
            block_height += 1
        block_width = 0
        for j in range(left, cols):
            if grid[top][j] != 8:
                break
            block_width += 1
        found_pattern = False
        for i in range(rows):
            for j in range(cols - block_width + 1):
                if all((grid[pi][pj] != 0 and grid[pi][pj] != 8 for pi in range(i, i + block_height) for pj in range(j, j + block_width))):
                    pattern = [row[j:j + block_width] for row in grid[i:i + block_height]]
                    for pi in range(block_height):
                        for pj in range(block_width):
                            result[top + pi][left + pj] = pattern[pi][pj]
                    found_pattern = True
                    break
            if found_pattern:
                break
    return result


# Not correct code (32b_gen2):
def transform(grid):
    new_grid = [[0 for _ in range(10)] for _ in range(10)]
    pattern = [[7, 6], [9, 4]]
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 8:
                if i + 1 < 10 and j + 1 < 10 and (grid[i][j + 1] == 8) and (grid[i + 1][j] == 8) and (grid[i + 1][j + 1] == 8):
                    for x in range(2):
                        for y in range(2):
                            new_grid[i + x][j + y] = pattern[x][y]
    return new_grid