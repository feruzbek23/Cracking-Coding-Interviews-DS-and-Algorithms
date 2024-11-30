# Time complexity O(n)
# Space complexity O(n)

from collections import deque

def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res_1 = []
        res_2 = []

        def is_leaf(node):
            return node.val and not node.left and not node.right
    
        def inorder(root, l):
            if not root:
                return
            if root.left:
                inorder(root.left, l)
            if is_leaf(root):
                l.append(root.val)
            if root.right:
                inorder(root.right, l)
        inorder(root1, res_1)
        inorder(root2, res_2)
        
        if res_1 == res_2:
            return True
        return False