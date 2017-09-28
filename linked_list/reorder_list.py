'''
Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        dummy = None
        next_head = slow.next
        slow.next = None
        while next_head:
            next_node = next_head.next
            next_head.next = dummy
            dummy = next_head
            next_head = next_node
        while head and dummy:
            print head.val, dummy.val
            next_node1 = head.next
            head.next = dummy
            head = next_node1
            next_node2 = dummy.next
            dummy.next = next_node1
            dummy = next_node2
