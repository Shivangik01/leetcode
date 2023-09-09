class Solution:
    def arraySign(self, nums: List[int]) -> int:
    
        neg = 1

        for num in nums:

            if num<0:
                neg *= -1
            elif num == 0:
                return 0

        return neg
