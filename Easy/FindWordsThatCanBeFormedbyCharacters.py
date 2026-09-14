from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        char_count = Counter(chars)

        result = 0

        for word in words:

            word_count = Counter(word)

            good = True

            for char in word_count:

                if char not in char_count:
                    good = False
                    break

                if word_count[char] > char_count[char]:
                    good = False
                    break

            if good:
                result += len(word)

        return result

solution = Solution()

print(solution.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
print(solution.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))
