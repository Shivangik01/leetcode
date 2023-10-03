from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        mp = Counter(nums)

        #print(mp)
        res = 0

        for val in mp.values():
            if val>1:
                res += math.comb(val, 2)

        return res