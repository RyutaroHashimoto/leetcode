#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)

        for c in text:
            count[c] += 1

        res = min(count["b"], count["a"], count["l"] // 2, count["o"] // 2, count["n"])

        return res


# @lc code=end
text = "leetcode"
Solution().maxNumberOfBalloons(text)
