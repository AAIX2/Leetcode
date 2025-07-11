# Approach-1 (Brute Force - Do as said)
# T.C : O(mlogm +m*n) , where Let n = number of rooms, m =  number of meetings
# S.C : O(n)

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()  # Sort by start time

        roomsUsedCount = [0] * n  # Track number of times each room is used
        lastAvailableAt = [0] * n  # Track when each room becomes available

        for start, end in meetings:
            found = False
            earlyEndRoomTime = float('inf')
            earlyEndRoom = 0

            for room in range(n):
                if lastAvailableAt[room] <= start:
                    found = True
                    lastAvailableAt[room] = end
                    roomsUsedCount[room] += 1
                    break

                if lastAvailableAt[room] < earlyEndRoomTime:
                    earlyEndRoomTime = lastAvailableAt[room]
                    earlyEndRoom = room

            if not found:
                lastAvailableAt[earlyEndRoom] += (end - start)
                roomsUsedCount[earlyEndRoom] += 1

        resultRoom = -1
        maxUse = 0

        for room in range(n):
            if roomsUsedCount[room] > maxUse:
                maxUse = roomsUsedCount[room]
                resultRoom = room

        return resultRoom
    
# Approach-2 (Use priority Queue to find the first available meeting room)
# T.C : O(mlogm + m*log(n)) , where Let n = number of rooms, m =  number of meetings
# S.C : O(n)

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = [i for i in range(n)]
        heapq.heapify(free)
        busy = []
        count = [0]*n
        for st,end in meetings:
            while busy and busy[0][0]<=st:
                t,room = heapq.heappop(busy)
                heapq.heappush(free,room)
            
            if free:
                room = heapq.heappop(free)
                count[room]+=1
                heapq.heappush(busy,[end,room])
            else:
                t,room = heapq.heappop(busy)
                count[room]+=1
                heapq.heappush(busy,[t+(end-st),room])
        res = 0
        maxi = 0
        for i in range(n):
            if count[i]>maxi:
                maxi = count[i]
                res = i
        return res
