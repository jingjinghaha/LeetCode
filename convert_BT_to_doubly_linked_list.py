# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:25:45 2017

@author: jingjing
"""

# convert binary tree to doubly linked list
class node():
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None
   
class binary_tree():  
    root = None
    head = None
    prev = None
    
    def print_list(self, head):
       while head:
           print head.val
           head = head.right
           
    def convert(self, root):
        if not root:
            return None
        stack = []
        stack.append(root)
        while root.left:
            stack.append(root.left)
            root = root.left
        root = None
        while stack:
            node = stack.pop()
            if not root:
                root = node
                head = node
            else:
                root.right = node
                node.left = root
                root = node
            if node.right:
                stack.append(node.right)
                node = node.right
                while node.left:
                    stack.append(node.left)
                    node = node.left
        self.print_list(head)
        return head
    
    def convert_recursive(self, root):
        if not root:
            return
        self.convert_recursive(root.left)
        if self.prev == None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root
        self.prev = root
        print self.prev.val
        self.convert_recursive(root.right)
   
root = node(10)
root.left = node(12)
root.right = node(15)
root.left.left = node(25)
root.left.right = node(30)
root.left.right.left = node(50)
root.right.left = node(36)
root.right.left.right = node(80)
tree = binary_tree()
tree.root = root
tree.convert(tree.root)
tree.convert_recursive(tree.root)