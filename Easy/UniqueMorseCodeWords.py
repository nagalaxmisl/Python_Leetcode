class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        return len({''.join(morse[ord(c) - ord('a')] for c in word) for word in words})

sol = Solution()

print(sol.uniqueMorseRepresentations(["gin","zen","gig","msg"]))
print(sol.uniqueMorseRepresentations(["a"]))