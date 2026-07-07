
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """

        from collections import Counter
        license_count = Counter()

        for ch in licensePlate.lower():
            if ch.isalpha():
                license_count[ch] += 1

        answer = ""

        for word in words:
            word_count = Counter(word.lower())

            valid = True

            for ch in license_count:
                if word_count[ch] < license_count[ch]:
                    valid = False
                    break

            if valid:
                if answer == "" or len(word) < len(answer):
                    answer = word

        return answer


sol = Solution()

print(sol.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))
print(sol.shortestCompletingWord(licensePlate = "1s3 456", words = ["looks","pest","stew","show"]))