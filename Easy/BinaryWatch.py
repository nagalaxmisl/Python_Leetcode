class Solution:

    def readBinaryWatch(self, turnedOn):

        result = []

        for hour in range(12):

            for minute in range(60):

                ones = bin(hour).count('1') + bin(minute).count('1')

                if ones == turnedOn:

                    result.append(f"{hour}:{minute:02d}")

        return result


# Driver code
sol = Solution()

print(sol.readBinaryWatch(1))