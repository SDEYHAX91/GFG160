#Given an array, arr[], determine if arr can be split into three 
#consecutive parts such that the sum of each part is equal. 
#If possible, return any index pair(i, j) in an array such that 
#sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise
return an array {-1,-1}.

def findSplit(self, arr):

        total = 0 #Sum of all elements in an array
        for i in arr:
            total += i
        
        if total % 3 != 0: #If sum is not divisible by 3 then return [-1,-1]
            res = [-1, -1]
            return res
        
        currSum = 0 #Finds partition 
        res = []
        
        for x in range(len(arr)):
            currSum += arr[x]
            
            if currSum == total / 3:
                currSum = 0
                res.append(x)
            
            if len(res) == 2 and x < len(arr) - 1: #if pair is formed then return it
                return res
        
        res = [-1, -1]
        return res
