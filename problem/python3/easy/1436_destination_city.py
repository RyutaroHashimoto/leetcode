#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

from typing import List


# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash_table = dict(paths)

        for i in hash_table.values():
            if i not in hash_table:
                return i


paths = [["B", "C"], ["D", "B"], ["C", "A"]]
Solution().destCity(paths)
