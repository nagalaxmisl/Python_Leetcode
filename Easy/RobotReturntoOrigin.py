class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('D') == moves.count('U') and moves.count('L') == moves.count('R')

sol = Solution()

print(sol.judgeCircle("UD"))
print(sol.judgeCircle("LL"))