class Solution:
    def triangleNumber(self, nums: list[int]) -> int:

        n=len(nums)
        nums.sort()
        count=0
        for k in range(n-1,1,-1):
            i=0
            j=k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    count+=(j-i)
                    j-=1
                else:
                    i+=1
        return count