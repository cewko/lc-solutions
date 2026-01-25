from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        saw = []
        queue = deque([root])

        while queue:
            right_side = None
            q_len = len(queue)

            for _ in range(q_len):
                node = queue.popleft()

                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)

            if right_side:
                saw.append(right_side.val)

        return saw

