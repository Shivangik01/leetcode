class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        skip = nums[0]
        noskip = nums[0]
        ans = nums[0]

        for num in nums[1:]:

            skip = max(skip+num,noskip)
            noskip = max(noskip+num,num)

            ans = max(ans,skip,noskip)

        return ans