#OPTIMAL CODE TO MOVE ALL ZEROES TO END OF THE ARRAY

def ShiftZeroes2right(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i],arr[count] = arr[count],arr[i]
            count+=1
    
    return arr
