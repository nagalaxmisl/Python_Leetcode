class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        result = []

        for i in range(len(matrix)):

            min_num = min(matrix[i])

            col = matrix[i].index(min_num)

            is_max = True

            for j in range(len(matrix)):
                if matrix[j][col] > min_num:
                    is_max = False
                    break

            if is_max:
                result.append(min_num)

        return result

sol = Solution()

print(sol.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
print(sol.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(sol.luckyNumbers([[7,8],[1,2]]))
