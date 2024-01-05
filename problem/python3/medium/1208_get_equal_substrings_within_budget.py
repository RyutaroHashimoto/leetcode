#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#


# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        res = 0
        cost = 0

        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost and left < right:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            if cost <= maxCost:
                res = max(res, right - left + 1)

        return res


# @lc code=end

s = "abcd"
t = "cdef"
maxCost = 1
print(Solution().equalSubstring(s, t, maxCost))
