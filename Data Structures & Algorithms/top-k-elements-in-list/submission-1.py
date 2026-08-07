from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        for num, counts in count.most_common(k):
            result.append(num)
        return result