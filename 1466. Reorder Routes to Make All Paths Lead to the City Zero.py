class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for a,b in connections:
            graph[a].append([b,True])
            graph[b].append([a,False])
        
        visited = set()
        cnt = 0

        print(graph)

        def dfs(city,flip):
            nonlocal cnt
            if city in visited:
                return
            visited.add(city)
            if flip:
                cnt += 1
            for a,b in graph[city]:
                dfs(a,b)    

        dfs(0,False)
        return cnt    