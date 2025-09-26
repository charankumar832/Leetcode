class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        dict={}

        for num in nums:
            if num in dict:
                return True
            else:
                dict[num]=1
        return False
    
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:

#         seen=set()

#         for num in nums:
#             if num in seen:
#                 return True
#             else:
#                 seen.add(num)
#         return False
        