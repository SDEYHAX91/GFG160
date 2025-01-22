#OPTIMAL FUNCTION TO FIND 2ND LARGEST VALUE IN AN ARRAY

def getSecondLargest(self, arr):
        # Code Here
        if len(arr) < 2:
            return -1
        
        Largest = Second_Largest = float('-inf')
        for i in arr:
            if i > Largest:
                Second_Largest = Largest
                Largest = i
            
            elif i > Second_Largest and i != Largest:
                Second_Largest = i
            
        if Second_Largest == float('-inf'):
            return -1
        else:
            return Second_Largest
