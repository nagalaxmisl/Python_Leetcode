class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1

        return count

solution = Solution()

print(solution.busyStudent(startTime = [1,2,3], endTime = [3,4,7], queryTime = 4))
print(solution.busyStudent(startTime = [4], endTime = [4], queryTime = 4))