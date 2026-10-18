class Solution:
    def maximum69Number(self, num: int) -> int:
        n = num
        i = 0
        add_to_num = 0
        while n:
            temp = n%10
            n = n//10
            if temp == 6:
                add_to_num = 10**i
            i+=1
        return num+3*add_to_num
