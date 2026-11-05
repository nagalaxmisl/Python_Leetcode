class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]

            if i != n-1-i:
                total += mat[i][n-1-i]

        return total

solution = Solution()

print(solution.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.diagonalSum([[5]]))
print(solution.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))