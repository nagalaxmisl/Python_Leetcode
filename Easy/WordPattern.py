class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False

            else:
                char_to_word[c] = w

            if w in word_to_char:
                if word_to_char[w] != c:
                    return False

            else:
                word_to_char[w] = c

        return True

    def main(self):
        print(self.wordPattern(pattern = "abba", s = "dog cat cat dog"))
        print(self.wordPattern(pattern = "abba", s = "dog cat cat fish"))
        print(self.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()