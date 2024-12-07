class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0]*n
        for n1,n2 in edges:
            indeg[n2]+=1

        team = -1
        for i in range(n):
            if indeg[i] == 0:
                if team!=-1:
                    return -1
                team = i
            
        return team
    