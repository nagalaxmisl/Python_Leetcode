class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums)):
            result.insert(index[i], nums[i])

        return result

sol = Solution()

print(sol.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))
print(sol.createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
print(sol.createTargetArray(nums = [1], index = [0]))