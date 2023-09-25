# for 
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        # provinces = 0   
        # n = len(isConnected)
        # vis = [0]*n

        # def dfs(i):
        #     for j in range(n):
        #         if isConnected[i][j]==1:
        #             isConnected[i][j]=-1
        #             vis[j]=1
        #             dfs(j)

        # for i in range(n):

        #     if vis[i]==0:
        #         vis[i]=1
        #         provinces +=1
        #         dfs(i)

        # return provinces

        if not M:
            return 0
        
        n = len(M)
        visit = [False]*n
        
        def dfs(u):
            for v in range(n):
                if M[u][v] ==1 and visit[v] == False:
                    visit[v] = True
                    dfs(v)
        
        count = 0
        for i in range(n):
            if visit[i] == False:
                count += 1
                visit[i] = True
                dfs(i)
        
        return count