class Solution:
    def punishmentNumber(self, n: int) -> int:
        def possible(x,current,target):
            for i in range(1,len(x)):
                if int(x[:i]) + int(x[i:]) + current == target:
                    return True
                elif int(x[:i]) + current > target:
                    return False
                else:
                    if possible(x[i:],current+int(x[:i]), target):
                        return True

        res = 0
        for k in range(2,n+1):
            if possible(str(k**2),0,k):
                res += k**2
        return res + 1
       
