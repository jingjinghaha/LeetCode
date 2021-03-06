'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        l1 = 0
        root = headA
        while root:
            l1 += 1
            root = root.next
        l2 = 0
        root = headB
        while root:
            l2 += 1
            root = root.next
        if l1 >= l2:
            for i in xrange(l1-l2):
                headA = headA.next
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
        else:
            for i in xrange(l2-l1):
                headB = headB.next
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
        return None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        p1 = headA
        p2 = headB
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
            if p1 == p2:
                return p1
            if not p1:
                p1 = headB
            if not p2:
                p2 = headA
        return p1
