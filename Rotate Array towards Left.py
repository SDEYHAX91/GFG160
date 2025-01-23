#OPTIMAL CODE TO ROTATE ARRAY ELEMENTS ANTI-CLOCKWISE BY REVERSAL METHOD

def RotateArrLeft(arr, d):
    
    n = len(arr)
    d %= n
    
    reverseArr(arr, 0, d-1)
    reverseArr(arr, d, n-1)
    reverseArr(arr, 0, n-1)
    
    return arr

def reverseArr(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
