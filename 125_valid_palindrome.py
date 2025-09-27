class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new_string=[ch for ch in s if ch.isalnum()]

        l=0
        h=len(new_string)-1
        while l<h:
            if new_string[l]!=new_string[h]:
                return False
            l+=1
            h-=1
        return True


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = re.sub(r'[^a-zA-Z0-9]', "", s).lower()
#         return s == s[::-1]