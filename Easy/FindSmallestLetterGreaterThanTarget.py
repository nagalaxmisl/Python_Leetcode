class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for char in letters:
            if char > target:
                return char

        return letters[0]

sol = Solution()
print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "c"))
print(sol.nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))