class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        left_zeros = 0
        right_ones = s.count('1')
        max_score = 0

        for i in range(len(s) - 1):

            if s[i] == '0':
                left_zeros += 1

            else:
                right_ones -= 1

            score = left_zeros + right_ones
            max_score = max(max_score, score)

        return max_score

solution = Solution()

print(solution.maxScore("011101"))
print(solution.maxScore("00111"))
print(solution.maxScore("1111"))