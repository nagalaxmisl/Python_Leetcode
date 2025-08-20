class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(word[::-1] for word in s.split(" "))

    def main(self):
        print(self.reverseWords(s = "Let's take LeetCode contest"))
        print(self.reverseWords(s = "Mr Ding"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
