def FindMaxProdSubarr(arr):
    
    maxpro = float('-inf') #Initialization
    l2r = 1
    r2l = 1
    
    for i in range(len(arr)): #Reset if arr[i] = 0
        if l2r == 0:
            l2r = 1
        if r2l == 0:
            r2l = 1
        
        l2r = l2r * arr[i]
        j = len(arr) - 1 - i
        
        r2l = r2l * arr[j]
        
        maxpro = max(l2r, r2l, maxpro)
    return maxpro
