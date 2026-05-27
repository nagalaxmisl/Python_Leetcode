class Solution:

    def canWinNim(self, n):

        return n % 4 != 0

sol = Solution()

print(sol.canWinNim(4))   # False
print(sol.canWinNim(1))   # True
print(sol.canWinNim(2))   # True
print(sol.canWinNim(8))   # False
print(sol.canWinNim(10))  # True