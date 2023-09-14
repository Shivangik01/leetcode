#2 of max
#max negative and max positive
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        optn = nums[0]
        optp = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            
            optp,optn = max(nums[i],nums[i]*optp,nums[i]*optn),min(nums[i],nums[i]*optn,nums[i]*optp)
            
            ans = max(ans,optp,optn)
            print(optp,optn,ans)

        return ans
            