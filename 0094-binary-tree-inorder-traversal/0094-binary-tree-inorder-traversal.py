# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        #solution1- this is the recursive approach- tc O(n) sc O(n) because of the recursive stack space
        res=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res


        #solution2- this is the iterative approach using stack- tc O(n) sc O(n)
        res=[]
        st=[]
        curr=root
        while curr or st:
            while curr:
                st.append(curr)
                curr=curr.left
            curr=st.pop()
            res.append(curr.val)
            curr=curr.right
        return res'''
        
        # solution 3- morris traversal approach- tc O(n) sc O(1)
        res=[]
        curr=root
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                if not prev.right:
                    prev.right=curr
                    curr=curr.left
                else:
                    prev.right=None
                    res.append(curr.val)
                    curr=curr.right
        return res