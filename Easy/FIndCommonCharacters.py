class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        from collections import Counter

        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        return list(common.elements())

sol = Solution()

print(sol.commonChars(["bella","label","roller"]))
print(sol.commonChars(["cool","lock","cook"]))
