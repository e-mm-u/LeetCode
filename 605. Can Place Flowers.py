class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool: 
        for i in range(0,len(flowerbed)):

            left = flowerbed[i-1] if i-1>=0 else 0
            right = flowerbed[i+1] if i+1<len(flowerbed) else 0
            if not flowerbed[i] and not left and not right:
                flowerbed[i] = 1
                n -= 1

        return n<=0