class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = ''.join(char for char in s if char.isalnum())
        result_s = result.lower()

        if result_s == "":
            return True

        return result_s == result_s[::-1]


    def main(self):
        print(self.isPalindrome(s = "A man, a plan, a canal: Panama"))
        print(self.isPalindrome(s="race a car"))
        print(self.isPalindrome(s=" "))

if __name__ == "__main__":
    sol = Solution()
    sol.main()



