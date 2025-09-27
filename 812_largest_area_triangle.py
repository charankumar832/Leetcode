class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a,b,c):
            return 0.5* abs(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))
        
        max_area=0
        n=len(points)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    a,b,c=points[i],points[j],points[k]
                    max_area=max(max_area,area(a,b,c))
        return max_area
    

# class Solution:
#     def largestTriangleArea(self, points: List[List[int]]) -> float:
#         def area(a,b,c):
#             return 0.5* abs(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))
        
#         max_area=0
#         from itertools import combinations
#         for a,b,c in combinations(points,3):
#             max_area=max(max_area,area(a,b,c))
#         return max_area