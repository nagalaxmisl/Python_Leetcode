class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """

        mid = len(s)//2

        a = s[:mid]
        b = s[mid:]

        count_a = 0
        count_b = 0

        vowels = set("aeiouAEIOU")

        for ch in a:
            if ch in vowels:
                count_a += 1

        for ch in b:
            if ch in vowels:
                count_b += 1

        return count_a == count_b

solution = Solution()

print(solution.halvesAreAlike("book"))
print(solution.halvesAreAlike("textbook"))