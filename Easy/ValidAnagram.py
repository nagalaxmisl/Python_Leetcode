class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def main(self):
        print(self.isAnagram(s = "anagram", t = "nagaram"))
        print(self.isAnagram(s = "rat", t = "car"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()