class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_count=0
        n=len(nums)
        if 1 not in nums:
            return 0

        for i in range(0,n):
            if nums[i]==1:
                count+=1
            else:
                max_count=max(max_count,count)
                count=0
        return max(max_count,count)