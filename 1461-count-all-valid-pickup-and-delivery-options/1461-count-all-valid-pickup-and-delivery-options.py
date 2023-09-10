import math

class Solution:
    def countOrders(self, n: int) -> int:
        
        # return (math.factorial(n*2)//(2**n))%(10**9+7)

        if n<2:
            return n
        elif n==2:
            return 6

        # dp = [ 0 for _ in range(n+1)]
        # dp[1]=1
        # dp[2]=6
        prev = 6
        mod = 10**9+7

        for i in range(3,n+1):

            each = 2*i -1
            total = ((each*(each+1))/2)%mod
            ans = (total*prev)%mod
            prev = ans

        return int(ans%mod)

