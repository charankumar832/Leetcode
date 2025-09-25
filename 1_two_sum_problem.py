class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dict={}
        for i in range(0,n):
            rem=target-nums[i]
            if rem in dict:
                return [i,dict[rem]]
            dict[nums[i]]=i