class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,num):
            sqr=i*i
            if sqr > num:
                return False
            elif sqr==num:
                return True