class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 100:
            return str(n)

        count = 0
        result = ""
        num = str(n)

        for i in range(len(num)-1, -1, -1):

            result += num[i]
            count += 1

            if count == 3 and i != 0:
                result += "."
                count = 0

        return result[::-1]

solution = Solution()

print(solution.thousandSeparator(n=987))
print(solution.thousandSeparator(n = 1234))