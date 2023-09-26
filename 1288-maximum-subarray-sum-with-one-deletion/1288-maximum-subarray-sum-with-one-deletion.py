class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        skip = nums[0]
        noskip = nums[0]
        ans = nums[0]

        for num in nums[1:]:

            if skip<0:
                skip=0

            skip = skip+num if num>=0 else max(skip+num,noskip)

            if noskip<0:
                noskip=0
            
            noskip+=num

            ans = max(ans,skip,noskip)

        return ans