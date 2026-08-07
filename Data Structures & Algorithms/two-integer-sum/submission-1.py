class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for pos, value in enumerate(nums):
            compliment = target - value
            if compliment in seen:
                return [seen[compliment], pos]
            seen[value] = pos
        return []