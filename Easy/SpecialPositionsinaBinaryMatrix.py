class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        rows = len(mat)
        col = len(mat[0])

        count = 0

        for i in range(rows):
            for j in range(col):

                if mat[i][j] == 1:

                    row_sum = sum(mat[i])

                    col_sum = 0

                    for k in range(rows):
                        col_sum += mat[k][j]

                    if row_sum == 1 and col_sum == 1:

                        count += 1

        return count

solution = Solution()

print(solution.numSpecial(mat = [[1,0,0],[0,0,1],[1,0,0]]))
print(solution.numSpecial(mat = [[1,0,0],[0,1,0],[0,0,1]]))