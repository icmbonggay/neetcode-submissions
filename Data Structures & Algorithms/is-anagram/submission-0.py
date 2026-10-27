class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = sorted([i for i in s])
        self.t = sorted([i for i in t])

        if self.s == self.t:
            return True

        return False 


