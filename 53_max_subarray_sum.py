class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float("-inf")
        total=0
        n=len(nums)
        for i in range(0,n):
            total+=nums[i]
            if total>maxi:
                maxi=total
            if total<0:
                total=0
        return maxi