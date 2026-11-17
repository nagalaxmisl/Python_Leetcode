class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """

        str1 = "".join(word1)
        str2 = "".join(word2)

        return str1 == str2

solution = Solution()

print(solution.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
print(solution.arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
print(solution.arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]))