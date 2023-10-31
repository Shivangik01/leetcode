from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        mp = defaultdict(list)

        for ele in arr:
            
            mp[bin(ele).count('1')].append(ele)


        res =[]
        temp = sorted(mp.keys())
        for k in temp:

            res+=sorted(mp[k])

        
        return res