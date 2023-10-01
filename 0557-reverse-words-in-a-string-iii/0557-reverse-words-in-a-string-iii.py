class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.split()
        # ans = ''

        # for w in words:
        #     ans+=w[::-1]+' '

        return " ".join(w[::-1] for w in s.split())
        