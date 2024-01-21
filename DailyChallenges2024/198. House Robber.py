class Solution:
    def rob(self, nums: List[int]) -> int:       
        house1, house2 = 0, 0
        for n in nums:
            # max value till current house
            temp = max(n+house1, house2)
            # reassign value to get previous 2 house of next current house
            house1 = house2
            house2 = temp # current house is adjacent to next house

        # when we reach at the end, house2 is the last house
        return house2