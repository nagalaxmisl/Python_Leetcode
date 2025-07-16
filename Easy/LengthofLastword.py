class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        stripped = s.strip()
        reversed = stripped[::-1]
        temp = ""

        for i in range(len(reversed)):
            if reversed[i] == " ":
                break
            else:
                temp +=reversed[i]
        return len(temp)
        # arr = s.strip().split(" ")
        # return len(arr[len(arr)-1])


    def main(self):
        print(self.lengthOfLastWord(s="Hello World"))
        print(self.lengthOfLastWord(s="   fly me   to   the moon  "))
        print(self.lengthOfLastWord(s="luffy is still joyboy"))


if __name__ == "__main__":
    sol = Solution()
    sol.main()
