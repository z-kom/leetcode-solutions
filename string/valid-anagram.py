# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Если длина не совпадает, возвращаем ЛОЖЬ
        if len(s) != len(t):
            return False
        
        # Считаем количество уникальных букв,
        # если совпадает, продолжаем, пока не закончим,
        # иначе возвращаем ЛОЖЬ
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True
