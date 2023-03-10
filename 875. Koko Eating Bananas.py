class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minn = 1
        maxx = max(piles)

        while minn<maxx:
            mid = minn+(maxx-minn)//2

            hr = 0
            for i in piles:
                hr += math.ceil(i/mid)
                if hr>h:
                    break
            
            if hr>h:
                minn = mid+1
            else:
                maxx = mid
            
        return maxx