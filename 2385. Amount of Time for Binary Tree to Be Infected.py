#2385. Amount of Time for Binary Tree to Be Infected-leetcode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque              
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def getParent(root):
            q=deque([root])
            d={}
            while(len(q)>0):
                node=q.popleft()
                if(node.left):
                    d[node.left]=node
                    q.append(node.left)
                if(node.right):
                    d[node.right]=node
                    q.append(node.right)
            return d
        def getAdd(root,start):
            if(root.val==start):
                return root
            q=deque([root])
            while(len(q)>0):
                node=q.popleft()
                if(node.val==start):
                    return node
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
        parent=getParent(root)
        startAdd=getAdd(root,start)    
        q=deque([startAdd])
        m=0
        visited={startAdd}
        while(len(q)>0):
            for _ in range(len(q)):
                node=q.popleft()
                #left
                if(node.left and node.left not in visited):
                    visited.add(node.left)
                    q.append(node.left)
                #right
                if(node.right and node.right not in visited):
                    visited.add(node.right)
                    q.append(node.right)
                #parent
                if(node in parent and parent[node] not in visited):
                    visited.add(parent[node])
                    q.append(parent[node])
            m+=1
        return m-1
        
