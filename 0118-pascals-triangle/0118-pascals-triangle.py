class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1],[1,1]]
        for i in range(2,numRows):
            temp=list(map(add,res[i-1],res[i-1][1:]))
            temp.insert(0,1)
            temp.insert(i,1)
            res.append(temp)
            
           
        return [] if numRows==0 else ([[1]] if numRows==1 else res)