# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if root==None:
            return None
        if root.val>=low and root.val<=high:
            root.left=self.trimBST(root.left,low,high)
            root.right=self.trimBST(root.right,low,high)
        else:
            if root.val>high:
                root=self.trimBST(root.left,low,high)
            else:
                root=self.trimBST(root.right,low,high)
        return root
        
