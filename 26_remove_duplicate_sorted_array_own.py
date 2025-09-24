class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n=len(nums)
        temp=[]
        i=0
        while i<n:
            if len(temp)==0 or temp[-1]!=nums[i]:
                temp.append(nums[i])
            i+=1
        k=len(temp)
        for i in range(0,k):
            nums[i]=temp[i]
        return k   