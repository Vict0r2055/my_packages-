from mypackage.Arrays.Array import Array


class Grid(object):
    """Represents a two-dimensional array."""
    def __init__(self, rows, columns, fillValue = None):
        self.data = Array(rows)
        for row in range (rows):
         self.data[row] = Array(columns, fillValue)
    def getHeight(self):
        """Returns the number of rows."""
        return len(self.data)
    def getWidth(self):
        "Returns the number of columns."""
        return len(self.data[0])
    def __getitem__(self, index):
        """Supports two-dimensional indexing
         with [row][column]."""
        return self.data[index]
    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self.data[row][col]) + " "
            result += "\n"  # Move this line outside of the inner loop
        return result

# Grid(3,3)   
# # matrix = Grid(3, 3)
# # print(matrix)
# my_grid = Grid(3, 3)
# print(my_grid)
