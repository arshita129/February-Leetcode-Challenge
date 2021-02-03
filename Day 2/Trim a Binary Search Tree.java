/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode trimBST(TreeNode root, int low, int high) {
        root=trimBSTutil(root,low,high);
        return root;
    }
    public TreeNode trimBSTutil(TreeNode root,int low,int high){
        if(root==null){
            return null;
        }
        
        if(root.val<=high && root.val>=low){
            root.left=trimBSTutil(root.left,low,high);
            root.right=trimBSTutil(root.right,low,high);
        }
        else{
            if(root.val>high){
                System.out.println("Left");
                root= trimBSTutil(root.left,low,high);
            }
            else{
                System.out.println("Left");
                root= trimBSTutil(root.right,low,high);
            }
        }
        return root;
    }
}
