class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return seen[complement], i
            else:
                seen[num] = i

    def main(self):
        print(self.twoSum(nums = [2,7,11,15], target = 9))
        print(self.twoSum(nums = [3,2,4], target = 6))
        print(self.twoSum(nums = [3,3], target = 6))

if __name__ == "__main__":
    sol = Solution()
    sol.main()



