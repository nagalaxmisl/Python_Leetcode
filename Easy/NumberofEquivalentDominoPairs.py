class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """

        count = {}

        result = 0

        for domino in dominoes:

            key = tuple(sorted(domino))

            result += count.get(key, 0)

            count[key] = count .get(key, 0) + 1

        return result

sol = Solution()

print(sol.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
print(sol.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))