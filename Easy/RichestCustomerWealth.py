class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        row = len(accounts)
        col = len(accounts[0])

        richest = 0

        for i in range(row):
            total = sum(accounts[i])

            richest = max(richest, total)

        return richest

solution = Solution()

print(solution.maximumWealth([[1,2,3],[3,2,1]]))
print(solution.maximumWealth([[1,5],[7,3],[3,5]]))
print(solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))