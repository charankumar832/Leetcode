class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        self.solve(0,candidates,target,res,0,subset)
        return res
    def solve(self,index,candidates,target,res,total,subset):
        if total==target:
            res.append(subset.copy())
            return
        elif total>target:
            return 
        if index>=len(candidates):
            return 
        subset.append(candidates[index])
        sum=total+candidates[index]
        self.solve(index,candidates,target,res,sum,subset)
        subset.pop()
        sum=total
        self.solve(index+1,candidates,target,res,sum,subset)
        