class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0

        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2

            else:
                i += 1

        return i == len(bits) - 1

sol = Solution()
print(sol.isOneBitCharacter([1,0,0]))
print(sol.isOneBitCharacter([1,1,1,0]))