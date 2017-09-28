'''
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# iteratively
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
        return new_head

# recursively
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head, None)
    
    def helper(self, head, new_head):
        if not head:
            return new_head
        next_node = head.next
        head.next = new_head
        new_head = head
        return self.helper(next_node, new_head)

'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        root = head
        pos = 1
        orig_tail = head
        while pos < m:
            orig_tail = head
            head = head.next
            pos += 1
        new_head = new_tail = head
        head = head.next
        pos += 1
        while pos <= n:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
            pos += 1
        if orig_tail == new_tail:
            new_tail.next = head
            return new_head
        orig_tail.next = new_head
        new_tail.next = head
        return root

# code from LintCode, which is much easy to understand
class Solution:

    def reverse(self, head):
        prev = None
        while head != None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def findkth(self, head, k):
        for i in xrange(k):
            if head is None:
                return None
            head = head.next
        return head

    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1, head)
        mth_prev = self.findkth(dummy, m - 1)
        mth = mth_prev.next
        nth = self.findkth(dummy, n)
        nth_next = nth.next
        nth.next = None

        self.reverse(mth)
        mth_prev.next = nth
        mth.next = nth_next
        return dummy.next

