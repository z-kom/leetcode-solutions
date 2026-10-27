# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Объявляем указатели
        l = 0
        r = len(nums)

        # Бинарным поиском ищем позицию вставки
        while l + 1 < r:
            m = (r+l)//2
            if nums[m] > target:
                r = m
            else: 
                l = m
        
        # Если левый указатель не указывает на таргет, 
        # возвращаем индекс правее, иначе исходный указатель
        if nums[l] < target:
            return l+1
        return l
