class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):
            s = sorted([i for i in s])
            t = sorted([i for i in t])
            if s == t:
                return True

        return False 


