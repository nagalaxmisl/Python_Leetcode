class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter

        mag_count = Counter(magazine)

        for char in ransomNote:
            if mag_count[char] == 0:
                return False
            mag_count[char] -= 1

        return True

    def main(self):
        print(self.canConstruct(ransomNote = "a", magazine = "b"))
        print(self.canConstruct(ransomNote = "aa", magazine = "ab"))
        print(self.canConstruct(ransomNote = "aa", magazine = "aab"))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
