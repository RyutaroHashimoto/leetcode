#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
import collections


# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        max_freq = max(counts.values())
        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            buckets[i].append(c)

        res = []
        for i in range(len(buckets)):
            for j in buckets[max_freq - i]:
                res.append(j * (max_freq - i))

        return "".join(res)


# @lc code=end
s = "Aabb"
Solution().frequencySort(s)
