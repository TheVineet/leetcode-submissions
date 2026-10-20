class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        visit = set()

        q = collections.deque()
        q.append(0)

        while q:
            node = q.popleft()
            visit.add(node)
            for nei in rooms[node]:
                if nei in visit:
                    continue
                q.append(nei)
        
        return len(visit) == len(rooms)
        