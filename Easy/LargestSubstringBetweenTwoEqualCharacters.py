class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """

        largest = -1

        first_index = {}

        for i in range(len(s)):

            ch = s[i]

            if ch in first_index:
                length = i - first_index[ch] - 1
                largest = max(largest, length)

            else:
                first_index[ch] = i

        return largest

solution = Solution()

print(solution.maxLengthBetweenEqualCharacters("aa"))
print(solution.maxLengthBetweenEqualCharacters("abca"))
print(solution.maxLengthBetweenEqualCharacters("xyza"))