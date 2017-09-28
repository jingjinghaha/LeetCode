'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
# there are some many cases that I didn't realise until I submitted the answer

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        last = dummy
        carry = 0
        while l1 and l2:
            remain = l1.val + l2.val + carry
            if remain > 9:
                remain %= 10
                carry = 1
            else:
                carry = 0
            last.next = ListNode(remain)
            last = last.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            if carry == 0:
                last.next = l1
                break
            else:
                remain = l1.val + carry
                if remain > 9:
                    remain %= 10
                    carry = 1
                else:
                    carry = 0
                last.next = ListNode(remain)
                last = last.next
                l1 = l1.next
        
        while l2:
            if carry == 0:
                last.next = l2
                break
            else:
                remain = l2.val + carry
                if remain > 9:
                    remain %= 10
                    carry = 1
                else:
                    carry = 0
                last.next = ListNode(remain)
                last = last.next
                l2 = l2.next
        
        if carry == 1:
            last.next = ListNode(carry)
        
        return dummy.next

'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''
# use stack
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        stack2 = []
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        sum = 0
        stack3 = []
        while stack1 or stack2:
            sum /= 10
            if stack1:
                sum += stack1[-1]
                stack1.pop()
            if stack2:
                sum += stack2[-1]
                stack2.pop()
            stack3.append(sum%10)
        if sum/10 == 1:
            stack3.append(sum/10)
        
        dummy = ListNode(0)
        last = dummy
        while stack3:
            last.next = ListNode(stack3[-1])
            stack3.pop()
            last = last.next
        return dummy.next

