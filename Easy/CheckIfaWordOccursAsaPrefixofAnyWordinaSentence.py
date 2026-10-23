class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()

        for i in range(len(words)):

            if words[i].startswith(searchWord):
                return i+1

        return -1

solution = Solution()

print(solution.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))
print(solution.isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro"))
print(solution.isPrefixOfWord(sentence = "i am tired", searchWord = "you"))