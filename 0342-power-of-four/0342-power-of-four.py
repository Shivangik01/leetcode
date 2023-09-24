class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # while n>0:
        #     if n==1:
        #         return True

        #     if n%4!=0:
        #         return False
            
        #     n /= 4
        
        # return False

        #print(n.bit_length()&1,2&1)
        #return n>0 and log(n,4).is_integer()

        return n>0 and not(n&(n-1)) and n.bit_length()&1