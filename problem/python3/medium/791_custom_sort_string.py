#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#


# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = collections.Counter(s)
        res = ""

        for c in order:
            if c in counts:
                res += c * counts[c]
                del counts[c]

        for c, n in counts.items():
            res += c * n

        return res


# @lc code=end
order = "cbafg"
s = "abcd"
print(Solution().customSortString(order, s))
