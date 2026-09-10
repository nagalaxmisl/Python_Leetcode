class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        a = 0
        b = 1
        c = 1

        for i in range(3, n+1):
            next_num = a + b + c
            a = b
            b = c
            c = next_num

        return c

solution = Solution()

print(solution.tribonacci(3))
print(solution.tribonacci(4))