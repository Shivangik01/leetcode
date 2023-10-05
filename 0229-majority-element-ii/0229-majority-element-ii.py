from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        r = n//3
        counts = Counter(nums)

        res = []
        for num in counts.keys():
            if counts[num]>r:
                res.append(num)

        return res
