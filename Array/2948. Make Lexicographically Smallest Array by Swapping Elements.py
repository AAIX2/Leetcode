# Approach-1 (Brute Force)
# T.C : O(n^3)
# S.C : O(1)

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            while True:
                minInd = -1
                val = nums[i]
                for j in range(i+1,n):
                    if nums[j]<val and val-nums[j]<=limit:
                        minInd = j
                        val = nums[j]
                if minInd!=-1:
                    nums[i],nums[minInd] = nums[minInd],nums[i]
                else:
                    break
        return nums
        
# Approach-2 (using sorting and grouping using unordered_map)
# T.C : ~O(n*logn)
# S.C : ~O(n)


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = nums.copy()
        # sort to make grouping elements easier
        arr.sort()
        groupMap = defaultdict(deque)
        eleGrpMp = defaultdict(int)
        grpNum = 0
        # Grouping the elements based on limit constraint and also keeping track of which group the element belongs to
        groupMap[grpNum].append(arr[0])
        eleGrpMp[arr[0]] = 0
        for i in range(1,n):
            if arr[i]-arr[i-1]>limit:
                grpNum+=1
            groupMap[grpNum].append(arr[i])
            eleGrpMp[arr[i]] = grpNum
        # Building the answer
        for i in range(n):
            grp = eleGrpMp[nums[i]]
            nums[i] = groupMap[grp].popleft()
        return nums


# Approach-3 (using DSU)
# T.C : ~O(n*logn)
# S.C : ~O(n)

class DisjointSet:
    def __init__(self,arr):
        self.parent = {num:num for num in arr}
        self.size = {num:1 for num in arr}
    def getPar(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.getPar(self.parent[node])
        return self.parent[node]
    def UnionBySize(self,u,v):
        ulti_u,ulti_v = self.getPar(u),self.getPar(v)
        if ulti_u == ulti_v:
            return 
        if self.size[ulti_u]>=self.size[ulti_v]:
            self.parent[ulti_v] = ulti_u
            self.size[ulti_u]+=self.size[ulti_v]
        else:
            self.parent[ulti_u] = ulti_v
            self.size[ulti_v]+=self.size[ulti_u]

    
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted(nums)
        dsu = DisjointSet(nums)
        
        for i in range(1,n):
            if arr[i]-arr[i-1]<=limit:
                dsu.UnionBySize(arr[i],arr[i-1])
                
        groupMap = defaultdict(deque)
        for i in range(n):
            groupMap[dsu.getPar(arr[i])].append(arr[i])
        for i in range(n):
            par = dsu.getPar(nums[i])
            nums[i] = groupMap[par].popleft()
        return nums


        