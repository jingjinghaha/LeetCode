'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''
# as cannot use extra memory, the basic idea is to reverse the first half of the list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        if head.next is None:
            return True
        if head.next.next is None:
            if head.val == head.next.val:
                return True
            else:
                return False
        root = head
        count = 0
        while root:
            count += 1
            root = root.next
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_head = None
        half = 0
        while head != slow:
            half += 1
            next = head.next
            head.next = new_head
            new_head = head
            head = next
        half += 1
        next = head.next
        head.next = new_head
        new_head = head
        head = next
        if 2 * half > count:
            new_head = new_head.next
        while new_head and head:
            if new_head.val != head.val:
                return False
            else:
                new_head = new_head.next
                head = head.next
        if new_head or head:
            return False
        return True

