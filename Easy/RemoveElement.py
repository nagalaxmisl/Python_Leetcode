class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1

        return i

    def main(self):
        print(self.removeElement(nums = [3,2,2,3], val = 3))
        print(self.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))

if __name__ == "__main__":
    sol = Solution()
    sol.main()