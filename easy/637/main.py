from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        queue = deque([root])
        avg = []

        while queue:
            n = len(queue)
            curr_avg = 0

            for _ in range(n):
                node = queue.popleft()
                curr_avg += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            avg.append(curr_avg / n)

        return avg