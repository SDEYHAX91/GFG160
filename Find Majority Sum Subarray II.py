def findMajority(self, arr):
        
        res = []
        
        ele1,ele2 = -1,-1 #initialization
        ct1,ct2 = 0,0
        
        for i in arr:
            if ele1 == i: #If element 1 is found
                ct1 += 1
            
            elif ele2 == i: #If element 2 is found
                ct2 += 1
            
            elif ct1 == 0: #If element 1 is found at 1st
                ele1 = i
                ct1 += 1
                
            elif ct2 == 0: #If element 2 is found at 1st
                ele2 = i
                ct2 += 1
            
            else:
                ct1 -= 1 
                ct2 -= 1
        
        ct1, ct2 = 0,0
        #Next iteration to count requried elements
        for i in arr:
            if i == ele1:
                ct1 += 1
            if i == ele2:
                ct2 += 1
        
        if ct1 > len(arr)//3:
            res.append(ele1)
        if ct2 > len(arr)//3 and ele1 != ele2:
            res.append(ele2)
            
        if len(res) == 2 and res[0] > res[1]:
            res[0], res[1] = res[1], res[0]
        
        return res
