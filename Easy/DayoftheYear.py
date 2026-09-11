class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """

        year, month, day = map(int, date.split('-'))

        days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days_of_month[1] = 29

        result = sum(days_of_month[:month-1])

        result += day

        return result

solution = Solution()

print(solution.dayOfYear("2019-01-09"))
print(solution.dayOfYear("2019-02-10"))