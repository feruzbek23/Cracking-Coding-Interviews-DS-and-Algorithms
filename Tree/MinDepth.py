# Time complexity O(n)
# Space complexity O(n)

from collections import deque

def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def is_leaf(node):
            return True and not node.left and not node.right

        min_path = 0
        queue = deque([root])
        
        while queue:
            min_path += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if is_leaf(node):
                    return min_path

                if node.left:
                    if is_leaf(node.left):
                        return min_path + 1
                    queue.append(node.left)

                if node.right:
                    if is_leaf(node.right):
                        return min_path + 1
                    queue.append(node.right)