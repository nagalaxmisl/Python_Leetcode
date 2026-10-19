class Solution(object):
    def reformat(self, s):
        letters = []
        digits = []

        # Separate letters and digits
        for char in s:
            if char.isalpha():
                letters.append(char)
            else:
                digits.append(char)

        # Check whether rearrangement is possible
        if abs(len(letters) - len(digits)) > 1:
            return ""

        result = []

        # Start with the group that has more characters
        if len(letters) > len(digits):
            first = letters
            second = digits
        else:
            first = digits
            second = letters

        # Alternate between the two groups
        for i in range(len(second)):
            result.append(first[i])
            result.append(second[i])

        # Add the remaining character, if any
        if len(first) > len(second):
            result.append(first[-1])

        return "".join(result)

solution = Solution()

print(solution.reformat("a0b1c2"))
print(solution.reformat("leetcode"))
print(solution.reformat("1229857369"))