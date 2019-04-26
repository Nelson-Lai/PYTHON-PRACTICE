class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        edges = 0
        for row in range(0,rows):
            for column in range(0,columns):
                #top
                if grid[row][column] == 1:
                    if row == 0:
                        edges += 1
                    elif grid[row][column] != grid[row - 1][column]:
                        edges += 1

                #right
                if grid[row][column] == 1:
                    if column == columns-1:
                        edges += 1
                    elif grid[row][column] != grid[row][column+1]:
                        edges += 1

                #left
                if grid[row][column] == 1:
                    if column == 0:
                        edges += 1
                    elif grid[row][column] != grid[row][column-1]:
                        edges += 1

                # bottom
                if grid[row][column] == 1:
                    if row == rows-1:
                        edges += 1
                    elif grid[row][column] != grid[row+1][column]:
                        edges += 1
        return edges
