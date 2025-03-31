# Correct code (32b_gen4):
def transform(grid):

    def find_innermost_pattern(grid):
        rows, cols = (len(grid), len(grid[0]))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    top, bottom, left, right = (i, i, j, j)
                    while top > 0 and grid[top - 1][j] != 0:
                        top -= 1
                    while bottom < rows - 1 and grid[bottom + 1][j] != 0:
                        bottom += 1
                    while left > 0 and grid[i][left - 1] != 0:
                        left -= 1
                    while right < cols - 1 and grid[i][right + 1] != 0:
                        right += 1
                    return (top, bottom, left, right)
        return (0, 0, 0, 0)

    def fill_outer_diagonals(grid, top, bottom, left, right, value):
        i, j = (top - 1, left - 1)
        while i >= 0 and j >= 0:
            grid[i][j] = value
            i -= 1
            j -= 1
        i, j = (top - 1, right + 1)
        while i >= 0 and j < len(grid[0]):
            grid[i][j] = value
            i -= 1
            j += 1
        i, j = (bottom + 1, left - 1)
        while i < len(grid) and j >= 0:
            grid[i][j] = value
            i += 1
            j -= 1
        i, j = (bottom + 1, right + 1)
        while i < len(grid) and j < len(grid[0]):
            grid[i][j] = value
            i += 1
            j += 1
    top, bottom, left, right = find_innermost_pattern(grid)
    if top == 0 and bottom == 0 and (left == 0) and (right == 0):
        return grid
    innermost_values = set()
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] != 0:
                innermost_values.add(grid[i][j])
    if len(innermost_values) < 2:
        return grid
    from collections import Counter
    value_counts = Counter()
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] != 0:
                value_counts[grid[i][j]] += 1
    most_common_values = value_counts.most_common(2)
    fill_value = most_common_values[1][0] if len(most_common_values) > 1 else most_common_values[0][0]
    fill_outer_diagonals(grid, top, bottom, left, right, fill_value)
    return grid


# Not correct code (32b_gen3):
def transform(grid):

    def fill_outer_diagonals(grid, target_value, fill_value):
        n = len(grid)
        m = len(grid[0])
        top_row = next((i for i in range(n) if target_value in grid[i]), None)
        bottom_row = next((i for i in range(n - 1, -1, -1) if target_value in grid[i]), None)
        if top_row is None or bottom_row is None:
            return
        top_col = grid[top_row].index(target_value)
        bottom_col = grid[bottom_row].index(target_value)
        right_col = next((j for j in range(m - 1, -1, -1) if grid[top_row][j] == target_value), None)
        left_col = next((j for j in range(m) if grid[top_row][j] == target_value), None)
        if right_col is None or left_col is None:
            return
        for i in range(top_row):
            j = left_col - (top_row - i)
            if 0 <= j < m and grid[i][j] == 0:
                grid[i][j] = fill_value
            j = right_col + (top_row - i)
            if 0 <= j < m and grid[i][j] == 0:
                grid[i][j] = fill_value
        for i in range(bottom_row + 1, n):
            j = left_col - (i - bottom_row)
            if 0 <= j < m and grid[i][j] == 0:
                grid[i][j] = fill_value
            j = right_col + (i - bottom_row)
            if 0 <= j < m and grid[i][j] == 0:
                grid[i][j] = fill_value
    target_to_fill = {2: 4, 6: 1, 8: 3}
    for target_value, fill_value in target_to_fill.items():
        fill_outer_diagonals(grid, target_value, fill_value)
    return grid