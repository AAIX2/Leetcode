# Approach (Using sorting + greedily selecting)
# T.C : O(nlogn + mlogm + min(m, n)), where m = size of players and n = size of trainers
# S.C : O(1)

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n,m = len(players),len(trainers)
        players.sort()
        trainers.sort()
        i = j = 0
        while i<n and j<m:
            if players[i]<=trainers[j]:
                i+=1
            j+=1
        return i