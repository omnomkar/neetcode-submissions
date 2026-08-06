class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        prefix_product = 1
        for index in range(length):
            result[index] = prefix_product
            prefix_product *= nums[index]

        suffix_product = 1
        for index in range(length - 1, -1, -1):
            result[index] *= suffix_product
            suffix_product *= nums[index]

        return result