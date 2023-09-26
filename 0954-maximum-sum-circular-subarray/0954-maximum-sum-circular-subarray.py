class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        # n = len(nums)

        # op = [0 for _ in range(n)]
        # ssop = [i for i in nums]
        # ans1 = nums[0]
        # ss = nums[-1]

        # for i in range(n-2,-1,-1):
        #     ss += nums[i]
        #     ssop[i]= max(ssop[i+1],ss)

        # #print(ssop)

        # ans2 = nums[0]
        # ps = 0

        # for i in range(n):
        #     ps += nums[i]
        #     op[i]= max(op[i-1]+nums[i],nums[i])
        #     ans1 = max(op[i],ans1)
        #     if i!=n-1: 
        #         ans2 = max(ans2,ps+ssop[i+1])
        

        # return max(ans1,ans2)

        mmax = nums[0]
        mmin = nums[0]
        cmax = 0
        cmin = 0
        t = 0

        for n in nums:
            cmax = max(cmax+n,n)
            cmin = min(cmin+n,n)
            mmax = max(mmax,cmax)
            mmin = min(mmin,cmin)
            t += n

        return max(mmax,t-mmin) if mmax>0 else mmax
