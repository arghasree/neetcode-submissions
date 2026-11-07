# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):

            if not root:
                return 
            
            tmp=root.left
            root.left=root.right
            root.right=tmp

            invert(root.left)
            invert(root.right)

        invert(root)
        return root


        # res=[]

        # def first(root):
        #     if root is None: 
        #         return
            
        #     res.append(root.val)
        #     first(root.right)
        #     first(root.left)

        # first(root)
        # ind=[0]

        # def second(root):
        #     if root is None:
        #         return 
        #     i=ind[0]
        #     root.val = res[i]
        #     # print(root.val)
        #     ind[0]+=1
        #     second(root.left)
        #     second(root.right)

        # second(root)
        # return root

        