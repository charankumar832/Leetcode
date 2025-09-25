class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n=len(nums)
        total=n*(n+1)//2
        add=sum(nums)
        return total-add
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n=len(nums)
        dict={}
        for i in range(0,n+1):
            dict[i]=0
        for num in nums:
            dict[num]=1
        for k,v in dict.items():
            if v==0:
                return k

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n=len(nums)
        nums.sort()
        for i in range(n):
            if nums[i]!=i:
                return i
        return n
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n=len(nums)
        for i in range(0,n+1):
            if i not in nums:
                return i