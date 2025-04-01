# Correct code (14b):
def transform(grid):

    def transform_row(row):
        transformed = []
        for i in range(len(row)):
            if len(row) % 2 == 0 and i % 2 == 1 or (len(row) % 2 == 1 and i % 2 == 0):
                if row[i] == 5:
                    transformed.append(3)
                else:
                    transformed.append(row[i])
            else:
                transformed.append(row[i])
        return transformed
    return [transform_row(row) for row in grid]


# Not correct code (32b) for gen 0:
def transform(grid):
    transformed_grid = [[grid[i][j] if j % 2 == 0 or grid[i][j] != 5 else 3 for j in range(len(grid[i]))] for i in range(len(grid))]
    return transformed_grid