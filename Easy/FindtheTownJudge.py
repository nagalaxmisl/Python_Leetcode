class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        trusts = [0] * (n + 1)
        trusted_by = [0] * (n + 1)

        for a, b in trust:
            trusts[a] += 1
            trusted_by[b] += 1

        for person in range(1, n + 1):
            if trusts[person] == 0 and trusted_by[person] == n - 1:
                return person

        return -1

sol = Solution()

print(sol.findJudge(n = 2, trust = [[1,2]]))
print(sol.findJudge(n = 3, trust = [[1,3],[2,3]]))
print(sol.findJudge(n = 3, trust = [[1,3],[2,3],[3,1]]))