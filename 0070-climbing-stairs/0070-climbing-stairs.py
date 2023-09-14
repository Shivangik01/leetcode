# -1 no. of ways+1
# -2

class Solution:
    
    def climbStairs(self, n: int) -> int:

        if n==1:
            return 1
        
        opt=[0 for i in range(n+1)]
        opt[1]=1
        opt[2]=2
        
        for i in range(3,n+1):
            
            opt[i] = opt[i-1] + opt[i-2]
            
        #print(opt)
                
        return opt[n]
            