'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# the idea is totally same as reverse nodes in k-group
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        end = head
        while end and end.next:
            end = end.next
            prev = self.reverse(prev, prev.next, end)
            end = prev.next
        return dummy.next
    def reverse(self, prev, start, end):
        end_next = end.next
        p = start
        cur = p.next
        while cur != end_next:
            next = cur.next
            cur.next = p
            p = cur
            cur = next
        prev.next = end
        start.next = end_next
        return start

# recursively from the discussion
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head
        return n