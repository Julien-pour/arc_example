# Correct code (7b):
def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    transformed_grid = [row[:] for row in grid]

    def find_nearest_non_zero(x, y, dx, dy):
        while 0 <= x < rows and 0 <= y < cols and (grid[x][y] == 0):
            x += dx
            y += dy
        if 0 <= x < rows and 0 <= y < cols:
            return grid[x][y]
        return None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 8:
                top = find_nearest_non_zero(i - 1, j, -1, 0)
                bottom = find_nearest_non_zero(i + 1, j, 1, 0)
                left = find_nearest_non_zero(i, j - 1, 0, -1)
                right = find_nearest_non_zero(i, j + 1, 0, 1)
                if top and top != 8:
                    transformed_grid[i][j] = top
                elif bottom and bottom != 8:
                    transformed_grid[i][j] = bottom
                elif left and left != 8:
                    transformed_grid[i][j] = left
                elif right and right != 8:
                    transformed_grid[i][j] = right
    return transformed_grid


# Not correct code (14b) for gen 4:
def transform(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0 and i > 0:
                grid[i][j] = grid[i - 1][j]
    return grid