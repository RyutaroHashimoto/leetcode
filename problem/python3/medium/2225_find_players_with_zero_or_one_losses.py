#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser = defaultdict(int)
        answer = [[], []]

        for i, j in matches:
            loser[i] += 0
            loser[j] += 1

        for i, j in loser.items():
            if j == 0:
                answer[0].append(i)
            elif j == 1:
                answer[1].append(i)

        answer[0].sort()
        answer[1].sort()
        return answer


# @lc code=end

matches = [
    [1, 3],
    [2, 3],
    [3, 6],
    [5, 6],
    [5, 7],
    [4, 5],
    [4, 8],
    [4, 9],
    [10, 4],
    [10, 9],
]
print(Solution().findWinners(matches))
