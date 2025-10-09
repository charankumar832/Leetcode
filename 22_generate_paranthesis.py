class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        subset=[""]*(n*2)
        res=[]
        self.solve(0,0,subset,n,res)
        return res
        
    def solve(self,index,total,subset,n,res):
        if index>=len(subset):
            if total==0:
                res.append("".join(subset))
            return
        if total>(len(subset)//2):
            return
        if total<0:
            return

        subset[index]="("
        sum=total+1
        self.solve(index+1,sum,subset,n,res)

        subset[index]=")"
        sum=total-1
        self.solve(index+1,sum,subset,n,res)
        