class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        result = []
        current = 0

        for bit in nums:
            current = ((current * 2) + bit) % 5

            if current == 0:
                result.append(True)

            else:
                result.append(False)

        return result

sol = Solution()

print(sol.prefixesDivBy5([0,1,1]))
print(sol.prefixesDivBy5([1,1,1]))
print(sol.prefixesDivBy5([1,0,1]))