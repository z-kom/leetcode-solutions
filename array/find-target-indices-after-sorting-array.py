class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
            else:
                if result:
                    break

        return result
