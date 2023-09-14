class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        opt = [i for i in nums]
        m = opt[0]
        
        for i in range(1,len(nums)):
            
            opt[i] = max(opt[i], opt[i-1]+nums[i])
            
            m = max(opt[i],m)

        
        return m
                        