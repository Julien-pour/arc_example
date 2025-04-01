# Correct code (14b):
def transform(grid):
    pos_3 = None
    pos_4 = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 3:
                pos_3 = (i, j)
            if grid[i][j] == 4:
                pos_4 = (i, j)
    if pos_3 and pos_4:
        i3, j3 = pos_3
        i4, j4 = pos_4
        grid[i3][j3] = 0
        new_i = i3 + (i4 - i3) // abs(i4 - i3) if i3 != i4 else i3
        new_j = j3 + (j4 - j3) // abs(j4 - j3) if j3 != j4 else j3
        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
            grid[new_i][new_j] = 3
    return grid


# Not correct code (32b):
def transform(grid):

    def move_to_center_if_possible(grid, number):
        middle_row = len(grid) // 2
        middle_col = len(grid[0]) // 2
        if grid[middle_row][middle_col] != 0:
            return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == number:
                    grid[middle_row][middle_col] = number
                    grid[i][j] = 0
                    return
    move_to_center_if_possible(grid, 3)
    move_to_center_if_possible(grid, 4)
    return grid