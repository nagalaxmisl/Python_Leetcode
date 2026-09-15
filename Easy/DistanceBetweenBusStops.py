class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """

        total = sum(distance)

        if start < destination:
            clockwise = sum(distance[start:destination])

        else:
            clockwise = sum(distance[destination:start])

        counter_clockwise = total - clockwise

        return min(clockwise, counter_clockwise)

solution = Solution()

print(solution.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))
print(solution.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2))
print(solution.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))