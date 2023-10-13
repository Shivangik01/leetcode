class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        p1=cost[-1]
        p2=cost[-2]
        res = 0
        # dp = [0 for i in range(n+2)]

        for i in range(n-3,-1,-1):
            res = cost[i]+min(p1,p2)
            #dp[i] = cost[i]+min(dp[i+1],dp[i+2])
            p1 = p2
            p2 = res
            

        return min(p2,p1)