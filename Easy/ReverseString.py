class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s

    def main(self):
        print(self.reverseString(s = ["h","e","l","l","o"]))
        print(self.reverseString(s = ["H","a","n","n","a","h"]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()