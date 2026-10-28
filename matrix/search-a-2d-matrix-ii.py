# 240. Search a 2D Matrix II
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Объявляем указатели
        row, col = 0, len(matrix[0])-1

        # Начинаем с верхнего правого угла, двигаемся влево/вниз,
        # пока не найдём таргет или не выйдем за границы матрицы
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        # Возвращаем ЛОЖЬ, если ничего не нашлось
        return False
