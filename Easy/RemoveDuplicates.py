class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i = i+1
                nums[i] = nums[j]

        return i+1

    def main(self):
        print(self.removeDuplicates(nums=[1, 1, 2]))
        print(self.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


if __name__ == "__main__":
    sol = Solution()
    sol.main()