class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """

        spaces = text.count(" ")

        words = text.split()

        if len(words) == 1:
            return words[0] + " " * spaces

        spaces_for_gap = spaces // (len(words) -1)

        extra_spaces = spaces % (len(words) - 1)

        result = (" " * spaces_for_gap).join(words)

        result += " " * extra_spaces

        return result

solution = Solution()

print(solution.reorderSpaces("  this   is  a sentence "))
print(solution.reorderSpaces(" practice   makes   perfect"))