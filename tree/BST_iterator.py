'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''
# the following inorder traversal does not meet the requirement of O(h) space
class BSTIterator(object):
    inorder = []
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.inorder_traversal(root)
        
    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        self.inorder.append(root.val)
        self.inorder_traversal(root.right)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.inorder:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        val = self.inorder[0]
        del self.inorder[0]
        return val

# using stack
class BSTIterator(object):
    stack = []
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.go_left(root)
        
    def go_left(self, root):
        if not root:
            return
        self.stack.append(root)
        self.go_left(root.left)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.go_left(node.right)
        return node.val

