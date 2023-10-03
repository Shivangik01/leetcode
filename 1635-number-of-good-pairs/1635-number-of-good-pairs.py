from collections import Counter, defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        mp = Counter(nums)

        #print(mp)
        res = 0

        for val in mp.values():
            
            res += math.comb(val, 2)

        return res

        # mp = defaultdict(int)
        # res = 0

        # for num in nums:

        #     res += mp[num]
        #     mp[num]+=1

        # return res
        