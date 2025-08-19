class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)

        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])

        return ''.join(s)

    def main(self):
        print(self.reverseStr(s = "abcdefg", k = 2))
        print(self.reverseStr(s = "abcd", k = 2))

if __name__ == "__main__":
    sol = Solution()
    sol.main()