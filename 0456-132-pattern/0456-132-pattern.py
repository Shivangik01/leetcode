class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[j]>nums[i]:
        #             for k in range(j+1,n):
        #                 if nums[k]>nums[i] and nums[k]<nums[j]:
        #                     return True

        
        # return False

        k = float("-inf")
        st = []

        for i in range(n-1,-1,-1):
            if nums[i]<k:
                return True
            while st and nums[i]>st[-1]:
                k = st.pop()

            st.append(nums[i])
        return False