class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        q = int(area**.5)        
        for i in range(q+1, 0, -1):
            if area % i == 0:
                return [max(i, area//i), min(i, area//i)]
