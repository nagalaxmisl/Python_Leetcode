class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n % 2 == 1:
            return "a" * n

        else:
            return "a" * (n-1) + "b"

sol = Solution()

print(sol.generateTheString(4))
print(sol.generateTheString(2))
print(sol.generateTheString(7))