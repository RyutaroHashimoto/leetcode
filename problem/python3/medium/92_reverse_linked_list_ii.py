#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

from typing import Optional


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # Empty list
        if not head:
            return None

        # set left pointer
        pre = None
        curr = head
        for i in range(left - 1):
            pre = curr
            curr = curr.next

        original_left_pointer = curr
        before_left = pre

        # reverse to right
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        # Adjust
        if before_left:
            before_left.next = pre
        else:
            head = pre
        original_left_pointer.next = curr

        return head


# @lc code=end
