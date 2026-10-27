# 3963. Create Grid With Exactly One Path
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Самое простое решение: путь проходит по верхней строчке,
        # а потом поворачивает вниз
        return ['.' * n] + ['#' * (n - 1) + '.'] * (m - 1)
