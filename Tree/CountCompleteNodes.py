# Time O(n)
# Space O(n) best-case O(logn)


def countNodes(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    self.count = 0
    def traverse(root):
        self.count += 1
        if root.right is not None:
            traverse(root.right) 
        if root.left is not None:
            traverse(root.left)
    traverse(root)
    return self.count