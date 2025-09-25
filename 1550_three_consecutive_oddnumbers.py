class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        n=len(arr)
        count=0
        for i in range(0,n):
            if arr[i]%2!=0:
               count+=1
               if count==3:
                return True
            else:
                count=0
        return False