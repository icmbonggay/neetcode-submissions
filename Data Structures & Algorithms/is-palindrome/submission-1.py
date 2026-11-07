import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"\W", "", s)
        s = s.lower()

        l, r = 0, len(s) - 1

        while l <= len(s) - 1 and r >= 0:
            if s[l] != s[r]:
                return False
            
            l = l + 1
            r = r - 1
            
        
        return True

        