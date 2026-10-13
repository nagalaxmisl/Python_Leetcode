class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter

        count = Counter(s)

        result = []

        while len(result) < len(s):

            for ch in "abcdefghijklmnopqrstuvwxyz":
                if count[ch] > 0:
                    result.append(ch)
                    count[ch] -= 1

            for ch in "zyxwvutsrqponmlkjihgfedcba":
                if count[ch] > 0:
                    result.append(ch)
                    count[ch] -= 1

        return "".join(result)

sol = Solution()

print(sol.sortString("aaaabbbbcccc"))
print(sol.sortString("rat"))