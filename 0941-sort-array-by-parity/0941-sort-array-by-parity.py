class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        cnt = 0
        n = len(nums)
        i = 0

        while cnt<n:

            if nums[i]%2!=0:
                nums.append(nums[i])
                nums.pop(i)
                
                i-=1
                
            cnt+=1
            i+=1

        print(nums)
        return nums