class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        l = len(accounts)
        wealth = []
        
        for i in range(0,l,1):
            
            wealth.append(sum(accounts[i]))
            
        return max(wealth)