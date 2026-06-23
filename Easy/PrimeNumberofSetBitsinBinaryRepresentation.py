class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        result = 0

        for num in range(left, right + 1):
            count = bin(num).count('1')

            if count in primes:
                result += 1

        return result

sol = Solution()

print(sol.countPrimeSetBits(6, 10))
print(sol.countPrimeSetBits(10, 15))