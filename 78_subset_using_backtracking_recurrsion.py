class Solution:

    def solve(self,index,subset,n,nums,res):
        
        if index==n:
            res.append(subset.copy())   
            return 
        subset.append(nums[index])
        self.solve(index+1,subset,n,nums,res)
        subset.pop()
        self.solve(index+1,subset,n,nums,res)  
        

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        res=[]
        index=0
        n=len(nums)
        self.solve(index,subset,n,nums,res)
        return res
