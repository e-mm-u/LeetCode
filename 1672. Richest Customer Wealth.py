class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in range(0,len(accounts),1):
            wealth = 0
            for j in range(0,len(accounts[i]),1):
                wealth += accounts[i][j]
            
            if(wealth > maxWealth):
                maxWealth = wealth
        
        
        return maxWealth