
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        res = [-1,-1]

        if target in nums:

            res[0]=bisect.bisect_left(nums,target)
            res[1]=bisect.bisect_right(nums,target)-1

        return res
        