#OPTIMAL FUNCTION TO FIND 2ND LARGEST VALUE IN AN ARRAY

def getSecondLargest(self, arr):
        # Code Here
        if len(arr) < 2: #If length of array is less than 2 return -1
            return -1
        
        Largest = Second_Largest = float('-inf') #initialization
        for i in arr: #Keeps track of both max and 2ndmax in one iteration
            if i > Largest: 
                Second_Largest = Largest 
                Largest = i
            
            elif i > Second_Largest and i != Largest:
                Second_Largest = i
            
        if Second_Largest == float('-inf'):
            return -1
        else:
            return Second_Largest
