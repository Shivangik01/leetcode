# for 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        provinces = 0   
        n = len(isConnected)

        for i in range(n):
            for j in range(n):

                if isConnected[i][j]==1:

                    q=[(i,j)]
                    provinces +=1

                    while q!=[]:

                        a,b = q.pop(0)

                        for k in range(n):
                            if isConnected[a][k]==1:
                                isConnected[a][k] = -1
                                q.append((a,k))
                        
                        for k in range(n):
                            if isConnected[b][k]==1:
                                isConnected[b][k] = -1
                                q.append((b,k))


        return provinces