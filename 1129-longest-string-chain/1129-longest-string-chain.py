# words of similar length together
# optimize len dp
# store max and last valids 

from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key=len)

        dp = {}
        m = 0

        for w in words:
            dp[w] = 1

            for i in range(len(w)):
                #print(w[:i]+w[i+1:],w)
                if w[:i]+w[i+1:] in dp:
                    dp[w] = max(dp[w],dp[w[:i]+w[i+1:]]+1)

            m = max(m,dp[w])

        return m