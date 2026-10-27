class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums

        no_duplicates = set(self.nums)

        if len(no_duplicates) == len(self.nums):
            return False

        
        return True



