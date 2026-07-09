class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """

        words = sentence.split()

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        result = []

        for i, word in enumerate(words, start=1):

            if word[0] in vowels:
                new_word = word + 'ma'
            else:
                new_word = word[1:] + word[0] + "ma"

            new_word += "a" * i

            result.append(new_word)

        return " ".join(result)

sol = Solution()

print(sol.toGoatLatin(sentence = "I speak Goat Latin"))
print(sol.toGoatLatin(sentence = "The quick brown fox jumped over the lazy dog"))