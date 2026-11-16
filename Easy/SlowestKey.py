class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """

        max_duration = releaseTimes[0]
        slow_key = keysPressed[0]

        for i in range(1, len(releaseTimes)):

            duration = releaseTimes[i] - releaseTimes[i-1]

            if duration > max_duration:
                max_duration = duration
                slow_key = keysPressed[i]

            elif duration == max_duration:
                if keysPressed[i] > slow_key:
                    slow_key = keysPressed[i]

        return slow_key

solution = Solution()

print(solution.slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd"))
print(solution.slowestKey(releaseTimes = [12,23,36,46,62], keysPressed = "spuda"))