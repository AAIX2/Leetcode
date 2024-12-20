# Approach-1 - Simple BFS
# T.C : O(n)
# S.C : O(n) Since the last level of perfect binary tree has roughly n/2 nodes


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lvl = 0
        q = deque([root])
        
        
        def reverse(st,end):
            while st<end:
                q[st].val,q[end].val = q[end].val,q[st].val
                st+=1
                end-=1
        
        while q:
            if lvl%2:
                reverse(0,len(q)-1)
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl+=1 
        return root
    

# Approach-2 - Tricky DFS (explained the trick on how to write such DFS)
# T.C : O(n)
# S.C : O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(c1,c2,lev):
            if not c1 and not c2:
                return 
            if lev%2 == 0:
                c1.val,c2.val = c2.val,c1.val
            dfs(c1.left,c2.right,lev+1)
            dfs(c1.right,c2.left,lev+1)
        dfs(root.left,root.right,0)
        return root