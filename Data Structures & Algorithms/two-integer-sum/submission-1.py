class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer_key = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in answer_key:
                return[answer_key[difference], index]
            answer_key[num] = index
