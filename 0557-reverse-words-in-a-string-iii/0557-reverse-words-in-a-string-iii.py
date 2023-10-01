class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = ''

        #print(words)
        for w in words:
            for i in range(len(w)-1,-1,-1):
                ans += w[i]

            ans+=' '

        return ans[:-1]
        