class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """

        from datetime import datetime

        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        return abs((d1-d2).days)

sol = Solution()

print(sol.daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30"))

print(sol.daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31"))