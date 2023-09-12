from collections import defaultdict
class Solution:
    def minDeletions(self, s: str) -> int:

        hp = defaultdict(int)

        for a in s:
            hp[a]+=1

        dels = 0
        freq = sorted(hp.values())
        seen = []

        for val in freq:
            
            if val in seen:   
                
                while val in seen and val>0:
                    val -= 1
                    dels += 1
            
            seen.append(val)

        #print(seen,dels)
        return dels

        