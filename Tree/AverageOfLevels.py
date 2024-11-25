import deque
def averageOfLevels(self, root):
        if not root:
            return
        result = []
        
        queue = deque([root])
        print(queue)

        while queue:
            level_sum = 0  # To store the sum of values at the current level
            level_count = len(queue)
            print(level_count)
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val
        
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / level_count)
        
        return result