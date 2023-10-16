class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
       #print(bin(n))

       return True if n>0 and bin(n).count('1')==1 else False