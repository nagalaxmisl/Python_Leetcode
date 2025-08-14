class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return seen[complement] + 1, i + 1

            else:
                seen[num] = i

    def main(self):
        print(self.twoSum(numbers = [2,7,11,15], target = 9))
        print(self.twoSum(numbers = [2,3,4], target = 6))
        print(self.twoSum(numbers = [-1,0], target = -1))

if __name__ == "__main__":
    sol = Solution()
    sol.main()