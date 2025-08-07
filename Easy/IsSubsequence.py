class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1

            j += 1

        return i == len(s)

    def main(self):
        print(self.isSubsequence(s = "abc", t = "ahbgdc"))
        print(self.isSubsequence(s = "axc", t = "ahbgdc"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()


