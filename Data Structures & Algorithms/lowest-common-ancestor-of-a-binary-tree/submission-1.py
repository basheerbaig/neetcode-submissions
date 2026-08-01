# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right # the line where it moves up from bottom see the example below


#         Imagine this tree.

#           3
#         /   \
#        5     1
#       / \   / \
#      6   2 0   8
#         / \
#        7   4

# Find

# p = 7
# q = 4

# Let's trace.

# Visit 7

# return 7

# Visit 4

# return 4

# Node 2 receives

# left = 7
# right = 4

# Both found.

# return 2

# Now node 5 gets

# left = None
# right = 2

# Only right exists.

# return 2

# Node 3 gets

# left = 2
# right = None

# Only left exists.

# return 2

# Final answer

# 2