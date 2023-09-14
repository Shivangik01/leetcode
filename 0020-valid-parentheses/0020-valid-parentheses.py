class Solution:
    def isValid(self, s: str) -> bool:

        hp = {'(':')',
                '[':']',
                '{':'}'
            }

        st = []

        for b in s:
            if b in hp.keys():
                st.append(hp[b])
            else:
                if len(st)==0 or st.pop()!=b:
                    return False
                
        return True if st==[] else False

        