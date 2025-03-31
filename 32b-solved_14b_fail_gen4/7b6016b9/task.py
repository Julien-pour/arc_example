# Correct code (32b):
def transform(grid):

    def is_border(x, y):
        return x == 0 or x == len(grid) - 1 or y == 0 or (y == len(grid[0]) - 1)

    def flood_fill(x, y, marker):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if 0 <= cx < len(grid) and 0 <= cy < len(grid[0]) and (grid[cx][cy] == 0):
                grid[cx][cy] = marker
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    stack.append((cx + dx, cy + dy))
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                if is_border(x, y):
                    flood_fill(x, y, 3)
                else:
                    flood_fill(x, y, 2)
    return grid


# Not correct code (14b) for gen 4:
def transform(grid):

    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def find_neighbors(x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = (x + dx, y + dy)
            if is_valid(nx, ny) and grid[nx][ny] == 0:
                yield (nx, ny)

    def find_all_zeros():
        zeros = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zeros.add((i, j))
        return zeros

    def fill_area(x, y, color):
        stack = [(x, y)]
        visited = set()
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            grid[cx][cy] = color
            for nx, ny in find_neighbors(cx, cy):
                stack.append((nx, ny))
    fill_area(0, 0, 3)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                fill_area(i, j, 2)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                fill_area(i, j, 1)
    return grid