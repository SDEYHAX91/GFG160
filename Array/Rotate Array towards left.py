#MOST OPTIMAL CODE TO ROTATE ARRAY ELEMENTS ANTI-CLOCKWISE BY REVERSAL METHOD

def RotateArrLeft(arr, k):
    n = len(arr)
    if k < 0: #Ensure that k must be +ve
        k = abs(k)
    k %= n #Ensure that k must be within bounds of the array i.e k <= n
    
    back = arr[:k] 
    front = arr[k:]
    arr[:] = front + back
