class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for i in range(n)] for i in range(n)]
        dp[n-1] = matrix[n-1]

        for i in range(n-2,-1,-1):
            for j in range(n):
                x = dp[i+1][j]

                if j-1>=0:
                    y = dp[i+1][j-1]
                    x = min(x,y)

                if j+1<n:
                    z = dp[i+1][j+1]
                    x = min(x,z)

                dp[i][j] = x+matrix[i][j]
       
        return min(dp[0])