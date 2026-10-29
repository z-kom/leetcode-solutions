# 540. Single Element in a Sorted Array
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Складываем все элементы XOR'ом, возращаем результат
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        return result
