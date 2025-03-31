# Correct code (14b):
def transform(grid):
    rows, cols = (len(grid), len(grid[0]))
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                left = grid[i][0]
                for k in range(cols):
                    if grid[i][k] != 0:
                        left = grid[i][k]
                        break
                right = grid[i][cols - 1]
                for k in range(cols - 1, -1, -1):
                    if grid[i][k] != 0:
                        right = grid[i][k]
                        break
                top = grid[0][j]
                for k in range(rows):
                    if grid[k][j] != 0:
                        top = grid[k][j]
                        break
                bottom = grid[rows - 1][j]
                for k in range(rows - 1, -1, -1):
                    if grid[k][j] != 0:
                        bottom = grid[k][j]
                        break
                if left == right:
                    for k in range(rows):
                        if grid[k][j] == left:
                            grid[k][j] = 0
                if top == bottom:
                    for k in range(cols):
                        if grid[i][k] == top:
                            grid[i][k] = 0
    return grid


# Not correct code (32b) for gen 4:
def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    for col in range(cols):
        zero_row = -1
        for row in range(rows):
            if grid[row][col] == 0:
                zero_row = row
                break
        if zero_row != -1:
            top_color = grid[zero_row - 1][col] if zero_row > 0 else None
            bottom_color = grid[zero_row + 1][col] if zero_row < rows - 1 else None
            for row in range(rows):
                if grid[row][col] == top_color or grid[row][col] == bottom_color:
                    grid[row][col] = 0
    return grid