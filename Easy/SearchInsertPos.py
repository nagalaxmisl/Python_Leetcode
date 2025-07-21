class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left


    def main(self):
        print(self.searchInsert(nums = [1,3,5,6], target = 5))
        print(self.searchInsert(nums = [1,3,5,6], target = 2))
        print(self.searchInsert(nums = [1,3,5,6], target = 7))

if __name__ == "__main__":
    sol = Solution()
    sol.main()