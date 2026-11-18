class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """

        count = 0
        repeated = word

        while repeated in sequence:
            count += 1
            repeated += word

        return repeated

solution = Solution()

print(solution.maxRepeating(sequence = "ababc", word = "ab"))
print(solution.maxRepeating(sequence = "ababc", word = "ba"))
print(solution.maxRepeating(sequence = "ababc", word = "ac"))