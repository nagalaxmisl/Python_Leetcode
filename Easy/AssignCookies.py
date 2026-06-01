class Solution:

    def findContentChildren(self, g, s):

        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return cookie

sol = Solution()

print(sol.findContentChildren([1,2,3], [1,1]))
print(sol.findContentChildren([1,2], [1,2,3]))