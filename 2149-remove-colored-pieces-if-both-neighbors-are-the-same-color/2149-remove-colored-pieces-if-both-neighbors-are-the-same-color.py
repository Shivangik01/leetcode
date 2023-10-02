# calculate total number of moves
class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        na = 0
        nb = 0

        for i in range(1,len(colors)-1):
            if colors[i-1] == colors[i]== colors[i+1]:
                if colors[i]=='A':
                    na+=1
                else:
                    nb+=1

        #print(na,nb)
            
        return False if nb>=na else True

        