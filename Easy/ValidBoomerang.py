class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        (x1, y1), (x2, y2), (x3, y3) = points

        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)

sol = Solution()

print(sol.isBoomerang([[1,1],[2,3],[3,2]]))
print(sol.isBoomerang([[1,1],[2,2],[3,3]]))