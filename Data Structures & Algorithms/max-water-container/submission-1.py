class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        result_area = 0

        while l < r:
            result_area = max(result_area, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result_area