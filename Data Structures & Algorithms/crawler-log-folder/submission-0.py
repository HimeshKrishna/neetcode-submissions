class Solution:
    def minOperations(self, logs: List[str]) -> int:
        opr=[]
        for i in logs:
            if i == "../":
                if opr:
                    opr.pop()
            elif i != "./":
                opr.append(i)
        return len(opr)

#2nd method
'''


'''