class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        xy = 0
        yz = 0
        zx = 0

        for row in grid:
            yz += max(row)

            for value in row:
                if value > 0:
                    xy += 1

        for col in range(n):
            column_max = 0

            for row in range(n):
                column_max = max(column_max, grid[row][col])

            zx += column_max

        return xy + yz + zx

sol = Solution()

print(sol.projectionArea([[1,2],[3,4]]))
print(sol.projectionArea([[2]]))
print(sol.projectionArea([[1,0],[0,2]]))