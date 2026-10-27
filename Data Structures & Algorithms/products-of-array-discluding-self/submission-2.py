class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        totalp = 1
        totals = 1
        ans = []
        for i in range(len(nums)):
            totalp*=nums[i]
            totals*=nums[len(nums)-i-1]
            prefix.append(totalp)
            suffix.append(totals)
        
        suffix.reverse()

        for i in range(len(nums)):
            if i-1<0:
                ans.append(1*suffix[i+1])
            elif i+1>=len(nums):
                ans.append(prefix[i-1]*1)
            else:
                ans.append(prefix[i-1]*suffix[i+1])
        return ans