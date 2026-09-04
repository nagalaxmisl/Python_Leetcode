class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        result = []

        for num in arr:
            result.append(num)

            if num == 0:
                result.append(0)

        return result[:len(arr)]

sol = Solution()

print(sol.duplicateZeros([1,0,2,3,0,4,5,0]))
print(sol.duplicateZeros([1,2,3]))