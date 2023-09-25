class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):

                c1 = 0 if i==0 else board[i-1][j]%2
                c2 = 0 if j==0 else board[i][j-1]%2
                c3 = 0 if i==m-1 else board[i+1][j]%2
                c4 = 0 if j==n-1 else board[i][j+1]%2
                c5 = 0 if i==0 or j==0 else board[i-1][j-1]%2
                c6 = 0 if i==m-1 or j==n-1 else board[i+1][j+1]%2
                c7 = 0 if i==0 or j==n-1 else board[i-1][j+1]%2
                c8 = 0 if i==m-1 or j==0 else board[i+1][j-1]%2
                
                #print(c1,c2,c3,c4,c5,c6,c7,c8,i,j)

                if board[i][j]==1 and (sum([c1,c2,c3,c4,c5,c6,c7,c8])==2 or sum([c1,c2,c3,c4,c5,c6,c7,c8])==3):
                    board[i][j]+=2

                elif board[i][j]==0 and sum([c1,c2,c3,c4,c5,c6,c7,c8])==3:
                    board[i][j]+=2

        for i in range(m):
            for j in range(n):

                if board[i][j]==0 or board[i][j]==1:
                    board[i][j]=0

                elif board[i][j]==2 or board[i][j]==3:
                    board[i][j]=1

