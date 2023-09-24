class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        mp = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
        }

        number1=0
        n1 = len(num1)

        for i in range(n1-1,0,-1):
            number1+= mp[num1[n1-i-1]]*(10**i)
            
        number1+=mp[num1[-1]]


        n2 = len(num2)
        number2=0

        for i in range(n2-1,0,-1):
            number2+= mp[num2[n2-i-1]]*(10**i)
            
        number2+=mp[num2[-1]]

        #print(number1,number2)
        return str(number1*number2)



        