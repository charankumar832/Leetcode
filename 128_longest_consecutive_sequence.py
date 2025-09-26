class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        my_set=set(nums)
        longest=0
        for num in my_set:
            if num-1 not in my_set:
                x=num
                count=1 
                while x+1 in my_set:
                    count+=1
                    x+=1
                longest=max(count,longest)
        return longest
    

# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:

#         nums.sort()

#         if not nums:
#             return 0
#         count=1
#         max_length=1
#         for i in range(1,len(nums)):
#             if nums[i]==nums[i-1]:
#                 continue
#             elif nums[i]==nums[i-1]+1:
#                 count+=1
#             else:
#                 count=1
#             max_length=max(max_length,count)
#         return max_length
