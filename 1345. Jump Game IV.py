class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        jumps = 0
        n = len(arr)
        # unique valur = [ all indexes of that value in arr ]
        d = defaultdict(list)
        for i in range(n):
            d[arr[i]].append(i)
        
        # q -> keep index
        q = deque()
        # start from index 0
        q.append(0)
        # already visited index, without duplicate
        visited = set([0])
        
        while q:
            size = len(q)
            for i in range(size):
                currIdx = q.popleft()
                # already last index, return
                if currIdx == n - 1:
                    return jumps
                # check 3 options to jump
                # 1) i + 1, if i + 1 not visited, add into visited, and add into queue
                if currIdx + 1 < n and currIdx + 1 not in visited:
                    visited.add(currIdx + 1)
                    q.append(currIdx + 1)
                # 2) i - 1, if i - 1 not visited, add into visited and queue
                if currIdx - 1 >= 0 and currIdx - 1 not in visited:
                    visited.add(currIdx - 1)
                    q.append(currIdx - 1)
                # 3) the same value with different indexes
                if arr[currIdx] in d:
                    for idx in d[arr[currIdx]]:
                        if idx not in visited:
                            visited.add(idx)
                            q.append(idx)
                    # already visited, remove from dict to avoid dup visit
                    del d[arr[currIdx]]
            # after checking 3 possible ways, jumps + 1
            jumps += 1
        
        return -1