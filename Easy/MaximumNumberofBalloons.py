from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        count = Counter(text)

        b = count.get('b',0)
        a = count.get('a',0)
        l = count.get('l',0) // 2
        o = count.get('o',0) // 2
        n = count.get('n',0)

        return min(b,a,l,o,n)

sol = Solution()

print(sol.maxNumberOfBalloons(text = "nlaebolko"))
print(sol.maxNumberOfBalloons(text = "loonbalxballpoon"))
print(sol.maxNumberOfBalloons(text = "leetcode"))
