class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """

        total = 0
        deposit = 1
        monday = 1

        for day in range(n):
            total += deposit
            deposit += 1

            if (day + 1) % 7 == 0:
                monday += 1
                deposit = monday

        return total

solution = Solution()

print(solution.totalMoney(4))
print(solution.totalMoney(10))
print(solution.totalMoney(20))