class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words1 = s1.split()
        words2 = s2.split()

        from collections import Counter

        count = Counter(words1 + words2)

        result = []

        for word in count:
            if count[word] == 1:
                result.append(word)

        return result

sol = Solution()

print(sol.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
print(sol.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))