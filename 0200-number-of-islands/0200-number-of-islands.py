class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island = 0

        r,c = len(grid),len(grid[0])

        for i in range(r):
            for j in range(c):

                if grid[i][j]=="1":

                    island += 1
                    q = [(i,j)]
                    grid[i][j]="#"

                    while q!=[]:

                        m,n = q.pop(0)
                        

                        if m+1!=r and grid[m+1][n]=="1":
                            grid[m+1][n]="#"
                            q.append((m+1,n))
                        
                        if n+1!=c and grid[m][n+1]=="1":
                            grid[m][n+1]="#"
                            q.append((m,n+1))
                        
                        if n-1>-1 and grid[m][n-1]=="1":
                            grid[m][n-1]="#"
                            q.append((m,n-1))
                        
                        if m-1>-1 and grid[m-1][n]=="1":
                            grid[m-1][n]="#"
                            q.append((m-1,n))

        return island
