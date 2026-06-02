class Solution(object):

    def constructRectangle(self, area):

        w = int(area ** 0.5)

        while area % w != 0:

            w -= 1

        l = area // w

        return [l,w]

sol = Solution()

print(sol.constructRectangle(4))
print(sol.constructRectangle(37))
print(sol.constructRectangle(122122))