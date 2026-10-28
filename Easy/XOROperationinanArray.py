class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

        result = 0

        for i in range(n):
            num = start + i * 2
            result = result ^ num

        return result

solution = Solution()

print(solution.xorOperation(n=5, start =0))
print(solution.xorOperation(n=4, start=3))