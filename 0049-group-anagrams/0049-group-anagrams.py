class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for s in strs:
            t = sorted(s)
            temp = ''.join(t)
            if temp not in dic.keys():
                dic[temp]=[s]
            else:
                dic[temp].append(s)
            
        return dic.values()
    
        