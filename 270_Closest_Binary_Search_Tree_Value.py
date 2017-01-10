# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

""" NOTES:
- We know that it is a BST, so lower on left and higher on right
- want to get base comparison of value to root
    - for example val is 10 and root is 90 -> diff of 80
- now check diff of R and L children,
    - if diff of L is lower go L
    - if diff of R is less go R
    - if diff of root is less than R or L then root is answer
    - if no children then don't go
    - will want to remember last root
    - new root is the left child or right child

- check dif of root
- check diff of right
- check diff or left
- if children and if R or L is less go there else return

"""

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return_val = root.val
        if not root.right and not root.left:
            return return_val
            
        root_diff = abs(root.val - target)
        
        left_diff = sys.maxint
        if root.left:
            left_diff = abs(root.left.val - target)
        
        right_diff = sys.maxint
        if root.right:
            right_diff = abs(root.right.val - target)
        
        if left_diff < root_diff and left_diff < right_diff:
            return_val = self.closestValue(root.left, target)
        
        if right_diff < root_diff:
            return_val = self.closestValue(root.right, target)
        
        return return_val
        
        
