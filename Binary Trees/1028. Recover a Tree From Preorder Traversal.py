# Approach-1 - Using Recursion (Simulation of DFS in Tree)
# T.C : O(n)
# S.C : O(n) for System Stack used for Recursion


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        ind = 0
        def solve(depth):
            nonlocal ind
            if ind == len(traversal):
                return 
            lvl = 0
            while ind+lvl<len(traversal) and traversal[ind+lvl] == "-":
                lvl+=1
            if lvl!=depth:
                return None
            ind+=lvl
            val = 0
            while ind<len(traversal) and traversal[ind].isdigit():
                val = val*10+int(traversal[ind])
                ind+=1
            node = TreeNode(val)
            node.left = solve(depth+1)
            node.right = solve(depth+1)
            return node
            
        return solve(0)
        

# Approach-2 - Using Stack 
# T.C : O(n)
# S.C : O(n) for System Stack used for Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        st = []
        dashes = 0
        ind = 0
        while ind<n:
            while ind<n and traversal[ind] == "-":
                ind+=1
                dashes+=1
            else:
                j = ind
                val = 0
                while j<n and traversal[j].isdigit():
                    val = val*10+int(traversal[j])
                    j+=1  
                node = TreeNode(val)
                while len(st)>dashes:
                    st.pop()
                if st and not st[-1].left:
                    st[-1].left = node
                elif st and not st[-1].right:
                    st[-1].right = node
                st.append(node)
                ind = j
                dashes = 0
        return st[0]


        