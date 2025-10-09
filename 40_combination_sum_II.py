class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        subset=[]
        self.solve(candidates,target,res,subset,0,0)
        return res

    def solve(self,candidates,target,res,subset,total,index):
        
        if total==target:
            res.append(subset.copy())
            return
        
        
        
        for i in range(index,len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            
            sum=total+candidates[i]
            if sum>target :
                return
            subset.append(candidates[i])
            self.solve(candidates,target,res,subset,sum,i+1)
            subset.pop()
            