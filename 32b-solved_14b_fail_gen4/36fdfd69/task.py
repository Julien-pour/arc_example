# Correct code (32b):
def transform(grid):

    def has_adjacent_2s_or_4s(x, y, grid):
        count = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (grid[nx][ny] in [2, 4]):
                count += 1
        return count > 1
    new_grid = [row[:] for row in grid]
    changed = True
    while changed:
        changed = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in [2, 4] and has_adjacent_2s_or_4s(i, j, grid):
                    new_grid[i][j] = 4
                    changed = True
        grid = [row[:] for row in new_grid]
    return new_grid


# Not correct code (14b) for gen 4:
def transform(grid):

    def transform_pixel(pixel, neighbors):
        if pixel == 0 or pixel == 2:
            return pixel
        count_2s = sum((1 for n in neighbors if n == 2))
        if count_2s >= 2:
            return 4
        return pixel
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            current_pixel = grid[i][j]
            neighbors = []
            if i > 0:
                neighbors.append(grid[i - 1][j])
            if i < rows - 1:
                neighbors.append(grid[i + 1][j])
            if j > 0:
                neighbors.append(grid[i][j - 1])
            if j < cols - 1:
                neighbors.append(grid[i][j + 1])
            new_grid[i][j] = transform_pixel(current_pixel, neighbors)
    return new_grid