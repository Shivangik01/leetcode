# dp till target
# check how many 1's 2's 3's so on
# number of ways to make that
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0 for i in range(target+1)]
        dp[0]=1
        nums = sorted(nums)

        for i in range(1,target+1):

            for j in range(len(nums)):

                if nums[j]>i:
                    break
                
                dp[i] += dp[i-nums[j]]

                
        return dp[target]


