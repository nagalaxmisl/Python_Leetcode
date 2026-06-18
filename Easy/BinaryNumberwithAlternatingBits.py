class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)[2:]

        for i in range(len(binary) - 1):
            if binary[i] == binary[i + 1]:
                return False

        return True

sol = Solution()
print(sol.hasAlternatingBits(4))
print(sol.hasAlternatingBits(5))
print(sol.hasAlternatingBits(7))
print(sol.hasAlternatingBits(11))