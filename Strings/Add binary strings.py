def trimLeadingZeros(b): #FUNCTION TO TRIM LEADING ZEROS OF BINARY STRING
    start = b.find('1')
    return b[start:]

def BinaryAdd(b1, b2):
    b1 = trimLeadingZeros(b1) #TRIMS LEADING ZEROS
    b2 = trimLeadingZeros(b2)
    m, n = len(b1), len(b2)
    
    if m < n: #MAKING SURE B1 > B2 BY LOGIC
        b1,b2 = b2,b1
        m,n = n,m
    
    j = n - 1 #B2[0:N]
    carry = 0 
    res = []
    
    for i in range(m - 1, -1, -1): #ONE ITERATION
        bit1 = int(b1[i]) #ONLY FOR B1 AND CARRY
        bitsum = carry + bit1
        
        if j >= 0: #B1 AND B2
            bit2 = int(b2[j])
            bitsum += bit2
            j -= 1
        
        bit = bitsum % 2 
        carry = bitsum // 2
        res.append(str(bit))
    
    if carry > 0: #REMAINING CARRY AT THE END
        res.append('1')
        
    return ''.join(res[::1])
