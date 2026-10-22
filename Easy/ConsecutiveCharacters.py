class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """''

        maximum = 1
        count = 1

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                count += 1

            else:
                count = 1

            maximimum = max(maximum, count)

        return maximum

solution = Solution()

print(solution.maxPower("leetcode"))
print(solution.maxPower("abbcccddddeeeeedcba"))