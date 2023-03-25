class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = { }
        for road in roads:
            if road[0] not in d:
                d[road[0]] = [[road[1],road[2]]]
            else:
                d[road[0]].append([road[1],road[2]])

            if road[1] not in d:
                d[road[1]] = [[road[0],road[2]]]
            else:
                d[road[1]].append([road[0],road[2]])


                
        q= [1]
        visited = set()
        minn = roads[0][2]
        print(d)
        while q:
          node = q.pop(0)
          for road,dist in d[node]:
            if road not in visited:
              visited.add(road)
              q.append(road)
            
            minn = min(minn,dist)
        
        return minn
