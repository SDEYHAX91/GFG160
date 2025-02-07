def getLastMoment(n, left, right):
        #code here
        res = 0
        
        for i in range(len(left)):
            res = max(res, left[i])
        
        for i in range(len(right)):
            res = max(res, n - right[i])
        
        return res
