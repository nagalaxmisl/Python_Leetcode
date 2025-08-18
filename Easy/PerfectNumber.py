class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        total = 1
        i = 2

        while i*i <= num:
            if num % i == 0:
                total += i

                if i != num // i:
                    total += num // i

            i += 1

        return total == num

    def main(self):
        print(self.checkPerfectNumber(num = 28))
        print(self.checkPerfectNumber(num=7))

if __name__ == "__main__":
    sol = Solution()
    sol.main()