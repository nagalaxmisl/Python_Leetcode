class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        total = sum(arr)

        target = total // 3

        if total % 3 != 0:
            return False

        current_sum = 0
        parts = 0

        for i in range(len(arr)):
            current_sum += arr[i]

            if current_sum == target:
                parts += 1
                current_sum = 0

                if parts == 2 and i < len(arr) - 1:
                    return True

        return parts == 3

sol = Solution()

print(sol.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(sol.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(sol.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))