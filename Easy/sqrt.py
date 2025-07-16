import math
class Solution:
    def mySqrt(self, x: int) -> int:
        result = math.sqrt(x)
        return int(result)

    def main(self):
        print(self.mySqrt(x=4))
        print(self.mySqrt(x=8))

if __name__ == "__main__":
    sol = Solution()
    sol.main()