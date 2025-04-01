# Correct code (32b_gen2):
def transform(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [row[:] for row in grid]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def fill_area(x, y, color):
        stack = [(x, y)]
        visited = set()
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) not in visited and is_valid(cx, cy) and (result[cx][cy] == 0):
                result[cx][cy] = color
                visited.add((cx, cy))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    stack.append((cx + dx, cy + dy))
    fill_area(0, 0, 1)
    fill_area(rows // 2, cols // 2, 2)
    fill_area(rows - 1, cols - 1, 3)
    return result


# Not correct code (32b_gen1):
def transform(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                if i < 3 and j < 3:
                    grid[i][j] = 1
                elif i > 6 and j > 6:
                    grid[i][j] = 3
                elif 3 <= i <= 6 and 3 <= j <= 6:
                    grid[i][j] = 2
    return grid