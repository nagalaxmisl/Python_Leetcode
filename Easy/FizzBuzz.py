class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")

            elif i % 3 == 0:
                result.append("Fizz")

            elif i % 5 == 0:
                result.append("Buzz")

            else:
                result.append(str(i))

        return result

    def main(self):
        print(self.fizzBuzz(n=3))
        print(self.fizzBuzz(n=5))
        print(self.fizzBuzz(n=15))

if __name__ == "__main__":
    sol = Solution()
    sol.main()