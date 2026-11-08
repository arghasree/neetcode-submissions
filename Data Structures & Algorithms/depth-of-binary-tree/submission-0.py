# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # BFS Solution
        que = deque()
        level = 0
        if root:
            que.append(root)

        while que:
            for i in range(len(que)):
                child = que.popleft()
                if child.left is not None:
                    que.append(child.left)
                if child.right is not None:
                    que.append(child.right)
            level+=1
        return level
        
        # # DFS iterative Solution
        # def tree(root):
        #     if root is None:
        #         return 0
            
        #     return 1 + max(tree(root.left), tree(root.right))
        
        # return tree(root)