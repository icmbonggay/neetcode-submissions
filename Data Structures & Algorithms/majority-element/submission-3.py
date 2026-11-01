from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = Counter(nums)
        key = next((k for k, v in num.items() if v == max(num.values())), None)
        return key