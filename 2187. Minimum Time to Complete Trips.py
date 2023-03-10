class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        if len(time)==1:
            return totalTrips*time[0]

        minn = min(time)
        maxx = max(time)*totalTrips
        count = 0
        while minn<maxx:
            mid = minn+(maxx-minn)//2
            t = 0
            for i in time:
                t += mid//i
                if t>=totalTrips:
                    break

            if t>=totalTrips:
                maxx = mid
            else:
                minn = mid+1
            
        return minn