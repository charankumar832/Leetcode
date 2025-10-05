class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n=len(nums)
        total_subset=2**n
        res=[]

        for num in range(0,total_subset):
            lis=[]
            for i in range(0,n):
                if num & (1<<i)!=0:
                    lis.append(nums[i])
            res.append(lis)
        return res