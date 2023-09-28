class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        i = 0
        n = len(nums)
        j = n-1

        while i<j:

            while i<n and nums[i]%2==0:
                i+=1

            while j>-1 and nums[j]%2!=0:
                j-=1

            #print(i,j,nums[i],nums[j])
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]


        #print(nums)
        return nums