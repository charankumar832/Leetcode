class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        h=len(s)-1
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        s=list(s)
        
        while l<h:
            while l<h and s[l] not in vowels:
                l+=1
            while l<h and s[h] not in vowels:
                h-=1
            if l<h:
                s[l],s[h]=s[h],s[l]
                l+=1
                h-=1
        return ''.join(s)