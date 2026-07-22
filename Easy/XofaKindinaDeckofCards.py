class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter
        from math import gcd

        count = Counter(deck)

        g = 0

        for freq in count.values():
            g = gcd(g, freq)

        return g >= 2

sol = Solution()

print(sol.hasGroupsSizeX([1,2,3,4,4,3,2,1]))
print(sol.hasGroupsSizeX([1,1,1,2,2,2,3,3]))