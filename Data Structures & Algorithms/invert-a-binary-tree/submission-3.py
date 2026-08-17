# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #need BFS to swap on the same level
        #checking for empty tree
        if not root:
            return None
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            #now we flip the nodes 3 <--1--> 4 becomes 4 <--1--> 3
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root