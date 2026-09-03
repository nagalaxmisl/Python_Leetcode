class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        import math

        length = math.gcd(len(str1), len(str2))

        return str1[:length]

sol = Solution()

print(sol.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(sol.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(sol.gcdOfStrings(str1 = "LEET", str2 = "CODE"))
print(sol.gcdOfStrings(str1 = "AAAAAB", str2 = "AAA"))