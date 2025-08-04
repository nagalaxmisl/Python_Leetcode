class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection_arr = set()

        for num in nums1:
            if num in nums2:
                intersection_arr.add(num)

        return list(intersection_arr)

    def main(self):
        print(self.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
        print(self.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
