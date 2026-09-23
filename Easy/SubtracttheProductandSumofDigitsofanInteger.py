class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1
        total = 0

        while n > 0:
            digit = n % 10
            n = n // 10

            product *= digit
            total += digit

        return product - total

solution = Solution()

print(solution.subtractProductAndSum(234))
print(solution.subtractProductAndSum(4421))