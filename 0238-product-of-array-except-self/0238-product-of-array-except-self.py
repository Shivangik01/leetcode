class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        l = [ nums[i] for i in range(n)]
        r = [ nums[i] for i in range(n)]
        res = [ 1 for _ in range(n)]

        for i in range(1,n):
            l[i] = l[i-1]*nums[i]

        for i in range(n-2,-1,-1):
            r[i] = r[i+1]*nums[i]
        
        res[0]=r[1]
        res[-1] = l[-2]
        
        for i in range(1,n-1):
            res[i] = l[i-1]*r[i+1]

        return res
            
