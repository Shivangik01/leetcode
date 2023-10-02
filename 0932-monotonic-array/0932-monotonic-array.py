class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        n = len(nums)

        if n==1:
            return True

        else:

            if nums[0]>nums[1]:
                p = "gt"
            
            elif nums[0]<nums[1]:
                p = "lt"
            
            else:
                p = "eq"
            
            for i in range(2,n):
                if p =="eq":
                    if nums[i-1]>nums[i]:
                        p = "gt"
                    
                    elif nums[i-1]<nums[i]:
                        p = "lt"
                    
                    else:
                        p = "eq"
        

                elif nums[i-1]<nums[i] and p=="gt":
                    return False
                elif nums[i-1]>nums[i] and p=="lt":
                    return False

            return True
