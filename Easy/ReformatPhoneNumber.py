class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """

        digits = number.replace(" ", "").replace("-", "")

        results = []

        while len(digits) > 4:
            results.append(digits[:3])
            digits = digits[3:]

        if len(digits) == 4:
            results.append(digits[:2])
            results.append(digits[2:])

        else:
            results.append(digits)

        return "-".join(results)

solution = Solution()

print(solution.reformatNumber("1-23-45 6"))
print(solution.reformatNumber("123 4-567"))
print(solution.reformatNumber("123 4-5678"))