# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
    def isValidBST(self, root):
        def helper(node, lower, upper):
            # logic for the helper function goes here 
        return helper(root, float('-inf'), float('inf'))