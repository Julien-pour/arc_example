# Correct code (32b_gen4):
def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [row[:] for row in grid]
    start_row, start_col = (-1, -1)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                start_row, start_col = (r, c)
                break
        if start_row != -1:
            break
    if start_row == -1:
        return result
    if grid[start_row][start_col] == 2:
        for i in range(start_col + 3, cols):
            result[start_row + 2][i] = 1
    elif grid[start_row][start_col] == 8:
        for i in range(start_row - 1, -1, -1):
            result[i][start_col] = 3
    elif grid[start_row][start_col] == 3:
        for i in range(start_row + 3, rows):
            result[i][start_col + 2] = 2
    elif grid[start_row][start_col] == 4:
        for i in range(start_row - 1, -1, -1):
            result[i][start_col] = 8
    return result


# Not correct code (32b_gen3):
def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [row[:] for row in grid]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                for i in range(c + 1, cols):
                    if grid[r][i] == 0:
                        result[r][i] = 1
            elif grid[r][c] == 3:
                for i in range(r):
                    if grid[i][c] == 0:
                        result[i][c] = 3
            elif grid[r][c] == 2:
                if c == cols // 2:
                    for i in range(r + 1, rows):
                        if grid[i][c] == 0:
                            result[i][c] = 2
    return result