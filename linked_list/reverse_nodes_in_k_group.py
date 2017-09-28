'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k < 2:
            return head
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        end = head
        while end:
            for i in range(k-1):
                end = end.next
                if end is None:
                    return dummy.next
            prev = self.reverse(prev, prev.next, end)
            end = prev.next
        return dummy.next
    
    def reverse(self, prev, start, end):
        end_next = end.next
        tmp = start
        cur = tmp.next
        while cur != end_next:
            next = cur.next
            cur.next = tmp
            tmp = cur
            cur = next
        prev.next = end
        start.next = end_next
        return start


# recursively 
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head
