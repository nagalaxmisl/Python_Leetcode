class Solution:

    def arrangeCoins(self, n):

        row = 1

        while n >= row:

            n = n-row
            row = row + 1

        return row -1

sol = Solution()

print(sol.arrangeCoins(5))
print(sol.arrangeCoins(8))