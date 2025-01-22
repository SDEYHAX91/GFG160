#OPTIMAL CODE TO REVERSE AN ARRAY (NO INBUILT FUNCTIONS OR ARR[::-1] REQUIRED)
#THERE ARE 2 OPTIMAL CODES

# CODE 1:

def ReverseArray(arr):
    left = 0
    right = len(arr) - 1
    
    while(left < right):
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
        
    return arr

# CODE 2:

def ReverseArray(arr):
    i = 0
    n = len(arr)
    for i in range(n//2):
       arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
       i += 1

    return arr 

#PEACE
