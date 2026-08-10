class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        i = len(num) - 1

        while i >= 0 or k > 0:

            if i >= 0:
                k += num[i]
                num[i] = k % 10
                k = k // 10
                i -= 1
            else:
                num.insert(0, k % 10)
                k = k // 10

        return num

sol = Solution()

print(sol.addToArrayForm(num = [1,2,0,0], k = 34))
print(sol.addToArrayForm(num = [2,7,4], k = 181))
print(sol.addToArrayForm(num = [2,1,5], k = 806))