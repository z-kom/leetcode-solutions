# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Создаем хеш-таблицу
        q = {}

        # Циклом проходим по словам
        for a in strs:
            # Разбиваем эти слова по буквам и сортируем буквы
            a_ = tuple(sorted(a))

            # Добавляем в хеш-таблицу слово по кортежу его букв
            if a_ not in q:
                q[a_] = []
            q[a_].append(a)
        
        # Возвращаем только значения хеш-таблицы
        return list(q.values())
