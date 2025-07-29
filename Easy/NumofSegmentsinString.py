class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        for i in range(len(s)):
            if (s[i] != ' ') and (i == 0 or s[i-1] == ' '):
                count += 1

        return count

        # if s == "":
        #     return 0
        #
        # count = 0
        #
        # for i in range(len(s)):
        #     if s[i] == " ":
        #         count += 1
        #
        # return count + 1

    def main(self):
        print(self.countSegments(s = "Hello, my name is John"))
        print(self.countSegments(s = "Hello"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
