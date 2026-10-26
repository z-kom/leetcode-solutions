class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Время: O(n)
        Память: O(n)
        """

        # Создаем множество
        seen = set()

        # Проход по массиву
        for num in nums:
            # Если находим число в множестве, значит, 
            # есть дубликаты, возвращаем ИСТИНУ
            if num in seen:
                return True

            # Если не нашлось, добавляем данное число
            # в множество
            seen.add(num)

        # Возвращаем ЛОЖЬ, если дубликат не обнаружен
        return False
