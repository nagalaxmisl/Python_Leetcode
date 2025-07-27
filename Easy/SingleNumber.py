class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        freq = Counter(nums)

        for i in range(len(nums)):
            if freq[nums[i]] == 1:
                num = nums[i]
        return num

    def main(self):
        print(self.singleNumber(nums = [2,2,1]))
        print(self.singleNumber(nums=[4,1,2,1,2]))
        print(self.singleNumber(nums=[1]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()

