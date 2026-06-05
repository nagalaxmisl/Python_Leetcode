class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.islower() or word.isupper() or word.istitle()

sol = Solution()

print(sol.detectCapitalUse("USA"))
print(sol.detectCapitalUse("FlaG"))