from collections import defaultdict
class Solution:
    def minDeletions(self, s: str) -> int:

        hp = defaultdict(int)

        for a in s:
            hp[a]+=1

        dels = 0
        seen = set()

        for val in hp.values():
            
            if val in seen:   
                
                while val in seen and val>0:
                    val -= 1
                    dels += 1
            
            seen.add(val)

        #print(seen,dels)
        return dels

        