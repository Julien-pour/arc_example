# Correct code (32b_gen2):
def transform(grid):

    def fill_middle_with_2s_or_7s(grid, start_row, end_row, start_col, end_col, fill_value):
        for i in range(start_row + 1, end_row):
            for j in range(start_col + 1, end_col):
                grid[i][j] = fill_value
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                start_row = i
                while start_row > 0 and grid[start_row - 1][j] == 1:
                    start_row -= 1
                end_row = i
                while end_row < rows - 1 and grid[end_row + 1][j] == 1:
                    end_row += 1
                start_col = j
                while start_col > 0 and grid[i][start_col - 1] == 1:
                    start_col -= 1
                end_col = j
                while end_col < cols - 1 and grid[i][end_col + 1] == 1:
                    end_col += 1
                if end_row - start_row > 1 and end_col - start_col > 1:
                    fill_value = 7 if (end_row - start_row) % 2 == 0 and (end_col - start_col) % 2 == 0 else 2
                    fill_middle_with_2s_or_7s(grid, start_row, end_row, start_col, end_col, fill_value)
    return grid


# Not correct code (32b_gen1):
def transform(grid):

    def fill_gaps(cluster, fill_value):
        min_x = min((point[0] for point in cluster))
        max_x = max((point[0] for point in cluster))
        min_y = min((point[1] for point in cluster))
        max_y = max((point[1] for point in cluster))
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if grid[x][y] == 0:
                    grid[x][y] = fill_value
    visited = set()
    clusters = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visited:
                cluster = set()
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if (x, y) not in visited:
                        visited.add((x, y))
                        cluster.add((x, y))
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = (x + dx, y + dy)
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (grid[nx][ny] == 1):
                                stack.append((nx, ny))
                clusters.append(cluster)
    clusters.sort(key=lambda c: (-len(c), min(c)))
    fill_values = [7, 2]
    for i, cluster in enumerate(clusters):
        if len(cluster) > 1:
            fill_value = fill_values[i % len(fill_values)]
            fill_gaps(cluster, fill_value)
    return grid