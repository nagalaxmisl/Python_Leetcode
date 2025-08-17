class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        freq = Counter(nums)
        max_freq = 0
        majority = None

        for num in freq:
            if freq[num] > max_freq:
                max_freq = freq[num]
                majority = num

        return majority

    def main(self):
        print(self.majorityElement(nums = [6,5,5]))
        print(self.majorityElement(nums = [2,2,1,1,1,2,2]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()

