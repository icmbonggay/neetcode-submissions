class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1


        for i in range(0, len(nums)):
            if nums[i] != nums[r - 1]:
                nums[r] = nums[i]
                r += 1 


        return r