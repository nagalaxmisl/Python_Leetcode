class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        total = sum(salary)
        minimum = min(salary)
        maximum = max(salary)

        average = float(total - minimum - maximum) / (len(salary) - 2)

        return round(average, 5)

solution = Solution()

print(solution.average([4000,3000,1000,2000]))
print(solution.average([1000,2000,3000]))