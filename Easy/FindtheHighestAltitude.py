class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        altitude = 0
        highest = 0

        for num in gain:
            altitude += num

            highest = max(highest, altitude)

        return highest

solution = Solution()

print(solution.largestAltitude([-5,1,5,0,-7]))
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))