class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        
        #Finding element smaller than next element from the end and making it pivot
        #Assuming traversing form end has descending order of some elements
        pivot = -1
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
            
        #if pivot doesn't exists, then the next permutation will be the smallest
        if pivot == -1:
            arr.reverse()
            return arr
          
        #swapping pivot element with the rightmost greater element
        for i in range(n-1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot],arr[i]
                break

      #reversing the elements to the right of pivot
        left = pivot+1
        right = n-1
        while(left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr
