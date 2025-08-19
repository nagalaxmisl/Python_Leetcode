class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        if a == b:
            return -1

        return max(len(a), len(b))

    def main(self):
        print(self.findLUSlength(a = "aba", b = "cdc"))
        print(self.findLUSlength(a = "aaa", b = "bbb"))
        print(self.findLUSlength(a = "aaa", b = "aaa"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()