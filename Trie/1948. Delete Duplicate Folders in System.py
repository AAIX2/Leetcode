# Approach (Using trie)
# T.C : O(N * L * ClogC), N = total Paths, L = average length of each path, C is the average number of children per node
# S.C : ~O(N * L), we store all the paths in the trie, approximated value.

class Node:
    def __init__(self):
        self.children = {}
        self.sub = ""

class Trie:
    def __init__(self):
        self.root = Node() 

    def insert(self,w):
        root = self.root
        for ch in w:
            if ch not in root.children:
                root.children[ch] = Node()
            root = root.children[ch] 

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie = Trie()
        for path in paths:
            trie.insert(path)
        root = trie.root
        def encode(node):
            if not node.children:
                return "()"

            cur = []
            for next,child in node.children.items():
                sub = encode(child)
                cur.append(next+sub)
            cur.sort()
            path = "("+"".join(cur)+")"
            node.sub = path
             
            mp[path]+=1
            return path

        mp = defaultdict(int)
        encode(root)
        
        

        def solve(node,path):
            for next,child in node.children.items():
                subfolder = child.sub
                if mp[subfolder]>=2:
                    continue 
                path.append(next)
                res.append(path[:])
                solve(child,path)
                path.pop()
        res = []
        solve(root,[])
        return res
