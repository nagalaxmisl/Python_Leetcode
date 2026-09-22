class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])

        k = k % (m * n)

        flat = []

        for row in grid:
            for val in row:
                flat.append(val)

        flat = flat[-k:] + flat[:-k]

        result = []

        for i in range(m):
            result.append(flat[i * n:(i+1)*n])

        return result

solution = Solution()

print(solution.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(solution.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
print(solution.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))