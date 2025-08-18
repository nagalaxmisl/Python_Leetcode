class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s + s)[1:-1]

    def main(self):
        print(self.repeatedSubstringPattern(s = "abab"))
        print(self.repeatedSubstringPattern(s = "aba"))
        print(self.repeatedSubstringPattern(s = "abcabcabcabc"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()