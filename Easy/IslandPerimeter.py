class Solution:

    def islandPerimeter(self, grid):

        perimeter = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                    perimeter += 4

                    if row > 0 and grid[row-1][col] == 1:
                        perimeter -= 2

                    if col > 0 and grid[row][col-1] == 1:
                        perimeter -= 2

        return perimeter

sol = Solution()

grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]

print(sol.islandPerimeter(grid))