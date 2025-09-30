class Solution:

    # Using single for loop and 2 pointers 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        nums.sort()
        for i in range(0,n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total<0:
                    j+=1
                elif total>0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    res.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return res

# Using 2 for loops(O(n2))   
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n=len(nums)
        
#         my_res=set()
#         for i in range(0,n):
#             my_set=set()
#             for j in range(i+1,n):
#                 third=-(nums[i]+nums[j])
#                 if third in my_set:
#                     temp=[nums[i],nums[j],third]
#                     temp.sort()
#                     my_res.add(tuple(temp))
#                 my_set.add(nums[j])
#         return[list(ans) for ans in my_res]



#Brute Force Solution (O(n**3))
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n=len(nums)
#         my_set=set()
#         for i in range(0,n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     if nums[i]+nums[j]+nums[k]==0:
#                         temp=[nums[i],nums[j],nums[k]]
#                         temp.sort()
#                         my_set.add(tuple(temp))
#         return [list(ans) for ans in my_set]