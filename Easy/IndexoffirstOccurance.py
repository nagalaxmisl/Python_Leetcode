class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return -1

        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1

    def main(self):
        print(self.strStr(haystack = "sadbutsad", needle = "sad"))
        print(self.strStr(haystack = "leetcode", needle = "leeto"))


if __name__ == "__main__":
    sol = Solution()
    sol.main()
