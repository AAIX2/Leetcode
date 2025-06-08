# /Approach (Simple Recursion - DFS)
# /T.C : O(n) - We visit each number (1 to n) only once.
# /S.C : O(d) - where d is the number of digits in n i.e. log10(n)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(node):
            if node!=0:
                ans.append(node)

            for i in range(10):
                if node == 0 and i == 0:
                    continue
                if node*10+i<=n:
                    dfs(node*10+i)
                else:
                    break
        dfs(0)
        return ans
