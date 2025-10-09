class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        subset=[]
        self.solve(k,n,res,subset,0,1)
        return res
    
    def solve(self,k,target,res,subset,total,last):
        
        if total==target and len(subset)==k:
            res.append(subset.copy())
            return
        if total>target or len(subset)>k:
            return
        
        for i in range(last,10): #Only numbers 1 through 9 are used.
            sum=total+i
            subset.append(i)
            self.solve(k,target,res,subset,sum,i+1)
            subset.pop()