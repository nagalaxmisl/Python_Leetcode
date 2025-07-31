class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True

    def main(self):
        print(self.isAnagram(s = "anagram", t = "nagaram"))
        print(self.isAnagram(s = "rat", t = "car"))
        print(self.isAnagram(s="rat", t="arr"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()