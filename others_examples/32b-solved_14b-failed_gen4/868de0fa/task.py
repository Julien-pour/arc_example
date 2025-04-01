# Correct code (32b):
def transform(grid):

    def fill_middle_with_color(grid, start_row, end_row, start_col, end_col, color):
        for i in range(start_row + 1, end_row):
            for j in range(start_col + 1, end_col):
                grid[i][j] = color
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                start_row, end_row = (i, i)
                start_col, end_col = (j, j)
                while end_row + 1 < rows and grid[end_row + 1][j] == 1:
                    end_row += 1
                while end_col + 1 < cols and grid[i][end_col + 1] == 1:
                    end_col += 1
                if end_row - start_row > 1 and end_col - start_col > 1:
                    fill_color = 7 if (end_row - start_row) % 2 == 0 else 2
                    fill_middle_with_color(grid, start_row, end_row, start_col, end_col, fill_color)
    return grid


# Not correct code (14b) for gen 4:
def transform(grid):

    def replace_sequence(row, start, end, new_value):
        for i in range(start + 1, end):
            row[i] = new_value
    for i, row in enumerate(grid):
        start = None
        for j, cell in enumerate(row):
            if cell == 1:
                if start is not None:
                    replace_sequence(row, start, j, 7 if i < len(grid) // 2 else 2)
                start = j
    return grid