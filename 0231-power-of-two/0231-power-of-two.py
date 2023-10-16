class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
       #print(bin(n))

       #return False if n<=0 or bin(n).count('1')>1 else True

       return n and not(n&n-1)