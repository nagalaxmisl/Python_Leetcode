class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        balance = 0

        for char in s:
            balance += 1 if char == 'L' else -1

            if balance == 0:
                count += 1

        return count

solution = Solution()

print(solution.balancedStringSplit("RLRRLLRLRL"))
print(solution.balancedStringSplit("RLRRRLLRLL"))
print(solution.balancedStringSplit("LLLLRRRR"))