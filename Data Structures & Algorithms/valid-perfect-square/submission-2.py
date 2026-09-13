class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,num+1):
            sqr=i*i
            if sqr > num:
                return False
            if sqr==num:
                return True