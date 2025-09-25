class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1

        int_max=2**31-1
        int_min=-2**31

        temp=abs(x)
        rev=0
        while temp>0:
            last_digit=temp%10
            rev=rev*10+last_digit
            temp//=10

        result=sign*rev
        
        if int_min<=result<=int_max:
            return result
        else:
            return 0 

# Second Solution
   
# class Solution:
#     def reverse(self, x: int) -> int:
#         sign=-1 if x<0 else 1

#         int_max=2**31-1
#         int_min=-2**31

#         temp=abs(x)
#         rev=0
#         while temp>0:
#             last_digit=temp%10
#             rev=rev*10+last_digit
#             temp//=10

#         result=sign*rev
        
#         if int_min<=result<=int_max:
#             return result
#         else:
#             return 0 