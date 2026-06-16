class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev, curr = 0, 1
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1

            else:
                prev = curr
                curr = 1

            if prev >= curr:
                result += 1

        return result

sol = Solution()

print(sol.countBinarySubstrings("00110011"))
print(sol.countBinarySubstrings("10101"))