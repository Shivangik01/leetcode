# sort
# curr counter and next counter

from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        res = []
        hp = defaultdict(list)

        for i in range(len(groupSizes)):
            hp[groupSizes[i]].append(i)
            if len(hp[groupSizes[i]])==groupSizes[i]:
                res.append(hp.pop(groupSizes[i]))

        # print(hp)

        # groupSizes = sorted(groupSizes)
        # curr = groupSizes[0]
        # temp = []

        # for i in range(len(groupSizes)):
        #     #print(i,curr)

        #     if curr!=0:
        #         curr -= 1
        #         temp.append(hp[groupSizes[i]].pop())

        #     else:
        #         res.append(temp)
        #         temp = []
        #         curr = groupSizes[i]-1
        #         temp.append(hp[groupSizes[i]].pop())

        # res.append(temp)
        
        return res