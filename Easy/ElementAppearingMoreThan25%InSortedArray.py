class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 1

        if len(arr) == 1:
            return arr[0]

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1

            else:
                count = 1

            if count * 4 > len(arr):
                return arr[i]

sol = Solution()

print(sol.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))
print(sol.findSpecialInteger(arr = [1,1]))