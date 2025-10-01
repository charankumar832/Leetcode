class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        my_dict=dict()
        for i in range(0,len(nums)):
            my_dict[nums[i]]=my_dict.get(nums[i],0)+1
        max_values=max(my_dict.values())
        return sum(count for count in my_dict.values() if count==max_values)