'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# copy every node and contrauct a maaping between the original node and the copied node, then copy the relationship between nodes
# time: O(n)
# space: O(n)
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head or head is None:
            return None
        mapping = {}
        root = head
        while head:
            new_node = RandomListNode(head.label)
            mapping[head] = new_node
            head = head.next
        for node in mapping:
            new_node = mapping[node]
            if node.next:
                new_node.next = mapping[node.next]
            if node.random:
                new_node.random = mapping[node.random]
        return mapping[root]

# copy each node of the original list, linked the original ndoe to the copied node. In this way, the structure of the input is changed. 
# the first while loop is to change the structure of the input list
# the second while loop copy the realationship between node
# the third loop is to constructure the ouput and reconstruct the input
# time: O(n)
# space: O(1)
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head or head is None:
            return None
        node = head
        while node:
            next_node = node.next
            copy = RandomListNode(node.label)
            copy.next = next_node
            node.next = copy
            node = next_node
        
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        
        dummy = RandomListNode(0)
        last = dummy
        node = head
        while node:
            next_node = node.next.next
            
            copy = node.next
            last.next = copy
            last = last.next
            
            node.next = next_node
            node = node.next
        return dummy.next

