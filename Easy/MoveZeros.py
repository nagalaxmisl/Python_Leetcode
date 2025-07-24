class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

    def main(self):
        print(self.moveZeroes(nums = [0,1,0,3,12]))
        print(self.moveZeroes(nums = [0]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
