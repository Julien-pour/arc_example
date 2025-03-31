# Correct code (32b_gen4):
def transform(grid):
    from collections import defaultdict
    elements = {}
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val != 0:
                if val not in elements:
                    elements[val] = []
                elements[val].append((y, x))
    center_row = defaultdict(int)
    for val, positions in elements.items():
        min_y = min((y for y, x in positions))
        max_y = max((y for y, x in positions))
        center_row[val] = (min_y + max_y) // 2
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for val, center_y in center_row.items():
        for y, x in elements[val]:
            offset = y - center_y
            new_y = center_row[1] + offset
            if 0 <= new_y < len(grid):
                new_grid[new_y][x] = val
    return new_grid


# Not correct code (32b_gen3):
def transform(grid):
    from collections import defaultdict
    elements = defaultdict(list)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val != 0:
                elements[val].append((y, x))
    if not elements:
        return grid
    min_y = min((min((y for y, x in positions)) for positions in elements.values()))
    max_y = max((max((y for y, x in positions)) for positions in elements.values()))
    center_y = (min_y + max_y) // 2
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for val, positions in elements.items():
        offset = center_y - (min((y for y, x in positions)) + max((y for y, x in positions))) // 2
        for y, x in positions:
            new_y = y + offset
            if 0 <= new_y < len(grid):
                new_grid[new_y][x] = val
    return new_grid