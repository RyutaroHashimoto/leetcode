#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#


# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = collections.Counter(arr)
        return len(set(counts.values())) == len(counts)


# @lc code=end
