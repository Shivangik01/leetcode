# for 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        provinces = 0   
        n = len(isConnected)
        vis = [0]*n

        def dfs(i):
            for j in range(n):
                if isConnected[i][j]==1:
                    isConnected[i][j]=-1
                    vis[j]=1
                    dfs(j)

        for i in range(n):

            if vis[i]==0:
                vis[i]=1
                provinces +=1
                dfs(i)

        return provinces