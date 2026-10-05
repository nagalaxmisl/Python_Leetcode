class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 1

        else:
            return 2

sol = Solution()

print(sol.removePalindromeSub('ababa'))
print(sol.removePalindromeSub('abb'))
print(sol.removePalindromeSub('baabb'))