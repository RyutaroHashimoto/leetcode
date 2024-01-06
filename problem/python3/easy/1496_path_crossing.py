#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#


# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}

        for i in path:
            if i == "N":
                y += 1
            elif i == "S":
                y -= 1
            elif i == "E":
                x += 1
            elif i == "W":
                x -= 1

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False


# @lc code=end
