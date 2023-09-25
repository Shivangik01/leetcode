from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        c1 = Counter(s)
        c2 = Counter(t)

        for k,v in c2.items():
            if c2[k]!=c1[k]:
                return k