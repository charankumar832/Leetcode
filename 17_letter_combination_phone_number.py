class Solution:
    def __init__(self):
        self.hash_map={
            '2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv",
            '9':"wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        subset=""
        if not digits:
            return res
        self.solve(digits,res,subset,0)
        return res

    
    def solve(self,digits,res,subset,index):

        if index==len(digits):
            res.append(subset)
            return
        
        # get all possible letters from current digit
        letters=self.hash_map.get(digits[index],"")

        for letter in letters:
            self.solve(digits,res,subset+letter,index+1)