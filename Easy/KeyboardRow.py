class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        result = []

        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        for word in words:
            w = word.lower()

            if all(ch in row1 for ch in w):
                result.append(word)

            elif all(ch in row2 for ch in w):
                result.append(word)

            elif all(ch in row3 for ch in w):
                result.append(word)

        return result

sol = Solution()

words = ["Hello", "Alaska", "Dad", "Peace"]

answer = sol.findWords(words)

print(answer)