# Correct code (32b_gen3):
def transform(grid):
    n = len(grid)
    m = len(grid[0])
    top = n
    bottom = -1
    left = m
    right = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                top = min(top, i)
                bottom = max(bottom, i)
                left = min(left, j)
                right = max(right, j)
    inner_elements = {}
    for i in range(top + 1, bottom):
        for j in range(left + 1, right):
            if grid[i][j] != 0:
                inner_elements[i, j] = grid[i][j]
                grid[i][j] = 0
    if inner_elements:
        grid[top - 1][left - 1] = inner_elements.get((bottom - 1, right - 1), 0)
        grid[top - 1][right + 1] = inner_elements.get((bottom - 1, left + 1), 0)
        grid[bottom + 1][left - 1] = inner_elements.get((top + 1, right - 1), 0)
        grid[bottom + 1][right + 1] = inner_elements.get((top + 1, left + 1), 0)
    return grid


# Not correct code (32b_gen2):
def transform(grid):
    n = len(grid)
    min_row, max_row, min_col, max_col = (n, -1, n, -1)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)
    new_grid = [[0] * n for _ in range(n)]
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            new_grid[i][j] = grid[i][j]
    elements = []
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if grid[i][j] != 0 and grid[i][j] != 8 and (grid[i][j] != 7) and (grid[i][j] != 1):
                elements.append((i, j, grid[i][j]))
    elements.sort(key=lambda x: (x[0], x[1]))
    if len(elements) >= 2:
        top_left = elements[0]
        bottom_right = elements[-1]
        new_grid[min_row - 1][min_col - 1] = bottom_right[2]
        new_grid[max_row + 1][max_col + 1] = top_left[2]
    if len(elements) >= 4:
        top_right = elements[1]
        bottom_left = elements[-2]
        new_grid[min_row - 1][max_col + 1] = bottom_left[2]
        new_grid[max_row + 1][min_col - 1] = top_right[2]
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if new_grid[i][j] != 0 and new_grid[i][j] != 8 and (new_grid[i][j] != 7) and (new_grid[i][j] != 1):
                new_grid[i][j] = 0
    if len(elements) >= 2:
        new_grid[min_row - 1][min_col - 1] = bottom_right[2]
        new_grid[max_row + 1][max_col + 1] = top_left[2]
    if len(elements) >= 4:
        new_grid[min_row - 1][max_col + 1] = bottom_left[2]
        new_grid[max_row + 1][min_col - 1] = top_right[2]
    return new_grid