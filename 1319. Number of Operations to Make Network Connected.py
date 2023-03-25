class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1

        d = {i: [] for i in range(n)}
        for connection in connections:
            d[connection[0]].append(connection[1])
            d[connection[1]].append(connection[0])
        
        visited = set()
        count = 0

        def helper(node):
            if node in visited:
                return
            visited.add(node)
            for n in d[node]:
              helper(n)
        
        for i in range(n):
          if i not in visited:
            helper(i)
            count += 1
        
        return count-1

        return 0