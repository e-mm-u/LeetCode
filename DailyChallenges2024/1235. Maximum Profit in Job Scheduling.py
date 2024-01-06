class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda job: job[1])
        n = len(jobs)
        
        dp = [0] * n
        dp[0] = jobs[0][2]
        
        for i in range(1, n):
            includingI = jobs[i][2]
            
            # Binary search to find the latest non-overlapping job
            nonOverlappingJob = -1  # Initialize outside the loop
            low, high = 0, i - 1
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    nonOverlappingJob = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            if nonOverlappingJob != -1:
                includingI += dp[nonOverlappingJob]
            
            excludingI = dp[i - 1]
            dp[i] = max(includingI, excludingI)

        return dp[-1]