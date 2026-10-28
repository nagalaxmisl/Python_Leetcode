class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        sorted_arr = sorted(arr)

        prev_diff = sorted_arr[1] - sorted_arr[0]

        for i in range(1, len(arr)-1):
            diff  = sorted_arr[i+1] - sorted_arr[i]

            if diff != prev_diff:
                return False

        return True

solution = Solution()

print(solution.canMakeArithmeticProgression([3,5,1]))
print(solution.canMakeArithmeticProgression([1,2,4]))