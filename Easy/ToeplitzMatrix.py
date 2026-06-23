class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        rows = len(matrix)
        col = len(matrix[0])

        for r in range(1, rows):
            for c in range(1, col):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False

        return True

sol = Solution()

print(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(sol.isToeplitzMatrix([[1,2],[2,2]]))