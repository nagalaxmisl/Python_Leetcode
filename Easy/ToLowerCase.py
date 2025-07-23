class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.lower()

    def main(self):
        print(self.toLowerCase(s = "Hello"))
        print(self.toLowerCase(s = "here"))
        print(self.toLowerCase(s = "LOVELY"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()