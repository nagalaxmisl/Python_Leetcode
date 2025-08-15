class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last = {}

        for i, num in enumerate(nums):
            if num in last and i - last[num] <= k:
                return True
            else:
                last[num] = i

        return False

    def main(self):
        print(self.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
        print(self.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
        print(self.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))

if __name__ == "__main__":
    sol = Solution()
    sol.main()