class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        
        def dfs(node, visited):
            visited.add(node)
            seen.add(node)
            for n in d[node]:
                if n not in visited:
                  dfs(n,visited)
                
        circle = []
        cnt = 0
        seen = set()
        for i in range(n-1):
            if i not in seen:
              visited = set()
              dfs(i,visited)
              circle.append(visited)

        for li in circle:
            l = len(li)
            cnt += l * (n-l)
            n -= l
        return cnt