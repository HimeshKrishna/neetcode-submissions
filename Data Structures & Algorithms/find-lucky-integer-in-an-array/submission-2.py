class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res=-1
        for num in arr:
            count=0
            for i in arr:
                if num==i:
                    count+=1
            if count==num:
                res=max(res,num)
        return res