class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 2 == 0

sol = Solution()
print(sol.divisorGame(4))
print(sol.divisorGame(3))
print(sol.divisorGame(5))
print(sol.divisorGame(2))