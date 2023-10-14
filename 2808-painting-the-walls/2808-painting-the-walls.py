class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        n = len(cost)
        dp = [float('inf') for i in range(n+1)]

        dp[0]=0 

        for j in range(n):
            for i in range(n,-1,-1):

                dp[i] = min(dp[i],dp[max(i-time[j]-1,0)]+cost[j])
        
        return dp[n]