class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                h = grid[i][j]

                if h > 0:
                    # Top + Bottom + Four sides
                    area += 2 + 4 * h

                    # Shared faces with the cell below
                    if i + 1 < n:
                        area -= 2 * min(h, grid[i + 1][j])

                    # Shared faces with the cell to the right
                    if j + 1 < n:
                        area -= 2 * min(h, grid[i][j + 1])

        return area

sol = Solution()
print(sol.surfaceArea([[1,2],[3,4]]))
print(sol.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
print(sol.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))