from mypackage.Grids.Grid import Grid

matrix = Grid(3, 3)
for row in range(matrix.getHeight()):
    for column in range(matrix.getWidth()):
        matrix[row][column] = row * column
print(matrix)
grid = Grid(4, 5, 0)
print(grid)
# Assuming 'grid' is an instance of the Grid class

# Go through rows
for row in range(grid.getHeight()):
    # Go through columns
    for column in range(grid.getWidth()):
        # Set the value of the cell based on the row and column indices
        grid[row][column] = int(str(row) + str(column))
        print(grid)


