class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        max_right = arr[-1]

        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):

            current =arr[i]

            arr[i] = max_right

            if current > max_right:
                max_right = current

        return arr

sol = Solution()

print(sol.replaceElements(arr = [17,18,5,4,6,1]))
print(sol.replaceElements(arr = [400]))