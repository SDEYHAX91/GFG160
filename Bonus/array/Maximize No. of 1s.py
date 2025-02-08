#Given a binary array arr[] (containing only 0s and 1s) and an integer k, you are 
#allowed to flip at most k 0s to 1s. Find the maximum number of consecutive 1's that
#can be obtained in the array after performing the operation at most k times.

class Solution:
    # k is the maximum number of zeros allowed to flip
    def maxOnes(self, arr, k):
        # code here
        ct = res = start = end = 0
        
        while end < len(arr):
            if arr[end] == 0:
                ct += 1
            
            while ct > k:
                if arr[start] == 0:
                    ct -= 1
                start += 1
                
            res = max(res, end - start + 1)
            end += 1
        return res    
