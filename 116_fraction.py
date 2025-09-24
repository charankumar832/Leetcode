class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator==0:
            return "0"
        if denominator==0:
            return ""

        res=""
        if numerator<0 or denominator <0:
            res+="-"
        numerator, denominator=abs(numerator),abs(denominator)

        res+= str(numerator//denominator)

        if numerator%denominator==0:
            return res

        res+="."

        rem_dict={}
        rem=numerator%denominator

        while rem!=0 and rem not in rem_dict:
            rem_dict[rem]=len(res)
            rem*=10
            res+=str(rem//denominator)
            rem%=denominator

        if rem in rem_dict:
            res=res[:rem_dict[rem]]+"("+res[rem_dict[rem]:]+")"
        return res