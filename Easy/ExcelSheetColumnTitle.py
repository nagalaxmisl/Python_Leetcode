class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""

        while columnNumber > 0:
            columnNumber -= 1

            remainder = columnNumber % 26

            character = chr(ord('A') + remainder)

            result = character + result

            columnNumber = columnNumber // 26

        return result

solution = Solution()

print(solution.convertToTitle(1)) 
print(solution.convertToTitle(28))
print(solution.convertToTitle(701))