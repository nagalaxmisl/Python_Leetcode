class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        sorted_score = sorted(score, reverse=True)

        rank_map = {}

        for i in range(len(sorted_score)):
            current_score = sorted_score[i]
            rank = i + 1

            if rank == 1:
                rank_map[current_score] = "Gold Medal"

            elif rank == 2:
                rank_map[current_score] = "Silver Medal"

            elif rank == 3:
                rank_map[current_score] = "Bronze Medal"

            else:
                rank_map[current_score] = str(rank)

        result = []

        for s in score:
            result.append(rank_map[s])

        return result

if __name__ == "__main__":
    sol = Solution()

    score1 = [5, 4, 3, 2, 1]
    print(sol.findRelativeRanks(score1))

    score2 = [10, 3, 8, 9, 4]
    print(sol.findRelativeRanks(score2))
