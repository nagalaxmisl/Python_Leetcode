class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()

        min_diff = float('inf')

        result = []

        for i in range(len(arr)-1):

            diff = arr[i+1] - arr[i]

            if diff < min_diff:
                min_diff = diff
                result = [[arr[i],arr[i+1]]]

            elif diff == min_diff:

                result.append([arr[i],arr[i+1]])

        return result

solution = Solution()

print(solution.minimumAbsDifference([4,2,1,3]))
print(solution.minimumAbsDifference([1,3,6,10,15]))
print(solution.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))