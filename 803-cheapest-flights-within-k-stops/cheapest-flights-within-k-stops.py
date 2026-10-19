
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adjMap = {i: [] for i in range(n)}

        for u, v, cost in flights:
            adjMap[u].append((cost, v))

       
        minHeap = []
        costCount = [[float("inf")] * (k + 2) for _ in range(n)] #costCount[node][flightsTaken] Cost to get to given node using flights taken
        minHeap.append([0,src,0]) #cost, node, numFlights 
        costCount[src][0] = 0


        while minHeap:
            cost,node,numFlights = heapq.heappop(minHeap)
            if node == dst:
                return cost
            
            if numFlights >= k + 1:
                continue
            
            if cost > costCount[node][numFlights]:
                continue

            for cost1,nei in adjMap[node]:
                newCost = cost + cost1
                newNumFlights = numFlights + 1

                if newCost < costCount[nei][newNumFlights]:
                    costCount[nei][newNumFlights] = newCost
                    heapq.heappush(minHeap, (newCost, nei, newNumFlights))
        
        return -1