#OPTIMAL CODE FOR STOCK BUY AND SELL WITH MULTIPLE TRANSACTIONS

def MaxProfit(arr):
    
    profit = 0
    
    for i in range(1,len(arr)):
        if arr[i-1] <= arr[i]:
            profit += (arr[i] - arr[i-1])
            
    return profit
