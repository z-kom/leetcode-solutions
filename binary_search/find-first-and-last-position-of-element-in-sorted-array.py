# 34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Если массив пустой, возвращаем (-1, -1)
        if not nums:
            return (-1, -1)
        
        # Объявляем указатели для бинарного поиска
        l = 0
        r = len(nums)

        # Бинарным поиском ищем lower_bound 
        while l < r:
            m = l + (r-l)//2
            if nums[m] < target:
                l = m + 1
            else: 
                r = m

        # Запоминаем первый индекс вхождения
        x = l

        # Если позиция вставки не совпадает с таргетом, возвращаем (-1, -1)
        if nums[x] != target:
            return (-1, -1)

        # Объявляем указатели для второго поиска
        l = 0
        r = len(nums)

        # Вторым бинарным поиском ищем upper_bound 
        while l < r:
            m = l + (r-l)//2
            if nums[m] <= target:
                l = m + 1
            else: 
                r = m

        # Делаем аналогичную проверку, как и с первым значением
        if nums[l-1] != target:
            return (-1, -1)
        
        # Возвращаем первое и последнее вхождение таргета-элемента
        return (x, l-1)
        
