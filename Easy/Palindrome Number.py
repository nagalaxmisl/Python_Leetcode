class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        else:
            return str(x) == str(x)[::-1]

    def main(self):
        print(self.isPalindrome(x=121))
        print(self.isPalindrome(x=-121))
        print(self.isPalindrome(x=10))

if __name__ == "__main__":
    sol = Solution()
    sol.main()