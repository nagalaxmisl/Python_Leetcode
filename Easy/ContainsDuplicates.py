class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter

        freq = Counter(nums)

        for i in range(len(nums)):
            if freq[nums[i]] > 1:
                return True

        return False

    def main(self):
        print(self.containsDuplicate( nums = [1,2,3,1]))
        print(self.containsDuplicate(nums=[1,2,3,4]))
        print(self.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()