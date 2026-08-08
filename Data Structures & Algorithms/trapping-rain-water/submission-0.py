class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftheight = height[l]
        rightheight = height[r]
        area = 0

        while l < r:
            if leftheight < rightheight:
                l += 1
                leftheight = max(leftheight, height[l])
                area += leftheight - height[l]
            else:
                r -= 1
                rightheight = max(rightheight, height[r])
                area += rightheight - height[r]
        return area