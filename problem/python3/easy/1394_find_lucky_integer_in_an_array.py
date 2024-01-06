#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#


# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        res = -1

        for n, c in count.items():
            if n == c:
                res = max(res, n)

        return res


# @lc code=end
