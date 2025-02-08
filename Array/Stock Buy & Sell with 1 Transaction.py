#Optimal Code for Stock, Buy & Transaction with 1 Transaction only
def MaxProfit(arr):
    
    min = arr[0] #Initializing Min value to starting element
    res = 0 #Initial profit
    
    for i in range(len(arr)): 
        if min > arr[i]: # Finding min value.
            min = arr[i]
        res = max(res, arr[i] - min) #Maximizing profit
    
    return res
