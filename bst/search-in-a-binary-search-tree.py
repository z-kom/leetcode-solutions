# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        Время: O(h), h - высота дерева, если дерево сбалансировано,
        то время - O(log n), иначе O(n)
        Память: O(1)
        """
        # Ставим курсор на корне
        curr = root

        # Ищем значение в дереве, пока курсор является узлом
        while curr is not None:
            x = curr.val

            # Если значение узла совпадает со поисковым
            # значением, возвращаем поддерево
            if val == x:
                return curr
            
            # Если поисковое значение меньше значения узла,
            # переносим курсор на левое поддерево
            elif val < x:
                curr = curr.left
            
            # Если поисковое значение больше значения узла,
            # переносим курсор на правое поддерево
            else:
                curr = curr.right
        
        # Возвращаем None, если поисковое значение не было найдено
        return None
