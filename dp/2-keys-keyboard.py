class Solution:
    def minSteps(self, n: int) -> int:
        if n==1: return 0
        def backtrack(a, copied, q):
            if len(a) == n: return q
            elif len(a)>n: return float('inf')
            if a==copied:
                return backtrack(a+copied, copied, q+1)
            return min(backtrack(a+copied, copied, q+1), backtrack(a, a, q+1))
        return backtrack('A', 'A', 1)
