class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter

        count = Counter(s)
        result = ""

        for char in t:
            if count[char] > 0:
                count[char] -= 1
            else:
                result = result + char

        return result

    def main(self):
        print(self.findTheDifference(s = "abcd", t = "abcde"))
        print(self.findTheDifference(s = "", t = "y"))
        print(self.findTheDifference(s="a", t="aaa"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()