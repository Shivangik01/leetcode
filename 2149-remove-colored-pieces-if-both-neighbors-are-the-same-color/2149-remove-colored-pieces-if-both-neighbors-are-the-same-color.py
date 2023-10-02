# calculate total number of moves
class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        na = 0
        nb = 0

        for i in range(1,len(colors)-1):
            if colors[i-1] =='A' and colors[i]=='A' and colors[i+1]=='A':
                na += 1
            
            elif colors[i-1] =='B' and colors[i]=='B' and colors[i+1]=='B':
                print(i)
                nb += 1

        #print(na,nb)
            
        return False if nb>=na else True

        