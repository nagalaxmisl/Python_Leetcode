class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        count = 0

        for row in grid:
            for num in row:
                if num < 0:
                    count += 1

        return count

sol = Solution()

print(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(sol.countNegatives([[3,2],[1,0]]))