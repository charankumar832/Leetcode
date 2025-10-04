# # Extreme Brute Force sol:
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n=len(height)
#         highest_sum=0
#         for i in range(0,n-1):
#             for j in range(i+1,n):
#                 mini=min(height[i],height[j])
#                 distance=j-i
#                 container_sum=distance*mini
#                 highest_sum=max(highest_sum,container_sum)
#         return highest_sum
        


#Optimised Sol:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        h=len(height)-1
        highest_sum=0

        while l<h:
            mini=min(height[l],height[h])
            distance=h-l
            container_sum=distance*mini
            highest_sum=max(container_sum,highest_sum)
            if height[l]<height[h]:
                l+=1
            else:
                h-=1
        return highest_sum
    